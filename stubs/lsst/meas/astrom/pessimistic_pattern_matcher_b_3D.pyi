from typing import Any, Optional

class PessimisticPatternMatcherB:
    log: Any = ...
    def __init__(self, reference_array: Any, log: Any) -> None: ...
    def match(self, source_array: Any, n_check: Any, n_match: Any, n_agree: Any, max_n_patterns: Any, max_shift: Any, max_rotation: Any, max_dist: Any, min_matches: Any, pattern_skip_array: Optional[Any] = ...): ...
