from enum import Enum


class TokenTypes(Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    MODULO = "MODULO"
    POWER = "POWER"
    EQ = "EQ"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LCURLY = "LCURLY"
    RCURLY = "RCURLY"
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    VERSION = "VERSION"
    NEWLINE = "NEWLINE"
    SEMICOLON = "SEMICOLON"
    EOF = "EOF"


class KeywordTypes(Enum):
    VAR = "var"
    IF = "IF"
    ELSE = "ELSE"
    DO = "DO"
    WHILE = "WHILE"
    FOR = "FOR"

    @classmethod
    def check_variable(cls, string):
        variables = [member.value for member in cls]
        return string in variables


class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"

        return f"{self.type}"
