import lsst.pex.config as pexConfig
import lsst.pex.config as pipeBase
from typing import Any

class DecamNullIsrConfig(pexConfig.Config):
    doWrite: Any = ...
    datasetType: Any = ...

class DecamNullIsrTask(pipeBase.Task):
    ConfigClass: Any = ...
    def runDataRef(self, sensorRef: Any): ...
