import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class MakePsfCandidatesConfig(pexConfig.Config):
    kernelSize: Any = ...
    borderWidth: Any = ...

class MakePsfCandidatesTask(pipeBase.Task):
    ConfigClass: Any = ...
    def __init__(self, **kwds: Any) -> None: ...
    def run(self, starCat: Any, exposure: Any, psfCandidateField: Optional[Any] = ...): ...
    def makePsfCandidates(self, starCat: Any, exposure: Any): ...