from typing import Any, Optional

def prepareWcsData(wcs: Any, amp: Any, isTrimmed: bool = ...): ...
def plotFocalPlane(camera: Any, fieldSizeDeg_x: int = ..., fieldSizeDeg_y: Optional[Any] = ..., dx: float = ..., dy: float = ..., figsize: Any = ..., useIds: bool = ..., showFig: bool = ..., savePath: Optional[Any] = ...) -> None: ...
def makeImageFromAmp(amp: Any, imValue: Optional[Any] = ..., imageFactory: Any = ..., markSize: int = ..., markValue: int = ..., scaleGain: Any = ...): ...
def calcRawCcdBBox(ccd: Any): ...
def makeImageFromCcd(ccd: Any, isTrimmed: bool = ..., showAmpGain: bool = ..., imageFactory: Any = ..., rcMarkSize: int = ..., binSize: int = ...): ...

class FakeImageDataSource:
    isTrimmed: Any = ...
    verbose: Any = ...
    background: Any = ...
    showAmpGain: Any = ...
    markSize: Any = ...
    markValue: Any = ...
    ampImValue: Any = ...
    scaleGain: Any = ...
    def __init__(self, isTrimmed: bool = ..., verbose: bool = ..., background: Any = ..., showAmpGain: bool = ..., markSize: int = ..., markValue: int = ..., ampImValue: Optional[Any] = ..., scaleGain: Any = ...): ...
    def getCcdImage(self, det: Any, imageFactory: Any, binSize: Any): ...
    def getAmpImage(self, amp: Any, imageFactory: Any): ...

class ButlerImage(FakeImageDataSource):
    isTrimmed: Any = ...
    type: Any = ...
    butler: Any = ...
    kwargs: Any = ...
    isRaw: bool = ...
    background: Any = ...
    verbose: Any = ...
    callback: Any = ...
    def __init__(self, butler: Optional[Any] = ..., type: str = ..., isTrimmed: bool = ..., verbose: bool = ..., background: Any = ..., callback: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
    def getCcdImage(self, ccd: Any, imageFactory: Any = ..., binSize: int = ..., asMaskedImage: bool = ...): ...

def rawCallback(im: Any, ccd: Optional[Any] = ..., imageSource: Optional[Any] = ..., correctGain: bool = ..., subtractBias: bool = ..., convertToFloat: bool = ..., obeyNQuarter: bool = ...): ...
def overlayCcdBoxes(ccd: Any, untrimmedCcdBbox: Optional[Any] = ..., nQuarter: int = ..., isTrimmed: bool = ..., ccdOrigin: Any = ..., display: Optional[Any] = ..., binSize: int = ...) -> None: ...
def showAmp(amp: Any, imageSource: Any = ..., display: Optional[Any] = ..., overlay: bool = ..., imageFactory: Any = ...) -> None: ...
def showCcd(ccd: Any, imageSource: Any = ..., display: Optional[Any] = ..., overlay: bool = ..., imageFactory: Any = ..., binSize: int = ..., inCameraCoords: bool = ...): ...
def getCcdInCamBBoxList(ccdList: Any, binSize: Any, pixelSize_o: Any, origin: Any): ...
def getCameraImageBBox(camBbox: Any, pixelSize: Any, bufferSize: Any): ...
def makeImageFromCamera(camera: Any, detectorNameList: Optional[Any] = ..., background: Any = ..., bufferSize: int = ..., imageSource: Any = ..., imageFactory: Any = ..., binSize: int = ...): ...
def showCamera(camera: Any, imageSource: Any = ..., imageFactory: Any = ..., detectorNameList: Optional[Any] = ..., binSize: int = ..., bufferSize: int = ..., overlay: bool = ..., title: str = ..., showWcs: Optional[Any] = ..., ctype: Any = ..., textSize: float = ..., originAtCenter: bool = ..., display: Optional[Any] = ..., **kwargs: Any): ...
def makeFocalPlaneWcs(pixelSize: Any, referencePixel: Any): ...
def findAmp(ccd: Any, pixelPosition: Any): ...
