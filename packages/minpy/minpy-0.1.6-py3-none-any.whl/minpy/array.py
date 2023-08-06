#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable= unused-argument, protected-access,
# logging-format-interpolation
"""Base type for arrays."""
from __future__ import absolute_import
from __future__ import print_function

import functools
import itertools
import operator
import logging
import collections

from .utils import log
#from .utils.minprof import minprof
from .array_variants import ArrayType
from .array_variants import array_types
from .array_variants import number_types

import mxnet
import numpy
import collections

# pylint: disable= invalid-name
_logger = log.get_logger(__name__, logging.WARN)

# pylint: enable= invalid-name


class UnknownArrayTypeError(TypeError):
    """ Unsupported underlying array type (now only support: numpy.ndarray and mxnet.ndarray)"""
    pass


class NoImplementationError(ValueError):
    """ Throw if not implemented currently """
    pass


class AutogradError(ValueError):
    """ Error during auto differentiation """
    pass

GradRecord = collections.namedtuple('GradRecord', ['grad_func', 'result', 'primitive'])

class Node(object):
    """Node representing data with gradient information."""
    __slots__ = ['_value', '_partial_derivatives', '_partial_derivative_cache']

    def __init__(self, value):
        """Initialize."""
        self._value = value
        self._partial_derivatives = []
        self._partial_derivative_cache = {}

    def add_partial_derivative(self, grad_func, res, prim):
        """Add partial derivative information.

        :param function grad_func: The function to calculate derivative with respect to result.
        :param Node res: Variable that represent the result of original function.
        :param Primitive prim: Primitive that the gradient function belongs to.
        """
        assert isinstance(res, Node), 'Result is not of type `Node`.'
        self._partial_derivatives.append(GradRecord(grad_func=grad_func,
                                                    result=res,
                                                    primitive=prim))

    def partial_derivative(self, target):
        """Get partial derivative. Mathematically, this function computes

           \\frac{\\partial{}target}{\\partial{}self}

        :param Node target: Target variable to compute partial derivative.
        :return: Partial derivative.
        """
        def _call_partial_derivative(rec):
            """Helper function for calling gradient function.

            :param GradRecord rec: The gradient record to be called.
            :return: Gradient result.
            """
            # The gradient of the target with respect to the result node should already be
            # computed.
            result_grad = rec.result._partial_derivative_cache[target]
            result_grad_value = result_grad.get_data(rec.primitive._type)
            _logger.debug('Call derivative func of "{}".'.format(rec.primitive._func))
            # Call gradient function to compute input gradient from result gradient
            if rec.primitive.type == ArrayType.MXNET:
                # Currently all MXNet function call will be performed on GPU 0.
                with mxnet.gpu(0) as ctx:
                    grad = rec.grad_func(result_grad_value)
            else:
                grad = rec.grad_func(result_grad_value)
            return grad

        # Array used to store intermediate gradients to be computed.
        pending_derivatives = []

        # Use DFS search to find all derivatives need to be computed in order to get the gradient
        # of final target.
        dfs_queue = [self]
        while len(dfs_queue) != 0:
            node = dfs_queue[-1]
            assert isinstance(target, Node), 'Type is not `Node`.'
            ready = True
            if target is not node:
                for rec in node._partial_derivatives:
                    n = rec.result
                    if target not in n._partial_derivative_cache:
                        dfs_queue.append(n)
                        ready = False
            # Successors all enqueued.
            if ready:
                dfs_queue.pop()
                if target not in node._partial_derivative_cache:
                    pending_derivatives.append(node)
                    # Init gradient buffer for accumulation.
                    node._partial_derivative_cache[target] = Value.wrap(
                        0.0 if isinstance(node._value, Number) else numpy.zeros(node._value.shape))

        # Compute gradient using chain rule.
        # The resolve order is the reversed order from target to input.
        for node in pending_derivatives:
            if node is target:
                # Current gradient node is the target node, the gradient is one.
                node._partial_derivative_cache[target] = Value.wrap(
                    1.0 if isinstance(node._value, Number) else numpy.ones(node._value.shape))
            else:
                # Call saved gradient function to compute gradient of each input.
                for rec in node._partial_derivatives:
                    node._partial_derivative_cache[target] += Value.wrap(
                        _call_partial_derivative(rec))

        return self._partial_derivative_cache[target]


