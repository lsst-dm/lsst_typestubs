import lsst.geom
from lsst.pex.config import Config
from lsst.pipe.base import Struct
from typing import Any, Optional

class DeconvolutionError(RuntimeError): ...

class ConvolvedFluxData(Struct):
    def __init__(self, name: Any, schema: Any, seeing: Any, config: Any, metadata: Any) -> None: ...

class BaseConvolvedFluxConfig(Config):
    seeing: Any = ...
    kernelScale: Any = ...
    aperture: Any = ...
    kronRadiusName: Any = ...
    maxSincRadius: Any = ...
    kronRadiusForFlux: Any = ...
    registerForApCorr: Any = ...
    def setDefaults(self) -> None: ...
    def getBaseNameForSeeing(self, seeing: Any, name: Any = ...): ...
    def getApertureResultName(self, seeing: Any, radius: Any, name: Any = ...): ...
    def getKronResultName(self, seeing: Any, name: Any = ...): ...
    def getAllApertureResultNames(self, name: Any = ...): ...
    def getAllKronResultNames(self, name: Any = ...): ...
    def getAllResultNames(self, name: Any = ...): ...

class BaseConvolvedFluxPlugin(lsst.meas.base.BaseMeasurementPlugin):
    @classmethod
    def getExecutionOrder(cls): ...
    seeingKey: Any = ...
    data: Any = ...
    flagHandler: Any = ...
    centroidExtractor: Any = ...
    def __init__(self, config: Any, name: Any, schema: Any, metadata: Any) -> None: ...
    def measure(self, measRecord: Any, exposure: Any): ...
    def measureForced(self, measRecord: Any, exposure: Any, refRecord: Any, refWcs: Any) -> None: ...
    def fail(self, measRecord: Any, error: Optional[Any] = ...) -> None: ...
    def getKronAperture(self, refRecord: Any, transform: Any): ...
    def getMaxRadius(self, kron: Any): ...
    def convolve(self, exposure: Any, seeing: Any, target: Any, footprint: Any, maxRadius: Any): ...
    def measureAperture(self, measRecord: Any, exposure: Any, aperturePhot: Any) -> None: ...
    def measureForcedKron(self, measRecord: Any, keys: Any, image: Any, aperture: Any) -> None: ...

SingleFrameConvolvedFluxPlugin: Any
SingleFrameConvolvedFluxConfig: Any
ForcedConvolvedFluxPlugin: Any
ForcedConvolvedFluxConfig: Any