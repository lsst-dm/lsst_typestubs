import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class ImageScaler:
    def __init__(self, scale: float = ...) -> None: ...
    def scaleMaskedImage(self, maskedImage: Any) -> None: ...

class SpatialImageScaler(ImageScaler):
    def __init__(self, interpStyle: Any, xList: Any, yList: Any, scaleList: Any) -> None: ...
    def scaleMaskedImage(self, maskedImage: Any) -> None: ...
    def getInterpImage(self, bbox: Any): ...

class ScaleZeroPointConfig(pexConfig.Config):
    zeroPoint: Any = ...

class SpatialScaleZeroPointConfig(ScaleZeroPointConfig):
    selectFluxMag0: Any = ...
    interpStyle: Any = ...

class ScaleZeroPointTask(pipeBase.Task):
    ConfigClass: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self, exposure: Any, dataRef: Optional[Any] = ...): ...
    def computeImageScaler(self, exposure: Any, dataRef: Optional[Any] = ...): ...
    def getPhotoCalib(self): ...
    def scaleFromPhotoCalib(self, calib: Any): ...
    def scaleFromFluxMag0(self, fluxMag0: Any): ...

class SpatialScaleZeroPointTask(ScaleZeroPointTask):
    ConfigClass: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self, exposure: Any, dataRef: Any): ...
    def computeImageScaler(self, exposure: Any, dataRef: Any): ...
