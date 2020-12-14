import lsst.pipe.base
from typing import Any, Optional

class ApCorrInfo:
    name: Any = ...
    modelName: Any = ...
    modelSigmaName: Any = ...
    doApCorrColumn: Any = ...
    instFluxName: Any = ...
    instFluxErrName: Any = ...
    instFluxKey: Any = ...
    instFluxErrKey: Any = ...
    fluxFlagKey: Any = ...
    apCorrKey: Any = ...
    apCorrErrKey: Any = ...
    apCorrFlagKey: Any = ...
    def __init__(self, schema: Any, model: Any, name: Optional[Any] = ...) -> None: ...

class ApplyApCorrConfig(lsst.pex.config.Config):
    ignoreList: Any = ...
    doFlagApCorrFailures: Any = ...
    proxies: Any = ...

class ApplyApCorrTask(lsst.pipe.base.Task):
    ConfigClass: Any = ...
    apCorrInfoDict: Any = ...
    def __init__(self, schema: Any, **kwds: Any) -> None: ...
    def run(self, catalog: Any, apCorrMap: Any) -> None: ...