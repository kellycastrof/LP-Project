import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens


def p_sentencias(p):
    '''sentencias : statement
    | if
    | for
    | while'''

def p_statements(p):
    'statement : stm'

def p_stm_asignacion(p):
    'stm : asignacion'

def p_stm_asignacion_date(p):
    'stm : asignacion_date'

def p_stm_array(p):
    'stm : array'

def p_stm_expression(p):
    'stm : expresion'

def p_stm_metodos(p):
    'stm : metodos'

def p_metodos(p):
    '''metodos : imprimir
    | touppercase
    | tolowercase
    | startwith
    | tostring
    | pop
    | push
    | shift
    | setdate
    | getfullyear'''

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

def p_pop(p):
    '''pop : ID POP LPAREN RPAREN
    | asignacion POP LPAREN RPAREN'''

def p_push(p):
    '''push : ID PUSH LPAREN factor RPAREN
    | asignacion PUSH LPAREN factor RPAREN'''

def p_shift(p):
    '''shift : ID SHIFT LPAREN RPAREN
    | asignacion SHIFT LPAREN RPAREN'''

def p_set_date(p):
    '''setdate : ID SETDATE LPAREN number RPAREN
    | asignacion SETDATE LPAREN number RPAREN'''

def p_get_full_year(p):
    '''getfullyear : ID GETFULLYEAR LPAREN RPAREN
    | asignacion GETFULLYEAR LPAREN RPAREN'''

def p_while(p):
    '''while : WHILE LPAREN condicion RPAREN LBRACE sentencias RBRACE'''

def p_if(p):
    '''if : IF LPAREN condicion RPAREN LBRACE sentencias RBRACE
    | IF LPAREN condicion RPAREN LBRACE sentencias RBRACE else
    | IF LPAREN condicion RPAREN LBRACE sentencias RBRACE elseif'''

def p_condicion(p):
    '''condicion : TRUE
    | FALSE
    | NOT expresion
    | expresion operadorlogico expresion
    | LPAREN condicion RPAREN operadorlogico expresion
    | expresion operadorlogico LPAREN condicion RPAREN'''

def p_else(p):
    'else : ELSE LBRACE sentencias RBRACE'

def p_else_if(p):
    'elseif : ELIF LPAREN condicion RPAREN LBRACE sentencias RBRACE else'

def p_for(p):
    '''for : FOR LPAREN type ID OF ID RPAREN LBRACE sentencias RBRACE'''

def p_asignacion(p):
    '''asignacion : ID EQUAL expresion
    | declaracion'''

def p_array(p):
    '''array : type ID EQUAL LBRACKET RBRACKET
    | type ID EQUAL LBRACKET arr_parametro RBRACKET
    | type ID EQUAL NEW ARRAY LPAREN RPAREN
    | type ID EQUAL NEW ARRAY LPAREN INTEGERP RPAREN'''

def p_arr_parametro(p):
    '''arr_parametro : expresion
    | expresion COMMA arr_parametro'''

def p_asignacion_new_date(p):
    '''asignacion_date : type ID EQUAL NEW DATE LPAREN RPAREN
    | type ID EQUAL NEW DATE LPAREN date_param RPAREN'''

def p_declaracion(p):
    '''declaracion : type ID EQUAL expresion'''

def p_date_param(p):
    '''date_param : STRING 
    | number
    | number COMMA number
    | number COMMA number COMMA number
    '''

def p_number(p):
    '''number : NUMBER
    | INTEGERP
    | INTEGERN'''

def p_type(p):
    '''type : VAR
    | LET'''

def p_expresion_operacion(p):
    '''expresion : expresion operador term
    | expresion operador expresion_entre_paren
    | expresion_entre_paren'''

def p_expresion_entre_paren(p):
    '''expresion_entre_paren : LPAREN expresion operador term RPAREN'''

def p_operador(p):
    '''operador : MINUS
    | PLUS
    | DIVIDE
    | TIMES
    | MOD'''

def p_operador_logico(p):
    '''operadorlogico : AND
    | OR
    | EQUALS
    | NOTEQUALS
    | STRICTEQUALS
    | MORETHAN
    | LESSTHAN
    | MORETHANEQUALS
    | LESSTHANEQUALS
    | STRICTNOTEQUALS'''

def p_expresion_term(p):
    'expresion : term'

def p_term_factor(p):
    'term : factor'

def p_factor_id(p):
    'factor : ID'

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
