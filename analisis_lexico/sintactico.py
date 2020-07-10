import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens

def p_sentencias(p):
    '''sentencias : asignacion
    | expresion
    | metodos '''

def p_imprimir(p):
    'imprimir : factor'

def p_metodos(p):
    '''metodos : imprimir
    | toUpper
    | toLower
    | startsWith'''

def p_asignacion(p):
    'asignacion : ID EQUAL expresion'

def p_expresion(p):
    'expresion : factor'

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_str(p):
    'factor : STRING'





#Error Generado
def p_error(p):
    print("Error de Sintaxis: ")

parser = sintaxis.yacc()

while True:
    try:
        s = input('JavaScript > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)