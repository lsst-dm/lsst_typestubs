from .deblendCoaddSourcesPipeline import DeblendCoaddSourcesMultiConfig as DeblendCoaddSourcesMultiConfig, DeblendCoaddSourcesMultiTask as DeblendCoaddSourcesMultiTask, DeblendCoaddSourcesSingleConfig as DeblendCoaddSourcesSingleConfig, DeblendCoaddSourcesSingleTask as DeblendCoaddSourcesSingleTask
from .mergeDetections import MergeDetectionsConfig as MergeDetectionsConfig, MergeDetectionsTask as MergeDetectionsTask
from .mergeMeasurements import MergeMeasurementsConfig as MergeMeasurementsConfig, MergeMeasurementsTask as MergeMeasurementsTask
from .multiBandUtils import CullPeaksConfig as CullPeaksConfig, MergeSourcesRunner as MergeSourcesRunner, getInputSchema as getInputSchema, getShortFilterName as getShortFilterName, readCatalog as readCatalog
from lsst.coadd.utils.coaddDataIdContainer import ExistingCoaddDataIdContainer as ExistingCoaddDataIdContainer
from lsst.daf.base import PropertyList as PropertyList
from lsst.meas.algorithms import DynamicDetectionTask as DynamicDetectionTask, ReferenceObjectLoader as ReferenceObjectLoader
from lsst.meas.astrom import DirectMatchTask as DirectMatchTask, denormalizeMatches as denormalizeMatches
from lsst.meas.base import ApplyApCorrTask as ApplyApCorrTask, CatalogCalculationTask as CatalogCalculationTask, SingleFrameMeasurementTask as SingleFrameMeasurementTask
from lsst.meas.deblender import SourceDeblendTask as SourceDeblendTask
from lsst.meas.extensions.scarlet import ScarletDeblendTask as ScarletDeblendTask
from lsst.pex.config import Config as Config, ConfigurableField as ConfigurableField, Field as Field
from lsst.pipe.base import ArgumentParser as ArgumentParser, ButlerInitializedTaskRunner as ButlerInitializedTaskRunner, CmdLineTask as CmdLineTask, PipelineTask as PipelineTask, PipelineTaskConfig as PipelineTaskConfig, PipelineTaskConnections as PipelineTaskConnections, Struct as Struct
from lsst.pipe.tasks.coaddBase import getSkyInfo as getSkyInfo
from lsst.pipe.tasks.fakes import BaseFakeSourcesTask as BaseFakeSourcesTask
from lsst.pipe.tasks.propagateVisitFlags import PropagateVisitFlagsTask as PropagateVisitFlagsTask
from lsst.pipe.tasks.scaleVariance import ScaleVarianceTask as ScaleVarianceTask
from lsst.pipe.tasks.setPrimaryFlags import SetPrimaryFlagsTask as SetPrimaryFlagsTask
from lsst.skymap import BaseSkyMap as BaseSkyMap
from typing import Any, Optional

class DetectCoaddSourcesConnections(PipelineTaskConnections):
    detectionSchema: Any = ...
    exposure: Any = ...
    outputBackgrounds: Any = ...
    outputSources: Any = ...
    outputExposure: Any = ...

class DetectCoaddSourcesConfig(PipelineTaskConfig):
    doScaleVariance: Any = ...
    scaleVariance: Any = ...
    detection: Any = ...
    coaddName: Any = ...
    doInsertFakes: Any = ...
    insertFakes: Any = ...
    hasFakes: Any = ...
    def setDefaults(self) -> None: ...

