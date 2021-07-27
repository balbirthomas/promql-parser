from ply.lex import TOKEN
import ply.lex as lex


class Lexer():

    # string of characters to ignore between tokens
    t_ignore = " \t"

    precedence = (
        ('nonassoc', "LSS", "GTR", "LTE", "GTE", "EQL", "EQLC", "NEQ",
         "EQL_REGEX", "NEQ_REGEX"),
        ('left', "ADD", "SUB"),
        ('left', "MUL", "DIV"),
        ('right', "UMINUS"),            # Unary minus operator
    )

    # reserved keywords
    reserved = {
        "and": "LAND",
        "or": "LOR",
        "unless": "LUNLESS",
        "sum": "SUM",
        "avg": "AVG",
        "count": "COUNT",
        "min": "MIN",
        "max": "MAX",
        "group": "GROUP",
        "stddev": "STDDEV",
        "stdvar": "STDVAR",
        "topk": "TOPK",
        "bottomk": "BOTTOMK",
        "count_values": "COUNT_VALUES",
        "quantile": "QUANTILE",
        "offset": "OFFSET",
        "by": "BY",
        "without": "WITHOUT",
        "on": "ON",
        "ignoring": "IGNORING",
        "group_left": "GROUP_LEFT",
        "group_right": "GROUP_RIGHT",
        "bool": "BOOL",
        "start": "START",
        "end": "END",
    }

    # set of token names
    tokens = [
        "NUMBER",
        "IDENTIFIER",
        "LEFT_PAREN",
        "RIGHT_PAREN",
        "LEFT_BRACE",
        "RIGHT_BRACE",
        "LEFT_BRACKET",
        "RIGHT_BRACKET",
        "COMMA",
        "COLON",
        "SEMICOLON",
        "BLANK",
        "EQL",
        "SUB",
        "ADD",
        "MUL",
        "MOD",
        "DIV",
        "EQLC",
        "NEQ",
        "LTE",
        "LSS",
        "GTE",
        "GTR",
        "EQL_REGEX",
        "NEQ_REGEX",
        "POW",
    ] + list(reserved.values())

    # regular expression rules for tokens
    # TODO: SPACE TIMES
    t_LEFT_PAREN = r"\("
    t_RIGHT_PAREN = r"\)"
    t_LEFT_BRACE = r"{"
    t_RIGHT_BRACE = r"}"
    t_LEFT_BRACKET = r"\["
    t_RIGHT_BRACKET = r"\]"
    t_COMMA = r","
    t_COLON = r":"
    t_SEMICOLON = r";"
    t_BLANK = r"_"
    t_EQL = r"="
    t_SUB = r"-"
    t_ADD = r"\+"
    t_MUL = r"\*"
    t_MOD = r"%"
    t_DIV = r"\/"
    t_EQLC = r"=="
    t_NEQ = r"!="
    t_LTE = r"<="
    t_LSS = r"<"
    t_GTE = r">="
    t_GTR = r">"
    t_EQL_REGEX = r"=~"
    t_NEQ_REGEX = r"!~"
    t_POW = r"\^"

    decnum = r"[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?"
    hexnum = r"0[xX][0-9a-fA-F]+"
    infnum = r"[iI][nN][fF]"
    nannum = r"[nN][aA][nN]"
    number = decnum + r"|" + hexnum + r"|" + infnum + r"|" + nannum

    @TOKEN(number)
    def t_NUMBER(self, t):
        # TODO signed hex, inf, (nan ?)
        if t.value.startswith('0x') or t.value.startswith('0X'):
            # TODO greedy hex
            t.value = int(t.value[2:], 16)
        else:
            t.value = float(t.value)
        return t

    def t_IDENTIFIER(self, t):
        r"[a-zA-Z_]+[a-zA-Z0-9_]*"
        t.type = self.reserved.get(t.value, "IDENTIFIER")
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        return t

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def get_tokens(self, data):
        self.lexer.input(data)
        for tok in self.lexer:
            yield tok


if __name__ == '__main__':
    lex.runmain()
