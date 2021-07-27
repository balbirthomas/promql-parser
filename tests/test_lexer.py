import unittest
from promparser import PromQLLexer


class TestCommon(unittest.TestCase):

    def setUp(self):
        self.lexer = PromQLLexer()

    def tokens(self, input):
        return list(self.lexer.tokenize(input))

    def test_comma(self):
        tokens = self.tokens(",")
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, "COMMA")

    def test_empty_parenthesis(self):
        tokens = self.tokens("()")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].type, "LEFT_PAREN")
        self.assertEqual(tokens[1].type, "RIGHT_PAREN")

    def test_empty_braces(self):
        tokens = self.tokens("{}")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].type, "LEFT_BRACE")
        self.assertEqual(tokens[1].type, "RIGHT_BRACE")

    def test_duration(self):
        tokens = self.tokens("[5m]")
        for tok in tokens:
            print(tok.type, tok.value)


if __name__ == '__main__':
    unittest.main()
