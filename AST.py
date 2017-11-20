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
    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"

        return id


class declaration_list02(nodo):
    def __init__(self, hijo1, name):
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

    def __init__(self, hijo1, name):
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

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class var_declaration01(nodo):
    'var-declaration : type-specifier ID SEMICOLON'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"

        return id


class var_declaration02(nodo):
    'var-declaration : type-specifier ID LSQUAREBRACKET NUM RSQUAREBRACKET SEMICOLON'

    def __init__(self, hijo1, hijo2, hijo3, name):
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

        return id


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


class fun_declaration(nodo):
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'

    def __init__(self, hijo1, hijo2, hijo3, hijo4, name):
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

    def __init__(self, hijo1, name):
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

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
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

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"

        return id


class param02(nodo):
    'param : type-specifier ID LSQUAREBRACKET  RSQUAREBRACKET'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"

        return id


class compound_stmt(nodo):
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        return id


class local_declarations01(nodo):
    'local-declarations : local-declarations var-declaration'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        return id


class local_declarations02(nodo):
    'local-declarations : empty'


class statement_list01(nodo):
    'statement-list : statement-list statement'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        return id


class statement_list02(nodo):
    'statement-list : empty'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class statement01(nodo):
    'statement : expression-stmt'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class statement02(nodo):
    'statement : compound-stmt'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class statement03(nodo):
    'statement : selection-stmt'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class statement04(nodo):
    'statement : iteration-stmt'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class statement05(nodo):
    'statement : return-stmt'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class expression_stmt01(nodo):
    'expression-stmt : expression SEMICOLON'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class expression_stmt02(nodo):
    'expression-stmt : SEMICOLON'


class selection_stmt01(nodo):
    'selection-stmt : IF LPAREN expression RPAREN statement'

    def __init__(self, hijo1, hijo2,hijo3, name):
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
        return id


class selection_stmt02(nodo):
    'selection-stmt : IF LPAREN expression RPAREN statement ELSE statement'

    def __init__(self, hijo1, hijo2, hijo3, name):
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
        return id


class iteration_stmt(nodo):
    'iteration-stmt : WHILE LPAREN expression RPAREN statement'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        return id


class return_stmt01(nodo):
    'return-stmt : RETURN SEMICOLON'


class return_stmt02(nodo):
    'return-stmt : RETURN expression SEMICOLON'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class expression01(nodo):
    'expression : var ASSIGN expression'

    def __init__(self, hijo1, hijo2, hijo3, name):
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
        return id


class expression02(nodo):
    'expression : simple-expression'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class var01(nodo):
    'var : ID'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class var02(nodo):
    'var : ID LSQUAREBRACKET expression RSQUAREBRACKET'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        return id


class simple_expression01(nodo):
    'simple-expression : additive-expression relop additive-expression'

    def __init__(self, hijo1, hijo2, hijo3, name):
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
        return id


class simple_expression02(nodo):
    'simple-expression : additive-expression'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class relop01(nodo):
    'relop : MUCHSMALLER'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class relop02(nodo):
    'relop : LESS'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class relop03(nodo):
    'relop : GREATER'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class relop04(nodo):
    'relop : MUCHGREATER'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class relop05(nodo):
    'relop : EQUAL'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class relop06(nodo):
    'relop : UNEQUAL'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class additive_expression01(nodo):
    'additive-expression : additive-expression addop term'

    def __init__(self, hijo1, hijo2, hijo3, name):
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
        return id


class additive_expression02(nodo):
    'additive-expression : term'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class addop01(nodo):
    'addop : PLUS'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class addop02(nodo):
    'addop :  MINUS'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class term01(nodo):
    'term : term mulop factor'

    def __init__(self, hijo1, hijo2, hijo3, name):
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
        return id


class term02(nodo):
    'term : factor'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class mulop01(nodo):
    'mulop : TIMES'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class mulop02(nodo):
    'mulop : DIVIDE'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class factor01(nodo):
    'factor :  LPAREN expression RPAREN'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class factor02(nodo):
    'factor : var'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class factor03(nodo):
    'factor : call'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class factor04(nodo):
    'factor : NUM'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class call(nodo):
    'call : ID LPAREN args RPAREN'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        return id


class args01(nodo):
    'args : arg-list'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


class args02(nodo):
    'args : empty'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()
        hijo2 = self.hijo2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        return id


class arg_list01(nodo):
    'arg-list : arg-list COMMA expression'


class arg_list02(nodo):
    'arg-list : expression'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.hijo1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"

        return id


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
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class ASSIGN(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class MUCHSMALLER(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class GREATER(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class LESS(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class MUCHGREATER(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class EQUAL(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class UNEQUAL(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class PLUS(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class MINUS(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class TIMES(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class DIVIDE(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class INT(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class VOID(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class IF(nodo):
    def __init__(self, name):
        self.name = name

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id