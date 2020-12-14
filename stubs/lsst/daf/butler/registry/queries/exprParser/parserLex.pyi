from typing import Any

class ParserLexError(Exception):
    expression: Any = ...
    remain: Any = ...
    pos: Any = ...
    lineno: Any = ...
    def __init__(self, expression: Any, remain: Any, pos: Any, lineno: Any) -> None: ...

class ParserLex:
    @classmethod
    def make_lexer(cls, reflags: int = ..., **kwargs: Any): ...
    reserved: Any = ...
    tokens: Any = ...
    t_LPAREN: str = ...
    t_RPAREN: str = ...
    t_EQ: str = ...
    t_NE: str = ...
    t_LT: str = ...
    t_LE: str = ...
    t_GT: str = ...
    t_GE: str = ...
    t_ADD: str = ...
    t_SUB: str = ...
    t_MUL: str = ...
    t_DIV: str = ...
    t_MOD: str = ...
    t_COMMA: str = ...
    t_ignore: str = ...
    def t_newline(self, t: Any) -> None: ...
    def t_TIME_LITERAL(self, t: Any): ...
    def t_STRING_LITERAL(self, t: Any): ...
    def t_RANGE_LITERAL(self, t: Any): ...
    def t_NUMERIC_LITERAL(self, t: Any): ...
    def t_QUALIFIED_IDENTIFIER(self, t: Any): ...
    def t_SIMPLE_IDENTIFIER(self, t: Any): ...
    def t_error(self, t: Any) -> None: ...
