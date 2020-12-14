from ..gen2to3 import CalibRepo as CalibRepo, ConvertRepoSkyMapConfig as ConvertRepoSkyMapConfig, ConvertRepoTask as ConvertRepoTask, Rerun as Rerun
from lsst.log import Log as Log
from lsst.log.utils import temporaryLogLevel as temporaryLogLevel
from typing import Any

def convert(repo: Any, gen2root: Any, skymap_name: Any, skymap_config: Any, calibs: Any, reruns: Any, config_file: Any, transfer: Any, processes: int = ...) -> None: ...
