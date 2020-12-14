import lsst.pex.config as pexConfig
from typing import Any

class PlatformConfig(pexConfig.Config):
    defaultRoot: Any = ...
    localScratch: Any = ...
    idsPerJob: Any = ...
    dataDirectory: Any = ...
    fileSystemDomain: Any = ...
    eupsPath: Any = ...
    nodeSetRequired: Any = ...
    scheduler: Any = ...
    manager: Any = ...
    setup_using: Any = ...
    manager_software_home: Any = ...

class CondorConfig(pexConfig.Config):
    platform: Any = ...

class FakeTypeMap(dict):
    configClass: Any = ...
    def __init__(self, configClass: Any) -> None: ...
    def __getitem__(self, k: Any): ...
