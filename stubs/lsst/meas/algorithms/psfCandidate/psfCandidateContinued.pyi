from .psfCandidate import PsfCandidateF as PsfCandidateF
from lsst.utils import continueClass as continueClass
from typing import Any

class PsfCandidateF:
    getCandidateRating: Any = ...
    def setCandidateRating(self, rating: Any) -> None: ...
