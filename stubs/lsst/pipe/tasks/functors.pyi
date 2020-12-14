from .parquetTable import MultilevelParquetTable as MultilevelParquetTable
from lsst.daf.persistence import doImport as doImport
from typing import Any, Optional

def init_fromDict(initDict: Any, basePath: str = ..., typeKey: str = ..., name: Optional[Any] = ...): ...

class Functor:
    filt: Any = ...
    dataset: Any = ...
    def __init__(self, filt: Optional[Any] = ..., dataset: Optional[Any] = ..., noDup: Optional[Any] = ...) -> None: ...
    @property
    def noDup(self): ...
    @property
    def columns(self): ...
    def multilevelColumns(self, parq: Any): ...
    def __call__(self, parq: Any, dropna: bool = ...): ...
    def difference(self, parq1: Any, parq2: Any, **kwargs: Any): ...
    def fail(self, df: Any): ...
    @property
    def name(self): ...
    @property
    def shortname(self): ...

class CompositeFunctor(Functor):
    dataset: Any = ...
    funcDict: Any = ...
    def __init__(self, funcs: Any, **kwargs: Any) -> None: ...
    @property
    def filt(self): ...
    @filt.setter
    def filt(self, filt: Any) -> None: ...
    def update(self, new: Any) -> None: ...
    @property
    def columns(self): ...
    def multilevelColumns(self, parq: Any): ...
    def __call__(self, parq: Any, **kwargs: Any): ...
    @classmethod
    def renameCol(cls, col: Any, renameRules: Any): ...
    @classmethod
    def from_file(cls, filename: Any, **kwargs: Any): ...
    @classmethod
    def from_yaml(cls, translationDefinition: Any, **kwargs: Any): ...

def mag_aware_eval(df: Any, expr: Any): ...

