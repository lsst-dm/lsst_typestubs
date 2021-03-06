from typing import Any, Optional

class ConfigurationError(RuntimeError): ...

class MultiIssueConfigurationError(ConfigurationError):
    def __init__(self, msg: Optional[Any] = ..., problem: Optional[Any] = ...) -> None: ...
    def addProblem(self, msg: Any) -> None: ...
    def hasProblems(self): ...
    def getProblems(self): ...
