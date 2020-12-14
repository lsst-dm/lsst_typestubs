from .sourceSelector import BaseSourceSelectorTask as BaseSourceSelectorTask, sourceSelectorRegistry as sourceSelectorRegistry
from lsst.afw.cameraGeom import PIXELS as PIXELS, TAN_PIXELS as TAN_PIXELS
from lsst.log import Log as Log
from lsst.pipe.base import Struct as Struct
from typing import Any, Optional

class ObjectSizeStarSelectorConfig(BaseSourceSelectorTask.ConfigClass):
    doFluxLimit: Any = ...
    fluxMin: Any = ...
    fluxMax: Any = ...
    doSignalToNoiseLimit: Any = ...
    signalToNoiseMin: Any = ...
    signalToNoiseMax: Any = ...
    widthMin: Any = ...
    widthMax: Any = ...
    sourceFluxField: Any = ...
    widthStdAllowed: Any = ...
    nSigmaClip: Any = ...
    badFlags: Any = ...
    def validate(self) -> None: ...

class EventHandler:
    axes: Any = ...
    xs: Any = ...
    ys: Any = ...
    x: Any = ...
    y: Any = ...
    frames: Any = ...
    cid: Any = ...
    def __init__(self, axes: Any, xs: Any, ys: Any, x: Any, y: Any, frames: Any = ...) -> None: ...
    def __call__(self, ev: Any) -> None: ...

def plot(mag: Any, width: Any, centers: Any, clusterId: Any, marker: str = ..., markersize: int = ..., markeredgewidth: int = ..., ltype: str = ..., magType: str = ..., clear: bool = ...): ...

class ObjectSizeStarSelectorTask(BaseSourceSelectorTask):
    ConfigClass: Any = ...
    usesMatches: bool = ...
    def selectSources(self, sourceCat: Any, matches: Optional[Any] = ..., exposure: Optional[Any] = ...): ...