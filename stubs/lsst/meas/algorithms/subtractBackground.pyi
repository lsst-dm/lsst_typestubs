import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class SubtractBackgroundConfig(pexConfig.Config):
    statisticsProperty: Any = ...
    undersampleStyle: Any = ...
    binSize: Any = ...
    binSizeX: Any = ...
    binSizeY: Any = ...
    algorithm: Any = ...
    ignoredPixelMask: Any = ...
    isNanSafe: Any = ...
    useApprox: Any = ...
    approxOrderX: Any = ...
    approxOrderY: Any = ...
    weighting: Any = ...

class SubtractBackgroundTask(pipeBase.Task):
    ConfigClass: Any = ...
    def run(self, exposure: Any, background: Optional[Any] = ..., stats: bool = ..., statsKeys: Optional[Any] = ...): ...
    def fitBackground(self, maskedImage: Any, nx: int = ..., ny: int = ..., algorithm: Optional[Any] = ...): ...
