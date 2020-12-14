from .radialProfile import RadialProfile as RadialProfile
from lsst.utils import continueClass as continueClass
from typing import Any

class RadialProfile:
    def evaluate(self, r: Any): ...
