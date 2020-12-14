import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any

class ExampleCmdLineConfig(pexConfig.Config):
    stats: Any = ...
    doFail: Any = ...

class ExampleCmdLineTask(pipeBase.CmdLineTask):
    ConfigClass: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def runDataRef(self, dataRef: Any): ...