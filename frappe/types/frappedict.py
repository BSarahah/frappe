<<<<<<< HEAD
class _dict(dict):
	"""dict like object that exposes keys as attributes"""

	__slots__ = ()
	__getattr__ = dict.get
	__setattr__ = dict.__setitem__
	__delattr__ = dict.__delitem__
	__setstate__ = dict.update

	def __getstate__(self):
		return self

	def update(self, *args, **kwargs):
		"""update and return self -- the missing dict feature in python"""

		super().update(*args, **kwargs)
		return self

	def copy(self):
=======
from collections.abc import Iterable, Mapping
from typing import (
	TYPE_CHECKING,
	TypeVar,
	overload,
)

from typing_extensions import Self, override

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class _dict(dict[_KT, _VT]):
	"""dict like object that exposes keys as attributes"""

	__slots__ = ()

	def __getattr__(self, k: str) -> _VT | None:
		return super().get(k)  # type: ignore[arg-type]

	@override
	def __setattr__(self, k: str, v: _VT) -> None:
		return super().__setitem__(k, v)  # type: ignore[index]

	@override
	def __delattr__(self, k: str):
		return super().__delitem__(k)  # type: ignore[arg-type]

	def __setstate__(self, m: Mapping[_KT, _VT]) -> None:
		return super().update(m)

	@override
	def __getstate__(self) -> Self:
		return self

	@overload  # type: ignore[override]
	def update(self, m: Mapping[_KT, _VT], /, **kwargs: _VT) -> Self: ...

	@overload
	def update(self, m: Iterable[tuple[_KT, _VT]], /, **kwargs: _VT) -> Self: ...

	@overload
	def update(self, /, **kwargs: _VT) -> Self: ...

	@override
	def update(
		self, m: Mapping[_KT, _VT] | Iterable[tuple[_KT, _VT]] | None = None, /, **kwargs: _VT
	) -> Self:
		"""update and return self -- the missing dict feature in python"""
		if m:
			super().update(m, **kwargs)
		else:
			super().update(**kwargs)
		return self

	@override
	def copy(self) -> "_dict[_KT, _VT]":
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		return _dict(self)
