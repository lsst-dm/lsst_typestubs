from typing import Any

class Pupil:
    illuminated: Any = ...
    size: Any = ...
    scale: Any = ...
    def __init__(self, illuminated: Any, size: Any, scale: Any) -> None: ...

class PupilFactory:
    visitInfo: Any = ...
    pupilSize: Any = ...
    npix: Any = ...
    pupilScale: Any = ...
    def __init__(self, visitInfo: Any, pupilSize: Any, npix: Any) -> None: ...
    def getPupil(self, point: Any) -> None: ...
