import lsst.pex.config as pexConfig
import lsst.pex.config as pipeBase
from lsst.obs.subaru import subtractCrosstalk as subtractCrosstalk
from lsst.obs.subaru.crosstalk import estimateCoeffs as estimateCoeffs, makeList as makeList, printCoeffs as printCoeffs, readImage as readImage, subtractXTalk as subtractXTalk
from typing import Any, Optional

class CrosstalkYagiCoeffsConfig(pexConfig.Config):
    crossTalkCoeffs1: Any = ...
    crossTalkCoeffs2: Any = ...
    relativeGainsPreampAndSigboard: Any = ...
    relativeGainsTotalBeforeOct2010: Any = ...
    relativeGainsTotalAfterOct2010: Any = ...
    shapeGainsArray: Any = ...
    shapeCoeffsArray: Any = ...
    def getCoeffs1(self): ...
    def getCoeffs2(self): ...
    def getGainsPreampSigboard(self): ...
    def getGainsTotal(self, dateobs: str = ...): ...

nAmp: int

def getCrosstalkX1(x: Any, xmax: int = ...): ...
def getCrosstalkX2(x: Any, xmax: int = ...): ...
def getAmplifier(image: Any, amp: Any, ampReference: Optional[Any] = ..., offset: int = ...): ...
def subtractCrosstalkYagi(mi: Any, coeffs1List: Any, coeffs2List: Any, gainsPreampSig: Any, minPixelToMask: int = ..., crosstalkStr: str = ...) -> None: ...
def main(visit: int = ..., ccd: Optional[Any] = ..., threshold: int = ..., nSample: int = ..., showCoeffs: bool = ..., fixXTalk: bool = ..., plot: bool = ..., title: Optional[Any] = ...): ...

class YagiCrosstalkConfig(pexConfig.Config):
    coeffs: Any = ...
    crosstalkMaskPlane: Any = ...
    minPixelToMask: Any = ...

class YagiCrosstalkTask(pipeBase.Task):
    ConfigClass: Any = ...
    def run(self, exposure: Any) -> None: ...
