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


def p_statement_expr(t):
    'statement : expression'
    print(t[1])



def p_statement_assign(t):
    'assign : NAME EQUALS expNormal'
    names[t[1]] = t[3]
    t[0]=t[3]


def p_statement_expresion(t):
    '''expression : expWhile
                  | expLineal
                  | expNormal'''
    t[0]=t[1]


def p_statement_print(t):
    'expLineal : PRINT LPAREN string RPAREN'
    t[0]=t[3]


def p_statement_string(t):
    'string : STRING'
    t[0] = t[1].strip("\"")


def p_expression_binop(t):
    '''operacion : expNormal PLUS expNormal
                 | expNormal MINUS expNormal
                 | expNormal TIMES expNormal
                 | expNormal DIVIDE expNormal
                 | expNormal EXPONENTE expNormal
                 | expNormal COMPARISON expNormal
                 | expNormal LOGICOS expNormal
                 | expNormal MODULO expNormal'''
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
    '''boolean : CONSTANTES'''
    if t[1] == "True":
        t[0] = True
    else:
        t[0] = False

def p_expression_group(t):
    'expLineal : LPAREN expLineal RPAREN'
    t[0] = t[2]



def p_expression_enter_tab(t):
    '''enterTab : NEWLN TAB statement enterTab
                | NEWLN TAB statement enterNormal
                | NEWLN TAB statement
                | NEWLN TAB expWhileA
                | NEWLN TAB expWhileA ELSE POINTS enterTab
                | NEWLN TAB BREAK'''
    if t[3] == "POINTS":
        t[0] = t[3]
    else:
        t[0] = t[3]



def p_expression_booleana(t):
    '''expBooleana : expNormal COMPARISON expNormal
                   | expBooleana LOGICOS expBooleana
                   | boolean'''
    t[0] = t[1]

def p_expression_booleana_par(t):
    '''expBooleana : LPAREN expBooleana RPAREN'''
    t[0] = t[2]

def p_expression_enter_tab_tab(t):
    '''enterTabTab : NEWLN TAB TAB statement enterNormal
                   | NEWLN TAB TAB statement enterTabTab
                   | NEWLN TAB TAB statement
                   | NEWLN TAB TAB BREAK'''
    t[0] = t[4]

def p_expression_enter_normal(t):
    '''enterNormal : NEWLN statement enterNormal
                   | NEWLN statement'''
    t[0] = t[2]

def p_expression_lineal(t):
    '''expLineal : operacion
                 | assign
                 | operacion enterNormal
                 | assign enterNormal'''
    t[0] = t[1]

def p_expression_normal(t):
    '''expNormal : NUMBER
                 | STRING
                 | boolean'''
    t[0] = t[1]

def p_expression_name(t):
    'expNormal : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Error léxico '%s'" % t[1])
        t[0] = 0

def p_expression_whileA(t):
    '''expWhileA : WHILE expBooleana POINTS enterTabTab
                 | WHILE expBooleana POINTS expLineal
                 | WHILE NAME POINTS enterTabTab
                 | WHILE NAME POINTS expLineal'''

def p_expression_while(t):
    '''expWhile : WHILE expBooleana POINTS enterTab
                | WHILE expBooleana POINTS expLineal
                | WHILE NAME POINTS enterTab
                | WHILE NAME POINTS expLineal'''
    t[0] = "♣"

def p_error(t):
    if t != None:
        print("Error sintáctico en '%s'" % t.value)
    else:
        print("Error semántico")
import libreriaFunciones as lib
import ply.yacc as yacc
from Console import *

def compilador():
    parser = yacc.yacc()
    try:
        window = GUI()
        s = window.show()
        t = s
        s = lib.trampita_Salto_de_linea(s)
        s = lib.trampita_Tabulacion(s)
    except EOFError:
        print("Algo salio mal")

    parser.parse(s)
    return t