class Value(object):
    # pylint: disable= no-self-use
    """ Class for all possible values in minpy. It contains the real underlying value and the
    gradient information for auto differentiation. It also defines common operators and redirects
    the call to the namespace dispatcher.
    """
    _ns = None

    def __init__(self, marked):
        self._marked_for_bp = marked

    @property
    def marked_for_bp(self):
        """Return whether the current Value will be used for autograd."""
        return self._marked_for_bp

    @staticmethod
    def wrap(data, *args, **kwargs):
        """ Wrap given data into its corresponding wrapper class. For example, `numpy.ndarray`
        will be converted to `minpy.Array` while float number will become `minpy.Number`. The
        allowed array types are defined in `minpy.array_variants.array_types`; the allowed number
        types are defined in `minpy.array_variants.number_types`.
        """
        if data is None:
            return None
        dtype = type(data)
        if isinstance(data, Value):
            return data
        elif dtype in array_types.values():
            return Array(data, *args, **kwargs)
        elif dtype in itertools.chain(*number_types.values()):
            return Number(data, *args, **kwargs)
        else:
            raise UnknownArrayTypeError('cannot wrap type: {}'.format(dtype))

    def __cmp__(self, other):
        raise NoImplementationError('Not implemented')

    def __eq__(self, other):
        return Value._ns.equal(self, other)

    def __ne__(self, other):
        return Value._ns.not_equal(self, other)

    def __lt__(self, other):
        return Value._ns.less(self, other)

    def __gt__(self, other):
        return Value._ns.greater(self, other)

    def __le__(self, other):
        return Value._ns.less_equal(self, other)

    def __ge__(self, other):
        return Value._ns.greater_equal(self, other)

    def __pos__(self):
        raise NoImplementationError('Not implemented')

    def __neg__(self):
        return Value._ns.negative(self)

    def __abs__(self):
        raise NoImplementationError('Not implemented')

    def __invert__(self):
        raise NoImplementationError('Not implemented')

    def __round__(self, nbits):
        raise NoImplementationError('Not implemented')

    def __floor__(self):
        raise NoImplementationError('Not implemented')

    def __ceil__(self):
        raise NoImplementationError('Not implemented')

    def __trunc__(self):
        raise NoImplementationError('Not implemented')

    def __add__(self, other):
        return Value._ns.add(self, other)

    def __sub__(self, other):
        return Value._ns.subtract(self, other)

    def __mul__(self, other):
        return Value._ns.multiply(self, other)

    def __floordiv__(self, other):
        raise NoImplementationError('Not implemented')

    def __div__(self, other):
        return Value._ns.divide(self, other)

    def __truediv__(self, other):
        return Value._ns.true_divide(self, other)

    def __mod__(self, other):
        return Value._ns.mod(self, other)

    def __divmod__(self, other):
        raise NoImplementationError('Not implemented')

    def __pow__(self, other):
        return Value._ns.power(self, other)

    def __lshift__(self, other):
        raise NoImplementationError('Not implemented')

    def __rshift__(self, other):
        raise NoImplementationError('Not implemented')

    def __and__(self, other):
        raise NoImplementationError('Not implemented')

    def __or__(self, other):
        raise NoImplementationError('Not implemented')

    def __xor__(self, other):
        raise NoImplementationError('Not implemented')

    def __radd__(self, other):
        return Value._ns.add(other, self)

    def __rsub__(self, other):
        return Value._ns.subtract(other, self)

    def __rmul__(self, other):
        return Value._ns.multiply(other, self)

    def __rfloordiv__(self, other):
        raise NoImplementationError('Not implemented')

    def __rdiv__(self, other):
        return Value._ns.divide(other, self)

    def __rtruediv__(self, other):
        return Value._ns.true_divide(other, self)

    def __rmod__(self, other):
        return Value._ns.mod(other, self)

    def __rdivmod__(self, other):
        return Value._ns.mod(other, self)

    def __rpow__(self, other):
        return Value._ns.power(other, self)

    def __rlshift__(self, other):
        raise NoImplementationError('Not implemented')

    def __rrshift__(self, other):
        raise NoImplementationError('Not implemented')

    def __rand__(self, other):
        raise NoImplementationError('Not implemented')

    def __ror__(self, other):
        raise NoImplementationError('Not implemented')

    def __rxor__(self, other):
        raise NoImplementationError('Not implemented')

    def __iadd__(self, other):
        return Value._ns.add(self, other)

    def __isub__(self, other):
        return Value._ns.subtract(self, other)

    def __imul__(self, other):
        return Value._ns.multiply(self, other)

    def __ifloordiv__(self, other):
        raise NoImplementationError('Not implemented')

    def __idiv__(self, other):
        return Value._ns.divide(self, other)

    def __itruediv__(self, other):
        return Value._ns.true_divide(self, other)

    def __imod__(self, other):
        return Value._ns.mod(self, other)

    def __ipow__(self, other):
        return Value._ns.power(self, other)

    def __ilshift__(self, other):
        raise NoImplementationError('Not implemented')

    def __irshift__(self, other):
        raise NoImplementationError('Not implemented')

    def __iand__(self, other):
        raise NoImplementationError('Not implemented')

    def __ior__(self, other):
        raise NoImplementationError('Not implemented')

    def __ixor__(self, other):
        raise NoImplementationError('Not implemented')
    # pylint: enable= no-self-use


