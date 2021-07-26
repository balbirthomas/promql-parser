from sly import Parser
from lexer import PromQLLexer


class PromQLParser(Parser):
    tokens = PromQLLexer.tokens

    def __init__(self):
        self.names = {}


if __name__ == '__main__':
    lexer = PromQLLexer()
    parser = PromQLParser()
    while True:
        try:
            text = input('promql > ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))
