from typing import Any, Optional

class DipoleTestImage:
    w: Any = ...
    h: Any = ...
    xcenPos: Any = ...
    ycenPos: Any = ...
    xcenNeg: Any = ...
    ycenNeg: Any = ...
    psfSigma: Any = ...
    flux: Any = ...
    fluxNeg: Any = ...
    noise: Any = ...
    gradientParams: Any = ...
    def __init__(self, w: int = ..., h: int = ..., xcenPos: Any = ..., ycenPos: Any = ..., xcenNeg: Any = ..., ycenNeg: Any = ..., psfSigma: float = ..., flux: Any = ..., fluxNeg: Optional[Any] = ..., noise: float = ..., gradientParams: Optional[Any] = ...) -> None: ...
    def fitDipoleSource(self, source: Any, **kwds: Any): ...
    def detectDipoleSources(self, doMerge: bool = ..., diffim: Optional[Any] = ..., detectSigma: float = ..., grow: int = ..., minBinSize: int = ...): ...
