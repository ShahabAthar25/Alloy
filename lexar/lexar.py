import string
from typing import List, Optional, Tuple, Union

from lexar.token_type import KeywordTypes, Token, TokenTypes

DIGITS = "0123456789"
LETTERS = string.ascii_letters


class Lexar:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos: int = -1
        self.current_char: str | None = None

        self.advance()

    def advance(self) -> None:
        self.pos += 1
        self.current_char = self.text[self.pos] if len(self.text) > self.pos else None

    def make_tokens(self):
        tokens: List[Token] = []

        while self.current_char != None:
            if self.current_char in " \t":  # Ignore whitespace
                pass
            elif self.current_char == "+":
                tokens.append(Token(TokenTypes.PLUS))

            elif self.current_char == "-":
                tokens.append(Token(TokenTypes.MINUS))

            elif self.current_char == "*":
                tokens.append(Token(TokenTypes.MULTIPLY))

            elif self.current_char == "/":
                tokens.append(Token(TokenTypes.DIVIDE))

            elif self.current_char == "%":
                tokens.append(Token(TokenTypes.MODULO))

            elif self.current_char == "^":
                tokens.append(Token(TokenTypes.POWER))

            elif self.current_char == "=":
                tokens.append(Token(TokenTypes.EQ))

            elif self.current_char == "(":
                tokens.append(Token(TokenTypes.LPAREN))

            elif self.current_char == ")":
                tokens.append(Token(TokenTypes.RPAREN))

            elif self.current_char == "{":
                tokens.append(Token(TokenTypes.LCURLY))

            elif self.current_char == "}":
                tokens.append(Token(TokenTypes.RCURLY))

            elif self.current_char in DIGITS:
                token, error = self.make_number_version()
                if error:
                    return [], error

                tokens.append(token)

            elif self.current_char in LETTERS:
                token = self.make_identifier()
                tokens.append(token)

            else:
                char = self.current_char
                return [], Exception(f"Illegal character '{char}'")

            self.advance()

        tokens.append(Token(TokenTypes.EOF))
        return tokens, None

    def make_number_version(self) -> Union[Tuple[Token, None], Tuple[None, str]]:
        num_str = ""
        dot_count = 0

        while (
            self.current_char != None and self.current_char in DIGITS + "._"
        ):  # "." for floats, "_" for readability
            if self.current_char == ".":
                if dot_count == 2:
                    break
                dot_count += 1
                num_str += "."
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TokenTypes.INT, int(num_str)), None

        elif dot_count == 1:
            return Token(TokenTypes.FLOAT, float(num_str)), None

        elif dot_count == 2:
            return Token(TokenTypes.VERSION, str(num_str)), None

        else:
            return None, "Too many dots '.'"

    def make_identifier(self) -> Token:
        id_str = ""

        while self.current_char != None and self.current_char in LETTERS + DIGITS + "_":
            id_str += self.current_char
            self.advance()

        if KeywordTypes.check_variable(id_str):
            return Token(TokenTypes.KEYWORD, KeywordTypes[id_str])
        else:
            return Token(TokenTypes.IDENTIFIER, id_str)
