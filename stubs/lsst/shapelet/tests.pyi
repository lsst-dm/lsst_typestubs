import lsst.afw.geom.ellipses
from typing import Any, Optional

class ShapeletTestCase(lsst.utils.tests.TestCase):
    @staticmethod
    def makeUnitVector(i: Any, n: Any): ...
    @staticmethod
    def makeImage(function: Any, x: Any, y: Any): ...
    @staticmethod
    def makeRandomShapeletFunction(order: int = ..., zeroCenter: bool = ..., ellipse: Optional[Any] = ..., scale: float = ...): ...
    @staticmethod
    def makeRandomMultiShapeletFunction(nComponents: int = ..., ellipse: Optional[Any] = ...): ...
    def compareShapeletFunctions(self, a: Any, b: Any, rtolEllipse: float = ..., rtolCoeff: float = ..., atolEllipse: float = ..., atolCoeff: float = ...) -> None: ...
    def simplifyMultiShapeletFunction(self, msf: Any): ...
    def compareMultiShapeletFunctions(self, a: Any, b: Any, simplify: bool = ..., rtolEllipse: float = ..., rtolCoeff: float = ..., atolEllipse: float = ..., atolCoeff: float = ...) -> None: ...
    def checkMoments(self, function: Any, x: Any, y: Any, z: Any) -> None: ...
    def checkConvolution(self, f1: Any, f2: Any): ...
