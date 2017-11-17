
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightELSEIFINTVOIDRETURNWHILErightIDrightASSIGNleftUNEQUALleftLESSMUCHSMALLERGREATERMUCHGREATERleftPLUSMINUSleftTIMESDIVIDEleftLPARENRPARENPLUS MINUS TIMES DIVIDE LPAREN RPAREN LBRACE RBRACE LSQUAREBRACKET RSQUAREBRACKET LESS GREATER MUCHSMALLER MUCHGREATER EQUAL UNEQUAL COMMA SEMICOLON ASSIGN MULTCOMMMENT LINECOMMENT ID NUM RETURN INT VOID ELSE WHILE IFprogram : declaration-listdeclaration-list : declaration-list declarationdeclaration-list : declarationdeclaration : var-declarationdeclaration : fun-declarationvar-declaration : type-specifier ID SEMICOLONvar-declaration : type-specifier ID LSQUAREBRACKET RSQUAREBRACKETtype-specifier : INTtype-specifier : VOIDfun-declaration : type-specifier ID LPAREN params RPAREN compound-stmtparams : param-listparams : VOIDparam-list : param-list COMMA paramparam-list :  paramparam : type-specifier IDparam : type-specifier ID LSQUAREBRACKET RSQUAREBRACKETcompound-stmt : LBRACE local-declarations statement-list RBRACElocal-declarations : local-declarations var-declarationlocal-declarations : emptystatement-list : statement-list statementstatement-list : emptystatement : expression-stmtstatement : compound-stmtstatement : selection-stmtstatement : iteration-stmtstatement : return-stmtexpression-stmt : expression SEMICOLONexpression-stmt : SEMICOLONselection-stmt : IF LPAREN expression RPAREN statementselection-stmt : IF LPAREN expression RPAREN statement ELSE statementiteration-stmt : WHILE LPAREN expression RPAREN statementreturn-stmt : RETURN SEMICOLONreturn-stmt : RETURN expression SEMICOLONexpression : var ASSIGN expressionexpression : simple-expressionvar : ID var : ID LSQUAREBRACKET expression RSQUAREBRACKETsimple-expression : additive-expression relop additive-expressionsimple-expression : additive-expressionrelop : MUCHSMALLERrelop : LESSrelop : GREATERrelop : MUCHGREATERrelop : EQUALrelop : UNEQUALadditive-expression : additive-expression addop termadditive-expression : termaddop : PLUSaddop :  MINUSterm : term mulop factorterm : factormulop : TIMESmulop : DIVIDEfactor :  LPAREN expression RPARENfactor : varfactor : callfactor : NUMcall : ID LPAREN args RPARENargs : arg-listargs : emptyarg-list : arg-list COMMA expressionarg-list : expressionempty :'
    
