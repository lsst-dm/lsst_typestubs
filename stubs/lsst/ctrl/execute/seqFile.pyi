from lsst.ctrl.execute import envString as envString
from typing import Any

class SeqFile:
    fileName: Any = ...
    def __init__(self, seqFileName: Any) -> None: ...
    def nextSeq(self): ...
    def readSeq(self): ...
    def writeSeq(self, seq: Any) -> None: ...