
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftCOMPARISONleftLOGICOSleftMODULOleftEXPONENTErightUMINUSCONSTANTES NAME NUMBER PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN WHILE EXPONENTE COMPARISON POINTS LOGICOS MODULO PRINT STRING BREAK ELSE NEWLN TABstatement : expressionassign : NAME EQUALS expNormal\n              | NAME EQUALS operacionexpression : expWhile\n                  | expLineal\n                  | expNormalexpLineal : PRINT LPAREN expNormal RPAREN\n                 | PRINT LPAREN operacion RPAREN\n                 | PRINT LPAREN expNormal RPAREN enterNormal\n                 | PRINT LPAREN operacion RPAREN enterNormal\n                 | PRINT LPAREN expNormal RPAREN enterTab\n                 | PRINT LPAREN operacion RPAREN enterTab\n                 | PRINT LPAREN expNormal RPAREN enterTabTab\n                 | PRINT LPAREN operacion RPAREN enterTabTabstring : STRINGoperacion : expNormal PLUS expNormal\n                 | expNormal MINUS expNormal\n                 | expNormal TIMES expNormal\n                 | expNormal DIVIDE expNormal\n                 | expNormal EXPONENTE expNormal\n                 | expNormal COMPARISON expNormal\n                 | expNormal LOGICOS expNormal\n                 | expNormal MODULO expNormalexpression : MINUS expression %prec UMINUSboolean : CONSTANTESexpLineal : LPAREN expLineal RPARENenterTab : NEWLN TAB statement enterTab\n                | NEWLN TAB statement enterNormal\n                | NEWLN TAB statement\n                | NEWLN TAB expWhileA\n                | NEWLN TAB expWhileA ELSE POINTS enterTabTab\n                | NEWLN TAB BREAKexpBooleana : expNormal COMPARISON expNormal\n                   | expBooleana LOGICOS expBooleana\n                   | booleanexpBooleana : LPAREN expBooleana RPARENenterTabTab : NEWLN TAB TAB statement enterNormal\n                   | NEWLN TAB TAB statement enterTabTab\n                   | NEWLN TAB TAB statement\n                   | NEWLN TAB TAB BREAKenterNormal : NEWLN statement enterNormal\n                   | NEWLN statement\n                   | NEWLN ELSE POINTS enterTabexpLineal : operacion\n                 | operacion enterNormal\n                 | operacion enterTab\n                 | operacion enterTabTab\n                 | assign\n                 | assign enterTab\n                 | assign enterTabTab\n                 | assign enterNormalexpNormal : NUMBER\n                 | string\n                 | booleanexpNormal : NAMEexpWhileA : WHILE expBooleana POINTS enterTabTab\n                 | WHILE expBooleana POINTS expLineal\n                 | WHILE NAME POINTS enterTabTab\n                 | WHILE NAME POINTS expLinealexpWhile : WHILE expBooleana POINTS enterTab\n                | WHILE expBooleana POINTS expLineal\n                | WHILE NAME POINTS enterTab\n                | WHILE NAME POINTS expLineal\n                | WHILE NAME LPAREN RPAREN POINTS enterTab\n                | WHILE NAME LPAREN RPAREN POINTS expLineal'
    
