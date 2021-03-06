from .psfDeterminer import BasePsfDeterminerTask
from typing import Any, Optional

class PcaPsfDeterminerConfig(BasePsfDeterminerTask.ConfigClass):
    nonLinearSpatialFit: Any = ...
    nEigenComponents: Any = ...
    spatialOrder: Any = ...
    sizeCellX: Any = ...
    sizeCellY: Any = ...
    nStarPerCell: Any = ...
    borderWidth: Any = ...
    nStarPerCellSpatialFit: Any = ...
    constantWeight: Any = ...
    nIterForPsf: Any = ...
    tolerance: Any = ...
    lam: Any = ...
    reducedChi2ForPsfCandidates: Any = ...
    spatialReject: Any = ...
    pixelThreshold: Any = ...
    doRejectBlends: Any = ...
    doMaskBlends: Any = ...

class PcaPsfDeterminerTask(BasePsfDeterminerTask):
    ConfigClass: Any = ...
    def determinePsf(self, exposure: Any, psfCandidateList: Any, metadata: Optional[Any] = ..., flagKey: Optional[Any] = ...): ...
