from typing import Any

class CovFft:
    pCov: Any = ...
    pMean: Any = ...
    pCount: Any = ...
    def __init__(self, diff: Any, w: Any, fftShape: Any, maxRangeCov: Any) -> None: ...
    def cov(self, dx: Any, dy: Any): ...
    def reportCovFft(self, maxRange: Any): ...

class LoadParams:
    r: int = ...
    subtractDistantValue: bool = ...
    start: int = ...
    offsetDegree: int = ...
    def __init__(self) -> None: ...