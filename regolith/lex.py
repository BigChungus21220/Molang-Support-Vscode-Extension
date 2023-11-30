import ply.lex as lex
import re

def getMolangString(file):
    content = open(file).read()
    define_name = re.findall("molang/[a-zA-Z1-9_\-/]+\.molang",file)[0]
    define_name = "_" + re.sub("[/\.]","_",define_name).upper()
    return "#ifndef " + define_name + "\n#define " + define_name + "\n" + content + "\n#endif"

tokens = (
   'COMMENT',
   'STRING',
   'NUMBER',
   'OPERATOR',
   'SEPARATOR',
   'KEYWORD',
   'IDENTIFIER',
   'MACRO'
)

t_COMMENT = r'/[*][^*]*[*]+([^/*][^*]*[*]+)*/|//[^\n]*'
t_STRING = r'[\"\'].*[\"\']'
t_OPERATOR = r'\:|\?|=|-=|/=|\*=|\+=|\+|-|/|\*|>|<|>=|<=|==|!=|!'
t_SEPARATOR  = r'\(|\{|\[|\]|\}|\)|;|,'
t_NUMBER = r'[1-9]\d*(\.\d+)?'
t_IDENTIFIER = r'[a-z]+[0-9_\-]*'
t_MACRO = r'\#[a-z]+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = '[ \t]'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test it out
data = file = getMolangString("./regolith/molang/myscript.molang")

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)