from ..python import reduceTransform as reduceTransform
from .skyWcs import SkyWcs as SkyWcs
from lsst.utils import continueClass as continueClass
from typing import Any

class SkyWcs:
    def pixelToSkyArray(self, x: Any, y: Any, degrees: bool = ...): ...
    def skyToPixelArray(self, ra: Any, dec: Any, degrees: bool = ...): ...
