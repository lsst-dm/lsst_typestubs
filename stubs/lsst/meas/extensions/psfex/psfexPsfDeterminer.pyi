import lsst.meas.extensions.psfex as measAlg
from typing import Any, Optional

class PsfexPsfDeterminerConfig(measAlg.BasePsfDeterminerConfig):
    spatialOrder: Any = ...
    sizeCellX: Any = ...
    sizeCellY: Any = ...
    samplingSize: Any = ...
    badMaskBits: Any = ...
    psfexBasis: Any = ...
    tolerance: Any = ...
    lam: Any = ...
    reducedChi2ForPsfCandidates: Any = ...
    spatialReject: Any = ...
    recentroid: Any = ...
    kernelSize: Any = ...

class PsfexPsfDeterminerTask(measAlg.BasePsfDeterminerTask):
    ConfigClass: Any = ...
    def determinePsf(self, exposure: Any, psfCandidateList: Any, metadata: Optional[Any] = ..., flagKey: Optional[Any] = ...): ...