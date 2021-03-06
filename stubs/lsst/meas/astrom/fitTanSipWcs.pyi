import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class FitTanSipWcsConfig(pexConfig.Config):
    order: Any = ...
    numIter: Any = ...
    numRejIter: Any = ...
    rejSigma: Any = ...
    maxScatterArcsec: Any = ...

class FitTanSipWcsTask(pipeBase.Task):
    ConfigClass: Any = ...
    def fitWcs(self, matches: Any, initWcs: Any, bbox: Optional[Any] = ..., refCat: Optional[Any] = ..., sourceCat: Optional[Any] = ..., exposure: Optional[Any] = ...): ...
    def initialWcs(self, matches: Any, wcs: Any): ...
    def rejectMatches(self, matches: Any, wcs: Any, rejected: Any): ...
    def plotFit(self, matches: Any, wcs: Any, rejected: Any) -> None: ...
