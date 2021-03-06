import lsst.afw.cameraGeom.utils as pipeBase
from typing import Any

class VisualizeBinExpConnections(pipeBase.PipelineTaskConnections):
    inputExp: Any = ...
    camera: Any = ...
    outputExp: Any = ...

class VisualizeBinExpConfig(pipeBase.PipelineTaskConfig):
    binning: Any = ...
    detectorKeyword: Any = ...

class VisualizeBinExpTask(pipeBase.PipelineTask, pipeBase.CmdLineTask):
    ConfigClass: Any = ...
    def run(self, inputExp: Any, camera: Any): ...

class VisualizeMosaicExpConnections(pipeBase.PipelineTaskConnections):
    inputExps: Any = ...
    camera: Any = ...
    outputData: Any = ...

class VisualizeMosaicExpConfig(pipeBase.PipelineTaskConfig):
    binning: Any = ...

class VisualizeMosaicExpTask(pipeBase.PipelineTask, pipeBase.CmdLineTask):
    ConfigClass: Any = ...
    def makeCameraImage(self, inputExps: Any, camera: Any, binning: Any): ...
    def run(self, inputExps: Any, camera: Any): ...

class ImageSource:
    exposures: Any = ...
    isTrimmed: bool = ...
    background: Any = ...
    def __init__(self, exposures: Any) -> None: ...
    def getCcdImage(self, detector: Any, imageFactory: Any, binSize: Any): ...
