import lsst.pipe.base.connectionTypes as pipeBase
from typing import Any, Optional

class CharacterizeImageConnections(pipeBase.PipelineTaskConnections):
    exposure: Any = ...
    characterized: Any = ...
    sourceCat: Any = ...
    backgroundModel: Any = ...
    outputSchema: Any = ...
    def adjustQuantum(self, datasetRefMap: pipeBase.InputQuantizedConnection) -> Any: ...

class CharacterizeImageConfig(pipeBase.PipelineTaskConfig):
    doMeasurePsf: Any = ...
    doWrite: Any = ...
    doWriteExposure: Any = ...
    psfIterations: Any = ...
    background: Any = ...
    detection: Any = ...
    doDeblend: Any = ...
    deblend: Any = ...
    measurement: Any = ...
    doApCorr: Any = ...
    measureApCorr: Any = ...
    applyApCorr: Any = ...
    catalogCalculation: Any = ...
    useSimplePsf: Any = ...
    installSimplePsf: Any = ...
    refObjLoader: Any = ...
    ref_match: Any = ...
    measurePsf: Any = ...
    repair: Any = ...
    requireCrForPsf: Any = ...
    checkUnitsParseStrict: Any = ...
    def setDefaults(self) -> None: ...
    def validate(self) -> None: ...

class CharacterizeImageTask(pipeBase.PipelineTask, pipeBase.CmdLineTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    def runQuantum(self, butlerQC: Any, inputRefs: Any, outputRefs: Any) -> None: ...
    schema: Any = ...
    algMetadata: Any = ...
    outputSchema: Any = ...
    def __init__(self, butler: Optional[Any] = ..., refObjLoader: Optional[Any] = ..., schema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def getInitOutputDatasets(self): ...
    def runDataRef(self, dataRef: Any, exposure: Optional[Any] = ..., background: Optional[Any] = ..., doUnpersist: bool = ...): ...
    def run(self, exposure: Any, exposureIdInfo: Optional[Any] = ..., background: Optional[Any] = ...): ...
    def detectMeasureAndEstimatePsf(self, exposure: Any, exposureIdInfo: Any, background: Any): ...
    def getSchemaCatalogs(self): ...
    def display(self, itemName: Any, exposure: Any, sourceCat: Optional[Any] = ...) -> None: ...
