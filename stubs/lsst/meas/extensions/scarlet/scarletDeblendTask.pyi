import lsst.afw.table as pexConfig
import lsst.afw.table as pipeBase
from typing import Any, Optional

class IncompleteDataError(Exception): ...

class ScarletGradientError(Exception):
    iterations: Any = ...
    sources: Any = ...
    message: Any = ...
    def __init__(self, iterations: Any, sources: Any) -> None: ...

def deblend(mExposure: Any, footprint: Any, config: Any): ...

class ScarletDeblendConfig(pexConfig.Config):
    maxIter: Any = ...
    relativeError: Any = ...
    edgeDistance: Any = ...
    morphThresh: Any = ...
    monotonic: Any = ...
    symmetric: Any = ...
    useWeights: Any = ...
    modelPsfSize: Any = ...
    modelPsfSigma: Any = ...
    saveTemplates: Any = ...
    processSingles: Any = ...
    sourceModel: Any = ...
    downgrade: Any = ...
    badMask: Any = ...
    statsMask: Any = ...
    maskLimits: Any = ...
    maxNumberOfPeaks: Any = ...
    maxFootprintArea: Any = ...
    maxFootprintSize: Any = ...
    minFootprintAxisRatio: Any = ...
    fallback: Any = ...
    notDeblendedMask: Any = ...
    catchFailures: Any = ...

class ScarletDeblendTask(pipeBase.Task):
    ConfigClass: Any = ...
    peakSchemaMapper: Any = ...
    schema: Any = ...
    def __init__(self, schema: Any, peakSchema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def run(self, mExposure: Any, mergedSources: Any): ...
    def deblend(self, mExposure: Any, sources: Any): ...
