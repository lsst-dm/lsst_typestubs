from .dictField import Dict, DictField
from typing import Any, Optional

class ConfigDict(Dict):
    def __init__(self, config: Any, field: Any, value: Any, at: Any, label: Any) -> None: ...
    def __setitem__(self, k: Any, x: Any, at: Optional[Any] = ..., label: str = ..., setHistory: bool = ...) -> None: ...
    def __delitem__(self, k: Any, at: Optional[Any] = ..., label: str = ...) -> None: ...

class ConfigDictField(DictField):
    DictClass: Any = ...
    keytype: Any = ...
    itemtype: Any = ...
    dictCheck: Any = ...
    itemCheck: Any = ...
    def __init__(self, doc: Any, keytype: Any, itemtype: Any, default: Optional[Any] = ..., optional: bool = ..., dictCheck: Optional[Any] = ..., itemCheck: Optional[Any] = ..., deprecated: Optional[Any] = ...) -> None: ...
    def rename(self, instance: Any) -> None: ...
    def validate(self, instance: Any) -> None: ...
    def toDict(self, instance: Any): ...
    def save(self, outfile: Any, instance: Any) -> None: ...
    def freeze(self, instance: Any) -> None: ...
