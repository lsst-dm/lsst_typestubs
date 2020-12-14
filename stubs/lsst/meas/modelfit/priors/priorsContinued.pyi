from .priors import SoftenedLinearPriorControl as SoftenedLinearPriorControl
from typing import Any

SemiEmpiricalPriorConfig: Any

class SemiEmpiricalPrior:
    ConfigClass: Any = ...

class SoftenedLinearPrior:
    ConfigClass: Any = ...

def fitMixture(data: Any, nComponents: Any, minFactor: float = ..., maxFactor: float = ..., nIterations: int = ..., df: Any = ...): ...
