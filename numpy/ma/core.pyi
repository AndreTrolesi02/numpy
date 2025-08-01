# pyright: reportIncompatibleMethodOverride=false
# ruff: noqa: ANN001, ANN002, ANN003, ANN201, ANN202 ANN204, ANN401

from _typeshed import Incomplete
from collections.abc import Sequence
from typing import (
    Any,
    Literal,
    Never,
    NoReturn,
    Self,
    SupportsIndex,
    TypeAlias,
    overload,
)
from typing_extensions import TypeIs, TypeVar

import numpy as np
from numpy import (
    _AnyShapeT,
    _HasDType,
    _HasDTypeWithRealAndImag,
    _ModeKind,
    _OrderACF,
    _OrderKACF,
    _PartitionKind,
    _SortKind,
    _ToIndices,
    amax,
    amin,
    bool_,
    bytes_,
    character,
    complex128,
    complexfloating,
    datetime64,
    dtype,
    dtypes,
    expand_dims,
    float16,
    float32,
    float64,
    floating,
    generic,
    inexact,
    int8,
    int64,
    int_,
    integer,
    intp,
    ndarray,
    number,
    object_,
    signedinteger,
    str_,
    timedelta64,
    unsignedinteger,
    void,
)
from numpy._globals import _NoValueType
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _32Bit,
    _64Bit,
    _AnyShape,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeBytes_co,
    _ArrayLikeComplex128_co,
    _ArrayLikeComplex_co,
    _ArrayLikeDT64_co,
    _ArrayLikeFloat64_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt,
    _ArrayLikeInt_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
    _ArrayLikeStr_co,
    _ArrayLikeString_co,
    _ArrayLikeTD64_co,
    _ArrayLikeUInt_co,
    _DTypeLike,
    _DTypeLikeBool,
    _IntLike_co,
    _ScalarLike_co,
    _Shape,
    _ShapeLike,
)
from numpy._typing._dtype_like import _VoidDTypeLike

__all__ = [
    "MAError",
    "MaskError",
    "MaskType",
    "MaskedArray",
    "abs",
    "absolute",
    "add",
    "all",
    "allclose",
    "allequal",
    "alltrue",
    "amax",
    "amin",
    "angle",
    "anom",
    "anomalies",
    "any",
    "append",
    "arange",
    "arccos",
    "arccosh",
    "arcsin",
    "arcsinh",
    "arctan",
    "arctan2",
    "arctanh",
    "argmax",
    "argmin",
    "argsort",
    "around",
    "array",
    "asanyarray",
    "asarray",
    "bitwise_and",
    "bitwise_or",
    "bitwise_xor",
    "bool_",
    "ceil",
    "choose",
    "clip",
    "common_fill_value",
    "compress",
    "compressed",
    "concatenate",
    "conjugate",
    "convolve",
    "copy",
    "correlate",
    "cos",
    "cosh",
    "count",
    "cumprod",
    "cumsum",
    "default_fill_value",
    "diag",
    "diagonal",
    "diff",
    "divide",
    "empty",
    "empty_like",
    "equal",
    "exp",
    "expand_dims",
    "fabs",
    "filled",
    "fix_invalid",
    "flatten_mask",
    "flatten_structured_array",
    "floor",
    "floor_divide",
    "fmod",
    "frombuffer",
    "fromflex",
    "fromfunction",
    "getdata",
    "getmask",
    "getmaskarray",
    "greater",
    "greater_equal",
    "harden_mask",
    "hypot",
    "identity",
    "ids",
    "indices",
    "inner",
    "innerproduct",
    "isMA",
    "isMaskedArray",
    "is_mask",
    "is_masked",
    "isarray",
    "left_shift",
    "less",
    "less_equal",
    "log",
    "log2",
    "log10",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "make_mask",
    "make_mask_descr",
    "make_mask_none",
    "mask_or",
    "masked",
    "masked_array",
    "masked_equal",
    "masked_greater",
    "masked_greater_equal",
    "masked_inside",
    "masked_invalid",
    "masked_less",
    "masked_less_equal",
    "masked_not_equal",
    "masked_object",
    "masked_outside",
    "masked_print_option",
    "masked_singleton",
    "masked_values",
    "masked_where",
    "max",
    "maximum",
    "maximum_fill_value",
    "mean",
    "min",
    "minimum",
    "minimum_fill_value",
    "mod",
    "multiply",
    "mvoid",
    "ndim",
    "negative",
    "nomask",
    "nonzero",
    "not_equal",
    "ones",
    "ones_like",
    "outer",
    "outerproduct",
    "power",
    "prod",
    "product",
    "ptp",
    "put",
    "putmask",
    "ravel",
    "remainder",
    "repeat",
    "reshape",
    "resize",
    "right_shift",
    "round",
    "round_",
    "set_fill_value",
    "shape",
    "sin",
    "sinh",
    "size",
    "soften_mask",
    "sometrue",
    "sort",
    "sqrt",
    "squeeze",
    "std",
    "subtract",
    "sum",
    "swapaxes",
    "take",
    "tan",
    "tanh",
    "trace",
    "transpose",
    "true_divide",
    "var",
    "where",
    "zeros",
    "zeros_like",
]

_ShapeT = TypeVar("_ShapeT", bound=_Shape)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_Shape, default=_AnyShape, covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=dtype)
_DTypeT_co = TypeVar("_DTypeT_co", bound=dtype, default=dtype, covariant=True)
_ArrayT = TypeVar("_ArrayT", bound=ndarray[Any, Any])
_ScalarT = TypeVar("_ScalarT", bound=generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=generic, covariant=True)
_NumberT = TypeVar("_NumberT", bound=number)
_RealNumberT = TypeVar("_RealNumberT", bound=floating | integer)
# A subset of `MaskedArray` that can be parametrized w.r.t. `np.generic`
_MaskedArray: TypeAlias = MaskedArray[_AnyShape, dtype[_ScalarT]]

_MaskedArrayUInt_co: TypeAlias = _MaskedArray[unsignedinteger | np.bool]
_MaskedArrayInt_co: TypeAlias = _MaskedArray[integer | np.bool]
_MaskedArrayFloat64_co: TypeAlias = _MaskedArray[floating[_64Bit] | float32 | float16 | integer | np.bool]
_MaskedArrayFloat_co: TypeAlias = _MaskedArray[floating | integer | np.bool]
_MaskedArrayComplex128_co: TypeAlias = _MaskedArray[number[_64Bit] | number[_32Bit] | float16 | integer | np.bool]
_MaskedArrayComplex_co: TypeAlias = _MaskedArray[inexact | integer | np.bool]
_MaskedArrayNumber_co: TypeAlias = _MaskedArray[number | np.bool]
_MaskedArrayTD64_co: TypeAlias = _MaskedArray[timedelta64 | integer | np.bool]

_ArrayInt_co: TypeAlias = NDArray[integer | bool_]
_Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_ScalarT]]

MaskType = bool_
nomask: bool_[Literal[False]]

class MaskedArrayFutureWarning(FutureWarning): ...
class MAError(Exception): ...
class MaskError(MAError): ...

def default_fill_value(obj): ...
def minimum_fill_value(obj): ...
def maximum_fill_value(obj): ...
def set_fill_value(a, fill_value): ...
def common_fill_value(a, b): ...
@overload
def filled(a: ndarray[_ShapeT_co, _DTypeT_co], fill_value: _ScalarLike_co | None = None) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
@overload
def filled(a: _ArrayLike[_ScalarT_co], fill_value: _ScalarLike_co | None = None) -> NDArray[_ScalarT_co]: ...
@overload
def filled(a: ArrayLike, fill_value: _ScalarLike_co | None = None) -> NDArray[Any]: ...
def getdata(a, subok=...): ...
get_data = getdata

