import ply.lex as lex
#RESERVED WORDS
reserved = {
    'var':'VAR',
    'let':'LET',
    'new':'NEW',
    'if':'IF',
    'else if':'ELIF',
    'else':'ELSE',
    'while':'WHILE',
    'for':'FOR',
    '||':'OR',
    '&&':'AND',
    '!':'NOT'

}
# TOKENS
tokens = ["MINUS","PLUS","TIMES","DIVIDE","MOD","LPAREN","RPAREN","ID",
          "LBRACKET","RBRACKET","EQUALS","NOTEQUALS","MORETHAN","LESSTHAN","MORETHANEQUALS","LESSTHANEQUALS","STRICTEQUALS",
          "STRICTNOTEQUALS"] + list(reserved.values())

#REGEX OF TOKENS
t_MINUS = r'-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
# t_NUMBER = r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALS = r'=='
# t_NOTEQUALS
t_MORETHAN = r'>'
t_LESSTHAN = r'<'
t_MORETHANEQUALS = r'>='
t_LESSTHANEQUALS = r'<='
t_STRICTEQUALS = r'==='
t_STRICTNOTEQUALS = r'!=='
t_IF = r'if'
t_FOR = r'for'
t_WHILE = r'while'
t_ELIF = r'elif'
t_ELSE = r'else'
t_VAR = r'var'
t_LET = r'let'
t_NEW = r'new'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_NOT = r'!'

t_ignore = ' \t'

def t_error(t):
    print("No se ha reconocido {}".format(t.value[0]))
    t.lexer.skip(1)

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t