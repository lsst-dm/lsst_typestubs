from typing import Any, Optional

def plotOutlinedAxline(axMethod: Any, x: Any, **kwargs: Any) -> None: ...
def plotAstrometryErrorModel(dataset: Any, astromModel: Any, outputPrefix: str = ...) -> None: ...
def plotAstromErrModelFit(snr: Any, dist: Any, model: Any, color: str = ..., ax: Optional[Any] = ..., verbose: bool = ...) -> None: ...
def plotPhotErrModelFit(mag: Any, mmag_err: Any, photomModel: Any, color: str = ..., ax: Optional[Any] = ..., verbose: bool = ...) -> None: ...
def plotPhotometryErrorModel(dataset: Any, photomModel: Any, filterName: str = ..., outputPrefix: str = ...) -> None: ...
def plotPA1(pa1: Any, outputPrefix: str = ...) -> None: ...
def plotAMx(job: Any, amx: Any, afx: Any, filterName: Any, amxSpecName: str = ..., outputPrefix: str = ...) -> None: ...
