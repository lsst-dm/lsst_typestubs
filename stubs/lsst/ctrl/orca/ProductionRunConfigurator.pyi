from lsst.ctrl.orca.NamedClassFactory import NamedClassFactory as NamedClassFactory
from lsst.ctrl.orca.WorkflowManager import WorkflowManager as WorkflowManager
from lsst.ctrl.orca.config.ProductionConfig import ProductionConfig as ProductionConfig
from lsst.ctrl.orca.exceptions import MultiIssueConfigurationError as MultiIssueConfigurationError
from typing import Any, Optional

class ProductionRunConfigurator:
    runid: Any = ...
    prodConfig: Any = ...
    repository: Any = ...
    workflowVerbosity: Any = ...
    provenanceDict: Any = ...
    configOverrides: Any = ...
    def __init__(self, runid: Any, configFile: Any, repository: Optional[Any] = ..., workflowVerbosity: Optional[Any] = ...) -> None: ...
    def createWorkflowManager(self, prodConfig: Any, wfName: Any, wfConfig: Any): ...
    def getProvenanceSetup(self): ...
    def configure(self, workflowVerbosity: Any): ...
    def checkConfiguration(self, care: int = ..., issueExc: Optional[Any] = ...) -> None: ...
    def createDatabaseConfigurator(self, databaseConfig: Any): ...
    def getWorkflowNames(self): ...
