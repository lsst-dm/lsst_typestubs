import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from lsst.meas.base import ForcedTransformedCentroidConfig, ForcedTransformedCentroidPlugin
from typing import Any

class ForcedTransformedCentroidFromCoordConfig(ForcedTransformedCentroidConfig): ...

class ForcedTransformedCentroidFromCoordPlugin(ForcedTransformedCentroidPlugin):
    ConfigClass: Any = ...
    def measure(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...

class DiaForcedSourcedConfig(pexConfig.Config):
    forcedMeasurement: Any = ...
    dropColumns: Any = ...
    def setDefaults(self) -> None: ...

class DiaForcedSourceTask(pipeBase.Task):
    ConfigClass: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def run(self, dia_objects: Any, updatedDiaObjectIds: Any, expIdBits: Any, exposure: Any, diffim: Any): ...
