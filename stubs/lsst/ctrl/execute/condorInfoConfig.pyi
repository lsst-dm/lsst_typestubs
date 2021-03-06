import lsst.pex.config as pexConfig
from lsst.ctrl.execute import envString as envString
from typing import Any

class FakeTypeMap(dict):
    configClass: Any = ...
    def __init__(self, configClass: Any) -> None: ...
    def __getitem__(self, k: Any): ...

class UserInfoConfig(pexConfig.Config):
    name: Any = ...
    home: Any = ...

class UserConfig(pexConfig.Config):
    user: Any = ...

class CondorInfoConfig(pexConfig.Config):
    platform: Any = ...
