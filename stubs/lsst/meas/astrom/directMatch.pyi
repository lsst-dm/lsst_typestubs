from lsst.pex.config import Config
from lsst.pipe.base import Task
from typing import Any, Optional

class DirectMatchConfigWithoutLoader(Config):
    matchRadius: Any = ...
    sourceSelection: Any = ...
    referenceSelection: Any = ...

class DirectMatchConfig(DirectMatchConfigWithoutLoader):
    refObjLoader: Any = ...

class DirectMatchTask(Task):
    ConfigClass: Any = ...
    refObjLoader: Any = ...
    def __init__(self, butler: Optional[Any] = ..., refObjLoader: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def setRefObjLoader(self, refObjLoader: Any) -> None: ...
    def run(self, catalog: Any, filterName: Optional[Any] = ..., epoch: Optional[Any] = ...): ...
    def calculateCircle(self, catalog: Any): ...