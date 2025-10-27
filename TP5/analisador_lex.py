import ply.lex as lex

# Lexer (mesmo do original)
tokens = (
    'INT','P_OP','P_CLS',
    'SUM','DIF','MUL','DIV'
)

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_P_OP= r'\('
t_P_CLS = r'\)'
t_SUM = r'\+'
t_DIF = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
