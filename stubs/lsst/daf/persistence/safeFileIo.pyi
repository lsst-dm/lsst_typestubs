from lsst.log import Log as Log
from typing import Any, Optional

class DoNotWrite(RuntimeError): ...

def safeMakeDir(directory: Any) -> None: ...
def setFileMode(filename: Any) -> None: ...

class FileForWriteOnceCompareSameFailure(RuntimeError): ...

def FileForWriteOnceCompareSame(name: Any) -> None: ...
def SafeFile(name: Any) -> None: ...
def SafeFilename(name: Any) -> None: ...
def SafeLockedFileForRead(name: Any) -> None: ...

class SafeLockedFileForWrite:
    log: Any = ...
    name: Any = ...
    def __init__(self, name: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    @property
    def readable(self): ...
    @property
    def writeable(self): ...
    def read(self, size: Optional[Any] = ...): ...
    def write(self, str: Any) -> None: ...
