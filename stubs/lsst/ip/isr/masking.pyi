from lsst.pex.config import Config as Config, Field as Field
from lsst.pipe.base import Task as Task
from typing import Any

class MaskingConfig(Config):
    doSpecificMasking: Any = ...

class MaskingTask(Task):
    ConfigClass: Any = ...
    def run(self, exposure: Any) -> None: ...
