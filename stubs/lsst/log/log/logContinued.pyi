import logging
from .log import Log as Log
from typing import Any

TRACE: int
DEBUG: int
INFO: int
WARN: int
ERROR: int
FATAL: int

class Log:
    UsePythonLogging: bool = ...
    @classmethod
    def usePythonLogging(cls) -> None: ...
    @classmethod
    def doNotUsePythonLogging(cls) -> None: ...
    def trace(self, fmt: Any, *args: Any) -> None: ...
    def debug(self, fmt: Any, *args: Any) -> None: ...
    def info(self, fmt: Any, *args: Any) -> None: ...
    def warn(self, fmt: Any, *args: Any) -> None: ...
    def warning(self, fmt: Any, *args: Any) -> None: ...
    def error(self, fmt: Any, *args: Any) -> None: ...
    def fatal(self, fmt: Any, *args: Any) -> None: ...
    def tracef(self, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
    def debugf(self, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
    def infof(self, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
    def warnf(self, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
    def errorf(self, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
    def fatalf(self, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
    def __reduce__(self): ...

def configure(*args: Any) -> None: ...
def configure_prop(properties: Any) -> None: ...
def getDefaultLogger(): ...
def getLogger(loggername: Any): ...
def MDC(key: Any, value: Any) -> None: ...
def MDCRemove(key: Any) -> None: ...
def MDCRegisterInit(func: Any) -> None: ...
def setLevel(loggername: Any, level: Any) -> None: ...
def getLevel(loggername: Any) -> None: ...
def isEnabledFor(logger: Any, level: Any) -> None: ...
def log(loggername: Any, level: Any, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def trace(fmt: Any, *args: Any) -> None: ...
def debug(fmt: Any, *args: Any) -> None: ...
def info(fmt: Any, *args: Any) -> None: ...
def warn(fmt: Any, *args: Any) -> None: ...
def warning(fmt: Any, *args: Any) -> None: ...
def error(fmt: Any, *args: Any) -> None: ...
def fatal(fmt: Any, *args: Any) -> None: ...
def logf(loggername: Any, level: Any, fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def tracef(fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def debugf(fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def infof(fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def warnf(fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def errorf(fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def fatalf(fmt: Any, *args: Any, **kwargs: Any) -> None: ...
def lwpID(): ...
def usePythonLogging() -> None: ...
def doNotUsePythonLogging() -> None: ...

class UsePythonLogging:
    current: Any = ...
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...

class LevelTranslator:
    @staticmethod
    def lsstLog2logging(level: Any): ...
    @staticmethod
    def logging2lsstLog(level: Any): ...

class LogHandler(logging.Handler):
    formatter: Any = ...
    def __init__(self, level: Any = ...) -> None: ...
    def handle(self, record: Any) -> None: ...
    def emit(self, record: Any) -> None: ...
