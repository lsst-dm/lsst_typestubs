import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any

class ReadTextCatalogConfig(pexConfig.Config):
    header_lines: Any = ...
    colnames: Any = ...
    delimiter: Any = ...
    format: Any = ...

class ReadTextCatalogTask(pipeBase.Task):
    ConfigClass: Any = ...
    def run(self, filename: Any): ...