import io
from . import QuantumGraph as QuantumGraph
from ..pipeline import TaskDef as TaskDef
from .quantumNode import NodeId as NodeId
from collections import UserDict
from lsst.daf.butler import ButlerURI as ButlerURI, Quantum as Quantum
from lsst.daf.butler.core._butlerUri.file import ButlerFileURI as ButlerFileURI
from lsst.daf.butler.core._butlerUri.s3 import ButlerS3URI as ButlerS3URI
from typing import Any, Iterable, Optional, Type, Union

class RegistryDict(UserDict):
    def __missing__(self, key: Any): ...

HELPER_REGISTRY: Any

def register_helper(URICLass: Union[Type[ButlerURI], Type[io.IO[bytes]]]) -> Any: ...

class DefaultLoadHelper:
    uriObject: Any = ...
    headerSize: Any = ...
    def __init__(self, uriObject: Union[ButlerURI, io.IO[bytes]]) -> None: ...
    def load(self, nodes: Optional[Iterable[int]]=..., graphID: Optional[str]=...) -> QuantumGraph: ...
    def close(self) -> None: ...

class S3LoadHelper(DefaultLoadHelper): ...

class FileLoadHelper(DefaultLoadHelper):
    def close(self) -> None: ...

class OpenFileHandleHelper(DefaultLoadHelper):
    uriObject: Any
    def __init__(self, uriObject: io.IO[bytes]) -> None: ...

class LoadHelper:
    uri: ButlerURI
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def __init__(self, uri: Any) -> None: ...
