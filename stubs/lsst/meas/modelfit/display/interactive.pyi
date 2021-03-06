from typing import Any, Optional

class Interactive:
    mode: Any = ...
    butler: Any = ...
    dataRef: Any = ...
    task: Any = ...
    inputs: Any = ...
    def __init__(self, root: Any, tag: Optional[Any] = ..., config: Optional[Any] = ..., dataId: Optional[Any] = ..., mode: str = ...) -> None: ...
    def fit(self, outRecord: Any): ...
    def plotDistribution(self, *records: Any): ...
    def displayOptimizer(self, record: Any, **kwds: Any): ...
    def displayResiduals(self, record: Any, nonlinear: str = ..., amplitudes: str = ..., doApplyWeights: bool = ...) -> None: ...