class Number(Value, float):
    """Class for numbers with derivative information"""
    __slots__ = ['_node', '_val', '_marked_for_bp']

    def __new__(cls, val, marked=False):
        return float.__new__(cls, val)

    def __init__(self, val, marked=False):
        super(Number, self).__init__(marked=marked)
        self._node = Node(self)
        self._val = val

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return self.__str__()

    def get_data(self, dtype):
        """Get data of given type. Directly return the underlying value here."""
        return self._val

    def asnumpy(self):
        """ Get data in numpy compatible type """
        return self._val

    @property
    def val(self):
        """ return the underlying value """
        return self._val

    @property
    def node(self):
        """ get node which contains derivative information from this array """
        return self._node


class Array(Value):
    """Base array type.

    It provides convenient methods for arithmetic operations. The Array class
    is used for:
    1. Redirect all special member functions to corresponding pure function.
    2. Redirect normal member functions to correct member functions of
    underlying array object.
    """
    __slots__ = ['_node', '_data', '_latest_version', '_marked_for_bp']
    __array_priority__ = 100.0  # highest priority when compute with numpy.ndarray

    def __init__(self, data, marked=False):
        super(Array, self).__init__(marked)
        self._data = {}
        self._node = Node(self)
        atype = Array.to_array_type(data)
        self._data[atype] = data
        self._latest_version = atype

    @staticmethod
    def to_array_type(arr):
        """ Return the type enum of the given array """
        atype = type(arr)
        if atype == array_types['numpy']:
            return ArrayType.NUMPY
        elif atype == array_types['mxnet']:
            return ArrayType.MXNET
        else:
            raise UnknownArrayTypeError(
                'Array data of type {} unknown.'.format(atype))

    def __str__(self):
        return str(self.get_data(ArrayType.NUMPY))

    def __repr__(self):
        return self.__str__()

    @property
    def node(self):
        """ get node which contains derivative information from this array """
        return self._node

    def has_type(self, atype):
        """ Return whether array data of given type exists in the underlying storage.
        """
        return atype in self._data.keys()

    def reshape(self, *args, **kwargs):
        """ Function for reshape this array

        Usage example:
        Assume a = np.ones([10, 10])
        b = a.reshape([5, 20])
        b = a.reshape(5, 20)

        See http://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
        for further explanation.

        :param args: a single iterable or a sequence of ints representing a new shape
        :return: reshaped array (minpy array)
        """
        # Although this usage is not documented in numpy official doc, it is renowned and
        # widely used in practice
        if len(args) == 1 and isinstance(args[0], collections.Iterable):
            new_shape = args[0]
        else:
            new_shape = tuple(x for x in args)
        if 'order' in kwargs and kwargs['order'] != 'C':
            raise ValueError('Orders other than C are not currently supported.')
        return Value._ns.reshape(self, new_shape)

    def dot(self, b, out=None):
        """ Function for dot production. """
        if out is not None:
            # TODO: Support out argument
            raise ValueError('out option is not supported.')
        return Value._ns.dot(self, b)

    def _synchronize_data(self):
        """ Synchronize the data of different array types. """
        if self._latest_version == ArrayType.MXNET:
            _logger.info('Copy from mxnet array to numpy array Node#{}'.format(
                id(self)))
            mxarray = self._data[ArrayType.MXNET]
            self._data[ArrayType.NUMPY] = mxarray.asnumpy()
        elif self._latest_version == ArrayType.NUMPY:
            _logger.info('Copy from numpy array to mxnet array Node#{}'.format(
                id(self)))
            nparray = self._data[ArrayType.NUMPY]
            # pylint: disable= fixme
            # TODO currently, we only use one gpu
            # pylint: enable= fixme
            self._data[ArrayType.MXNET] = mxnet.ndarray.array(
                nparray, ctx=mxnet.gpu(0))
        self._latest_version = None

    def enforce_data(self, dtype):
        """Enforce array data of given type."""
        if self._latest_version is not None and self._latest_version != dtype:
            self._synchronize_data()
            self._latest_version = None

    def get_data(self, dtype):
        """Get array data of given type."""
        self.enforce_data(dtype)
        return self._data[dtype]

    def asnumpy(self):
        """Get raw NumPy array.

        This will return a copied array of numpy.ndarray type
        """
        return numpy.array(self.get_data(ArrayType.NUMPY))

    def get_data_mutable(self, dtype):
        """Get exclusive access to array data of given type."""
        if self._latest_version is not None and self._latest_version != dtype:
            self._synchronize_data()
        self._latest_version = dtype
        return self._data[dtype]

    @property
    def shape(self):
        """ Get the shape of array """
        if ArrayType.NUMPY in self._data:
            return self._data[ArrayType.NUMPY].shape
        else:
            return self._data[ArrayType.MXNET].shape

    def __getitem__(self, index):
        """NumPy indexing operations.

        Currently `mxnet.ndarray` does not support full indexing, so there is an implicit
        conversion to NumPy array.
        """
        np_index = None
        to_np = lambda x: x if isinstance(x, slice) else Value.wrap(x).get_data(ArrayType.NUMPY)
        if isinstance(index, tuple):
            np_index = tuple(to_np(i) for i in index)
        else:
            np_index = to_np(index)
        return Value._ns._minpy_getitem(self, np_index)

    def __setitem__(self, index, val):
        """NumPy indexing operations.

        Currently `mxnet.ndarray` does not support full indexing, so there is an implicit
        conversion to NumPy array. Also note that this operation breaks gradient chain.
        """
        np_index = None
        np_val = Value.wrap(val).get_data(ArrayType.NUMPY)
        to_np = lambda x: x if isinstance(x, slice) else Value.wrap(x).get_data(ArrayType.NUMPY)
        if isinstance(index, tuple):
            np_index = tuple(to_np(i) for i in index)
        else:
            np_index = to_np(index)
        np_array = self.get_data_mutable(ArrayType.NUMPY)
        np_array.__setitem__(np_index, np_val)

    def __delitem__(self, index):
        """NumPy indexing operations.

        Currently `mxnet.ndarray` does not support full indexing, so there is an implicit
        conversion to NumPy array.  Also note that this operation breaks gradient chain.
        """
        self.get_data_mutable(ArrayType.NUMPY).__delitem(index)

    # pylint: disable= invalid-name
    @property
    def T(self):
        """ Get transposed array """
        return Value._ns.transpose(self)
    # pylint: enable= invalid-name


