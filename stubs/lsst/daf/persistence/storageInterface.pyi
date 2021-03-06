import abc
from abc import abstractmethod
from typing import Any, Optional

class NoRepositroyAtRoot(RuntimeError): ...

class StorageInterface(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    def __init__(self, uri: Any, create: Any) -> None: ...
    @classmethod
    def getReadFormatter(cls, objType: Any): ...
    @classmethod
    def getWriteFormatter(cls, objType: Any): ...
    @classmethod
    def registerFormatters(cls, formatable: Any, readFormatter: Optional[Any] = ..., writeFormatter: Optional[Any] = ...) -> None: ...
    @abstractmethod
    def write(self, butlerLocation: Any, obj: Any) -> Any: ...
    @abstractmethod
    def read(self, butlerLocation: Any) -> Any: ...
    @abstractmethod
    def getLocalFile(self, path: Any) -> Any: ...
    @abstractmethod
    def exists(self, location: Any) -> Any: ...
    @abstractmethod
    def instanceSearch(self, path: Any) -> Any: ...
    @classmethod
    @abstractmethod
    def search(cls, root: Any, path: Any) -> Any: ...
    @abstractmethod
    def copyFile(self, fromLocation: Any, toLocation: Any) -> Any: ...
    @abstractmethod
    def locationWithRoot(self, location: Any) -> Any: ...
    @classmethod
    @abstractmethod
    def getRepositoryCfg(cls, uri: Any) -> Any: ...
    @classmethod
    @abstractmethod
    def putRepositoryCfg(cls, cfg: Any, loc: Optional[Any] = ...) -> Any: ...
    @classmethod
    @abstractmethod
    def getMapperClass(cls, root: Any) -> Any: ...
    @classmethod
    def relativePath(cls, fromPath: Any, toPath: Any): ...
    @classmethod
    def absolutePath(cls, fromPath: Any, relativePath: Any): ...
