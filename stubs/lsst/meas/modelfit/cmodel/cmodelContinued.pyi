import lsst.meas.base
from typing import Any, Optional

CModelStageConfig: Any
CModelConfig: Any

class CModelSingleFrameConfig(lsst.meas.base.SingleFramePluginConfig, CModelConfig):
    def setDefaults(self) -> None: ...

class CModelSingleFramePlugin(lsst.meas.base.SingleFramePlugin):
    ConfigClass: Any = ...
    @staticmethod
    def getExecutionOrder(): ...
    algorithm: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...

class CModelForcedConfig(lsst.meas.base.ForcedPluginConfig, CModelConfig):
    def setDefaults(self) -> None: ...

class CModelForcedPlugin(lsst.meas.base.ForcedPlugin):
    ConfigClass: Any = ...
    @staticmethod
    def getExecutionOrder(): ...
    algorithm: Any = ...
    def __init__(self, config: Any, name: Any, schemaMapper: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...
