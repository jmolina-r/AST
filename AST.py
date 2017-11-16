txt = " "
cont = 0


def incremetarContador():
    global cont
    cont += 1
    return "%d" % cont


class nodo():
    pass


class Null(nodo):
    def __init__(self):
        self.type = 'void'

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= " + "nodo_nulo" + "]" + "\n\t"

        return id


class program(nodo):
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + hijo1 + "\n\t"

        return "digraph G {\n\t" + txt + "}"


class declaration_list01(nodo):
    def __init__(self,hijo1,hijo2,name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

class declaration_list02(nodo):
    def __init__(self,hijo1,name):
        self.name = name
        self.hijo1 = hijo1
    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id

        
class declaration01(nodo):
    'declaration : var-declaration'

    def __init__(self, hijo1,name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()

        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id

class declaration02(nodo):
    'declaration : fun-declaration'
    def __init__(self,hijo1,hijo2,hijo3,name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()
        hijo3 = self.hijo3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1+ "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        txt += id + " -> " + hijo3 + "\n\t"
        return  id

class var_declaration01(nodo):
    'var-declaration : type-specifier ID SEMICOLON'
    def __init__(self,hijo1,hijo2,name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1+ "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"

        return id

class var_declaration02(nodo):
    'var-declaration : type-specifier ID LSQUAREBRACKET NUM RSQUAREBRACKET SEMICOLON'
    def __init__(self, hijo1, hijo2, hijo3,name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3

    def traducir(self):
        global txt
        id = incremetarContador()

        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()
        hijo3 = self.hijo3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        txt += id + " -> " + hijo3 + "\n\t"

class type_specifier01(nodo):
    'type-specifier : INT'
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()

        hijo1 = self.hijo1.traducir()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id

class type_specifier02(nodo):
    'type-specifier : VOID'

class fun_declaration(nodo):
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'
    def __init__(self,hijo1,hijo2,hijo3,hijo4,name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
        self.hijo3 = hijo3
        self.hijo4 = hijo4

    def traducir(self):
        global txt
        id = incremetarContador()

        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()
        hijo3 = self.hijo3.traducir()
        hijo4 = self.hijo4.traducir()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        txt += id + " -> " + hijo3 + "\n\t"
        txt += id + " -> " + hijo4 + "\n\t"

        return id

class params01(nodo):
    'params : param-list'
    def __init__(self,hijo1,name):
        self.name = name
        self.hijo1 = hijo1
    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id

class params02(nodo):
    'params : VOID'


class param_list01(nodo):
    'param-list : param-list COMMA param'
    def __init__(self, hijo1,hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2
    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1+ "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"

        return id

class param_list02(nodo):
    'param-list :  param'
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()

        hijo1 = self.hijo1.traducir()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id

class param01(nodo):
    'param : type-specifier ID'


class param02(nodo):
    'param : type-specifier ID LSQUAREBRACKET  RSQUAREBRACKET'


class compound_stmt(nodo):
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'


class local_declarations01(nodo):
    'local-declarations : local-declarations var-declaration'


class local_declarations02(nodo):
    'local-declarations : empty'


class statement_list01(nodo):
    'statement-list : statement-list statement'


class statement_list02(nodo):
    'statement-list : empty'


class statement01(nodo):
    'statement : expression-stmt'


class statement02(nodo):
    'statement : compound-stmt'


class statement03(nodo):
    'statement : selection-stmt'


class statement04(nodo):
    'statement : iteration-stmt'


class statement05(nodo):
    'statement : return-stmt'


class expression_stmt01(nodo):
    'expression-stmt : expression SEMICOLON'


class expression_stmt02(nodo):
    'expression-stmt : SEMICOLON'


class selection_stmt01(nodo):
    'selection-stmt : IF LPAREN expression RPAREN statement'


class selection_stmt02(nodo):
    'selection-stmt : IF LPAREN expression RPAREN statement ELSE statement'


class iteration_stmt(nodo):
    'iteration-stmt : WHILE LPAREN expression RPAREN statement'


class return_stmt01(nodo):
    'return-stmt : RETURN SEMICOLON'


class return_stmt02(nodo):
    'return-stmt : RETURN expression SEMICOLON'


class expression01(nodo):
    'expression : var ASSIGN expression'


class expression02(nodo):
    'expression : simple-expression'


class var01(nodo):
    'var : ID '


class var02(nodo):
    'var : ID LSQUAREBRACKET expression RSQUAREBRACKET'


class simple_expression01(nodo):
    'simple-expression : additive-expression relop additive-expression'


class simple_expression02(nodo):
    'simple-expression : additive-expression'


class relop01(nodo):
    'relop : MUCHSMALLER'


class relop02(nodo):
    'relop : LESS'


class relop03(nodo):
    'relop : GREATER'


class relop04(nodo):
    'relop : MUCHGREATER'


class relop05(nodo):
    'relop : EQUAL'


class relop06(nodo):
    'relop : UNEQUAL'


class additive_expression01(nodo):
    'additive-expression : additive-expression addop term'


class additive_expression02(nodo):
    'additive-expression : term'


class addop01(nodo):
    'addop : PLUS'


class addop02(nodo):
    'addop :  MINUS'


class term01(nodo):
    'term : term mulop factor'


class term02(nodo):
    'term : factor'


class mulop01(nodo):
    'mulop : TIMES'


class mulop02(nodo):
    'mulop : DIVIDE'


class factor01(nodo):
    'factor :  LPAREN expression RPAREN'


class factor02(nodo):
    'factor : var'


class factor03(nodo):
    'factor : call'


class factor04(nodo):
    'factor : NUM'


class call(nodo):
    'call : ID LPAREN args RPAREN'


class args01(nodo):
    'args : arg-list'


class args02(nodo):
    'args : empty'


class arg_list01(nodo):
    'arg-list : arg-list COMMA expression'


class arg_list02(nodo):
    'arg-list : expression'

class num(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id
class ID(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id