class Primitive(object):
    """Class for primitives. It includes both forward function and gradient definition."""
    __slots__ = [
        '_func',
        '_grad_func',
        '_grad_func_kw',
        '_type',
        '_mutate_args',
        '_mutate_kw',
    ]

    def __init__(self, func, ty, mutate_args=None, mutate_kw=None):
        """Initialize.
        Args:
            func: A function that performs the action.
        """
        self._func = func
        self._grad_func = {}
        self._grad_func_kw = {}
        self._type = ty
        self._mutate_args = [] if mutate_args is None else mutate_args
        self._mutate_kw = [] if mutate_kw is None else mutate_kw

    @property
    def type(self):
        """ Return the type of the primitive (ArrayType.NUMPY or ArrayType.MXNET) """
        return self._type

    @property
    def typestr(self):
        """Return the string representation of primitive type.

        :return: String representation.
        """
        if self._type == ArrayType.NUMPY:
            return "NumPy"
        elif self._type == ArrayType.MXNET:
            return "MXNet"
        else:
            raise NotImplementedError()

    def __str__(self):
        return self._func.__name__

    def __call__(self, *args, **kwargs):
        """Call wrapped function.

        :param args: Arguments for the wrapped function.
        :param kwargs: Arguments for the wrapped function.
        :return: An :class:`array.Value` representing the result.
        :raises IndexError: No corresponding gradient function.
        :raises KeyError: No corresponding gradient function.
        """
        # pylint: disable= missing-docstring, invalid-name
        _logger.debug('Calling {} type {}.'.format(self._func, self.typestr))

        def get_val(x, mutate):
            try:
                xv = Value.wrap(x)
                if mutate:
                    return xv.get_data_mutable(self._type)
                else:
                    return xv.get_data(self._type)
            # If wrap failed, just return the original value.
            except UnknownArrayTypeError:
                return x
        # Get underlying data.
        arg_values = tuple(
            get_val(args[i], i in self._mutate_args) for i in range(len(args)))
        kwargs_values = {
            k: get_val(kwargs[k], k in self._mutate_kw)
            for k in kwargs
        }
        # Call the real function with raw value.
        if self.type == ArrayType.MXNET:
            # Currently all MXNet function call will be performed on GPU 0.
            with mxnet.gpu(0) as ctx:
                result_value = self._func(*arg_values, **kwargs_values)
        else:
            result_value = self._func(*arg_values, **kwargs_values)
        # if you want to do profiling, try to use minprof(<func>):
        # result_value = minprof(self._func)(*arg_values, **kwargs_values)

        # whether the result is on the bp path
        def scan(accum, x):
            if isinstance(x, Value):
                return operator.or_(accum, x._marked_for_bp)
            else:
                return accum
        # Check whether the result value is on the path of bp phase
        # If all the input arguments are not on the bp path, the result value
        # is not as well.
        need_bp = functools.reduce(scan, itertools.chain(
            args, kwargs.values()), False)
        # Wrap the result raw value with wrapper and node.
        result = Value.wrap(result_value, marked=need_bp)
        if need_bp:
            # Record partial derivative paths, only for `Value` type values.
            # If no gradient function is defined, also omit it
            for i, arg in enumerate(args):
                if isinstance(arg, Value) and arg.marked_for_bp:
                    if i >= len(self._grad_func):
                        _logger.warn('Partial derivative of func "{}" on #{} \
                            arg is not defined.'
                                     .format(self._func.__name__, i))
                        continue
                    _logger.debug(
                        'Adding partial derivative to func "{}" on #{} arg.'.format(
                            self._func, i))
                    arg.node.add_partial_derivative(self._grad_func[i](
                        result_value, *arg_values, **kwargs_values),
                                                    result.node, self)
            for k, arg in kwargs.items():
                if isinstance(arg, Value) and arg.marked_for_bp:
                    if k not in self._grad_func_kw:
                        _logger.warn(
                            'Partial derivative of func "{}" on kwarg "{}"\
                            is not defined.'.format(self._func.__name__, k))
                        continue
                    _logger.debug(
                        'Adding partial derivative to func "{}" on kwarg "{}".'.format(
                            self._func, k))
                    arg.node.add_partial_derivative(self._grad_func_kw[k](
                        result_value, *arg_values, **kwargs_values),
                                                    result.node, self)
        return result
        # pylint: enable= missing-docstring, invalid-name

    def def_grad(self, func, argnum=0):
        """Define gradient function.

        :param func: Gradient function.
        :param argnum: Index of the argument.
        :return: Self.
        """
        self._grad_func[argnum] = func
        return self

    def def_grad_kw(self, func, key):
        """Define gradient function.

        :param func: Gradient function.
        :param key: Key name of the argument.
        :return: Self.
        """
        self._grad_func_kw[key] = func
        return self

    def def_grad_zero(self, argnum=0):
        """Define zero gradient

        :param argnum: Index of the argument.
        :return: Self.
        """
        self._grad_func[argnum] = lambda *args, **kwargs: lambda g: 0.0
        return self

    def gradable(self, bp_args, bp_kwargs):
        """Return whether the primitive has gradient function defined.

        :param tuple bp_args: Positional arguments that need back propagation.
        :param tuple bp_kwargs: Keyword arguments that need back propagation.
        :return: Whether all the arguments have gradients defined.
        """
        for i in bp_args:
            if i not in self._grad_func:
                return False
        for i in bp_kwargs:
            if i not in self._grad_func_kw:
                return False
        return True
