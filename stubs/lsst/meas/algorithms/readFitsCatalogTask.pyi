import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any

class ReadFitsCatalogConfig(pexConfig.Config):
    hdu: Any = ...
    column_map: Any = ...

class ReadFitsCatalogTask(pipeBase.Task):
    ConfigClass: Any = ...
    def run(self, filename: Any): ...
