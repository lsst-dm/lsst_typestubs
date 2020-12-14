import lsst.pex.config
from .chebyshevBoundedField import ChebyshevBoundedField as ChebyshevBoundedField, ChebyshevBoundedFieldControl as ChebyshevBoundedFieldControl

class ChebyshevBoundedFieldConfig(lsst.pex.config.Config):
    def computeSize(self): ...
