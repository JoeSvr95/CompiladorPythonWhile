
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftCOMPARISONleftLOGICOSleftMODULOleftEXPONENTErightUMINUSCONSTANTES NAME NUMBER PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN WHILE EXPONENTE COMPARISON POINTS LOGICOS MODULO PRINT STRING BREAK ELSE NEWLN TABstatement : expressionassign : NAME EQUALS expNormal\n              | NAME EQUALS operacionexpression : expWhile\n                  | expLineal\n                  | expNormalexpLineal : PRINT LPAREN expNormal RPAREN\n                 | PRINT LPAREN operacion RPAREN\n                 | PRINT LPAREN expNormal RPAREN enterNormal\n                 | PRINT LPAREN operacion RPAREN enterNormal\n                 | PRINT LPAREN expNormal RPAREN enterTab\n                 | PRINT LPAREN operacion RPAREN enterTab\n                 | PRINT LPAREN expNormal RPAREN enterTabTab\n                 | PRINT LPAREN operacion RPAREN enterTabTabstring : STRINGoperacion : expNormal PLUS expNormal\n                 | expNormal MINUS expNormal\n                 | expNormal TIMES expNormal\n                 | expNormal DIVIDE expNormal\n                 | expNormal EXPONENTE expNormal\n                 | expNormal COMPARISON expNormal\n                 | expNormal LOGICOS expNormal\n                 | expNormal MODULO expNormalexpression : MINUS expression %prec UMINUSboolean : CONSTANTESexpLineal : LPAREN expLineal RPARENenterTab : NEWLN TAB statement enterTab\n                | NEWLN TAB statement enterNormal\n                | NEWLN TAB statement\n                | NEWLN TAB expWhileA\n                | NEWLN TAB expWhileA ELSE POINTS enterTabTab\n                | NEWLN TAB BREAKexpBooleana : expNormal COMPARISON expNormal\n                   | expBooleana LOGICOS expBooleana\n                   | booleanexpBooleana : LPAREN expBooleana RPARENenterTabTab : NEWLN TAB TAB statement enterNormal\n                   | NEWLN TAB TAB statement enterTabTab\n                   | NEWLN TAB TAB statement\n                   | NEWLN TAB TAB BREAKenterNormal : NEWLN statement enterNormal\n                   | NEWLN statement\n                   | NEWLN ELSE POINTS enterTabexpLineal : operacion\n                 | operacion enterNormal\n                 | operacion enterTab\n                 | operacion enterTabTab\n                 | assign\n                 | assign enterTab\n                 | assign enterTabTab\n                 | assign enterNormalexpNormal : NUMBER\n                 | string\n                 | booleanexpNormal : NAMEexpWhileA : WHILE expBooleana POINTS enterTabTab\n                 | WHILE expBooleana POINTS expLineal\n                 | WHILE NAME POINTS enterTabTab\n                 | WHILE NAME POINTS expLinealexpWhile : WHILE expBooleana POINTS enterTab\n                | WHILE expBooleana POINTS expLineal\n                | WHILE NAME POINTS enterTab\n                | WHILE NAME POINTS expLineal\n                | WHILE NAME LPAREN RPAREN POINTS enterTab\n                | WHILE NAME LPAREN RPAREN POINTS expLineal'
    
