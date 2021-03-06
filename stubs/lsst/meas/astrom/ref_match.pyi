import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any

class RefMatchConfig(pexConfig.Config):
    matcher: Any = ...
    matchDistanceSigma: Any = ...
    sourceSelector: Any = ...
    referenceSelector: Any = ...
    sourceFluxType: Any = ...
    def setDefaults(self) -> None: ...

class RefMatchTask(pipeBase.Task):
    ConfigClass: Any = ...
    refObjLoader: Any = ...
    def __init__(self, refObjLoader: Any, **kwargs: Any) -> None: ...
    def setRefObjLoader(self, refObjLoader: Any) -> None: ...
    def loadAndMatch(self, exposure: Any, sourceCat: Any): ...
