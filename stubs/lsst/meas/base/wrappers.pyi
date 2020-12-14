from .forcedMeasurement import ForcedPlugin
from .pluginsBase import BasePlugin
from .sfm import SingleFramePlugin
from typing import Any, Optional

class WrappedSingleFramePlugin(SingleFramePlugin):
    cpp: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any, logName: Optional[Any] = ...) -> None: ...
    def measure(self, measRecord: Any, exposure: Any) -> None: ...
    def measureN(self, measCat: Any, exposure: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

class WrappedForcedPlugin(ForcedPlugin):
    cpp: Any = ...
    def __init__(self, config: Any, name: Any, schemaMapper: Any, metadata: Any, logName: Optional[Any] = ...) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...
    def measureN(self, measCat: Any, exposure: Any, refCat: Any, refWcs: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

def wrapAlgorithmControl(Base: Any, Control: Any, module: Optional[Any] = ..., hasMeasureN: bool = ...): ...
def wrapAlgorithm(Base: Any, AlgClass: Any, factory: Any, executionOrder: Any, name: Optional[Any] = ..., Control: Optional[Any] = ..., ConfigClass: Optional[Any] = ..., TransformClass: Optional[Any] = ..., doRegister: bool = ..., shouldApCorr: bool = ..., apCorrList: Any = ..., hasLogName: bool = ..., **kwds: Any): ...
def wrapSingleFrameAlgorithm(AlgClass: Any, executionOrder: Any, name: Optional[Any] = ..., needsMetadata: bool = ..., hasMeasureN: bool = ..., hasLogName: bool = ..., **kwds: Any): ...
def wrapForcedAlgorithm(AlgClass: Any, executionOrder: Any, name: Optional[Any] = ..., needsMetadata: bool = ..., hasMeasureN: bool = ..., needsSchemaOnly: bool = ..., hasLogName: bool = ..., **kwds: Any): ...
def wrapSimpleAlgorithm(AlgClass: Any, executionOrder: Any, name: Optional[Any] = ..., needsMetadata: bool = ..., hasMeasureN: bool = ..., hasLogName: bool = ..., **kwds: Any): ...
def wrapTransform(transformClass: Any, hasLogName: bool = ...) -> None: ...

class GenericPlugin(BasePlugin):
    ConfigClass: Any = ...
    @classmethod
    def getExecutionOrder(cls): ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any, logName: Optional[Any] = ...) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, center: Any) -> None: ...
    def measureN(self, measCat: Any, exposure: Any, refCat: Any, refWcs: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...
    @classmethod
    def makeSingleFramePlugin(cls, name: Any): ...
    @classmethod
    def makeForcedPlugin(cls, name: Any): ...