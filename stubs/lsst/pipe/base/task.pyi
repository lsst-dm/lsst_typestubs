from typing import Any, Optional

class TaskError(Exception): ...

class Task:
    metadata: Any = ...
    log: Any = ...
    config: Any = ...
    def __init__(self, config: Optional[Any] = ..., name: Optional[Any] = ..., parentTask: Optional[Any] = ..., log: Optional[Any] = ...) -> None: ...
    def emptyMetadata(self) -> None: ...
    def getSchemaCatalogs(self): ...
    def getAllSchemaCatalogs(self): ...
    def getFullMetadata(self): ...
    def getFullName(self): ...
    def getName(self): ...
    def getTaskDict(self): ...
    def makeSubtask(self, name: Any, **keyArgs: Any) -> None: ...
    def timer(self, name: Any, logLevel: Any = ...) -> None: ...
    @classmethod
    def makeField(cls, doc: Any): ...
    def __reduce__(self): ...
