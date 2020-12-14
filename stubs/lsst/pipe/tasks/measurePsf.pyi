import lsst.meas.extensions.psfex.psfexPsfDeterminer as pexConfig
import lsst.meas.extensions.psfex.psfexPsfDeterminer as pipeBase
from typing import Any, Optional

class MeasurePsfConfig(pexConfig.Config):
    starSelector: Any = ...
    makePsfCandidates: Any = ...
    psfDeterminer: Any = ...
    reserve: Any = ...

class MeasurePsfTask(pipeBase.Task):
    ConfigClass: Any = ...
    candidateKey: Any = ...
    usedKey: Any = ...
    def __init__(self, schema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def run(self, exposure: Any, sources: Any, expId: int = ..., matches: Optional[Any] = ...): ...
    @property
    def usesMatches(self): ...

def showPsfSpatialCells(exposure: Any, cellSet: Any, showBadCandidates: Any, frame: int = ...) -> None: ...
def plotPsfCandidates(cellSet: Any, showBadCandidates: bool = ..., frame: int = ...) -> None: ...
def plotResiduals(exposure: Any, cellSet: Any, showBadCandidates: bool = ..., normalizeResiduals: bool = ..., frame: int = ...): ...