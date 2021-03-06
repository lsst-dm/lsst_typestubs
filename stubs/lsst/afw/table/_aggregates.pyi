from lsst.utils import TemplateMeta
from typing import Any

class PointKey(metaclass=TemplateMeta):
    TEMPLATE_PARAMS: Any = ...
    TEMPLATE_DEFAULTS: Any = ...

class CovarianceMatrixKey(metaclass=TemplateMeta):
    TEMPLATE_PARAMS: Any = ...
