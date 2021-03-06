import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class ProcessCcdConfig(pexConfig.Config):
    isr: Any = ...
    charImage: Any = ...
    doCalibrate: Any = ...
    calibrate: Any = ...
    def setDefaults(self) -> None: ...

class ProcessCcdTask(pipeBase.CmdLineTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    def __init__(self, butler: Optional[Any] = ..., psfRefObjLoader: Optional[Any] = ..., astromRefObjLoader: Optional[Any] = ..., photoRefObjLoader: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def runDataRef(self, sensorRef: Any): ...
