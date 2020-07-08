import ply.lex as lex
#RESERVED WORDS
reserved = {
    'var':'VAR',  'let':'LET',
    'new':'NEW',
    'if':'IF', 'else if':'ELIF', 'else':'ELSE', 'while':'WHILE', 'for':'FOR',
    '||':'OR', '&&':'AND', '!':'NOT'  ,
    'true':'TRUE', 'false':'FALSE', 'null':'NULL',
    'function' : 'FUNCTION'

}

#RESERVED FUNCTION NAMES
function = {
    'toUpperCase':'TOUPPERCASE',
    'toLowerCase': 'TOLOWERCASE',
    'startsWith': 'STARTSWITH',
    'pop':'POP',
    'push':'PUSH',
    'shift':'SHIFT'
}

literals = ['{', '}']

# TOKENS
tokens = ["MINUS","PLUS","TIMES","DIVIDE","MOD","LPAREN","RPAREN","ID", "EQUAL",
          "LBRACKET","RBRACKET","EQUALS","NOTEQUALS","MORETHAN","LESSTHAN",
          "MORETHANEQUALS","LESSTHANEQUALS","STRICTEQUALS","STRICTNOTEQUALS",
          "SEMICOLON", "POINT" ,
          "NUMBER", "STRING"] + list(reserved.values()) + list(function.values())

#REGEX OF TOKENS
t_MINUS = r'-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_NUMBER = r'-?[0-9]+(\.\d+)?'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUAL = r'\='
t_EQUALS = r'=='
t_NOTEQUALS = r'\!\='
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
t_SEMICOLON = r';'
t_POINT = r'\.'
t_STRING= r'[\'\"].*[\'\"]'

t_ignore = ' \t'


def t_lbrace(t):
    r'\{'
    t.type = '{'
    return t

def t_rbrace(t):
    r'\}'
    t.type = '}'
    return t

def t_error(t):
    print("No se ha reconocido {}".format(t.value[0]))
    t.lexer.skip(1)

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_\$][a-zA-Z_0-9\$]*'
    if reserved.get(t.value)!=None:
        t.type = reserved.get(t.value)
    elif function.get(t.value)!=None:
        t.type = function.get(t.value)
    else:
        t.type= 'ID'  # Check for reserved words
    return t


def printLex(cadena):
    analizador=lex.lex()
    analizador.input(cadena)
    for tok in analizador:
        print(tok)


def t_COMMENT(t):
     r'(\/\/.*)|(\/\*.*\*\/)'
     pass


################## PRIMER EJEMPLO ###########
print("PRIMER EJEMPLO\n")
cadena= "let  example = \"hello\";"
cadena2= "a.toLowerCase()"
cadena3 = "function hola(){hola=5}"
print(cadena)
printLex(cadena)
print("\n",cadena2)
printLex(cadena2)
print("\n",cadena3)
printLex(cadena3)
