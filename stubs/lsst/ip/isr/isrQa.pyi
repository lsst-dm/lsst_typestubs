import lsst.pex.config as pexConfig
from typing import Any, Optional

class IsrQaFlatnessConfig(pexConfig.Config):
    meshX: Any = ...
    meshY: Any = ...
    doClip: Any = ...
    clipSigma: Any = ...
    nIter: Any = ...

class IsrQaConfig(pexConfig.Config):
    saveStats: Any = ...
    flatness: Any = ...
    doWriteOss: Any = ...
    doThumbnailOss: Any = ...
    doWriteFlattened: Any = ...
    doThumbnailFlattened: Any = ...
    thumbnailBinning: Any = ...
    thumbnailStdev: Any = ...
    thumbnailRange: Any = ...
    thumbnailQ: Any = ...
    thumbnailSatBorder: Any = ...

def makeThumbnail(exposure: Any, isrQaConfig: Optional[Any] = ...): ...
def writeThumbnail(dataRef: Any, thumb: Any, dataset: Any) -> None: ...
