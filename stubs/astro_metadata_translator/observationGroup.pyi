from collections.abc import MutableSequence
from typing import Any, Optional

class ObservationGroup(MutableSequence):
    def __init__(self, members: Any, translator_class: Optional[Any] = ..., pedantic: Optional[Any] = ...) -> None: ...
    def __len__(self): ...
    def __delitem__(self, index: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __iter__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def insert(self, index: Any, value: Any) -> None: ...
    def reverse(self) -> None: ...
    def sort(self, key: Optional[Any] = ..., reverse: bool = ...) -> None: ...
    def extremes(self): ...
    def newest(self): ...
    def oldest(self): ...
    def property_values(self, property: Any): ...