_lr_action_items = {'RETURN':([12,14,23,27,28,30,31,33,37,38,41,44,45,46,48,54,56,77,78,92,96,97,99,100,101,],[-6,-7,-63,-63,-19,34,-18,-21,-26,-28,-20,-17,-22,-24,-23,-25,-32,-27,-33,34,34,-31,-29,34,-30,]),'LESS':([36,39,40,42,43,49,51,80,81,84,91,93,94,],[62,-57,-56,-51,-55,-36,-47,-46,-55,-54,-50,-37,-58,]),'VOID':([0,3,4,6,8,9,12,13,14,22,23,24,27,28,31,44,],[2,-5,2,-3,-4,-2,-6,15,-7,2,-63,-10,2,-19,-18,-17,]),'EQUAL':([36,39,40,42,43,49,51,80,81,84,91,93,94,],[64,-57,-56,-51,-55,-36,-47,-46,-55,-54,-50,-37,-58,]),'WHILE':([12,14,23,27,28,30,31,33,37,38,41,44,45,46,48,54,56,77,78,92,96,97,99,100,101,],[-6,-7,-63,-63,-19,35,-18,-21,-26,-28,-20,-17,-22,-24,-23,-25,-32,-27,-33,35,35,-31,-29,35,-30,]),'UNEQUAL':([36,39,40,42,43,49,51,80,81,84,91,93,94,],[60,-57,-56,-51,-55,-36,-47,-46,-55,-54,-50,-37,-58,]),'MINUS':([36,39,40,42,43,49,51,80,81,82,84,91,93,94,],[67,-57,-56,-51,-55,-36,-47,-46,-55,67,-54,-50,-37,-58,]),'DIVIDE':([39,40,42,43,49,51,80,81,84,91,93,94,],[-57,-56,-51,-55,-36,75,75,-55,-54,-50,-37,-58,]),'RPAREN':([15,16,17,19,21,26,29,36,39,40,42,43,49,51,52,70,72,79,80,81,82,83,84,86,87,88,89,90,91,93,94,98,],[-12,-14,20,-11,-15,-13,-16,-39,-57,-56,-51,-55,-36,-47,-35,84,-63,92,-46,-55,-38,-34,-54,94,-59,-62,-60,96,-50,-37,-58,-61,]),'SEMICOLON':([10,12,14,23,27,28,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,48,49,51,52,53,54,55,56,57,77,78,80,81,82,83,84,91,92,93,94,96,97,99,100,101,],[12,-6,-7,-63,-63,-19,38,-18,-21,56,-39,-26,-28,-57,-56,-20,-51,-55,-17,-22,-24,-23,-36,-47,-35,77,-25,12,-32,78,-27,-33,-46,-55,-38,-34,-54,-50,38,-37,-58,38,-31,-29,38,-30,]),'NUM':([12,14,23,27,28,30,31,33,34,37,38,41,44,45,46,47,48,54,56,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,92,95,96,97,99,100,101,],[-6,-7,-63,-63,-19,39,-18,-21,39,-26,-28,-20,-17,-22,-24,39,-23,-25,-32,39,39,-45,39,-41,-43,-44,-40,-48,-49,-42,39,39,39,39,-52,-53,39,-27,-33,39,39,39,-31,-29,39,-30,]),'PLUS':([36,39,40,42,43,49,51,80,81,82,84,91,93,94,],[66,-57,-56,-51,-55,-36,-47,-46,-55,66,-54,-50,-37,-58,]),'COMMA':([16,19,21,26,29,36,39,40,42,43,49,51,52,80,81,82,83,84,87,88,91,93,94,98,],[-14,22,-15,-13,-16,-39,-57,-56,-51,-55,-36,-47,-35,-46,-55,-38,-34,-54,95,-62,-50,-37,-58,-61,]),'RSQUAREBRACKET':([11,25,36,39,40,42,43,49,51,52,80,81,82,83,84,85,91,93,94,],[14,29,-39,-57,-56,-51,-55,-36,-47,-35,-46,-55,-38,-34,-54,93,-50,-37,-58,]),'ASSIGN':([43,49,93,],[69,-36,-37,]),'$end':([3,4,5,6,8,9,12,14,24,44,],[-5,-1,0,-3,-4,-2,-6,-7,-10,-17,]),'LSQUAREBRACKET':([10,21,49,55,],[11,25,71,11,]),'RBRACE':([12,14,23,27,28,30,31,33,37,38,41,44,45,46,48,54,56,77,78,97,99,101,],[-6,-7,-63,-63,-19,44,-18,-21,-26,-28,-20,-17,-22,-24,-23,-25,-32,-27,-33,-31,-29,-30,]),'MUCHGREATER':([36,39,40,42,43,49,51,80,81,84,91,93,94,],[63,-57,-56,-51,-55,-36,-47,-46,-55,-54,-50,-37,-58,]),'ELSE':([37,38,44,45,46,48,54,56,77,78,97,99,101,],[-26,-28,-17,-22,-24,-23,-25,-32,-27,-33,-31,-29,-30,]),'LPAREN':([10,12,14,23,27,28,30,31,33,34,35,37,38,41,44,45,46,47,48,49,50,54,56,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,92,95,96,97,99,100,101,],[13,-6,-7,-63,-63,-19,47,-18,-21,47,58,-26,-28,-20,-17,-22,-24,47,-23,72,73,-25,-32,47,47,-45,47,-41,-43,-44,-40,-48,-49,-42,47,47,47,47,-52,-53,47,-27,-33,47,47,47,-31,-29,47,-30,]),'TIMES':([39,40,42,43,49,51,80,81,84,91,93,94,],[-57,-56,-51,-55,-36,74,74,-55,-54,-50,-37,-58,]),'ID':([1,2,7,12,14,15,18,23,27,28,30,31,32,33,34,37,38,41,44,45,46,47,48,54,56,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,92,95,96,97,99,100,101,],[-8,-9,10,-6,-7,-9,21,-63,-63,-19,49,-18,55,-21,49,-26,-28,-20,-17,-22,-24,49,-23,-25,-32,49,49,-45,49,-41,-43,-44,-40,-48,-49,-42,49,49,49,49,-52,-53,49,-27,-33,49,49,49,-31,-29,49,-30,]),'IF':([12,14,23,27,28,30,31,33,37,38,41,44,45,46,48,54,56,77,78,92,96,97,99,100,101,],[-6,-7,-63,-63,-19,50,-18,-21,-26,-28,-20,-17,-22,-24,-23,-25,-32,-27,-33,50,50,-31,-29,50,-30,]),'LBRACE':([12,14,20,23,27,28,30,31,33,37,38,41,44,45,46,48,54,56,77,78,92,96,97,99,100,101,],[-6,-7,23,-63,-63,-19,23,-18,-21,-26,-28,-20,-17,-22,-24,-23,-25,-32,-27,-33,23,23,-31,-29,23,-30,]),'GREATER':([36,39,40,42,43,49,51,80,81,84,91,93,94,],[68,-57,-56,-51,-55,-36,-47,-46,-55,-54,-50,-37,-58,]),'INT':([0,3,4,6,8,9,12,13,14,22,23,24,27,28,31,44,],[1,-5,1,-3,-4,-2,-6,1,-7,1,-63,-10,1,-19,-18,-17,]),'MUCHSMALLER':([36,39,40,42,43,49,51,80,81,84,91,93,94,],[65,-57,-56,-51,-55,-36,-47,-46,-55,-54,-50,-37,-58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration':([0,4,],[6,9,]),'additive-expression':([30,34,47,58,61,69,71,72,73,92,95,96,100,],[36,36,36,36,82,36,36,36,36,36,36,36,36,]),'return-stmt':([30,92,96,100,],[37,37,37,37,]),'param':([13,22,],[16,26,]),'var-declaration':([0,4,27,],[8,8,31,]),'arg-list':([72,],[87,]),'program':([0,],[5,]),'call':([30,34,47,58,59,61,69,71,72,73,76,92,95,96,100,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'statement':([30,92,96,100,],[41,97,99,101,]),'factor':([30,34,47,58,59,61,69,71,72,73,76,92,95,96,100,],[42,42,42,42,42,42,42,42,42,42,91,42,42,42,42,]),'var':([30,34,47,58,59,61,69,71,72,73,76,92,95,96,100,],[43,43,43,43,81,81,43,43,43,43,81,43,43,43,43,]),'params':([13,],[17,]),'empty':([23,27,72,],[28,33,89,]),'addop':([36,82,],[59,59,]),'mulop':([51,80,],[76,76,]),'args':([72,],[86,]),'expression-stmt':([30,92,96,100,],[45,45,45,45,]),'compound-stmt':([20,30,92,96,100,],[24,48,48,48,48,]),'term':([30,34,47,58,59,61,69,71,72,73,92,95,96,100,],[51,51,51,51,80,51,51,51,51,51,51,51,51,51,]),'selection-stmt':([30,92,96,100,],[46,46,46,46,]),'relop':([36,],[61,]),'fun-declaration':([0,4,],[3,3,]),'declaration-list':([0,],[4,]),'local-declarations':([23,],[27,]),'param-list':([13,],[19,]),'statement-list':([27,],[30,]),'simple-expression':([30,34,47,58,69,71,72,73,92,95,96,100,],[52,52,52,52,52,52,52,52,52,52,52,52,]),'type-specifier':([0,4,13,22,27,],[7,7,18,18,32,]),'expression':([30,34,47,58,69,71,72,73,92,95,96,100,],[53,57,70,79,83,85,88,90,53,98,53,53,]),'iteration-stmt':([30,92,96,100,],[54,54,54,54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration-list','program',1,'p_program','parser.py',23),
  ('declaration-list -> declaration-list declaration','declaration-list',2,'p_declaration_list01','parser.py',28),
  ('declaration-list -> declaration','declaration-list',1,'p_declaration_list02','parser.py',33),
  ('declaration -> var-declaration','declaration',1,'p_declaration01','parser.py',38),
  ('declaration -> fun-declaration','declaration',1,'p_declaration02','parser.py',43),
  ('var-declaration -> type-specifier ID SEMICOLON','var-declaration',3,'p_var_declaration01','parser.py',48),
  ('var-declaration -> type-specifier ID LSQUAREBRACKET RSQUAREBRACKET','var-declaration',4,'p_var_declaration02','parser.py',53),
  ('type-specifier -> INT','type-specifier',1,'p_type_specifier01','parser.py',58),
  ('type-specifier -> VOID','type-specifier',1,'p_type_specifier02','parser.py',63),
  ('fun-declaration -> type-specifier ID LPAREN params RPAREN compound-stmt','fun-declaration',6,'p_fun_declaration','parser.py',67),
  ('params -> param-list','params',1,'p_params01','parser.py',72),
  ('params -> VOID','params',1,'p_params02','parser.py',77),
  ('param-list -> param-list COMMA param','param-list',3,'p_param_list01','parser.py',81),
  ('param-list -> param','param-list',1,'p_param_list02','parser.py',86),
  ('param -> type-specifier ID','param',2,'p_param01','parser.py',91),
  ('param -> type-specifier ID LSQUAREBRACKET RSQUAREBRACKET','param',4,'p_param02','parser.py',95),
  ('compound-stmt -> LBRACE local-declarations statement-list RBRACE','compound-stmt',4,'p_compound_stmt','parser.py',99),
  ('local-declarations -> local-declarations var-declaration','local-declarations',2,'p_local_declarations01','parser.py',103),
  ('local-declarations -> empty','local-declarations',1,'p_local_declarations02','parser.py',107),
  ('statement-list -> statement-list statement','statement-list',2,'p_statement_list01','parser.py',111),
  ('statement-list -> empty','statement-list',1,'p_statement_list02','parser.py',115),
  ('statement -> expression-stmt','statement',1,'p_statement01','parser.py',119),
  ('statement -> compound-stmt','statement',1,'p_statement02','parser.py',123),
  ('statement -> selection-stmt','statement',1,'p_statement03','parser.py',127),
  ('statement -> iteration-stmt','statement',1,'p_statement04','parser.py',131),
  ('statement -> return-stmt','statement',1,'p_statement05','parser.py',135),
  ('expression-stmt -> expression SEMICOLON','expression-stmt',2,'p_expression_stmt01','parser.py',139),
  ('expression-stmt -> SEMICOLON','expression-stmt',1,'p_expression_stmt02','parser.py',143),
  ('selection-stmt -> IF LPAREN expression RPAREN statement','selection-stmt',5,'p_selection_stmt01','parser.py',147),
  ('selection-stmt -> IF LPAREN expression RPAREN statement ELSE statement','selection-stmt',7,'p_selection_stmt02','parser.py',151),
  ('iteration-stmt -> WHILE LPAREN expression RPAREN statement','iteration-stmt',5,'p_iteration_stmt','parser.py',155),
  ('return-stmt -> RETURN SEMICOLON','return-stmt',2,'p_return_stmt01','parser.py',159),
  ('return-stmt -> RETURN expression SEMICOLON','return-stmt',3,'p_return_stmt02','parser.py',163),
  ('expression -> var ASSIGN expression','expression',3,'p_expression01','parser.py',167),
  ('expression -> simple-expression','expression',1,'p_expression02','parser.py',171),
  ('var -> ID','var',1,'p_var01','parser.py',175),
  ('var -> ID LSQUAREBRACKET expression RSQUAREBRACKET','var',4,'p_var02','parser.py',179),
  ('simple-expression -> additive-expression relop additive-expression','simple-expression',3,'p_simple_expression01','parser.py',183),
  ('simple-expression -> additive-expression','simple-expression',1,'p_simple_expression02','parser.py',187),
  ('relop -> MUCHSMALLER','relop',1,'p_relop01','parser.py',190),
  ('relop -> LESS','relop',1,'p_relop02','parser.py',194),
  ('relop -> GREATER','relop',1,'p_relop03','parser.py',198),
  ('relop -> MUCHGREATER','relop',1,'p_relop04','parser.py',203),
  ('relop -> EQUAL','relop',1,'p_relop05','parser.py',207),
  ('relop -> UNEQUAL','relop',1,'p_relop06','parser.py',212),
  ('additive-expression -> additive-expression addop term','additive-expression',3,'p_additive_expression01','parser.py',217),
  ('additive-expression -> term','additive-expression',1,'p_additive_expression02','parser.py',221),
  ('addop -> PLUS','addop',1,'p_addop01','parser.py',225),
  ('addop -> MINUS','addop',1,'p_addop02','parser.py',229),
  ('term -> term mulop factor','term',3,'p_term01','parser.py',233),
  ('term -> factor','term',1,'p_term02','parser.py',237),
  ('mulop -> TIMES','mulop',1,'p_mulop01','parser.py',241),
  ('mulop -> DIVIDE','mulop',1,'p_mulop02','parser.py',245),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor01','parser.py',250),
  ('factor -> var','factor',1,'p_factor02','parser.py',254),
  ('factor -> call','factor',1,'p_factor03','parser.py',258),
  ('factor -> NUM','factor',1,'p_factor04','parser.py',262),
  ('call -> ID LPAREN args RPAREN','call',4,'p_call','parser.py',266),
  ('args -> arg-list','args',1,'p_args01','parser.py',270),
  ('args -> empty','args',1,'p_args02','parser.py',274),
  ('arg-list -> arg-list COMMA expression','arg-list',3,'p_arg_list01','parser.py',278),
  ('arg-list -> expression','arg-list',1,'p_arg_list02','parser.py',282),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',286),
]