def fix_invalid(a, mask=..., copy=..., fill_value=...): ...

class _MaskedUFunc:
    f: Any
    __doc__: Any
    __name__: Any
    def __init__(self, ufunc): ...

class _MaskedUnaryOperation(_MaskedUFunc):
    fill: Any
    domain: Any
    def __init__(self, mufunc, fill=..., domain=...): ...
    def __call__(self, a, *args, **kwargs): ...

class _MaskedBinaryOperation(_MaskedUFunc):
    fillx: Any
    filly: Any
    def __init__(self, mbfunc, fillx=..., filly=...): ...
    def __call__(self, a, b, *args, **kwargs): ...
    def reduce(self, target, axis=..., dtype=...): ...
    def outer(self, a, b): ...
    def accumulate(self, target, axis=...): ...

class _DomainedBinaryOperation(_MaskedUFunc):
    domain: Any
    fillx: Any
    filly: Any
    def __init__(self, dbfunc, domain, fillx=..., filly=...): ...
    def __call__(self, a, b, *args, **kwargs): ...

exp: _MaskedUnaryOperation
conjugate: _MaskedUnaryOperation
sin: _MaskedUnaryOperation
cos: _MaskedUnaryOperation
arctan: _MaskedUnaryOperation
arcsinh: _MaskedUnaryOperation
sinh: _MaskedUnaryOperation
cosh: _MaskedUnaryOperation
tanh: _MaskedUnaryOperation
abs: _MaskedUnaryOperation
absolute: _MaskedUnaryOperation
angle: _MaskedUnaryOperation
fabs: _MaskedUnaryOperation
negative: _MaskedUnaryOperation
floor: _MaskedUnaryOperation
ceil: _MaskedUnaryOperation
around: _MaskedUnaryOperation
logical_not: _MaskedUnaryOperation
sqrt: _MaskedUnaryOperation
log: _MaskedUnaryOperation
log2: _MaskedUnaryOperation
log10: _MaskedUnaryOperation
tan: _MaskedUnaryOperation
arcsin: _MaskedUnaryOperation
arccos: _MaskedUnaryOperation
arccosh: _MaskedUnaryOperation
arctanh: _MaskedUnaryOperation

add: _MaskedBinaryOperation
subtract: _MaskedBinaryOperation
multiply: _MaskedBinaryOperation
arctan2: _MaskedBinaryOperation
equal: _MaskedBinaryOperation
not_equal: _MaskedBinaryOperation
less_equal: _MaskedBinaryOperation
greater_equal: _MaskedBinaryOperation
less: _MaskedBinaryOperation
greater: _MaskedBinaryOperation
logical_and: _MaskedBinaryOperation
def alltrue(target: ArrayLike, axis: SupportsIndex | None = 0, dtype: _DTypeLikeBool | None = None) -> Incomplete: ...
logical_or: _MaskedBinaryOperation
def sometrue(target: ArrayLike, axis: SupportsIndex | None = 0, dtype: _DTypeLikeBool | None = None) -> Incomplete: ...
logical_xor: _MaskedBinaryOperation
bitwise_and: _MaskedBinaryOperation
bitwise_or: _MaskedBinaryOperation
bitwise_xor: _MaskedBinaryOperation
hypot: _MaskedBinaryOperation

divide: _DomainedBinaryOperation
true_divide: _DomainedBinaryOperation
floor_divide: _DomainedBinaryOperation
remainder: _DomainedBinaryOperation
fmod: _DomainedBinaryOperation
mod: _DomainedBinaryOperation

def make_mask_descr(ndtype): ...

@overload
def getmask(a: _ScalarLike_co) -> bool_: ...
@overload
def getmask(a: MaskedArray[_ShapeT_co, Any]) -> np.ndarray[_ShapeT_co, dtype[bool_]] | bool_: ...
@overload
def getmask(a: ArrayLike) -> NDArray[bool_] | bool_: ...

get_mask = getmask

def getmaskarray(arr): ...

# It's sufficient for `m` to have dtype with type: `type[np.bool_]`,
# which isn't necessarily a ndarray. Please open an issue if this causes issues.
def is_mask(m: object) -> TypeIs[NDArray[bool_]]: ...

def make_mask(m, copy=..., shrink=..., dtype=...): ...
def make_mask_none(newshape, dtype=...): ...
def mask_or(m1, m2, copy=..., shrink=...): ...
def flatten_mask(mask): ...
def masked_where(condition, a, copy=...): ...
def masked_greater(x, value, copy=...): ...
def masked_greater_equal(x, value, copy=...): ...
def masked_less(x, value, copy=...): ...
def masked_less_equal(x, value, copy=...): ...
def masked_not_equal(x, value, copy=...): ...
def masked_equal(x, value, copy=...): ...
def masked_inside(x, v1, v2, copy=...): ...
def masked_outside(x, v1, v2, copy=...): ...
def masked_object(x, value, copy=..., shrink=...): ...
def masked_values(x, value, rtol=..., atol=..., copy=..., shrink=...): ...
def masked_invalid(a, copy=...): ...

class _MaskedPrintOption:
    def __init__(self, display): ...
    def display(self): ...
    def set_display(self, s): ...
    def enabled(self): ...
    def enable(self, shrink=...): ...

masked_print_option: _MaskedPrintOption

def flatten_structured_array(a): ...

class MaskedIterator:
    ma: Any
    dataiter: Any
    maskiter: Any
    def __init__(self, ma): ...
    def __iter__(self): ...
    def __getitem__(self, indx): ...
    def __setitem__(self, index, value): ...
    def __next__(self): ...

