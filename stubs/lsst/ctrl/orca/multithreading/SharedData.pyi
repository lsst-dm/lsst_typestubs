from typing import Any, Optional

class SharedData:
    acquire: Any = ...
    release: Any = ...
    notify: Any = ...
    notifyAll: Any = ...
    wait: Any = ...
    def __init__(self, needLockOnRead: bool = ..., data: Optional[Any] = ..., cond: Optional[Any] = ...) -> None: ...
    def __enter__(self, *args: Any, **kwds: Any): ...
    def __exit__(self, *args: Any, **kwds: Any): ...
    def __getattribute__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any) -> None: ...
    def initData(self, data: Any) -> None: ...
    def dir(self): ...
