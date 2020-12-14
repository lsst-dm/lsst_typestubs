from lsst.ctrl.orca.EnvString import EnvString as EnvString
from lsst.ctrl.orca.PegasusWorkflowLauncher import PegasusWorkflowLauncher as PegasusWorkflowLauncher
from lsst.ctrl.orca.TemplateWriter import TemplateWriter as TemplateWriter
from lsst.ctrl.orca.WorkflowConfigurator import WorkflowConfigurator as WorkflowConfigurator
from typing import Any

class PegasusWorkflowConfigurator(WorkflowConfigurator):
    runid: Any = ...
    repository: Any = ...
    prodConfig: Any = ...
    wfConfig: Any = ...
    wfName: Any = ...
    wfVerbosity: Any = ...
    dirs: Any = ...
    directories: Any = ...
    nodes: Any = ...
    numNodes: Any = ...
    logFileNames: Any = ...
    pipelineNames: Any = ...
    directoryList: Any = ...
    initialWorkDir: Any = ...
    firstRemoteWorkDir: Any = ...
    defaultRoot: Any = ...
    def __init__(self, runid: Any, repository: Any, prodConfig: Any, wfConfig: Any, wfName: Any) -> None: ...
    def configure(self, provSetup: Any, wfVerbosity: Any): ...
    def writeSitesXML(self, outputFile: Any, template: Any, keywords: Any) -> None: ...
    def getWorkflowName(self): ...
    def deploySetup(self, provSetup: Any, wfConfig: Any, platformConfig: Any, pipelineConfigGroup: Any) -> None: ...
    def createDirs(self, localStagingDir: Any, platformDirConfig: Any) -> None: ...
    def setupDatabase(self) -> None: ...
