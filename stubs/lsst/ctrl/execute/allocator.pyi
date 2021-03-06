from lsst.ctrl.execute import envString as envString
from lsst.ctrl.execute.allocationConfig import AllocationConfig as AllocationConfig
from lsst.ctrl.execute.condorInfoConfig import CondorInfoConfig as CondorInfoConfig
from lsst.ctrl.execute.seqFile import SeqFile as SeqFile
from lsst.ctrl.execute.templateWriter import TemplateWriter as TemplateWriter
from typing import Any

class Allocator:
    opts: Any = ...
    defaults: Any = ...
    configuration: Any = ...
    platform: Any = ...
    commandLineDefaults: Any = ...
    def __init__(self, platform: Any, opts: Any, configuration: Any, condorInfoFileName: Any) -> None: ...
    def createNodeSetName(self): ...
    def createUniqueIdentifier(self): ...
    def load(self) -> None: ...
    uniqueIdentifier: Any = ...
    configDir: Any = ...
    submitFileName: Any = ...
    condorConfigFileName: Any = ...
    def loadAllocationConfig(self, name: Any, suffix: Any): ...
    def createSubmitFile(self, inputFile: Any): ...
    def createCondorConfigFile(self, input: Any): ...
    def createFile(self, input: Any, output: Any): ...
    def isVerbose(self): ...
    def getUserName(self): ...
    def getUserHome(self): ...
    def getHostName(self): ...
    def getUtilityPath(self): ...
    def getScratchDirectory(self): ...
    def getLocalScratchDirectory(self): ...
    def getNodeSetName(self): ...
    def getNodes(self): ...
    def getCPUs(self): ...
    def getWallClock(self): ...
    def getScheduler(self): ...
    def getReservation(self): ...
    def getParameter(self, value: Any): ...
    def printNodeSetInfo(self) -> None: ...
    def runCommand(self, cmd: Any, verbose: Any): ...