class CustomFunctor(Functor):
    expr: Any = ...
    def __init__(self, expr: Any, **kwargs: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def columns(self): ...

class Column(Functor):
    col: Any = ...
    def __init__(self, col: Any, **kwargs: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def columns(self): ...

class Index(Functor):
    columns: Any = ...

class IDColumn(Column):
    col: str = ...

class FootprintNPix(Column):
    col: str = ...

class CoordColumn(Column):
    def __init__(self, col: Any, **kwargs: Any) -> None: ...

class RAColumn(CoordColumn):
    name: str = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def __call__(self, catalog: Any, **kwargs: Any): ...

class DecColumn(CoordColumn):
    name: str = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def __call__(self, catalog: Any, **kwargs: Any): ...

def fluxName(col: Any): ...
def fluxErrName(col: Any): ...

class Mag(Functor):
    col: Any = ...
    calib: Any = ...
    fluxMag0: Any = ...
    def __init__(self, col: Any, calib: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def columns(self): ...
    @property
    def name(self): ...

class MagErr(Mag):
    fluxMag0Err: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def columns(self): ...
    @property
    def name(self): ...

class NanoMaggie(Mag): ...

class MagDiff(Functor):
    col1: Any = ...
    col2: Any = ...
    def __init__(self, col1: Any, col2: Any, **kwargs: Any) -> None: ...
    @property
    def columns(self): ...
    @property
    def name(self): ...
    @property
    def shortname(self): ...

class Color(Functor):
    col: Any = ...
    filt2: Any = ...
    filt1: Any = ...
    mag2: Any = ...
    mag1: Any = ...
    def __init__(self, col: Any, filt2: Any, filt1: Any, **kwargs: Any) -> None: ...
    @property
    def filt(self) -> None: ...
    @filt.setter
    def filt(self, filt: Any) -> None: ...
    @property
    def columns(self): ...
    def multilevelColumns(self, parq: Any): ...
    @property
    def name(self): ...
    @property
    def shortname(self): ...

class Labeller(Functor):
    name: str = ...
    def __call__(self, parq: Any, dropna: bool = ..., **kwargs: Any): ...

class StarGalaxyLabeller(Labeller): ...

class NumStarLabeller(Labeller):
    labels: Any = ...

class DeconvolvedMoments(Functor):
    name: str = ...
    shortname: str = ...

class SdssTraceSize(Functor):
    name: str = ...
    shortname: str = ...

class PsfSdssTraceSizeDiff(Functor):
    name: str = ...
    shortname: str = ...

class HsmTraceSize(Functor):
    name: str = ...
    shortname: str = ...

class PsfHsmTraceSizeDiff(Functor):
    name: str = ...
    shortname: str = ...

class HsmFwhm(Functor):
    name: str = ...
    pixelScale: float = ...
    SIGMA2FWHM: Any = ...

class E1(Functor):
    name: str = ...
    shortname: str = ...
    colXX: Any = ...
    colXY: Any = ...
    colYY: Any = ...
    def __init__(self, colXX: Any, colXY: Any, colYY: Any, **kwargs: Any) -> None: ...
    @property
    def columns(self): ...

class E2(Functor):
    name: str = ...
    colXX: Any = ...
    colXY: Any = ...
    colYY: Any = ...
    def __init__(self, colXX: Any, colXY: Any, colYY: Any, **kwargs: Any) -> None: ...
    @property
    def columns(self): ...

class RadiusFromQuadrupole(Functor):
    colXX: Any = ...
    colXY: Any = ...
    colYY: Any = ...
    def __init__(self, colXX: Any, colXY: Any, colYY: Any, **kwargs: Any) -> None: ...
    @property
    def columns(self): ...

class LocalWcs(Functor):
    name: str = ...
    colCD_1_1: Any = ...
    colCD_1_2: Any = ...
    colCD_2_1: Any = ...
    colCD_2_2: Any = ...
    def __init__(self, colCD_1_1: Any, colCD_1_2: Any, colCD_2_1: Any, colCD_2_2: Any, **kwargs: Any) -> None: ...
    def computeDeltaRaDec(self, x: Any, y: Any, cd11: Any, cd12: Any, cd21: Any, cd22: Any): ...
    def computeSkySeperation(self, ra1: Any, dec1: Any, ra2: Any, dec2: Any): ...
    def getSkySeperationFromPixel(self, x1: Any, y1: Any, x2: Any, y2: Any, cd11: Any, cd12: Any, cd21: Any, cd22: Any): ...

class ComputePixelScale(LocalWcs):
    name: str = ...
    @property
    def columns(self): ...
    def pixelScaleArcseconds(self, cd11: Any, cd12: Any, cd21: Any, cd22: Any): ...

class ConvertPixelToArcseconds(ComputePixelScale):
    col: Any = ...
    def __init__(self, col: Any, colCD_1_1: Any, colCD_1_2: Any, colCD_2_1: Any, colCD_2_2: Any, **kwargs: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def columns(self): ...

class ReferenceBand(Functor):
    name: str = ...
    shortname: str = ...
    @property
    def columns(self): ...

class Photometry(Functor):
    AB_FLUX_SCALE: Any = ...
    LOG_AB_FLUX_SCALE: float = ...
    FIVE_OVER_2LOG10: float = ...
    COADD_ZP: int = ...
    vhypot: Any = ...
    col: Any = ...
    colFluxErr: Any = ...
    calib: Any = ...
    fluxMag0: Any = ...
    fluxMag0Err: float = ...
    def __init__(self, colFlux: Any, colFluxErr: Optional[Any] = ..., calib: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def columns(self): ...
    @property
    def name(self): ...
    @classmethod
    def hypot(cls, a: Any, b: Any): ...
    def dn2flux(self, dn: Any, fluxMag0: Any): ...
    def dn2mag(self, dn: Any, fluxMag0: Any): ...
    def dn2fluxErr(self, dn: Any, dnErr: Any, fluxMag0: Any, fluxMag0Err: Any): ...
    def dn2MagErr(self, dn: Any, dnErr: Any, fluxMag0: Any, fluxMag0Err: Any): ...

class NanoJansky(Photometry): ...

class NanoJanskyErr(Photometry):
    @property
    def columns(self): ...

class Magnitude(Photometry): ...

class MagnitudeErr(Photometry):
    @property
    def columns(self): ...

class LocalPhotometry(Functor):
    logNJanskyToAB: Any = ...
    instFluxCol: Any = ...
    instFluxErrCol: Any = ...
    photoCalibCol: Any = ...
    photoCalibErrCol: Any = ...
    def __init__(self, instFluxCol: Any, instFluxErrCol: Any, photoCalibCol: Any, photoCalibErrCol: Any, **kwargs: Any) -> None: ...
    def instFluxToNanojansky(self, instFlux: Any, localCalib: Any): ...
    def instFluxErrToNanojanskyErr(self, instFlux: Any, instFluxErr: Any, localCalib: Any, localCalibErr: Any): ...
    def instFluxToMagnitude(self, instFlux: Any, localCalib: Any): ...
    def instFluxErrToMagnitudeErr(self, instFlux: Any, instFluxErr: Any, localCalib: Any, localCalibErr: Any): ...

class LocalNanojansky(LocalPhotometry):
    @property
    def columns(self): ...
    @property
    def name(self): ...

class LocalNanojanskyErr(LocalPhotometry):
    @property
    def columns(self): ...
    @property
    def name(self): ...

class LocalMagnitude(LocalPhotometry):
    @property
    def columns(self): ...
    @property
    def name(self): ...

class LocalMagnitudeErr(LocalPhotometry):
    @property
    def columns(self): ...
    @property
    def name(self): ...