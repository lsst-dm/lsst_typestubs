from typing import Any, Optional

class ConfigMeta(type):
    def __init__(cls, name: Any, bases: Any, dict_: Any): ...
    def __setattr__(cls, name: Any, value: Any) -> None: ...

class FieldValidationError(ValueError):
    fieldType: Any = ...
    fieldName: Any = ...
    fullname: Any = ...
    history: Any = ...
    fieldSource: Any = ...
    configSource: Any = ...
    def __init__(self, field: Any, config: Any, msg: Any) -> None: ...

class Field:
    supportedTypes: Any = ...
    def __init__(self, doc: Any, dtype: Any, default: Optional[Any] = ..., check: Optional[Any] = ..., optional: bool = ..., deprecated: Optional[Any] = ...) -> None: ...
    def rename(self, instance: Any) -> None: ...
    def validate(self, instance: Any) -> None: ...
    def freeze(self, instance: Any) -> None: ...
    def save(self, outfile: Any, instance: Any) -> None: ...
    def toDict(self, instance: Any): ...
    def __get__(self, instance: Any, owner: Optional[Any] = ..., at: Optional[Any] = ..., label: str = ...): ...
    def __set__(self, instance: Any, value: Any, at: Optional[Any] = ..., label: str = ...) -> None: ...
    def __delete__(self, instance: Any, at: Optional[Any] = ..., label: str = ...) -> None: ...

class RecordingImporter:
    def __init__(self) -> None: ...
    origMetaPath: Any = ...
    def __enter__(self): ...
    def __exit__(self, *args: Any): ...
    def uninstall(self) -> None: ...
    def find_module(self, fullname: Any, path: Optional[Any] = ...) -> None: ...
    def getModules(self): ...

class Config(metaclass=ConfigMeta):
    def __iter__(self) -> Any: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def iteritems(self): ...
    def itervalues(self): ...
    def iterkeys(self): ...
    def __contains__(self, name: Any): ...
    def __new__(cls, *args: Any, **kw: Any): ...
    def __reduce__(self): ...
    def setDefaults(self) -> None: ...
    def update(self, **kw: Any) -> None: ...
    def load(self, filename: Any, root: str = ...) -> None: ...
    def loadFromStream(self, stream: Any, root: str = ..., filename: Optional[Any] = ...) -> None: ...
    def save(self, filename: Any, root: str = ...) -> None: ...
    def saveToStream(self, outfile: Any, root: str = ..., skipImports: bool = ...) -> None: ...
    def freeze(self) -> None: ...
    def toDict(self): ...
    def names(self): ...
    def validate(self) -> None: ...
    def formatHistory(self, name: Any, **kwargs: Any): ...
    history: Any = ...
    def __setattr__(self, attr: Any, value: Any, at: Optional[Any] = ..., label: str = ...): ...
    def __delattr__(self, attr: Any, at: Optional[Any] = ..., label: str = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def compare(self, other: Any, shortcut: bool = ..., rtol: float = ..., atol: float = ..., output: Optional[Any] = ...): ...
    @classmethod
    def __init_subclass__(cls, **kwargs: Any) -> None: ...