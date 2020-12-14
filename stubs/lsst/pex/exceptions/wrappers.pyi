import builtins
from typing import Any

def register(cls): ...

class ExceptionMeta(type):
    def __getattr__(cls, name: Any): ...

class Exception(builtins.Exception, metaclass=ExceptionMeta):
    __module__: str = ...
    WrappedClass: Any = ...
    cpp: Any = ...
    def __init__(self, arg: Any, *args: Any, **kwds: Any) -> None: ...
    def __getattr__(self, name: Any): ...

class LogicError(Exception):
    WrappedClass: Any = ...

class DomainError(LogicError):
    WrappedClass: Any = ...

class InvalidParameterError(LogicError):
    WrappedClass: Any = ...

class LengthError(LogicError):
    WrappedClass: Any = ...

class OutOfRangeError(LogicError):
    WrappedClass: Any = ...

class RuntimeError(Exception, builtins.RuntimeError):
    WrappedClass: Any = ...

class RangeError(RuntimeError):
    WrappedClass: Any = ...

class OverflowError(RuntimeError, builtins.OverflowError):
    WrappedClass: Any = ...

class UnderflowError(RuntimeError, builtins.ArithmeticError):
    WrappedClass: Any = ...

class NotFoundError(Exception, builtins.LookupError):
    WrappedClass: Any = ...

class IoError(RuntimeError, builtins.IOError):
    WrappedClass: Any = ...

class TypeError(LogicError, builtins.TypeError):
    WrappedClass: Any = ...

def translate(cpp: Any): ...
def declare(module: Any, exception_name: Any, base: Any, wrapped_class: Any) -> None: ...