from . import psfexLib as psfexLib
from lsst.afw.fits import readMetadata as readMetadata
from typing import Any, Optional

def compute_fwhmrange(fwhm: Any, maxvar: Any, minin: Any, maxin: Any, plot: Any = ...): ...
def select_candidates(set: Any, prefs: Any, frmin: Any, frmax: Any, flags: Any, flux: Any, fluxerr: Any, rmsSize: Any, elong: Any, vignet: Any, plot: Any = ..., title: str = ...): ...
def showPsf(psf: Any, set: Any, ext: Optional[Any] = ..., wcsData: Optional[Any] = ..., trim: int = ..., nspot: int = ..., diagnostics: bool = ..., outDir: str = ..., frame: Optional[Any] = ..., title: Optional[Any] = ...) -> None: ...
def getFlags(tab: Optional[Any] = ...): ...
def guessCalexp(fileName: Any): ...
def makeitLsst(prefs: Any, context: Any, saveWcs: bool = ..., plot: Any = ...): ...
def read_samplesLsst(prefs: Any, set: Any, filename: Any, frmin: Any, frmax: Any, ext: Any, next: Any, catindex: Any, context: Any, pcval: Any, nobj: Any, plot: Any = ...): ...
def load_samplesLsst(prefs: Any, context: Any, ext: Any = ..., next: int = ..., plot: Any = ...): ...