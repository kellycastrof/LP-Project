import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens


def p_sentencias(p):
    '''sentencias : statement
    | if'''

def p_statements(p):
    'statement : stm'

def p_stm_asignacion(p):
    'stm : asignacion'
def p_stm_expression(p):
    'stm : expresion'
def p_stm_metodos(p):
    'stm : metodos'

def p_metodos(p):
    '''metodos : imprimir
    | touppercase
    | tolowercase
    | startwith
    | tostring'''

def p_imprimir(p):
    'imprimir : PRINT LPAREN factor RPAREN'

def p_to_upper_case(p):
    '''touppercase : ID TOUPPERCASE LPAREN RPAREN
    | asignacion TOUPPERCASE LPAREN RPAREN '''


def p_to_lower_case(p):
    '''tolowercase : ID TOLOWERCASE LPAREN RPAREN
    | asignacion TOLOWERCASE LPAREN RPAREN'''

def p_start_with(p):
    '''startwith : ID STARTSWITH LPAREN STRING RPAREN
    | asignacion STARTSWITH LPAREN RPAREN '''

def p_to_string(p):
    '''tostring : ID TOSTRING LPAREN RPAREN
        | asignacion TOSTRING LPAREN RPAREN '''

def p_if(p):
    '''if : IF LPAREN condicion RPAREN LBRACE sentencias RBRACE
    | IF LPAREN condicion RPAREN LBRACE sentencias RBRACE else
    | IF LPAREN condicion RPAREN LBRACE sentencias RBRACE elseif'''

def p_condicion(p):
    '''condicion : TRUE
    | FALSE
    | NOT expresion
    | expresion EQUALS expresion
    | expresion NOTEQUALS expresion
    | expresion STRICTEQUALS expresion
    | expresion MORETHAN expresion
    | expresion LESSTHAN expresion
    | expresion MORETHANEQUALS expresion
    | expresion LESSTHANEQUALS expresion
    | expresion STRICTNOTEQUALS expresion
    | LPAREN condicion RPAREN EQUALS expresion
    | LPAREN condicion RPAREN NOTEQUALS expresion
    | LPAREN condicion RPAREN STRICTEQUALS expresion
    | LPAREN condicion RPAREN MORETHAN expresion
    | LPAREN condicion RPAREN LESSTHAN expresion
    | LPAREN condicion RPAREN MORETHANEQUALS expresion
    | LPAREN condicion RPAREN LESSTHANEQUALS expresion
    | LPAREN condicion RPAREN STRICTNOTEQUALS expresion'''

def p_else(p):
    'else : ELSE LBRACE sentencias RBRACE'

def p_else_if(p):
    'elseif : ELIF LPAREN condicion RPAREN LBRACE sentencias RBRACE else'



def p_asignacion(p):
    '''asignacion : ID EQUAL expresion
        | VAR ID EQUAL expresion
        | LET ID EQUAL expresion'''


def p_expresion_term(p):
    'expresion : term'


def p_term_factor(p):
    'term : factor'

def p_factor_id(p):
    'term : ID'

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_str(p):
    'factor : STRING'

def p_factor_bool(p):
    '''factor : TRUE
    | FALSE '''


#Error Generado
def p_error(p):
    print("No se ha reconocido en el analisis sintactico {}".format(p))


parser=sintaxis.yacc()

while True:
    try:
        s = input('JavaScript > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
