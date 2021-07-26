from sly import Lexer


class PromQLLexer(Lexer):

    # set of token names
    tokens = {
        NUMBER,
        IDENTIFIER,
        EQLC,
        NEQ,
        LTE,
        GTE,
        EQL_REGEX,
        NEQ_REGEX,
        LAND,
        LOR,
        LUNLESS,
        SUM,
        AVG,
        COUNT,
        MIN,
        MAX,
        GROUP,
        STDDEV,
        STDVAR,
        TOPK,
        BOTTOMK,
        COUNT_VALUES,
        QUANTILE,
        OFFSET,
        BY,
        WITHOUT,
        ON,
        IGNORING,
        GROUP_LEFT,
        GROUP_RIGHT,
        BOOL,
        START,
        END,
    }

    # string of characters to ignore between tokens
    ignore = r"\s"

    # TODO: BLANK SPACE TIMES
    literals = {",", ":", ";", "-", "+", "*", "%",
                "/", "<", ">", "=", "^", "(", ")",
                "{", "}", "[", "]"}

    # regular expression rules for tokens
    # TODO: use token remapping for keywords
    EQLC = r"=="
    NEQ = r"!="
    LTE = r"<="
    GTE = r">="
    EQL_REGEX = r"=~"
    NEQ_REGEX = r"!~"
    LAND = r"and"
    LOR = r"or"
    LUNLESS = r"unless"
    SUM = r"sum"
    AVG = r"avg"
    COUNT = r"count"
    MIN = r"min"
    MAX = r"max"
    GROUP = r"group"
    STDDEV = r"stddev"
    STDVAR = r"stdvar"
    TOPK = r"topk"
    BOTTOMK = r"bottomk"
    COUNT_VALUES = r"count_values"
    QUANTILE = r"quantile"
    OFFSET = r"offset"
    BY = r"by"
    WITHOUT = r"without"
    ON = r"on"
    IGNORING = r"ignoring"
    GROUP_LEFT = r"group_left"
    GROUP_RIGHT = r"group_right"
    BOOL = r"bool"
    START = r"start"
    END = r"end"

    @_(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?",
       r"0[xX][0-9a-fA-F]+",
       r"[nN][aA][nN]",
       r"[iI][nN][fF]")
    def NUMBER(self, t):
        # TODO signed hex, inf, (nan ?)
        if t.value.startswith('0x') or t.value.startswith('0X'):
            # TODO greedy hex
            t.value = int(t.value[2:], 16)
        else:
            t.value = float(t.value)
        return t

    @_(r"[a-zA-Z_]+[a-zA-Z0-9_]*")
    def IDENTIFIER(self, t):
        t.value = str(t.value)
        return t

    def error(self, t):
        self.index += 1
        return t


if __name__ == '__main__':
    def lex(expr):
        lexer = PromQLLexer()
        for tok in lexer.tokenize(expr):
            print('type=%r, value=%r' % (tok.type, tok.value))

    expr = '-1.67e-7'
    lex(expr)
