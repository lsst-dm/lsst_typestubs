import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any

class IsrMockConfig(pexConfig.Config):
    isLsstLike: Any = ...
    plateScale: Any = ...
    radialDistortion: Any = ...
    isTrimmed: Any = ...
    detectorIndex: Any = ...
    rngSeed: Any = ...
    gain: Any = ...
    readNoise: Any = ...
    expTime: Any = ...
    skyLevel: Any = ...
    sourceFlux: Any = ...
    sourceAmp: Any = ...
    sourceX: Any = ...
    sourceY: Any = ...
    overscanScale: Any = ...
    biasLevel: Any = ...
    darkRate: Any = ...
    darkTime: Any = ...
    flatDrop: Any = ...
    fringeScale: Any = ...
    fringeX0: Any = ...
    fringeY0: Any = ...
    doAddSky: Any = ...
    doAddSource: Any = ...
    doAddCrosstalk: Any = ...
    doAddOverscan: Any = ...
    doAddBias: Any = ...
    doAddDark: Any = ...
    doAddFlat: Any = ...
    doAddFringe: Any = ...
    doTransmissionCurve: Any = ...
    doDefects: Any = ...
    doBrighterFatter: Any = ...
    doCrosstalkCoeffs: Any = ...
    doDataRef: Any = ...
    doGenerateImage: Any = ...
    doGenerateData: Any = ...
    doGenerateAmpDict: Any = ...

class IsrMock(pipeBase.Task):
    ConfigClass: Any = ...
    rng: Any = ...
    crosstalkCoeffs: Any = ...
    bfKernel: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def run(self): ...
    def makeData(self): ...
    def makeBfKernel(self): ...
    def makeDefectList(self): ...
    def makeCrosstalkCoeff(self): ...
    def makeTransmissionCurve(self): ...
    def makeImage(self): ...
    def getCamera(self): ...
    def getExposure(self): ...
    def getWcs(self): ...
    def localCoordToExpCoord(self, ampData: Any, x: Any, y: Any): ...
    def amplifierAddNoise(self, ampData: Any, mean: Any, sigma: Any) -> None: ...
    def amplifierAddYGradient(self, ampData: Any, start: Any, end: Any) -> None: ...
    def amplifierAddSource(self, ampData: Any, scale: Any, x0: Any, y0: Any) -> None: ...
    def amplifierAddCT(self, ampDataSource: Any, ampDataTarget: Any, scale: Any) -> None: ...
    def amplifierAddFringe(self, amp: Any, ampData: Any, scale: Any, x0: int = ..., y0: int = ...) -> None: ...
    def amplifierMultiplyFlat(self, amp: Any, ampData: Any, fracDrop: Any, u0: float = ..., v0: float = ...) -> None: ...

class RawMock(IsrMock):
    def __init__(self, **kwargs: Any) -> None: ...

class TrimmedRawMock(RawMock):
    def __init__(self, **kwargs: Any) -> None: ...

class CalibratedRawMock(RawMock):
    def __init__(self, **kwargs: Any) -> None: ...

class RawDictMock(RawMock):
    def __init__(self, **kwargs: Any) -> None: ...

class MasterMock(IsrMock):
    def __init__(self, **kwargs: Any) -> None: ...

class BiasMock(MasterMock):
    def __init__(self, **kwargs: Any) -> None: ...

class DarkMock(MasterMock):
    def __init__(self, **kwargs: Any) -> None: ...

class FlatMock(MasterMock):
    def __init__(self, **kwargs: Any) -> None: ...

class FringeMock(MasterMock):
    def __init__(self, **kwargs: Any) -> None: ...

class UntrimmedFringeMock(FringeMock):
    def __init__(self, **kwargs: Any) -> None: ...

class BfKernelMock(IsrMock):
    def __init__(self, **kwargs: Any) -> None: ...

class DefectMock(IsrMock):
    def __init__(self, **kwargs: Any) -> None: ...

class CrosstalkCoeffMock(IsrMock):
    def __init__(self, **kwargs: Any) -> None: ...

class TransmissionMock(IsrMock):
    def __init__(self, **kwargs: Any) -> None: ...

class DataRefMock:
    dataId: str = ...
    darkval: float = ...
    oscan: float = ...
    gradient: float = ...
    exptime: float = ...
    darkexptime: float = ...
    config: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def expectImage(self) -> None: ...
    def expectData(self) -> None: ...
    def get(self, dataType: Any, **kwargs: Any): ...
    def put(self, exposure: Any, filename: Any) -> None: ...

class FringeDataRefMock:
    dataId: str = ...
    darkval: float = ...
    oscan: float = ...
    gradient: float = ...
    exptime: int = ...
    darkexptime: float = ...
    config: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def get(self, dataType: Any, **kwargs: Any): ...
    def put(self, exposure: Any, filename: Any) -> None: ...