class DetectCoaddSourcesTask(PipelineTask, CmdLineTask):
    ConfigClass: Any = ...
    getSchemaCatalogs: Any = ...
    makeIdFactory: Any = ...
    schema: Any = ...
    detectionSchema: Any = ...
    def __init__(self, schema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def runDataRef(self, patchRef: Any): ...
    def runQuantum(self, butlerQC: Any, inputRefs: Any, outputRefs: Any) -> None: ...
    def run(self, exposure: Any, idFactory: Any, expId: Any): ...
    def write(self, results: Any, patchRef: Any) -> None: ...

class DeblendCoaddSourcesConfig(Config):
    singleBandDeblend: Any = ...
    multiBandDeblend: Any = ...
    simultaneous: Any = ...
    coaddName: Any = ...
    hasFakes: Any = ...
    def setDefaults(self) -> None: ...

class DeblendCoaddSourcesRunner(MergeSourcesRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...

class DeblendCoaddSourcesTask(CmdLineTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    makeIdFactory: Any = ...
    schemaMapper: Any = ...
    schema: Any = ...
    def __init__(self, butler: Optional[Any] = ..., schema: Optional[Any] = ..., peakSchema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def getSchemaCatalogs(self): ...
    def runDataRef(self, patchRefList: Any, psfCache: int = ...) -> None: ...
    def readSources(self, dataRef: Any): ...
    def write(self, dataRef: Any, flux_sources: Any, template_sources: Optional[Any] = ...) -> None: ...
    def writeMetadata(self, dataRefList: Any) -> None: ...
    def getExposureId(self, dataRef: Any): ...

class MeasureMergedCoaddSourcesConnections(PipelineTaskConnections):
    inputSchema: Any = ...
    outputSchema: Any = ...
    refCat: Any = ...
    exposure: Any = ...
    skyMap: Any = ...
    visitCatalogs: Any = ...
    inputCatalog: Any = ...
    outputSources: Any = ...
    matchResult: Any = ...
    denormMatches: Any = ...
    def __init__(self, *, config: Optional[Any] = ...) -> None: ...

class MeasureMergedCoaddSourcesConfig(PipelineTaskConfig):
    inputCatalog: Any = ...
    measurement: Any = ...
    setPrimaryFlags: Any = ...
    doPropagateFlags: Any = ...
    propagateFlags: Any = ...
    doMatchSources: Any = ...
    match: Any = ...
    doWriteMatchesDenormalized: Any = ...
    coaddName: Any = ...
    psfCache: Any = ...
    checkUnitsParseStrict: Any = ...
    doApCorr: Any = ...
    applyApCorr: Any = ...
    doRunCatalogCalculation: Any = ...
    catalogCalculation: Any = ...
    hasFakes: Any = ...
    @property
    def refObjLoader(self): ...
    def setDefaults(self) -> None: ...
    def validate(self) -> None: ...

class MeasureMergedCoaddSourcesRunner(ButlerInitializedTaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...

class MeasureMergedCoaddSourcesTask(PipelineTask, CmdLineTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    getSchemaCatalogs: Any = ...
    makeIdFactory: Any = ...
    deblended: Any = ...
    inputCatalog: Any = ...
    schemaMapper: Any = ...
    schema: Any = ...
    algMetadata: Any = ...
    outputSchema: Any = ...
    def __init__(self, butler: Optional[Any] = ..., schema: Optional[Any] = ..., peakSchema: Optional[Any] = ..., refObjLoader: Optional[Any] = ..., initInputs: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def runQuantum(self, butlerQC: Any, inputRefs: Any, outputRefs: Any) -> None: ...
    def runDataRef(self, patchRef: Any, psfCache: int = ...) -> None: ...
    def run(self, exposure: Any, sources: Any, skyInfo: Any, exposureId: Any, ccdInputs: Optional[Any] = ..., visitCatalogs: Optional[Any] = ..., wcsUpdates: Optional[Any] = ..., butler: Optional[Any] = ...): ...
    def readSources(self, dataRef: Any): ...
    def writeMatches(self, dataRef: Any, results: Any) -> None: ...
    def write(self, dataRef: Any, sources: Any) -> None: ...
    def getExposureId(self, dataRef: Any): ...
