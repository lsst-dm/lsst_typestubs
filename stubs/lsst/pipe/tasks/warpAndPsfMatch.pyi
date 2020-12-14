import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class WarpAndPsfMatchConfig(pexConfig.Config):
    psfMatch: Any = ...
    warp: Any = ...

class WarpAndPsfMatchTask(pipeBase.Task):
    ConfigClass: Any = ...
    warper: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self, exposure: Any, wcs: Any, modelPsf: Optional[Any] = ..., maxBBox: Optional[Any] = ..., destBBox: Optional[Any] = ..., makeDirect: bool = ..., makePsfMatched: bool = ...): ...
