from lsst.afw.image import ExposureF as ExposureF
from lsst.pipe.base import PipelineTask as PipelineTask, PipelineTaskConfig as PipelineTaskConfig, PipelineTaskConnections as PipelineTaskConnections, Struct as Struct
from typing import Any

class RawToCalexpTaskConnections(PipelineTaskConnections):
    input: Any = ...
    output: Any = ...

class RawToCalexpTaskConfig(PipelineTaskConfig): ...

class RawToCalexpTask(PipelineTask):
    ConfigClass: Any = ...
    def run(self, input: Any): ...