_lr_action_items = {'PLUS':([2,3,4,6,9,10,13,32,34,49,58,60,],[-15,-54,24,-55,-25,-53,-52,-55,24,-55,24,24,]),'STRING':([0,7,11,16,18,22,23,24,25,26,27,28,29,30,31,35,41,46,63,64,66,67,70,71,74,94,102,103,105,107,108,120,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'$end':([1,2,3,4,6,8,9,10,12,13,14,15,17,19,20,21,40,42,43,44,47,48,49,50,51,52,53,54,55,56,59,60,61,69,72,73,75,76,77,80,82,84,85,87,88,89,93,95,96,97,98,99,100,101,104,106,110,111,113,115,116,117,119,],[-44,-15,-54,-6,-55,-1,-25,-53,-4,-52,-5,-48,0,-46,-47,-45,-49,-50,-51,-24,-42,-23,-55,-21,-16,-19,-18,-22,-17,-20,-3,-2,-26,-32,-30,-29,-41,-8,-7,-62,-63,-60,-61,-43,-40,-39,-27,-28,-14,-12,-10,-13,-9,-11,-38,-37,-64,-65,-58,-59,-56,-57,-31,]),'EXPONENTE':([2,3,4,6,9,10,13,32,34,49,58,60,],[-15,-54,29,-55,-25,-53,-52,-55,29,-55,29,29,]),'NEWLN':([1,2,3,4,6,8,9,10,12,13,14,15,19,20,21,40,42,43,44,47,48,49,50,51,52,53,54,55,56,59,60,61,64,66,68,69,72,73,75,76,77,80,82,84,85,87,88,89,93,95,96,97,98,99,100,101,103,104,106,107,108,109,110,111,113,115,116,117,119,],[18,-15,-54,-6,-55,-1,-25,-53,-4,-52,-5,41,-46,-47,-45,-49,-50,-51,-24,74,-23,-55,-21,-16,-19,-18,-22,-17,-20,-3,-2,-26,81,81,81,-32,-30,94,-41,18,18,-62,-63,-60,-61,-43,-40,105,-27,-28,-14,-12,-10,-13,-9,-11,81,-38,-37,114,114,118,-64,-65,-58,-59,-56,-57,-31,]),'PRINT':([0,7,16,18,41,46,64,66,70,74,94,102,103,105,107,108,120,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'BREAK':([46,70,102,120,],[69,88,69,69,]),'EQUALS':([6,32,],[31,31,]),'MODULO':([2,3,4,6,9,10,13,32,34,49,58,60,],[-15,-54,22,-55,-25,-53,-52,-55,22,-55,22,22,]),'NAME':([0,7,11,16,18,22,23,24,25,26,27,28,29,30,31,35,41,46,63,64,66,67,70,71,74,94,102,103,105,107,108,120,],[6,32,38,6,6,49,49,49,49,49,49,49,49,49,49,49,6,6,49,32,32,49,6,90,6,6,6,32,6,32,32,6,]),'LPAREN':([0,5,7,11,16,18,35,38,41,46,64,66,67,70,71,74,90,94,102,103,105,107,108,120,],[7,30,7,35,7,7,35,65,7,7,7,7,35,7,35,7,65,7,7,7,7,7,7,7,]),'RPAREN':([1,2,3,4,6,8,9,10,12,13,14,15,19,20,21,33,36,40,42,43,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,65,69,72,73,75,76,77,78,79,80,82,84,85,86,87,88,89,93,95,96,97,98,99,100,101,104,106,110,111,113,115,116,117,119,],[-44,-15,-54,-6,-55,-1,-25,-53,-4,-52,-5,-48,-46,-47,-45,61,-35,-49,-50,-51,-24,-42,-23,-55,-21,-16,-19,-18,-22,-17,-20,76,77,-3,-2,-26,78,83,-32,-30,-29,-41,-8,-7,-36,-33,-62,-63,-60,-61,-34,-43,-40,-39,-27,-28,-14,-12,-10,-13,-9,-11,-38,-37,-64,-65,-58,-59,-56,-57,-31,]),'TAB':([18,41,46,81,94,105,112,114,118,120,],[46,46,70,102,102,112,70,120,112,70,]),'CONSTANTES':([0,7,11,16,18,22,23,24,25,26,27,28,29,30,31,35,41,46,63,64,66,67,70,71,74,94,102,103,105,107,108,120,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'ELSE':([1,2,3,4,6,8,9,10,12,13,14,15,18,19,20,21,40,41,42,43,44,47,48,49,50,51,52,53,54,55,56,59,60,61,69,72,73,74,75,76,77,80,82,84,85,87,88,89,93,94,95,96,97,98,99,100,101,104,105,106,110,111,113,115,116,117,119,],[-44,-15,-54,-6,-55,-1,-25,-53,-4,-52,-5,-48,45,-46,-47,-45,-49,45,-50,-51,-24,-42,-23,-55,-21,-16,-19,-18,-22,-17,-20,-3,-2,-26,-32,92,-29,45,-41,-8,-7,-62,-63,-60,-61,-43,-40,-39,-27,45,-28,-14,-12,-10,-13,-9,-11,-38,45,-37,-64,-65,-58,-59,-56,-57,-31,]),'POINTS':([2,3,9,10,13,36,38,39,45,49,78,79,83,86,90,91,92,],[-15,-54,-25,-53,-52,-35,64,66,68,-55,-36,-33,103,-34,107,108,109,]),'WHILE':([0,16,18,41,46,70,74,94,102,105,120,],[11,11,11,11,71,11,11,11,71,11,71,]),'COMPARISON':([2,3,4,6,9,10,13,32,34,36,37,38,49,58,60,90,],[-15,-54,23,-55,-25,-53,-52,-55,23,-54,63,-55,-55,23,23,-55,]),'NUMBER':([0,7,11,16,18,22,23,24,25,26,27,28,29,30,31,35,41,46,63,64,66,67,70,71,74,94,102,103,105,107,108,120,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'MINUS':([0,2,3,4,6,9,10,13,16,18,32,34,41,46,49,58,60,70,74,94,102,105,120,],[16,-15,-54,28,-55,-25,-53,-52,16,16,-55,28,16,16,-55,28,28,16,16,16,16,16,16,]),'DIVIDE':([2,3,4,6,9,10,13,32,34,49,58,60,],[-15,-54,25,-55,-25,-53,-52,-55,25,-55,25,25,]),'TIMES':([2,3,4,6,9,10,13,32,34,49,58,60,],[-15,-54,26,-55,-25,-53,-52,-55,26,-55,26,26,]),'LOGICOS':([2,3,4,6,9,10,13,32,34,36,39,49,58,60,62,78,79,86,91,],[-15,-54,27,-55,-25,-53,-52,-55,27,-35,67,-55,27,27,67,-36,-33,-34,67,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'operacion':([0,7,16,18,30,31,41,46,64,66,70,74,94,102,103,105,107,108,120,],[1,1,1,1,57,59,1,1,1,1,1,1,1,1,1,1,1,1,1,]),'boolean':([0,7,11,16,18,22,23,24,25,26,27,28,29,30,31,35,41,46,63,64,66,67,70,71,74,94,102,103,105,107,108,120,],[3,3,36,3,3,3,3,3,3,3,3,3,3,3,3,36,3,3,3,3,3,36,3,36,3,3,3,3,3,3,3,3,]),'expBooleana':([11,35,67,71,],[39,62,86,91,]),'enterTabTab':([1,15,76,77,89,107,108,109,],[20,42,96,99,104,113,116,119,]),'enterTab':([1,15,64,66,68,73,76,77,103,107,108,],[19,40,80,84,87,93,97,101,110,80,84,]),'expWhile':([0,16,18,41,46,70,74,94,102,105,120,],[12,12,12,12,12,12,12,12,12,12,12,]),'expLineal':([0,7,16,18,41,46,64,66,70,74,94,102,103,105,107,108,120,],[14,33,14,14,14,14,82,85,14,14,14,14,111,14,115,117,14,]),'assign':([0,7,16,18,41,46,64,66,70,74,94,102,103,105,107,108,120,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'expNormal':([0,7,11,16,18,22,23,24,25,26,27,28,29,30,31,35,41,46,63,64,66,67,70,71,74,94,102,103,105,107,108,120,],[4,34,37,4,4,48,50,51,52,53,54,55,56,58,60,37,4,4,79,34,34,37,4,37,4,4,4,34,4,34,34,4,]),'expWhileA':([46,102,120,],[72,72,72,]),'statement':([0,18,41,46,70,74,94,102,105,120,],[17,47,47,73,89,47,47,73,47,73,]),'string':([0,7,11,16,18,22,23,24,25,26,27,28,29,30,31,35,41,46,63,64,66,67,70,71,74,94,102,103,105,107,108,120,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'enterNormal':([1,15,47,73,76,77,89,],[21,43,75,95,98,100,106,]),'expression':([0,16,18,41,46,70,74,94,102,105,120,],[8,44,8,8,8,8,8,8,8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','libreriaCompilador.py',75),
  ('assign -> NAME EQUALS expNormal','assign',3,'p_statement_assign','libreriaCompilador.py',81),
  ('assign -> NAME EQUALS operacion','assign',3,'p_statement_assign','libreriaCompilador.py',82),
  ('expression -> expWhile','expression',1,'p_statement_expresion','libreriaCompilador.py',88),
  ('expression -> expLineal','expression',1,'p_statement_expresion','libreriaCompilador.py',89),
  ('expression -> expNormal','expression',1,'p_statement_expresion','libreriaCompilador.py',90),
  ('expLineal -> PRINT LPAREN expNormal RPAREN','expLineal',4,'p_statement_print','libreriaCompilador.py',95),
  ('expLineal -> PRINT LPAREN operacion RPAREN','expLineal',4,'p_statement_print','libreriaCompilador.py',96),
  ('expLineal -> PRINT LPAREN expNormal RPAREN enterNormal','expLineal',5,'p_statement_print','libreriaCompilador.py',97),
  ('expLineal -> PRINT LPAREN operacion RPAREN enterNormal','expLineal',5,'p_statement_print','libreriaCompilador.py',98),
  ('expLineal -> PRINT LPAREN expNormal RPAREN enterTab','expLineal',5,'p_statement_print','libreriaCompilador.py',99),
  ('expLineal -> PRINT LPAREN operacion RPAREN enterTab','expLineal',5,'p_statement_print','libreriaCompilador.py',100),
  ('expLineal -> PRINT LPAREN expNormal RPAREN enterTabTab','expLineal',5,'p_statement_print','libreriaCompilador.py',101),
  ('expLineal -> PRINT LPAREN operacion RPAREN enterTabTab','expLineal',5,'p_statement_print','libreriaCompilador.py',102),
  ('string -> STRING','string',1,'p_statement_string','libreriaCompilador.py',107),
  ('operacion -> expNormal PLUS expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',112),
  ('operacion -> expNormal MINUS expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',113),
  ('operacion -> expNormal TIMES expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',114),
  ('operacion -> expNormal DIVIDE expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',115),
  ('operacion -> expNormal EXPONENTE expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',116),
  ('operacion -> expNormal COMPARISON expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',117),
  ('operacion -> expNormal LOGICOS expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',118),
  ('operacion -> expNormal MODULO expNormal','operacion',3,'p_expression_binop','libreriaCompilador.py',119),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','libreriaCompilador.py',136),
  ('boolean -> CONSTANTES','boolean',1,'p_expression_constant','libreriaCompilador.py',141),
  ('expLineal -> LPAREN expLineal RPAREN','expLineal',3,'p_expression_group','libreriaCompilador.py',148),
  ('enterTab -> NEWLN TAB statement enterTab','enterTab',4,'p_expression_enter_tab','libreriaCompilador.py',154),
  ('enterTab -> NEWLN TAB statement enterNormal','enterTab',4,'p_expression_enter_tab','libreriaCompilador.py',155),
  ('enterTab -> NEWLN TAB statement','enterTab',3,'p_expression_enter_tab','libreriaCompilador.py',156),
  ('enterTab -> NEWLN TAB expWhileA','enterTab',3,'p_expression_enter_tab','libreriaCompilador.py',157),
  ('enterTab -> NEWLN TAB expWhileA ELSE POINTS enterTabTab','enterTab',6,'p_expression_enter_tab','libreriaCompilador.py',158),
  ('enterTab -> NEWLN TAB BREAK','enterTab',3,'p_expression_enter_tab','libreriaCompilador.py',159),
  ('expBooleana -> expNormal COMPARISON expNormal','expBooleana',3,'p_expression_booleana','libreriaCompilador.py',165),
  ('expBooleana -> expBooleana LOGICOS expBooleana','expBooleana',3,'p_expression_booleana','libreriaCompilador.py',166),
  ('expBooleana -> boolean','expBooleana',1,'p_expression_booleana','libreriaCompilador.py',167),
  ('expBooleana -> LPAREN expBooleana RPAREN','expBooleana',3,'p_expression_booleana_par','libreriaCompilador.py',171),
  ('enterTabTab -> NEWLN TAB TAB statement enterNormal','enterTabTab',5,'p_expression_enter_tab_tab','libreriaCompilador.py',175),
  ('enterTabTab -> NEWLN TAB TAB statement enterTabTab','enterTabTab',5,'p_expression_enter_tab_tab','libreriaCompilador.py',176),
  ('enterTabTab -> NEWLN TAB TAB statement','enterTabTab',4,'p_expression_enter_tab_tab','libreriaCompilador.py',177),
  ('enterTabTab -> NEWLN TAB TAB BREAK','enterTabTab',4,'p_expression_enter_tab_tab','libreriaCompilador.py',178),
  ('enterNormal -> NEWLN statement enterNormal','enterNormal',3,'p_expression_enter_normal','libreriaCompilador.py',182),
  ('enterNormal -> NEWLN statement','enterNormal',2,'p_expression_enter_normal','libreriaCompilador.py',183),
  ('enterNormal -> NEWLN ELSE POINTS enterTab','enterNormal',4,'p_expression_enter_normal','libreriaCompilador.py',184),
  ('expLineal -> operacion','expLineal',1,'p_expression_lineal','libreriaCompilador.py',188),
  ('expLineal -> operacion enterNormal','expLineal',2,'p_expression_lineal','libreriaCompilador.py',189),
  ('expLineal -> operacion enterTab','expLineal',2,'p_expression_lineal','libreriaCompilador.py',190),
  ('expLineal -> operacion enterTabTab','expLineal',2,'p_expression_lineal','libreriaCompilador.py',191),
  ('expLineal -> assign','expLineal',1,'p_expression_lineal','libreriaCompilador.py',192),
  ('expLineal -> assign enterTab','expLineal',2,'p_expression_lineal','libreriaCompilador.py',193),
  ('expLineal -> assign enterTabTab','expLineal',2,'p_expression_lineal','libreriaCompilador.py',194),
  ('expLineal -> assign enterNormal','expLineal',2,'p_expression_lineal','libreriaCompilador.py',195),
  ('expNormal -> NUMBER','expNormal',1,'p_expression_normal','libreriaCompilador.py',199),
  ('expNormal -> string','expNormal',1,'p_expression_normal','libreriaCompilador.py',200),
  ('expNormal -> boolean','expNormal',1,'p_expression_normal','libreriaCompilador.py',201),
  ('expNormal -> NAME','expNormal',1,'p_expression_name','libreriaCompilador.py',205),
  ('expWhileA -> WHILE expBooleana POINTS enterTabTab','expWhileA',4,'p_expression_whileA','libreriaCompilador.py',213),
  ('expWhileA -> WHILE expBooleana POINTS expLineal','expWhileA',4,'p_expression_whileA','libreriaCompilador.py',214),
  ('expWhileA -> WHILE NAME POINTS enterTabTab','expWhileA',4,'p_expression_whileA','libreriaCompilador.py',215),
  ('expWhileA -> WHILE NAME POINTS expLineal','expWhileA',4,'p_expression_whileA','libreriaCompilador.py',216),
  ('expWhile -> WHILE expBooleana POINTS enterTab','expWhile',4,'p_expression_while','libreriaCompilador.py',219),
  ('expWhile -> WHILE expBooleana POINTS expLineal','expWhile',4,'p_expression_while','libreriaCompilador.py',220),
  ('expWhile -> WHILE NAME POINTS enterTab','expWhile',4,'p_expression_while','libreriaCompilador.py',221),
  ('expWhile -> WHILE NAME POINTS expLineal','expWhile',4,'p_expression_while','libreriaCompilador.py',222),
  ('expWhile -> WHILE NAME LPAREN RPAREN POINTS enterTab','expWhile',6,'p_expression_while','libreriaCompilador.py',223),
  ('expWhile -> WHILE NAME LPAREN RPAREN POINTS expLineal','expWhile',6,'p_expression_while','libreriaCompilador.py',224),
]
