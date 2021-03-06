from typing import Any, Optional

class TestObject:
    data: Any = ...
    def __init__(self, data: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class TestObjectPair:
    objA: Any = ...
    objB: Any = ...
    usedInitSetter: Any = ...
    usedASetter: bool = ...
    usedBSetter: bool = ...
    def __init__(self, objA: Optional[Any] = ..., objB: Optional[Any] = ...) -> None: ...
    @staticmethod
    def assembler(dataId: Any, componentInfo: Any, cls: Any): ...
    @staticmethod
    def disassembler(obj: Any, dataId: Any, componentInfo: Any) -> None: ...
    def set_a(self, obj: Any) -> None: ...
    def set_b(self, obj: Any) -> None: ...
    def get_a(self): ...
    def get_b(self): ...

class TestObjectCamelCaseSetter:
    def __init__(self) -> None: ...
    def setFoo(self, val: Any) -> None: ...
    def getFoo(self): ...

class TestObjectUnderscoreSetter:
    def __init__(self) -> None: ...
    def set_foo(self, val: Any) -> None: ...
    def get_foo(self): ...
