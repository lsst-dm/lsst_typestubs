from .fits import FitsTranslator

class SubaruTranslator(FitsTranslator):
    def to_location(self): ...
    def to_observation_counter(self): ...