_lr_action_items = {'NAME':([0,5,11,14,18,20,21,22,23,24,25,26,27,31,37,40,44,58,61,63,64,65,70,73,74,90,96,97,106,108,109,120,],[1,1,32,39,45,45,45,45,45,45,45,45,45,1,1,45,45,1,32,45,32,45,1,1,94,1,32,1,1,32,32,1,]),'EQUALS':([1,32,],[18,18,]),'MODULO':([1,3,4,7,8,15,17,32,34,45,47,66,],[-55,-53,-25,-52,22,-54,-15,-55,22,-55,22,22,]),'EXPONENTE':([1,3,4,7,8,15,17,32,34,45,47,66,],[-55,-53,-25,-52,23,-54,-15,-55,23,-55,23,23,]),'MINUS':([0,1,3,4,5,7,8,15,17,31,32,34,37,45,47,58,66,70,73,90,97,106,120,],[5,-55,-53,-25,5,-52,24,-54,-15,5,-55,24,5,-55,24,5,24,5,5,5,5,5,5,]),'ELSE':([1,2,3,4,6,7,8,10,12,13,15,17,19,28,29,30,31,35,36,37,38,45,46,47,48,49,50,51,52,53,54,55,57,59,69,70,71,72,75,77,78,82,83,85,86,87,89,90,91,92,93,98,99,100,101,102,103,105,106,107,110,111,112,115,117,118,119,],[-55,-5,-53,-25,-4,-52,-6,-48,-1,-44,-54,-15,-24,-49,-51,-50,56,-46,-47,56,-45,-55,-3,-2,-21,-18,-23,-20,-17,-16,-19,-22,-42,-26,-41,56,88,-29,-32,-62,-63,-60,-61,-7,-8,-43,-27,56,-28,-39,-40,-11,-9,-13,-12,-10,-14,-38,56,-37,-64,-65,-31,-59,-58,-57,-56,]),'POINTS':([3,4,7,15,17,39,41,42,45,56,76,80,81,84,88,94,95,],[-53,-25,-52,-54,-15,61,-35,64,-55,68,96,-36,-34,-33,104,108,109,]),'TAB':([31,37,58,79,90,106,113,114,116,120,],[58,58,73,97,97,114,114,73,120,73,]),'CONSTANTES':([0,5,11,14,18,20,21,22,23,24,25,26,27,31,37,40,44,58,61,63,64,65,70,73,74,90,96,97,106,108,109,120,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'TIMES':([1,3,4,7,8,15,17,32,34,45,47,66,],[-55,-53,-25,-52,21,-54,-15,-55,21,-55,21,21,]),'$end':([1,2,3,4,6,7,8,9,10,12,13,15,17,19,28,29,30,35,36,38,45,46,47,48,49,50,51,52,53,54,55,57,59,69,71,72,75,77,78,82,83,85,86,87,89,91,92,93,98,99,100,101,102,103,105,107,110,111,112,115,117,118,119,],[-55,-5,-53,-25,-4,-52,-6,0,-48,-1,-44,-54,-15,-24,-49,-51,-50,-46,-47,-45,-55,-3,-2,-21,-18,-23,-20,-17,-16,-19,-22,-42,-26,-41,-30,-29,-32,-62,-63,-60,-61,-7,-8,-43,-27,-28,-39,-40,-11,-9,-13,-12,-10,-14,-38,-37,-64,-65,-31,-59,-58,-57,-56,]),'NEWLN':([1,2,3,4,6,7,8,10,12,13,15,17,19,28,29,30,35,36,38,45,46,47,48,49,50,51,52,53,54,55,57,59,61,64,68,69,71,72,75,77,78,82,83,85,86,87,89,91,92,93,96,98,99,100,101,102,103,104,105,107,108,109,110,111,112,115,117,118,119,],[-55,-5,-53,-25,-4,-52,-6,31,-1,37,-54,-15,-24,-49,-51,-50,-46,-47,-45,-55,-3,-2,-21,-18,-23,-20,-17,-16,-19,-22,70,-26,79,79,79,-41,-30,90,-32,-62,-63,-60,-61,37,37,-43,-27,-28,106,-40,79,-11,-9,-13,-12,-10,-14,113,-38,-37,116,116,-64,-65,-31,-59,-58,-57,-56,]),'WHILE':([0,5,31,37,58,70,73,90,97,106,120,],[14,14,14,14,74,14,14,14,74,14,74,]),'LPAREN':([0,5,11,14,16,31,37,39,40,58,61,63,64,70,73,74,90,94,96,97,106,108,109,120,],[11,11,11,40,44,11,11,60,40,11,11,40,11,11,11,40,11,60,11,11,11,11,11,11,]),'NUMBER':([0,5,11,14,18,20,21,22,23,24,25,26,27,31,37,40,44,58,61,63,64,65,70,73,74,90,96,97,106,108,109,120,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'PLUS':([1,3,4,7,8,15,17,32,34,45,47,66,],[-55,-53,-25,-52,25,-54,-15,-55,25,-55,25,25,]),'DIVIDE':([1,3,4,7,8,15,17,32,34,45,47,66,],[-55,-53,-25,-52,26,-54,-15,-55,26,-55,26,26,]),'LOGICOS':([1,3,4,7,8,15,17,32,34,41,42,45,47,62,66,80,81,84,95,],[-55,-53,-25,-52,27,-54,-15,-55,27,-35,63,-55,27,63,27,-36,-34,-33,63,]),'COMPARISON':([1,3,4,7,8,15,17,32,34,39,41,43,45,47,66,94,],[-55,-53,-25,-52,20,-54,-15,-55,20,-55,-54,65,-55,20,20,-55,]),'PRINT':([0,5,11,31,37,58,61,64,70,73,90,96,97,106,108,109,120,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'STRING':([0,5,11,14,18,20,21,22,23,24,25,26,27,31,37,40,44,58,61,63,64,65,70,73,74,90,96,97,106,108,109,120,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'RPAREN':([1,2,3,4,6,7,8,10,12,13,15,17,19,28,29,30,33,35,36,38,41,45,46,47,48,49,50,51,52,53,54,55,57,59,60,62,66,67,69,71,72,75,77,78,80,81,82,83,84,85,86,87,89,91,92,93,98,99,100,101,102,103,105,107,110,111,112,115,117,118,119,],[-55,-5,-53,-25,-4,-52,-6,-48,-1,-44,-54,-15,-24,-49,-51,-50,59,-46,-47,-45,-35,-55,-3,-2,-21,-18,-23,-20,-17,-16,-19,-22,-42,-26,76,80,85,86,-41,-30,-29,-32,-62,-63,-36,-34,-60,-61,-33,-7,-8,-43,-27,-28,-39,-40,-11,-9,-13,-12,-10,-14,-38,-37,-64,-65,-31,-59,-58,-57,-56,]),'BREAK':([58,73,97,120,],[75,93,75,75,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'enterTab':([10,13,61,64,68,72,85,86,96,108,109,],[28,35,77,82,87,89,98,101,110,77,82,]),'enterNormal':([10,13,57,72,85,86,92,],[29,38,69,91,99,102,107,]),'statement':([0,31,37,58,70,73,90,97,106,120,],[9,57,57,72,57,92,57,72,57,72,]),'assign':([0,5,11,31,37,58,61,64,70,73,90,96,97,106,108,109,120,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'enterTabTab':([10,13,85,86,92,104,108,109,],[30,36,100,103,105,112,117,119,]),'expWhileA':([58,97,120,],[71,71,71,]),'expWhile':([0,5,31,37,58,70,73,90,97,106,120,],[6,6,6,6,6,6,6,6,6,6,6,]),'operacion':([0,5,11,18,31,37,44,58,61,64,70,73,90,96,97,106,108,109,120,],[13,13,13,46,13,13,67,13,13,13,13,13,13,13,13,13,13,13,13,]),'expression':([0,5,31,37,58,70,73,90,97,106,120,],[12,19,12,12,12,12,12,12,12,12,12,]),'string':([0,5,11,14,18,20,21,22,23,24,25,26,27,31,37,40,44,58,61,63,64,65,70,73,74,90,96,97,106,108,109,120,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'boolean':([0,5,11,14,18,20,21,22,23,24,25,26,27,31,37,40,44,58,61,63,64,65,70,73,74,90,96,97,106,108,109,120,],[15,15,15,41,15,15,15,15,15,15,15,15,15,15,15,41,15,15,15,41,15,15,15,15,41,15,15,15,15,15,15,15,]),'expLineal':([0,5,11,31,37,58,61,64,70,73,90,96,97,106,108,109,120,],[2,2,33,2,2,2,78,83,2,2,2,111,2,2,115,118,2,]),'expBooleana':([14,40,63,74,],[42,62,81,95,]),'expNormal':([0,5,11,14,18,20,21,22,23,24,25,26,27,31,37,40,44,58,61,63,64,65,70,73,74,90,96,97,106,108,109,120,],[8,8,34,43,47,48,49,50,51,52,53,54,55,8,8,43,66,8,34,43,34,84,8,8,43,8,34,8,8,34,34,8,]),}

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
