import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class MakeGen3DcrSubfiltersConfig(pexConfig.Config):
    numSubfilters: Any = ...
    filterNames: Any = ...

class MakeGen3DcrSubfiltersTask(pipeBase.Task):
    ConfigClass: Any = ...
    def __init__(self, *, config: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def run(self, butler: Any) -> None: ...
    def register(self, registry: Any) -> None: ...