class MaskedArray(ndarray[_ShapeT_co, _DTypeT_co]):
    __array_priority__: Any
    @overload
    def __new__(
        cls,
        data: _ArrayLike[_ScalarT],
        mask: _ArrayLikeBool_co = nomask,
        dtype: None = None,
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _MaskedArray[_ScalarT]: ...
    @overload
    def __new__(
        cls,
        data: object,
        mask: _ArrayLikeBool_co,
        dtype: _DTypeLike[_ScalarT],
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _MaskedArray[_ScalarT]: ...
    @overload
    def __new__(
        cls,
        data: object,
        mask: _ArrayLikeBool_co = nomask,
        *,
        dtype: _DTypeLike[_ScalarT],
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _MaskedArray[_ScalarT]: ...
    @overload
    def __new__(
        cls,
        data: object,
        mask: _ArrayLikeBool_co = nomask,
        dtype: DTypeLike | None = None,
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _MaskedArray[Any]: ...

    def __array_finalize__(self, obj): ...
    def __array_wrap__(self, obj, context=..., return_scalar=...): ...

    @overload  # ()
    def view(self, /, dtype: None = None, type: None = None, fill_value: _ScalarLike_co | None = None) -> Self: ...
    @overload  # (dtype: DTypeT)
    def view(
        self,
        /,
        dtype: _DTypeT | _HasDType[_DTypeT],
        type: None = None,
        fill_value: _ScalarLike_co | None = None
    ) -> MaskedArray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[ScalarT])
    def view(
        self,
        /,
        dtype: _DTypeLike[_ScalarT],
        type: None = None,
        fill_value: _ScalarLike_co | None = None
    ) -> MaskedArray[_ShapeT_co, dtype[_ScalarT]]: ...
    @overload  # ([dtype: _, ]*, type: ArrayT)
    def view(
        self,
        /,
        dtype: DTypeLike | None = None,
        *,
        type: type[_ArrayT],
        fill_value: _ScalarLike_co | None = None
    ) -> _ArrayT: ...
    @overload  # (dtype: _, type: ArrayT)
    def view(self, /, dtype: DTypeLike | None, type: type[_ArrayT], fill_value: _ScalarLike_co | None = None) -> _ArrayT: ...
    @overload  # (dtype: ArrayT, /)
    def view(self, /, dtype: type[_ArrayT], type: None = None, fill_value: _ScalarLike_co | None = None) -> _ArrayT: ...
    @overload  # (dtype: ?)
    def view(
        self,
        /,
        # `_VoidDTypeLike | str | None` is like `DTypeLike` but without `_DTypeLike[Any]` to avoid
        # overlaps with previous overloads.
        dtype: _VoidDTypeLike | str | None,
        type: None = None,
        fill_value: _ScalarLike_co | None = None
    ) -> MaskedArray[_ShapeT_co, dtype]: ...

    # Keep in sync with `ndarray.__getitem__`
    @overload
    def __getitem__(self, key: _ArrayInt_co | tuple[_ArrayInt_co, ...], /) -> MaskedArray[_AnyShape, _DTypeT_co]: ...
    @overload
    def __getitem__(self, key: SupportsIndex | tuple[SupportsIndex, ...], /) -> Any: ...
    @overload
    def __getitem__(self, key: _ToIndices, /) -> MaskedArray[_AnyShape, _DTypeT_co]: ...
    @overload
    def __getitem__(self: _MaskedArray[void], indx: str, /) -> MaskedArray[_ShapeT_co, dtype]: ...
    @overload
    def __getitem__(self: _MaskedArray[void], indx: list[str], /) -> MaskedArray[_ShapeT_co, dtype[void]]: ...

    @property
    def shape(self) -> _ShapeT_co: ...
    @shape.setter
    def shape(self: MaskedArray[_ShapeT, Any], shape: _ShapeT, /) -> None: ...
    def __setmask__(self, mask: _ArrayLikeBool_co, copy: bool = False) -> None: ...
    @property
    def mask(self) -> np.ndarray[_ShapeT_co, dtype[MaskType]] | MaskType: ...
    @mask.setter
    def mask(self, value: _ArrayLikeBool_co, /) -> None: ...
    @property
    def recordmask(self) -> np.ndarray[_ShapeT_co, dtype[MaskType]] | MaskType: ...
    @recordmask.setter
    def recordmask(self, mask: Never, /) -> NoReturn: ...
    def harden_mask(self) -> Self: ...
    def soften_mask(self) -> Self: ...
    @property
    def hardmask(self) -> bool: ...
    def unshare_mask(self) -> Self: ...
    @property
    def sharedmask(self) -> bool: ...
    def shrink_mask(self) -> Self: ...
    @property
    def baseclass(self) -> type[NDArray[Any]]: ...
    data: Any
    @property
    def flat(self) -> MaskedIterator: ...
    @flat.setter
    def flat(self, value: ArrayLike, /) -> None: ...
    @property
    def fill_value(self: _MaskedArray[_ScalarT]) -> _ScalarT: ...
    @fill_value.setter
    def fill_value(self, value: _ScalarLike_co | None = None) -> None: ...
    get_fill_value: Any
    set_fill_value: Any
    def filled(self, /, fill_value: _ScalarLike_co | None = None) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    def compressed(self) -> ndarray[tuple[int], _DTypeT_co]: ...

    @overload
    def compress(
        self,
        condition: _ArrayLikeBool_co,
        axis: _ShapeLike | None,
        out: _ArrayT
    ) -> _ArrayT: ...
    @overload
    def compress(
        self,
        condition: _ArrayLikeBool_co,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT
    ) -> _ArrayT: ...
    @overload
    def compress(
        self,
        condition: _ArrayLikeBool_co,
        axis: None = None,
        out: None = None
    ) -> MaskedArray[tuple[int], _DTypeT_co]: ...
    @overload
    def compress(
        self,
        condition: _ArrayLikeBool_co,
        axis: _ShapeLike | None = None,
        out: None = None
    ) -> MaskedArray[_AnyShape, _DTypeT_co]: ...

    # TODO: How to deal with the non-commutative nature of `==` and `!=`?
    # xref numpy/numpy#17368
    def __eq__(self, other: Incomplete, /) -> Incomplete: ...
    def __ne__(self, other: Incomplete, /) -> Incomplete: ...

    def __ge__(self, other: ArrayLike, /) -> _MaskedArray[bool_]: ...  # type: ignore[override]
    def __gt__(self, other: ArrayLike, /) -> _MaskedArray[bool_]: ...  # type: ignore[override]
    def __le__(self, other: ArrayLike, /) -> _MaskedArray[bool_]: ...  # type: ignore[override]
    def __lt__(self, other: ArrayLike, /) -> _MaskedArray[bool_]: ...  # type: ignore[override]

    # Keep in sync with `ndarray.__add__`
    @overload
    def __add__(self: _MaskedArray[_NumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __add__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> _MaskedArray[np.bool]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __add__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __add__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __add__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __add__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, /) -> _MaskedArray[complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _MaskedArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __add__(self: _MaskedArrayTD64_co, other: _ArrayLikeDT64_co, /) -> _MaskedArray[datetime64]: ...
    @overload
    def __add__(self: _MaskedArray[datetime64], other: _ArrayLikeTD64_co, /) -> _MaskedArray[datetime64]: ...
    @overload
    def __add__(self: _MaskedArray[bytes_], other: _ArrayLikeBytes_co, /) -> _MaskedArray[bytes_]: ...
    @overload
    def __add__(self: _MaskedArray[str_], other: _ArrayLikeStr_co, /) -> _MaskedArray[str_]: ...
    @overload
    def __add__(
        self: MaskedArray[Any, dtypes.StringDType],
        other: _ArrayLikeStr_co | _ArrayLikeString_co,
        /,
    ) -> MaskedArray[_AnyShape, dtypes.StringDType]: ...
    @overload
    def __add__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __add__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__radd__`
    @overload  # signature equivalent to __add__
    def __radd__(self: _MaskedArray[_NumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __radd__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> _MaskedArray[np.bool]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __radd__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __radd__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __radd__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __radd__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, /) -> _MaskedArray[complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _MaskedArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __radd__(self: _MaskedArrayTD64_co, other: _ArrayLikeDT64_co, /) -> _MaskedArray[datetime64]: ...
    @overload
    def __radd__(self: _MaskedArray[datetime64], other: _ArrayLikeTD64_co, /) -> _MaskedArray[datetime64]: ...
    @overload
    def __radd__(self: _MaskedArray[bytes_], other: _ArrayLikeBytes_co, /) -> _MaskedArray[bytes_]: ...
    @overload
    def __radd__(self: _MaskedArray[str_], other: _ArrayLikeStr_co, /) -> _MaskedArray[str_]: ...
    @overload
    def __radd__(
        self: MaskedArray[Any, dtypes.StringDType],
        other: _ArrayLikeStr_co | _ArrayLikeString_co,
        /,
    ) -> MaskedArray[_AnyShape, dtypes.StringDType]: ...
    @overload
    def __radd__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __radd__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__sub__`
    @overload
    def __sub__(self: _MaskedArray[_NumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __sub__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> NoReturn: ...
    @overload
    def __sub__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __sub__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __sub__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __sub__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __sub__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, /) -> _MaskedArray[complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _MaskedArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __sub__(self: _MaskedArray[datetime64], other: _ArrayLikeTD64_co, /) -> _MaskedArray[datetime64]: ...
    @overload
    def __sub__(self: _MaskedArray[datetime64], other: _ArrayLikeDT64_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __sub__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __sub__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__rsub__`
    @overload
    def __rsub__(self: _MaskedArray[_NumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __rsub__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> NoReturn: ...
    @overload
    def __rsub__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __rsub__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __rsub__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __rsub__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __rsub__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, /) -> _MaskedArray[complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _MaskedArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __rsub__(self: _MaskedArrayTD64_co, other: _ArrayLikeDT64_co, /) -> _MaskedArray[datetime64]: ...
    @overload
    def __rsub__(self: _MaskedArray[datetime64], other: _ArrayLikeDT64_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __rsub__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __rsub__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__mul__`
    @overload
    def __mul__(self: _MaskedArray[_NumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __mul__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> _MaskedArray[np.bool]: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __mul__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __mul__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __mul__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __mul__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, /) -> _MaskedArray[complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...
    @overload
    def __mul__(self: _MaskedArray[timedelta64], other: _ArrayLikeFloat_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __mul__(self: _MaskedArrayFloat_co, other: _ArrayLike[timedelta64], /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __mul__(
        self: MaskedArray[Any, dtype[character] | dtypes.StringDType],
        other: _ArrayLikeInt,
        /,
    ) -> MaskedArray[tuple[Any, ...], _DTypeT_co]: ...
    @overload
    def __mul__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __mul__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__rmul__`
    @overload  # signature equivalent to __mul__
    def __rmul__(self: _MaskedArray[_NumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __rmul__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> _MaskedArray[np.bool]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __rmul__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __rmul__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __rmul__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __rmul__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, /) -> _MaskedArray[complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...
    @overload
    def __rmul__(self: _MaskedArray[timedelta64], other: _ArrayLikeFloat_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __rmul__(self: _MaskedArrayFloat_co, other: _ArrayLike[timedelta64], /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __rmul__(
        self: MaskedArray[Any, dtype[character] | dtypes.StringDType],
        other: _ArrayLikeInt,
        /,
    ) -> MaskedArray[tuple[Any, ...], _DTypeT_co]: ...
    @overload
    def __rmul__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __rmul__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__truediv__`
    @overload
    def __truediv__(self: _MaskedArrayInt_co | _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __truediv__(self: _MaskedArrayFloat64_co, other: _ArrayLikeInt_co | _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __truediv__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __truediv__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __truediv__(self: _MaskedArray[floating], other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...
    @overload
    def __truediv__(self: _MaskedArrayFloat_co, other: _ArrayLike[floating], /) -> _MaskedArray[floating]: ...
    @overload
    def __truediv__(self: _MaskedArray[complexfloating], other: _ArrayLikeNumber_co, /) -> _MaskedArray[complexfloating]: ...
    @overload
    def __truediv__(self: _MaskedArrayNumber_co, other: _ArrayLike[complexfloating], /) -> _MaskedArray[complexfloating]: ...
    @overload
    def __truediv__(self: _MaskedArray[inexact], other: _ArrayLikeNumber_co, /) -> _MaskedArray[inexact]: ...
    @overload
    def __truediv__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...
    @overload
    def __truediv__(self: _MaskedArray[timedelta64], other: _ArrayLike[timedelta64], /) -> _MaskedArray[float64]: ...
    @overload
    def __truediv__(self: _MaskedArray[timedelta64], other: _ArrayLikeBool_co, /) -> NoReturn: ...
    @overload
    def __truediv__(self: _MaskedArray[timedelta64], other: _ArrayLikeFloat_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __truediv__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __truediv__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__rtruediv__`
    @overload
    def __rtruediv__(self: _MaskedArrayInt_co | _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __rtruediv__(self: _MaskedArrayFloat64_co, other: _ArrayLikeInt_co | _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, /) -> _MaskedArray[complex128]: ...
    @overload
    def __rtruediv__(self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], /) -> _MaskedArray[complex128]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[floating], other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...
    @overload
    def __rtruediv__(self: _MaskedArrayFloat_co, other: _ArrayLike[floating], /) -> _MaskedArray[floating]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[complexfloating], other: _ArrayLikeNumber_co, /) -> _MaskedArray[complexfloating]: ...
    @overload
    def __rtruediv__(self: _MaskedArrayNumber_co, other: _ArrayLike[complexfloating], /) -> _MaskedArray[complexfloating]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[inexact], other: _ArrayLikeNumber_co, /) -> _MaskedArray[inexact]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, /) -> _MaskedArray[number]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[timedelta64], other: _ArrayLike[timedelta64], /) -> _MaskedArray[float64]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[integer | floating], other: _ArrayLike[timedelta64], /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __rtruediv__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __rtruediv__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__floordiv__`
    @overload
    def __floordiv__(self: _MaskedArray[_RealNumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_RealNumberT]]: ...
    @overload
    def __floordiv__(self: _MaskedArray[_RealNumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> _MaskedArray[int8]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: _MaskedArray[np.bool], other: _ArrayLike[_RealNumberT], /) -> _MaskedArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __floordiv__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __floordiv__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...
    @overload
    def __floordiv__(self: _MaskedArray[timedelta64], other: _ArrayLike[timedelta64], /) -> _MaskedArray[int64]: ...
    @overload
    def __floordiv__(self: _MaskedArray[timedelta64], other: _ArrayLikeBool_co, /) -> NoReturn: ...
    @overload
    def __floordiv__(self: _MaskedArray[timedelta64], other: _ArrayLikeFloat_co, /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __floordiv__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __floordiv__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__rfloordiv__`
    @overload
    def __rfloordiv__(self: _MaskedArray[_RealNumberT], other: int | np.bool, /) -> MaskedArray[_ShapeT_co, dtype[_RealNumberT]]: ...
    @overload
    def __rfloordiv__(self: _MaskedArray[_RealNumberT], other: _ArrayLikeBool_co, /) -> _MaskedArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /) -> _MaskedArray[int8]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: _MaskedArray[np.bool], other: _ArrayLike[_RealNumberT], /) -> _MaskedArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, /) -> _MaskedArray[float64]: ...
    @overload
    def __rfloordiv__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], /) -> _MaskedArray[float64]: ...
    @overload
    def __rfloordiv__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: _MaskedArray[timedelta64], other: _ArrayLike[timedelta64], /) -> _MaskedArray[int64]: ...
    @overload
    def __rfloordiv__(self: _MaskedArray[floating | integer], other: _ArrayLike[timedelta64], /) -> _MaskedArray[timedelta64]: ...
    @overload
    def __rfloordiv__(self: _MaskedArray[object_], other: Any, /) -> Any: ...
    @overload
    def __rfloordiv__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, /) -> Any: ...

    # Keep in sync with `ndarray.__pow__`
    @overload
    def __pow__(self: _MaskedArray[_NumberT], other: int | np.bool, mod: None = None, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __pow__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, mod: None = None, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, mod: None = None, /) -> _MaskedArray[int8]: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], mod: None = None, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, mod: None = None, /) -> _MaskedArray[float64]: ...
    @overload
    def __pow__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], mod: None = None, /) -> _MaskedArray[float64]: ...
    @overload
    def __pow__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, mod: None = None, /) -> _MaskedArray[complex128]: ...
    @overload
    def __pow__(
        self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], mod: None = None, /
    ) -> _MaskedArray[complex128]: ...
    @overload
    def __pow__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, mod: None = None, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, mod: None = None, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, mod: None = None, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, mod: None = None, /) -> _MaskedArray[complexfloating]: ...
    @overload
    def __pow__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, mod: None = None, /) -> _MaskedArray[number]: ...
    @overload
    def __pow__(self: _MaskedArray[object_], other: Any, mod: None = None, /) -> Any: ...
    @overload
    def __pow__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, mod: None = None, /) -> Any: ...

    # Keep in sync with `ndarray.__rpow__`
    @overload
    def __rpow__(self: _MaskedArray[_NumberT], other: int | np.bool, mod: None = None, /) -> MaskedArray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __rpow__(self: _MaskedArray[_NumberT], other: _ArrayLikeBool_co, mod: None = None, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rpow__(self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, mod: None = None, /) -> _MaskedArray[int8]: ...  # type: ignore[overload-overlap]
    @overload
    def __rpow__(self: _MaskedArray[np.bool], other: _ArrayLike[_NumberT], mod: None = None, /) -> _MaskedArray[_NumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rpow__(self: _MaskedArray[float64], other: _ArrayLikeFloat64_co, mod: None = None, /) -> _MaskedArray[float64]: ...
    @overload
    def __rpow__(self: _MaskedArrayFloat64_co, other: _ArrayLike[floating[_64Bit]], mod: None = None, /) -> _MaskedArray[float64]: ...
    @overload
    def __rpow__(self: _MaskedArray[complex128], other: _ArrayLikeComplex128_co, mod: None = None, /) -> _MaskedArray[complex128]: ...
    @overload
    def __rpow__(
        self: _MaskedArrayComplex128_co, other: _ArrayLike[complexfloating[_64Bit]], mod: None = None, /
    ) -> _MaskedArray[complex128]: ...
    @overload
    def __rpow__(self: _MaskedArrayUInt_co, other: _ArrayLikeUInt_co, mod: None = None, /) -> _MaskedArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rpow__(self: _MaskedArrayInt_co, other: _ArrayLikeInt_co, mod: None = None, /) -> _MaskedArray[signedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rpow__(self: _MaskedArrayFloat_co, other: _ArrayLikeFloat_co, mod: None = None, /) -> _MaskedArray[floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __rpow__(self: _MaskedArrayComplex_co, other: _ArrayLikeComplex_co, mod: None = None, /) -> _MaskedArray[complexfloating]: ...
    @overload
    def __rpow__(self: _MaskedArray[number], other: _ArrayLikeNumber_co, mod: None = None, /) -> _MaskedArray[number]: ...
    @overload
    def __rpow__(self: _MaskedArray[object_], other: Any, mod: None = None, /) -> Any: ...
    @overload
    def __rpow__(self: _MaskedArray[Any], other: _ArrayLikeObject_co, mod: None = None, /) -> Any: ...

    # Keep in sync with `ndarray.__iadd__`
    @overload
    def __iadd__(
        self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _MaskedArray[integer], other: _ArrayLikeInt_co, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: _MaskedArray[floating], other: _ArrayLikeFloat_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: _MaskedArray[complexfloating], other: _ArrayLikeComplex_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: _MaskedArray[timedelta64 | datetime64], other: _ArrayLikeTD64_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _MaskedArray[bytes_], other: _ArrayLikeBytes_co, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: MaskedArray[Any, dtype[str_] | dtypes.StringDType],
        other: _ArrayLikeStr_co | _ArrayLikeString_co,
        /,
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: _MaskedArray[object_], other: Any, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    # Keep in sync with `ndarray.__isub__`
    @overload
    def __isub__(self: _MaskedArray[integer], other: _ArrayLikeInt_co, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(
        self: _MaskedArray[floating], other: _ArrayLikeFloat_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(
        self: _MaskedArray[complexfloating], other: _ArrayLikeComplex_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(
        self: _MaskedArray[timedelta64 | datetime64], other: _ArrayLikeTD64_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(
        self: _MaskedArray[object_], other: Any, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    # Keep in sync with `ndarray.__imul__`
    @overload
    def __imul__(
        self: _MaskedArray[np.bool], other: _ArrayLikeBool_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: MaskedArray[Any, dtype[integer] | dtype[character] | dtypes.StringDType], other: _ArrayLikeInt_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: _MaskedArray[floating | timedelta64], other: _ArrayLikeFloat_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: _MaskedArray[complexfloating], other: _ArrayLikeComplex_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: _MaskedArray[object_], other: Any, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    # Keep in sync with `ndarray.__ifloordiv__`
    @overload
    def __ifloordiv__(self: _MaskedArray[integer], other: _ArrayLikeInt_co, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _MaskedArray[floating | timedelta64], other: _ArrayLikeFloat_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _MaskedArray[object_], other: Any, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    # Keep in sync with `ndarray.__itruediv__`
    @overload
    def __itruediv__(
        self: _MaskedArray[floating | timedelta64], other: _ArrayLikeFloat_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _MaskedArray[complexfloating],
        other: _ArrayLikeComplex_co,
        /,
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _MaskedArray[object_], other: Any, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    # Keep in sync with `ndarray.__ipow__`
    @overload
    def __ipow__(self: _MaskedArray[integer], other: _ArrayLikeInt_co, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(
        self: _MaskedArray[floating], other: _ArrayLikeFloat_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(
        self: _MaskedArray[complexfloating], other: _ArrayLikeComplex_co, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(
        self: _MaskedArray[object_], other: Any, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    #
    @property  # type: ignore[misc]
    def imag(self: _HasDTypeWithRealAndImag[object, _ScalarT], /) -> MaskedArray[_ShapeT_co, dtype[_ScalarT]]: ...
    get_imag: Any
    @property  # type: ignore[misc]
    def real(self: _HasDTypeWithRealAndImag[_ScalarT, object], /) -> MaskedArray[_ShapeT_co, dtype[_ScalarT]]: ...
    get_real: Any

    # keep in sync with `np.ma.count`
    @overload
    def count(self, axis: None = None, keepdims: Literal[False] | _NoValueType = ...) -> int: ...
    @overload
    def count(self, axis: _ShapeLike, keepdims: bool | _NoValueType = ...) -> NDArray[int_]: ...
    @overload
    def count(self, axis: _ShapeLike | None = ..., *, keepdims: Literal[True]) -> NDArray[int_]: ...
    @overload
    def count(self, axis: _ShapeLike | None, keepdims: Literal[True]) -> NDArray[int_]: ...

    def ravel(self, order: _OrderKACF = "C") -> MaskedArray[tuple[int], _DTypeT_co]: ...

    # Keep in sync with `ndarray.reshape`
    # NOTE: reshape also accepts negative integers, so we can't use integer literals
    @overload  # (None)
    def reshape(self, shape: None, /, *, order: _OrderACF = "C", copy: bool | None = None) -> Self: ...
    @overload  # (empty_sequence)
    def reshape(  # type: ignore[overload-overlap]  # mypy false positive
        self,
        shape: Sequence[Never],
        /,
        *,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[tuple[()], _DTypeT_co]: ...
    @overload  # (() | (int) | (int, int) | ....)  # up to 8-d
    def reshape(
        self,
        shape: _AnyShapeT,
        /,
        *,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[_AnyShapeT, _DTypeT_co]: ...
    @overload  # (index)
    def reshape(
        self,
        size1: SupportsIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[tuple[int], _DTypeT_co]: ...
    @overload  # (index, index)
    def reshape(
        self,
        size1: SupportsIndex,
        size2: SupportsIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[tuple[int, int], _DTypeT_co]: ...
    @overload  # (index, index, index)
    def reshape(
        self,
        size1: SupportsIndex,
        size2: SupportsIndex,
        size3: SupportsIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[tuple[int, int, int], _DTypeT_co]: ...
    @overload  # (index, index, index, index)
    def reshape(
        self,
        size1: SupportsIndex,
        size2: SupportsIndex,
        size3: SupportsIndex,
        size4: SupportsIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[tuple[int, int, int, int], _DTypeT_co]: ...
    @overload  # (int, *(index, ...))
    def reshape(
        self,
        size0: SupportsIndex,
        /,
        *shape: SupportsIndex,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[_AnyShape, _DTypeT_co]: ...
    @overload  # (sequence[index])
    def reshape(
        self,
        shape: Sequence[SupportsIndex],
        /,
        *,
        order: _OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[_AnyShape, _DTypeT_co]: ...

    def resize(self, newshape: Never, refcheck: bool = True, order: bool = False) -> NoReturn: ...
    def put(self, indices: _ArrayLikeInt_co, values: ArrayLike, mode: _ModeKind = "raise") -> None: ...
    def ids(self) -> tuple[int, int]: ...
    def iscontiguous(self) -> bool: ...

    @overload
    def all(
        self,
        axis: None = None,
        out: None = None,
        keepdims: Literal[False] | _NoValueType = ...,
    ) -> bool_: ...
    @overload
    def all(
        self,
        axis: _ShapeLike | None = None,
        out: None = None,
        *,
        keepdims: Literal[True],
    ) -> _MaskedArray[bool_]: ...
    @overload
    def all(
        self,
        axis: _ShapeLike | None,
        out: None,
        keepdims: Literal[True],
    ) -> _MaskedArray[bool_]: ...
    @overload
    def all(
        self,
        axis: _ShapeLike | None = None,
        out: None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> bool_ | _MaskedArray[bool_]: ...
    @overload
    def all(
        self,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def all(
        self,
        axis: _ShapeLike | None,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    @overload
    def any(
        self,
        axis: None = None,
        out: None = None,
        keepdims: Literal[False] | _NoValueType = ...,
    ) -> bool_: ...
    @overload
    def any(
        self,
        axis: _ShapeLike | None = None,
        out: None = None,
        *,
        keepdims: Literal[True],
    ) -> _MaskedArray[bool_]: ...
    @overload
    def any(
        self,
        axis: _ShapeLike | None,
        out: None,
        keepdims: Literal[True],
    ) -> _MaskedArray[bool_]: ...
    @overload
    def any(
        self,
        axis: _ShapeLike | None = None,
        out: None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> bool_ | _MaskedArray[bool_]: ...
    @overload
    def any(
        self,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def any(
        self,
        axis: _ShapeLike | None,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    def nonzero(self) -> tuple[_Array1D[intp], ...]: ...

    # Keep in sync with `ndarray.trace`
    @overload
    def trace(
        self,  # >= 2D MaskedArray
        offset: SupportsIndex = ...,
        axis1: SupportsIndex = ...,
        axis2: SupportsIndex = ...,
        dtype: DTypeLike | None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def trace(
        self,  # >= 2D MaskedArray
        offset: SupportsIndex = ...,
        axis1: SupportsIndex = ...,
        axis2: SupportsIndex = ...,
        dtype: DTypeLike | None = ...,
        *,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload
    def trace(
        self,  # >= 2D MaskedArray
        offset: SupportsIndex,
        axis1: SupportsIndex,
        axis2: SupportsIndex,
        dtype: DTypeLike | None,
        out: _ArrayT,
    ) -> _ArrayT: ...

    # This differs from `ndarray.dot`, in that 1D dot 1D returns a 0D array.
    @overload
    def dot(self, b: ArrayLike, out: None = ..., strict: bool = ...) -> _MaskedArray[Any]: ...
    @overload
    def dot(self, b: ArrayLike, out: _ArrayT, strict: bool = ...) -> _ArrayT: ...

    @overload
    def sum(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> Any: ...
    @overload
    def sum(
        self,
        /,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def sum(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    # Keep in sync with `ndarray.cumsum`
    @overload  # out: None (default)
    def cumsum(self, /, axis: SupportsIndex | None = None, dtype: DTypeLike | None = None, out: None = None) -> _MaskedArray[Any]: ...
    @overload  # out: ndarray
    def cumsum(self, /, axis: SupportsIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def cumsum(self, /, axis: SupportsIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

    @overload
    def prod(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> Any: ...
    @overload
    def prod(
        self,
        /,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def prod(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    product: Any

    # Keep in sync with `ndarray.cumprod`
    @overload  # out: None (default)
    def cumprod(self, /, axis: SupportsIndex | None = None, dtype: DTypeLike | None = None, out: None = None) -> _MaskedArray[Any]: ...
    @overload  # out: ndarray
    def cumprod(self, /, axis: SupportsIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def cumprod(self, /, axis: SupportsIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

    @overload
    def mean(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> Any: ...
    @overload
    def mean(
        self,
        /,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def mean(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    @overload
    def anom(self, axis: SupportsIndex | None = None, dtype: None = None) -> Self: ...
    @overload
    def anom(self, axis: SupportsIndex | None = None, *, dtype: DTypeLike) -> MaskedArray[_ShapeT_co, dtype]: ...
    @overload
    def anom(self, axis: SupportsIndex | None, dtype: DTypeLike) -> MaskedArray[_ShapeT_co, dtype]: ...

    @overload
    def var(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        ddof: float = 0,
        keepdims: bool | _NoValueType = ...,
        mean: _ArrayLikeNumber_co | _NoValueType = ...,
    ) -> Any: ...
    @overload
    def var(
        self,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: bool | _NoValueType = ...,
        mean: _ArrayLikeNumber_co | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def var(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: bool | _NoValueType = ...,
        mean: _ArrayLikeNumber_co | _NoValueType = ...,
    ) -> _ArrayT: ...

    @overload
    def std(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        ddof: float = 0,
        keepdims: bool | _NoValueType = ...,
        mean: _ArrayLikeNumber_co | _NoValueType = ...,
    ) -> Any: ...
    @overload
    def std(
        self,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: bool | _NoValueType = ...,
        mean: _ArrayLikeNumber_co | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def std(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: bool | _NoValueType = ...,
        mean: _ArrayLikeNumber_co | _NoValueType = ...,
    ) -> _ArrayT: ...

    # Keep in sync with `ndarray.round`
    @overload  # out=None (default)
    def round(self, /, decimals: SupportsIndex = 0, out: None = None) -> Self: ...
    @overload  # out=ndarray
    def round(self, /, decimals: SupportsIndex, out: _ArrayT) -> _ArrayT: ...
    @overload
    def round(self, /, decimals: SupportsIndex = 0, *, out: _ArrayT) -> _ArrayT: ...

    def argsort(
        self,
        axis: SupportsIndex | _NoValueType = ...,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
        endwith: bool = True,
        fill_value: _ScalarLike_co | None = None,
        *,
        stable: bool = False,
    ) -> _MaskedArray[intp]: ...

    # Keep in-sync with np.ma.argmin
    @overload  # type: ignore[override]
    def argmin(
        self,
        axis: None = None,
        fill_value: _ScalarLike_co | None = None,
        out: None = None,
        *,
        keepdims: Literal[False] | _NoValueType = ...,
    ) -> intp: ...
    @overload
    def argmin(
        self,
        axis: SupportsIndex | None = None,
        fill_value: _ScalarLike_co | None = None,
        out: None = None,
        *,
        keepdims: bool | _NoValueType = ...,
    ) -> Any: ...
    @overload
    def argmin(
        self,
        axis: SupportsIndex | None = None,
        fill_value: _ScalarLike_co | None = None,
        *,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def argmin(
        self,
        axis: SupportsIndex | None,
        fill_value: _ScalarLike_co | None,
        out: _ArrayT,
        *,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    # Keep in-sync with np.ma.argmax
    @overload  # type: ignore[override]
    def argmax(
        self,
        axis: None = None,
        fill_value: _ScalarLike_co | None = None,
        out: None = None,
        *,
        keepdims: Literal[False] | _NoValueType = ...,
    ) -> intp: ...
    @overload
    def argmax(
        self,
        axis: SupportsIndex | None = None,
        fill_value: _ScalarLike_co | None = None,
        out: None = None,
        *,
        keepdims: bool | _NoValueType = ...,
    ) -> Any: ...
    @overload
    def argmax(
        self,
        axis: SupportsIndex | None = None,
        fill_value: _ScalarLike_co | None = None,
        *,
        out: _ArrayT,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def argmax(
        self,
        axis: SupportsIndex | None,
        fill_value: _ScalarLike_co | None,
        out: _ArrayT,
        *,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    #
    def sort(  # type: ignore[override]
        self,
        axis: SupportsIndex = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
        endwith: bool | None = True,
        fill_value: _ScalarLike_co | None = None,
        *,
        stable: Literal[False] | None = False,
    ) -> None: ...

    #
    @overload  # type: ignore[override]
    def min(
        self: _MaskedArray[_ScalarT],
        axis: None = None,
        out: None = None,
        fill_value: _ScalarLike_co | None = None,
        keepdims: Literal[False] | _NoValueType = ...,
    ) -> _ScalarT: ...
    @overload
    def min(
        self,
        axis: _ShapeLike | None = None,
        out: None = None,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool | _NoValueType = ...
    ) -> Any: ...
    @overload
    def min(
        self,
        axis: _ShapeLike | None,
        out: _ArrayT,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def min(
        self,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    #
    @overload  # type: ignore[override]
    def max(
        self: _MaskedArray[_ScalarT],
        axis: None = None,
        out: None = None,
        fill_value: _ScalarLike_co | None = None,
        keepdims: Literal[False] | _NoValueType = ...,
    ) -> _ScalarT: ...
    @overload
    def max(
        self,
        axis: _ShapeLike | None = None,
        out: None = None,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool | _NoValueType = ...
    ) -> Any: ...
    @overload
    def max(
        self,
        axis: _ShapeLike | None,
        out: _ArrayT,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...
    @overload
    def max(
        self,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool | _NoValueType = ...,
    ) -> _ArrayT: ...

    #
    @overload
    def ptp(
        self: _MaskedArray[_ScalarT],
        axis: None = None,
        out: None = None,
        fill_value: _ScalarLike_co | None = None,
        keepdims: Literal[False] = False,
    ) -> _ScalarT: ...
    @overload
    def ptp(
        self,
        axis: _ShapeLike | None = None,
        out: None = None,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool = False,
    ) -> Any: ...
    @overload
    def ptp(
        self,
        axis: _ShapeLike | None,
        out: _ArrayT,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool = False,
    ) -> _ArrayT: ...
    @overload
    def ptp(
        self,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT,
        fill_value: _ScalarLike_co | None = None,
        keepdims: bool = False,
    ) -> _ArrayT: ...

    #
    @overload
    def partition(
        self,
        /,
        kth: _ArrayLikeInt,
        axis: SupportsIndex = -1,
        kind: _PartitionKind = "introselect",
        order: None = None
    ) -> None: ...
    @overload
    def partition(
        self: _MaskedArray[np.void],
        /,
        kth: _ArrayLikeInt,
        axis: SupportsIndex = -1,
        kind: _PartitionKind = "introselect",
        order: str | Sequence[str] | None = None,
    ) -> None: ...

    #
    @overload
    def argpartition(
        self,
        /,
        kth: _ArrayLikeInt,
        axis: SupportsIndex | None = -1,
        kind: _PartitionKind = "introselect",
        order: None = None,
    ) -> _MaskedArray[intp]: ...
    @overload
    def argpartition(
        self: _MaskedArray[np.void],
        /,
        kth: _ArrayLikeInt,
        axis: SupportsIndex | None = -1,
        kind: _PartitionKind = "introselect",
        order: str | Sequence[str] | None = None,
    ) -> _MaskedArray[intp]: ...

    # Keep in-sync with np.ma.take
    @overload
    def take(  # type: ignore[overload-overlap]
        self: _MaskedArray[_ScalarT],
        indices: _IntLike_co,
        axis: None = None,
        out: None = None,
        mode: _ModeKind = 'raise'
    ) -> _ScalarT: ...
    @overload
    def take(
        self: _MaskedArray[_ScalarT],
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex | None = None,
        out: None = None,
        mode: _ModeKind = 'raise',
    ) -> _MaskedArray[_ScalarT]: ...
    @overload
    def take(
        self,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex | None,
        out: _ArrayT,
        mode: _ModeKind = 'raise',
    ) -> _ArrayT: ...
    @overload
    def take(
        self,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex | None = None,
        *,
        out: _ArrayT,
        mode: _ModeKind = 'raise',
    ) -> _ArrayT: ...

    copy: Any
    diagonal: Any
    flatten: Any

    @overload
    def repeat(
        self,
        repeats: _ArrayLikeInt_co,
        axis: None = None,
    ) -> MaskedArray[tuple[int], _DTypeT_co]: ...
    @overload
    def repeat(
        self,
        repeats: _ArrayLikeInt_co,
        axis: SupportsIndex,
    ) -> MaskedArray[_AnyShape, _DTypeT_co]: ...

    squeeze: Any

    def swapaxes(
        self,
        axis1: SupportsIndex,
        axis2: SupportsIndex,
        /
    ) -> MaskedArray[_AnyShape, _DTypeT_co]: ...

    #
    def toflex(self) -> Incomplete: ...
    def torecords(self) -> Incomplete: ...
    def tolist(self, fill_value: Incomplete | None = None) -> Incomplete: ...
    def tobytes(self, /, fill_value: Incomplete | None = None, order: _OrderKACF = "C") -> bytes: ...  # type: ignore[override]
    def tofile(self, /, fid: Incomplete, sep: str = "", format: str = "%s") -> Incomplete: ...

    #
    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> Self: ...

    # Keep `dtype` at the bottom to avoid name conflicts with `np.dtype`
    @property
    def dtype(self) -> _DTypeT_co: ...
    @dtype.setter
    def dtype(self: MaskedArray[_AnyShape, _DTypeT], dtype: _DTypeT, /) -> None: ...

class mvoid(MaskedArray[_ShapeT_co, _DTypeT_co]):
    def __new__(
        self,  # pyright: ignore[reportSelfClsParameterName]
        data,
        mask=...,
        dtype=...,
        fill_value=...,
        hardmask=...,
        copy=...,
        subok=...,
    ): ...
    def __getitem__(self, indx): ...
    def __setitem__(self, indx, value): ...
    def __iter__(self): ...
    def __len__(self): ...
    def filled(self, fill_value=...): ...
    def tolist(self): ...

def isMaskedArray(x): ...
isarray = isMaskedArray
isMA = isMaskedArray

# 0D float64 array
class MaskedConstant(MaskedArray[_AnyShape, dtype[float64]]):
    def __new__(cls): ...
    __class__: Any
    def __array_finalize__(self, obj): ...
    def __array_wrap__(self, obj, context=..., return_scalar=...): ...
    def __format__(self, format_spec): ...
    def __reduce__(self): ...
    def __iop__(self, other): ...
    __iadd__: Any
    __isub__: Any
    __imul__: Any
    __ifloordiv__: Any
    __itruediv__: Any
    __ipow__: Any
    def copy(self, *args, **kwargs): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __setattr__(self, attr, value): ...

masked: MaskedConstant
masked_singleton: MaskedConstant
masked_array = MaskedArray

def array(
    data,
    dtype=...,
    copy=...,
    order=...,
    mask=...,
    fill_value=...,
    keep_mask=...,
    hard_mask=...,
    shrink=...,
    subok=...,
    ndmin=...,
): ...
def is_masked(x: object) -> bool: ...

class _extrema_operation(_MaskedUFunc):
    compare: Any
    fill_value_func: Any
    def __init__(self, ufunc, compare, fill_value): ...
    # NOTE: in practice `b` has a default value, but users should
    # explicitly provide a value here as the default is deprecated
    def __call__(self, a, b): ...
    def reduce(self, target, axis=...): ...
    def outer(self, a, b): ...

@overload
def min(
    obj: _ArrayLike[_ScalarT],
    axis: None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: Literal[False] | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def min(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...
) -> Any: ...
@overload
def min(
    obj: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def min(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

@overload
def max(
    obj: _ArrayLike[_ScalarT],
    axis: None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: Literal[False] | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def max(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...
) -> Any: ...
@overload
def max(
    obj: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def max(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

@overload
def ptp(
    obj: _ArrayLike[_ScalarT],
    axis: None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: Literal[False] | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def ptp(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...
) -> Any: ...
@overload
def ptp(
    obj: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def ptp(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

class _frommethod:
    __name__: Any
    __doc__: Any
    reversed: Any
    def __init__(self, methodname, reversed=...): ...
    def getdoc(self): ...
    def __call__(self, a, *args, **params): ...

all: _frommethod
anomalies: _frommethod
anom: _frommethod
any: _frommethod
compress: _frommethod
cumprod: _frommethod
cumsum: _frommethod
copy: _frommethod
diagonal: _frommethod
harden_mask: _frommethod
ids: _frommethod
mean: _frommethod
nonzero: _frommethod
prod: _frommethod
product: _frommethod
ravel: _frommethod
repeat: _frommethod
soften_mask: _frommethod
std: _frommethod
sum: _frommethod
swapaxes: _frommethod
trace: _frommethod
var: _frommethod

@overload
def count(self: ArrayLike, axis: None = None, keepdims: Literal[False] | _NoValueType = ...) -> int: ...
@overload
def count(self: ArrayLike, axis: _ShapeLike, keepdims: bool | _NoValueType = ...) -> NDArray[int_]: ...
@overload
def count(self: ArrayLike, axis: _ShapeLike | None = ..., *, keepdims: Literal[True]) -> NDArray[int_]: ...
@overload
def count(self: ArrayLike, axis: _ShapeLike | None, keepdims: Literal[True]) -> NDArray[int_]: ...

@overload
def argmin(
    self: ArrayLike,
    axis: None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: Literal[False] | _NoValueType = ...,
) -> intp: ...
@overload
def argmin(
    self: ArrayLike,
    axis: SupportsIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Any: ...
@overload
def argmin(
    self: ArrayLike,
    axis: SupportsIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def argmin(
    self: ArrayLike,
    axis: SupportsIndex | None,
    fill_value: _ScalarLike_co | None,
    out: _ArrayT,
    *,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def argmax(
    self: ArrayLike,
    axis: None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: Literal[False] | _NoValueType = ...,
) -> intp: ...
@overload
def argmax(
    self: ArrayLike,
    axis: SupportsIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Any: ...
@overload
def argmax(
    self: ArrayLike,
    axis: SupportsIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def argmax(
    self: ArrayLike,
    axis: SupportsIndex | None,
    fill_value: _ScalarLike_co | None,
    out: _ArrayT,
    *,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

minimum: _extrema_operation
maximum: _extrema_operation

@overload
def take(
    a: _ArrayLike[_ScalarT],
    indices: _IntLike_co,
    axis: None = None,
    out: None = None,
    mode: _ModeKind = 'raise'
) -> _ScalarT: ...
@overload
def take(
    a: _ArrayLike[_ScalarT],
    indices: _ArrayLikeInt_co,
    axis: SupportsIndex | None = None,
    out: None = None,
    mode: _ModeKind = 'raise',
) -> _MaskedArray[_ScalarT]: ...
@overload
def take(
    a: ArrayLike,
    indices: _IntLike_co,
    axis: SupportsIndex | None = None,
    out: None = None,
    mode: _ModeKind = 'raise',
) -> Any: ...
@overload
def take(
    a: ArrayLike,
    indices: _ArrayLikeInt_co,
    axis: SupportsIndex | None = None,
    out: None = None,
    mode: _ModeKind = 'raise',
) -> _MaskedArray[Any]: ...
@overload
def take(
    a: ArrayLike,
    indices: _ArrayLikeInt_co,
    axis: SupportsIndex | None,
    out: _ArrayT,
    mode: _ModeKind = 'raise',
) -> _ArrayT: ...
@overload
def take(
    a: ArrayLike,
    indices: _ArrayLikeInt_co,
    axis: SupportsIndex | None = None,
    *,
    out: _ArrayT,
    mode: _ModeKind = 'raise',
) -> _ArrayT: ...

def power(a, b, third=...): ...
def argsort(a, axis=..., kind=..., order=..., endwith=..., fill_value=..., *, stable=...): ...
@overload
def sort(
    a: _ArrayT,
    axis: SupportsIndex = -1,
    kind: _SortKind | None = None,
    order: str | Sequence[str] | None = None,
    endwith: bool | None = True,
    fill_value: _ScalarLike_co | None = None,
    *,
    stable: Literal[False] | None = False,
) -> _ArrayT: ...
@overload
def sort(
    a: ArrayLike,
    axis: SupportsIndex = -1,
    kind: _SortKind | None = None,
    order: str | Sequence[str] | None = None,
    endwith: bool | None = True,
    fill_value: _ScalarLike_co | None = None,
    *,
    stable: Literal[False] | None = False,
) -> NDArray[Any]: ...
@overload
def compressed(x: _ArrayLike[_ScalarT_co]) -> _Array1D[_ScalarT_co]: ...
@overload
def compressed(x: ArrayLike) -> _Array1D[Any]: ...
def concatenate(arrays, axis=...): ...
def diag(v, k=...): ...
def left_shift(a, n): ...
def right_shift(a, n): ...
def put(a: NDArray[Any], indices: _ArrayLikeInt_co, values: ArrayLike, mode: _ModeKind = 'raise') -> None: ...
def putmask(a: NDArray[Any], mask: _ArrayLikeBool_co, values: ArrayLike) -> None: ...
def transpose(a, axes=...): ...
def reshape(a, new_shape, order=...): ...
def resize(x, new_shape): ...
def ndim(obj: ArrayLike) -> int: ...
def shape(obj): ...
def size(obj: ArrayLike, axis: SupportsIndex | None = None) -> int: ...
def diff(a, /, n=..., axis=..., prepend=..., append=...): ...
def where(condition, x=..., y=...): ...
def choose(indices, choices, out=..., mode=...): ...
def round_(a, decimals=..., out=...): ...
round = round_

def inner(a, b): ...
innerproduct = inner

def outer(a, b): ...
outerproduct = outer

def correlate(a, v, mode=..., propagate_mask=...): ...
def convolve(a, v, mode=..., propagate_mask=...): ...

def allequal(a: ArrayLike, b: ArrayLike, fill_value: bool = True) -> bool: ...

def allclose(a: ArrayLike, b: ArrayLike, masked_equal: bool = True, rtol: float = 1e-5, atol: float = 1e-8) -> bool: ...

def asarray(a, dtype=..., order=...): ...
def asanyarray(a, dtype=...): ...
def fromflex(fxarray): ...

class _convert2ma:
    def __init__(self, /, funcname: str, np_ret: str, np_ma_ret: str, params: dict[str, Any] | None = None) -> None: ...
    def __call__(self, /, *args: object, **params: object) -> Any: ...
    def getdoc(self, /, np_ret: str, np_ma_ret: str) -> str | None: ...

arange: _convert2ma
clip: _convert2ma
empty: _convert2ma
empty_like: _convert2ma
frombuffer: _convert2ma
fromfunction: _convert2ma
identity: _convert2ma
indices: _convert2ma
ones: _convert2ma
ones_like: _convert2ma
squeeze: _convert2ma
zeros: _convert2ma
zeros_like: _convert2ma

def append(a, b, axis=...): ...
def dot(a, b, strict=..., out=...): ...
def mask_rowcols(a, axis=...): ...
