from lsst.pex.config import Config
from lsst.pipe.base import Task
from typing import Any

class RegisterConfig(Config):
    matchRadius: Any = ...
    sipOrder: Any = ...
    sipIter: Any = ...
    sipRej: Any = ...
    warper: Any = ...

class RegisterTask(Task):
    ConfigClass: Any = ...
    def run(self, inputSources: Any, inputWcs: Any, inputBBox: Any, templateSources: Any): ...
    def matchSources(self, inputSources: Any, templateSources: Any): ...
    def fitWcs(self, matches: Any, inputWcs: Any, inputBBox: Any): ...
    def warpExposure(self, inputExp: Any, newWcs: Any, templateWcs: Any, templateBBox: Any): ...
    def warpSources(self, inputSources: Any, newWcs: Any, templateWcs: Any, templateBBox: Any): ...