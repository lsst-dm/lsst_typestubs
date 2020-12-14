from ._GenericMap import AutoKeyMeta, MutableGenericMap
from typing import Any, Optional

class SimpleGenericMap(MutableGenericMap, metaclass=AutoKeyMeta):
    @classmethod
    def fromkeys(cls, iterable: Any, value: Optional[Any] = ...): ...

class SimpleGenericMapS:
    def __init__(self, source: Optional[Any] = ..., **kwargs: Any) -> None: ...
