# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _tinysplinepython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_tinysplinepython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_tinysplinepython')
    _tinysplinepython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_tinysplinepython', [dirname(__file__)])
        except ImportError:
            import _tinysplinepython
            return _tinysplinepython
        try:
            _mod = imp.load_module('_tinysplinepython', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _tinysplinepython = swig_import_helper()
    del swig_import_helper
else:
    import _tinysplinepython
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


FLT_MAX_ABS_ERROR = _tinysplinepython.FLT_MAX_ABS_ERROR
FLT_MAX_REL_ERROR = _tinysplinepython.FLT_MAX_REL_ERROR
NONE = _tinysplinepython.NONE
OPENED = _tinysplinepython.OPENED
CLAMPED = _tinysplinepython.CLAMPED
BEZIERS = _tinysplinepython.BEZIERS

def ts_bspline_degree(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_degree(spline)
ts_bspline_degree = _tinysplinepython.ts_bspline_degree

def ts_bspline_set_degree(spline: 'tsBSpline *', deg: 'size_t') -> "tsError":
    return _tinysplinepython.ts_bspline_set_degree(spline, deg)
ts_bspline_set_degree = _tinysplinepython.ts_bspline_set_degree

def ts_bspline_order(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_order(spline)
ts_bspline_order = _tinysplinepython.ts_bspline_order

def ts_bspline_set_order(spline: 'tsBSpline *', order: 'size_t') -> "tsError":
    return _tinysplinepython.ts_bspline_set_order(spline, order)
ts_bspline_set_order = _tinysplinepython.ts_bspline_set_order

def ts_bspline_dimension(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_dimension(spline)
ts_bspline_dimension = _tinysplinepython.ts_bspline_dimension

def ts_bspline_set_dimension(spline: 'tsBSpline *', dim: 'size_t') -> "tsError":
    return _tinysplinepython.ts_bspline_set_dimension(spline, dim)
ts_bspline_set_dimension = _tinysplinepython.ts_bspline_set_dimension

def ts_bspline_len_control_points(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_len_control_points(spline)
ts_bspline_len_control_points = _tinysplinepython.ts_bspline_len_control_points

def ts_bspline_num_control_points(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_num_control_points(spline)
ts_bspline_num_control_points = _tinysplinepython.ts_bspline_num_control_points

def ts_bspline_sof_control_points(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_sof_control_points(spline)
ts_bspline_sof_control_points = _tinysplinepython.ts_bspline_sof_control_points

def ts_bspline_control_points(spline: 'tsBSpline const *', ctrlp: 'tsReal **') -> "tsError":
    return _tinysplinepython.ts_bspline_control_points(spline, ctrlp)
ts_bspline_control_points = _tinysplinepython.ts_bspline_control_points

def ts_bspline_set_control_points(spline: 'tsBSpline *', ctrlp: 'tsReal const *') -> "tsError":
    return _tinysplinepython.ts_bspline_set_control_points(spline, ctrlp)
ts_bspline_set_control_points = _tinysplinepython.ts_bspline_set_control_points

def ts_bspline_num_knots(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_num_knots(spline)
ts_bspline_num_knots = _tinysplinepython.ts_bspline_num_knots

def ts_bspline_sof_knots(spline: 'tsBSpline const *') -> "size_t":
    return _tinysplinepython.ts_bspline_sof_knots(spline)
ts_bspline_sof_knots = _tinysplinepython.ts_bspline_sof_knots

def ts_bspline_knots(spline: 'tsBSpline const *', knots: 'tsReal **') -> "tsError":
    return _tinysplinepython.ts_bspline_knots(spline, knots)
ts_bspline_knots = _tinysplinepython.ts_bspline_knots

def ts_bspline_set_knots(spline: 'tsBSpline *', knots: 'tsReal const *') -> "tsError":
    return _tinysplinepython.ts_bspline_set_knots(spline, knots)
ts_bspline_set_knots = _tinysplinepython.ts_bspline_set_knots

def ts_deboornet_knot(net: 'tsDeBoorNet const *') -> "tsReal":
    return _tinysplinepython.ts_deboornet_knot(net)
ts_deboornet_knot = _tinysplinepython.ts_deboornet_knot

def ts_deboornet_index(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_index(net)
ts_deboornet_index = _tinysplinepython.ts_deboornet_index

def ts_deboornet_multiplicity(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_multiplicity(net)
ts_deboornet_multiplicity = _tinysplinepython.ts_deboornet_multiplicity

def ts_deboornet_num_insertions(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_num_insertions(net)
ts_deboornet_num_insertions = _tinysplinepython.ts_deboornet_num_insertions

def ts_deboornet_dimension(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_dimension(net)
ts_deboornet_dimension = _tinysplinepython.ts_deboornet_dimension

def ts_deboornet_len_points(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_len_points(net)
ts_deboornet_len_points = _tinysplinepython.ts_deboornet_len_points

def ts_deboornet_num_points(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_num_points(net)
ts_deboornet_num_points = _tinysplinepython.ts_deboornet_num_points

def ts_deboornet_sof_points(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_sof_points(net)
ts_deboornet_sof_points = _tinysplinepython.ts_deboornet_sof_points

def ts_deboornet_points(net: 'tsDeBoorNet const *', points: 'tsReal **') -> "tsError":
    return _tinysplinepython.ts_deboornet_points(net, points)
ts_deboornet_points = _tinysplinepython.ts_deboornet_points

def ts_deboornet_len_result(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_len_result(net)
ts_deboornet_len_result = _tinysplinepython.ts_deboornet_len_result

def ts_deboornet_num_result(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_num_result(net)
ts_deboornet_num_result = _tinysplinepython.ts_deboornet_num_result

def ts_deboornet_sof_result(net: 'tsDeBoorNet const *') -> "size_t":
    return _tinysplinepython.ts_deboornet_sof_result(net)
ts_deboornet_sof_result = _tinysplinepython.ts_deboornet_sof_result

def ts_deboornet_result(net: 'tsDeBoorNet const *', result: 'tsReal **') -> "tsError":
    return _tinysplinepython.ts_deboornet_result(net, result)
ts_deboornet_result = _tinysplinepython.ts_deboornet_result

def ts_bspline_new(num_control_points: 'size_t', dimension: 'size_t', degree: 'size_t', type: 'tsBSplineType', _spline_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_new(num_control_points, dimension, degree, type, _spline_)
ts_bspline_new = _tinysplinepython.ts_bspline_new

def ts_bspline_copy(original: 'tsBSpline const *', _copy_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_copy(original, _copy_)
ts_bspline_copy = _tinysplinepython.ts_bspline_copy

def ts_bspline_move(arg1: 'tsBSpline *', _to_: 'tsBSpline *') -> "void":
    return _tinysplinepython.ts_bspline_move(arg1, _to_)
ts_bspline_move = _tinysplinepython.ts_bspline_move

def ts_bspline_free(_spline_: 'tsBSpline *') -> "void":
    return _tinysplinepython.ts_bspline_free(_spline_)
ts_bspline_free = _tinysplinepython.ts_bspline_free

def ts_deboornet_copy(original: 'tsDeBoorNet const *', _copy_: 'tsDeBoorNet *') -> "tsError":
    return _tinysplinepython.ts_deboornet_copy(original, _copy_)
ts_deboornet_copy = _tinysplinepython.ts_deboornet_copy

def ts_deboornet_move(arg1: 'tsDeBoorNet *', _to_: 'tsDeBoorNet *') -> "void":
    return _tinysplinepython.ts_deboornet_move(arg1, _to_)
ts_deboornet_move = _tinysplinepython.ts_deboornet_move

def ts_deboornet_free(_net_: 'tsDeBoorNet *') -> "void":
    return _tinysplinepython.ts_deboornet_free(_net_)
ts_deboornet_free = _tinysplinepython.ts_deboornet_free

def ts_bspline_interpolate_cubic(points: 'tsReal const *', n: 'size_t', dim: 'size_t', _spline_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_interpolate_cubic(points, n, dim, _spline_)
ts_bspline_interpolate_cubic = _tinysplinepython.ts_bspline_interpolate_cubic

def ts_bspline_eval(spline: 'tsBSpline const *', u: 'tsReal', _deBoorNet_: 'tsDeBoorNet *') -> "tsError":
    return _tinysplinepython.ts_bspline_eval(spline, u, _deBoorNet_)
ts_bspline_eval = _tinysplinepython.ts_bspline_eval

def ts_bspline_derive(spline: 'tsBSpline const *', n: 'size_t', _derivative_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_derive(spline, n, _derivative_)
ts_bspline_derive = _tinysplinepython.ts_bspline_derive

def ts_bspline_fill_knots(spline: 'tsBSpline const *', type: 'tsBSplineType', min: 'tsReal', max: 'tsReal', _result_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_fill_knots(spline, type, min, max, _result_)
ts_bspline_fill_knots = _tinysplinepython.ts_bspline_fill_knots

def ts_bspline_insert_knot(spline: 'tsBSpline const *', u: 'tsReal', n: 'size_t', _result_: 'tsBSpline *', _k_: 'size_t *') -> "tsError":
    return _tinysplinepython.ts_bspline_insert_knot(spline, u, n, _result_, _k_)
ts_bspline_insert_knot = _tinysplinepython.ts_bspline_insert_knot

def ts_bspline_resize(spline: 'tsBSpline const *', num_control_points: 'int', back: 'int', _resized_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_resize(spline, num_control_points, back, _resized_)
ts_bspline_resize = _tinysplinepython.ts_bspline_resize

def ts_bspline_split(spline: 'tsBSpline const *', u: 'tsReal', _split_: 'tsBSpline *', _k_: 'size_t *') -> "tsError":
    return _tinysplinepython.ts_bspline_split(spline, u, _split_, _k_)
ts_bspline_split = _tinysplinepython.ts_bspline_split

def ts_bspline_buckle(spline: 'tsBSpline const *', b: 'tsReal', _buckled_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_buckle(spline, b, _buckled_)
ts_bspline_buckle = _tinysplinepython.ts_bspline_buckle

def ts_bspline_to_beziers(spline: 'tsBSpline const *', _beziers_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_to_beziers(spline, _beziers_)
ts_bspline_to_beziers = _tinysplinepython.ts_bspline_to_beziers

def ts_bspline_to_json(spline: 'tsBSpline const *', _json_: 'char **') -> "tsError":
    return _tinysplinepython.ts_bspline_to_json(spline, _json_)
ts_bspline_to_json = _tinysplinepython.ts_bspline_to_json

def ts_bspline_from_json(json: 'char const *', _spline_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_from_json(json, _spline_)
ts_bspline_from_json = _tinysplinepython.ts_bspline_from_json

def ts_bspline_save_json(spline: 'tsBSpline const *', path: 'char const *') -> "tsError":
    return _tinysplinepython.ts_bspline_save_json(spline, path)
ts_bspline_save_json = _tinysplinepython.ts_bspline_save_json

def ts_bspline_load_json(path: 'char const *', _spline_: 'tsBSpline *') -> "tsError":
    return _tinysplinepython.ts_bspline_load_json(path, _spline_)
ts_bspline_load_json = _tinysplinepython.ts_bspline_load_json

def ts_fequals(x: 'tsReal', y: 'tsReal') -> "int":
    return _tinysplinepython.ts_fequals(x, y)
ts_fequals = _tinysplinepython.ts_fequals

def ts_enum_str(err: 'tsError') -> "char const *":
    return _tinysplinepython.ts_enum_str(err)
ts_enum_str = _tinysplinepython.ts_enum_str

def ts_str_enum(str: 'char const *') -> "tsError":
    return _tinysplinepython.ts_str_enum(str)
ts_str_enum = _tinysplinepython.ts_str_enum

def ts_arr_fill(arr: 'tsReal *', num: 'size_t', val: 'tsReal') -> "void":
    return _tinysplinepython.ts_arr_fill(arr, num, val)
ts_arr_fill = _tinysplinepython.ts_arr_fill

def ts_ctrlp_dist2(x: 'tsReal const *', y: 'tsReal const *', dim: 'size_t') -> "tsReal":
    return _tinysplinepython.ts_ctrlp_dist2(x, y, dim)
ts_ctrlp_dist2 = _tinysplinepython.ts_ctrlp_dist2
class DeBoorNet(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, other: 'DeBoorNet'):
        _tinysplinepython.DeBoorNet_swiginit(self, _tinysplinepython.new_DeBoorNet(other))
    __swig_destroy__ = _tinysplinepython.delete_DeBoorNet
    knot = _swig_property(_tinysplinepython.DeBoorNet_knot_get)
    index = _swig_property(_tinysplinepython.DeBoorNet_index_get)
    multiplicity = _swig_property(_tinysplinepython.DeBoorNet_multiplicity_get)
    numInsertions = _swig_property(_tinysplinepython.DeBoorNet_numInsertions_get)
    dimension = _swig_property(_tinysplinepython.DeBoorNet_dimension_get)
    points = _swig_property(_tinysplinepython.DeBoorNet_points_get)
    result = _swig_property(_tinysplinepython.DeBoorNet_result_get)
DeBoorNet_swigregister = _tinysplinepython.DeBoorNet_swigregister
DeBoorNet_swigregister(DeBoorNet)

class BSpline(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _tinysplinepython.BSpline_swiginit(self, _tinysplinepython.new_BSpline(*args))
    __swig_destroy__ = _tinysplinepython.delete_BSpline
    degree = _swig_property(_tinysplinepython.BSpline_degree_get)
    order = _swig_property(_tinysplinepython.BSpline_order_get)
    dimension = _swig_property(_tinysplinepython.BSpline_dimension_get)
    controlPoints = _swig_property(_tinysplinepython.BSpline_controlPoints_get, _tinysplinepython.BSpline_controlPoints_set)
    knots = _swig_property(_tinysplinepython.BSpline_knots_get, _tinysplinepython.BSpline_knots_set)
BSpline.__call__ = new_instancemethod(_tinysplinepython.BSpline___call__, None, BSpline)
BSpline.eval = new_instancemethod(_tinysplinepython.BSpline_eval, None, BSpline)
BSpline.toJSON = new_instancemethod(_tinysplinepython.BSpline_toJSON, None, BSpline)
BSpline.fromJSON = new_instancemethod(_tinysplinepython.BSpline_fromJSON, None, BSpline)
BSpline.save = new_instancemethod(_tinysplinepython.BSpline_save, None, BSpline)
BSpline.load = new_instancemethod(_tinysplinepython.BSpline_load, None, BSpline)
BSpline.fillKnots = new_instancemethod(_tinysplinepython.BSpline_fillKnots, None, BSpline)
BSpline.insertKnot = new_instancemethod(_tinysplinepython.BSpline_insertKnot, None, BSpline)
BSpline.resize = new_instancemethod(_tinysplinepython.BSpline_resize, None, BSpline)
BSpline.split = new_instancemethod(_tinysplinepython.BSpline_split, None, BSpline)
BSpline.buckle = new_instancemethod(_tinysplinepython.BSpline_buckle, None, BSpline)
BSpline.toBeziers = new_instancemethod(_tinysplinepython.BSpline_toBeziers, None, BSpline)
BSpline.derive = new_instancemethod(_tinysplinepython.BSpline_derive, None, BSpline)
BSpline_swigregister = _tinysplinepython.BSpline_swigregister
BSpline_swigregister(BSpline)

class Utils(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    interpolateCubic = staticmethod(_tinysplinepython.Utils_interpolateCubic)
    fequals = staticmethod(_tinysplinepython.Utils_fequals)
    enum_str = staticmethod(_tinysplinepython.Utils_enum_str)
    str_enum = staticmethod(_tinysplinepython.Utils_str_enum)
    __swig_destroy__ = _tinysplinepython.delete_Utils
Utils_swigregister = _tinysplinepython.Utils_swigregister
Utils_swigregister(Utils)

def Utils_interpolateCubic(points: 'std::vector< tinyspline::real,std::allocator< tinyspline::real > > const *', dim: 'size_t') -> "tinyspline::BSpline":
    return _tinysplinepython.Utils_interpolateCubic(points, dim)
Utils_interpolateCubic = _tinysplinepython.Utils_interpolateCubic

def Utils_fequals(x: 'tinyspline::real', y: 'tinyspline::real') -> "bool":
    return _tinysplinepython.Utils_fequals(x, y)
Utils_fequals = _tinysplinepython.Utils_fequals

def Utils_enum_str(err: 'tsError') -> "std::string":
    return _tinysplinepython.Utils_enum_str(err)
Utils_enum_str = _tinysplinepython.Utils_enum_str

def Utils_str_enum(str: 'std::string') -> "tsError":
    return _tinysplinepython.Utils_str_enum(str)
Utils_str_enum = _tinysplinepython.Utils_str_enum

class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _tinysplinepython.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_tinysplinepython.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_tinysplinepython.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_tinysplinepython.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_tinysplinepython.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_tinysplinepython.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_tinysplinepython.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_tinysplinepython.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_tinysplinepython.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_tinysplinepython.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_tinysplinepython.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_tinysplinepython.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_tinysplinepython.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_tinysplinepython.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_tinysplinepython.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_tinysplinepython.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_tinysplinepython.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _tinysplinepython.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


