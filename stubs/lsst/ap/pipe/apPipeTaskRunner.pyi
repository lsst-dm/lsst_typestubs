import lsst.pipe.base as pipeBase
from typing import Any

class ApPipeTaskRunner(pipeBase.ButlerInitializedTaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...
