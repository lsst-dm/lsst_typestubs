from .camera import Camera as Camera
from lsst.utils import continueClass as continueClass, doImport as doImport
from typing import Any

class Camera:
    def getPupilFactory(self, visitInfo: Any, pupilSize: Any, npix: Any, **kwargs: Any): ...
    @property
    def telescopeDiameter(self): ...
