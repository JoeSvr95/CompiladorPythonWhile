
tokens = ('CONSTANTES',
    'NAME' ,'NUMBER',
    'PLUS' ,'MINUS' ,'TIMES' ,'DIVIDE' ,'EQUALS',
    'LPAREN' ,'RPAREN', 'WHILE', 'EXPONENTE', 'COMPARISON', 'POINTS',
    'LOGICOS', 'MODULO', 'PRINT', 'STRING', 'BREAK', 'ELSE', 'NEWLN','TAB',
)

# Tokens

t_CONSTANTES = r'True|False'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_MODULO  = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'(?!(while|True|False|or|and|print|break|else))[a-zA-Z_][a-zA-Z0-9_]*(?!(while|True|False|or|and|print|break|else))'
t_WHILE   = r'while'
t_COMPARISON = r'>=|<=|!=|==|>|<'
t_EXPONENTE = r'\^'
t_POINTS = r':'
t_LOGICOS = r'or|and'
t_PRINT = r'print'
t_STRING = r'"[a-zA-Z0-9_ +-/*]*"'
t_BREAK = r'break'
t_ELSE = r'else'
t_NEWLN= r'@'
t_TAB= r'&'



def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left' ,'PLUS' ,'MINUS'),
    ('left' ,'TIMES' ,'DIVIDE'),
    ('left', 'COMPARISON'),
    ('left', 'LOGICOS'),
    ('left', 'MODULO'),
    ('left', 'EXPONENTE'),
    ('right' ,'UMINUS'),
)

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_statement_print(t):
    'statement : PRINT LPAREN string RPAREN'
    print(t[3].strip("\""))

def p_statement_string(t):
    'string : STRING'
    t[0] = t[1].strip("\"")

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EXPONENTE expression
                  | expression COMPARISON expression
                  | expression LOGICOS expression
                  | expression MODULO expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[2] == '^': t[0] = t[1] ** t[3]
    elif t[2] == '>': t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '>=':t[0] = t[1] >= t[3]
    elif t[2] == '<=':t[0] = t[1] <= t[3]
    elif t[2] == '!=':t[0] = t[1] != t[3]
    elif t[2] == '==':t[0] = t[1] == t[3]
    elif t[2] == '%': t[0] = t[1] % t[3]
    elif t[2] == 'and':t[0] = t[1] and t[3]
    elif t[2] == 'or': t[0] = t[1] or t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_constant(t):
    'expression : CONSTANTES'
    if t[1] == "True":
        t[0] = True
    else:
        t[0] = False

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_enter(t):
    '''enter : NEWLN TAB statement enter
             | NEWLN TAB statement'''

    t[0] = t[3]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Error léxico '%s'" % t[1])
        t[0] = 0

def p_expression_while(t):
    '''statement : WHILE expression POINTS enter
                 | WHILE expression POINTS expression ELSE statement
                 | WHILE expression POINTS statement BREAK'''
    print("♣")

def p_error(t):
    if t != None:
        print("Error sintáctico en '%s'" % t.value)
    else:
        print("Error semántico")
import libreriaFunciones as lib
import ply.yacc as yacc
from Console import *

while True:
    parser = yacc.yacc()
    try:
        window = GUI()
        s = window.show()
        print(s)
        s=lib.trampita_Salto_de_linea(s)
        s=lib.trampita_Tabulacion(s)
        #s = input('>>> ')   # Use raw_input on Python 2
    except EOFError:
        break
    print(s)
    parser.parse(s)