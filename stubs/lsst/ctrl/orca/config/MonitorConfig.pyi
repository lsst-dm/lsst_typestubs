import lsst.pex.config as pexConfig
from typing import Any

class MonitorConfig(pexConfig.Config):
    statusCheckInterval: Any = ...
