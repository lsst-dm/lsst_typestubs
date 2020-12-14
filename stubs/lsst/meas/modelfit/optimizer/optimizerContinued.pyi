from typing import Any

OptimizerConfig: Any

class OptimizerControl:
    ConfigClass: Any = ...

class Optimizer:
    ConfigClass: Any = ...
    def getConfig(self): ...
