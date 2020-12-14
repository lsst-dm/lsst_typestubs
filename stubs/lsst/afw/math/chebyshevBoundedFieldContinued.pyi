from .chebyshevBoundedField import ChebyshevBoundedField as ChebyshevBoundedField, ChebyshevBoundedFieldControl as ChebyshevBoundedFieldControl
from lsst.utils import continueClass as continueClass
from typing import Any

class ChebyshevBoundedField:
    @classmethod
    def approximate(cls, boundedField: Any, orderX: int = ..., orderY: int = ..., nStepX: int = ..., nStepY: int = ...): ...
