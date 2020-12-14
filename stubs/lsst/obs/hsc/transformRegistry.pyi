from lsst.afw.geom import TransformPoint2ToPoint2 as TransformPoint2ToPoint2, transformRegistry as transformRegistry
from lsst.geom import arcseconds as arcseconds
from lsst.pex.config import Config as Config, Field as Field, ListField as ListField
from typing import Any

class HscDistortionConfig(Config):
    ccdToSkyOrder: Any = ...
    xCcdToSky: Any = ...
    yCcdToSky: Any = ...
    tolerance: Any = ...
    maxIter: Any = ...
    plateScale: Any = ...
    pixelSize: Any = ...

def makeAstPolyMapCoeffs(order: Any, xCoeffs: Any, yCoeffs: Any): ...
def makeHscDistortion(config: Any): ...
