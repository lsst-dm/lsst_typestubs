import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from lsst.skymap import skyMapRegistry as skyMapRegistry
from typing import Any, Optional

class MakeGen3SkyMapConfig(pexConfig.Config):
    name: Any = ...
    skyMap: Any = ...
    def validate(self) -> None: ...

class MakeGen3SkyMapTask(pipeBase.Task):
    ConfigClass: Any = ...
    def __init__(self, *, config: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def run(self, butler: Any): ...
