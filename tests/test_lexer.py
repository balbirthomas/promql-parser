import unittest
from promparser import Lexer


def token_type(token):
    return token[0]


def token_value(token):
    return token[1]


class TestCommon(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.lexer.build()

    def tokens(self, data):
        tokens = []
        for tok in self.lexer.get_tokens(data):
            tokens.append((tok.type, tok.value))
        return tokens

    def test_comma(self):
        tokens = self.tokens(",")
        self.assertEqual(len(tokens), 1)
        self.assertEqual(token_type(tokens[0]), "COMMA")

    def test_empty_parenthesis(self):
        tokens = self.tokens("()")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(token_type(tokens[0]), "LEFT_PAREN")
        self.assertEqual(token_type(tokens[1]), "RIGHT_PAREN")

    def test_empty_braces(self):
        tokens = self.tokens("{}")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(token_type(tokens[0]), "LEFT_BRACE")
        self.assertEqual(token_type(tokens[1]), "RIGHT_BRACE")

    def test_duration(self):
        tokens = self.tokens("[5m]")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(token_type(tokens[0]), "LEFT_BRACKET")
        self.assertEqual(token_type(tokens[1]), "DURATION")
        self.assertEqual(token_value(tokens[1]), "5m")
        self.assertEqual(token_type(tokens[2]), "RIGHT_BRACKET")

    def test_duration_with_spaces(self):
        tokens = self.tokens("[ 5m ]")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(token_type(tokens[0]), "LEFT_BRACKET")
        self.assertEqual(token_type(tokens[1]), "DURATION")
        self.assertEqual(token_value(tokens[1]), "5m")
        self.assertEqual(token_type(tokens[2]), "RIGHT_BRACKET")

if __name__ == '__main__':
    unittest.main()
