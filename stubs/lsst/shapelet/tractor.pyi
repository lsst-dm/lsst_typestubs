from .multiShapeletBasis import MultiShapeletBasis as MultiShapeletBasis
from .radialProfile import RadialProfile as RadialProfile
from .shapeletFunction import ShapeletFunction as ShapeletFunction
from typing import Any

def registerRadialProfiles() -> None: ...
def evaluateRadial(basis: Any, r: Any, sbNormalize: bool = ..., doComponents: bool = ...): ...
def integrateNormalizedFluxes(maxRadius: float = ..., nSteps: int = ...): ...
def plotSuite(doComponents: bool = ...): ...