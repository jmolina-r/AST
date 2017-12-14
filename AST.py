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

        if isinstance(self.hijo1, list):
            for hijo in self.hijo1:
                hijo1 = hijo.traducir()
                txt += str(id) + " -> " + str(hijo1) + "\n\t"
        else:
            hijo1 = self.hijo1.traducir()
            txt += id + "->" + hijo1 + "\n\t"

        txt += id + "[label= " + self.name + "]" + "\n\t"
        # txt += id + "->" + hijo1 + "\n\t"

        return "digraph G {\n\t" + txt + "}"


class var_declaration01(nodo):
    'var-declaration : type-specifier ID SEMICOLON'

    def __init__(self, type_var, ID, NUM, name):
        self.name = name
        self.type_var = type_var
        self.ID = ID
        self.NUM = NUM

    def traducir(self):
        global txt
        id = incremetarContador()

        if self.NUM is not None:
            txt += id + "[label= \" " + self.name + " " + self.type_var + " " + self.ID + " [" + str(
                self.NUM) + "]\" ]" + "\n\t"
        else:
            txt += id + "[label= \" " + self.name + " " + self.type_var + " " + self.ID + "\" ]" + "\n\t"

        return id


class fun_declaration(nodo):
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'

    def __init__(self, type_var, ID, params, compound_stmt, name):
        self.name = name
        self.type_var = type_var
        self.ID = ID
        self.compound_stmt = compound_stmt
        self.params = params

    def traducir(self):
        global txt
        id = incremetarContador()

        compound_stmt = self.compound_stmt.traducir()

        if isinstance(self.params, list):
            for param in self.params:
                print "lista"
                idp = param.traducir()
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
                txt += str(id) + " -> " + str(idp) + "\n\t"
        else:
            print "no lista"
            if self.params == "void":
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
            else:
                idp = self.params.traducir()
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
                txt += id + "->" + str(idp) + "\n\t"


        if self.compound_stmt.local_declar is not None or self.compound_stmt.statement_list is not None:
            txt += id + " -> " + compound_stmt + "\n\t"
        return id


class param01(nodo):
    'param : type-specifier ID'

    def __init__(self, var_type, ID, isarray, name):
        self.name = name
        self.var_type = var_type
        self.ID = ID
        self.isarray = isarray

    def traducir(self):
        global txt
        id = incremetarContador()
        print self.isarray
        if self.isarray == False:
            txt += id + "[label= \" " + self.name + " " + self.var_type + " " + self.ID + "\"]" + "\n\t"
        else:
            txt += id + "[label= \" " + self.name + " " + self.var_type + " " + self.ID + "[" + "]\"]" + "\n\t"

        return id


class compound_stmt(nodo):
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'

    def __init__(self, local_declar, statement_list, name):
        self.name = name
        self.local_declar = local_declar
        self.statement_list = statement_list

    def traducir(self):
        global txt
        id = incremetarContador()

        if isinstance(self.local_declar, list):
            for hijo in self.local_declar:
                if hijo is not None:
                    hijo1 = hijo.traducir()
                    txt += str(id) + " -> " + str(hijo1) + "\n\t"
        else:
            if self.local_declar is not None:
                hijo1 = self.local_declar.traducir()
                txt += id + "->" + hijo1 + "\n\t"

        if isinstance(self.statement_list, list):
            for hijo in self.statement_list:
                if hijo is not None:
                    hijo1 = hijo.traducir()
                    txt += str(id) + " -> " + str(hijo1) + "\n\t"
        else:
            if self.statement_list is not None:
                hijo2 = self.statement_list.traducir()
                txt += id + "->" + hijo2 + "\n\t"

        if self.statement_list is not None or self.local_declar is not None:
            txt += id + "[label= " + self.name + "]" + "\n\t"
        return id


class statement_list01(nodo):
    'statement-list : statement-list statement'

    def __init__(self, hijo1, hijo2, name):
        self.name = name
        self.hijo1 = hijo1
        self.hijo2 = hijo2

    def traducir(self):
        global txt
        id = incremetarContador()
        if self.hijo2 == ";":
            hijo1 = self.hijo1.traducir()
            # hijo2 = self.hijo2.traducir()
            txt += id + "[label= " + self.name + "]" + "\n\t"
            txt += id + " -> " + hijo1 + "\n\t"
            # txt += id + " -> " + hijo2 + "\n\t"
        else:
            hijo1 = self.hijo1.traducir()
            hijo2 = self.hijo2.traducir()

            txt += id + "[label= " + self.name + "]" + "\n\t"
            txt += id + " -> " + hijo1 + "\n\t"
            txt += id + " -> " + hijo2 + "\n\t"
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

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()

        if self.hijo1 is None:
            txt += id + "[label= e ]" + "\n\t"
        else:
            hijo1 = self.hijo1.traducir()
            txt += id + " -> " + str(hijo1) + "\n\t"
            txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class selection_stmt01(nodo):
    'selection-stmt : IF LPAREN expression RPAREN statement'

    def __init__(self, expresion, statement, name):
        self.name = name
        self.expresion = expresion
        self.statement = statement

    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        if isinstance(self.statement, list):
            for s in self.statement:
                print 'lista statement'
                statement = s.traducir()
                txt += id + " -> " + str(statement) + "\n\t"
        else:
            statement = self.statement.traducir()
            txt += id + " -> " + str(statement) + "\n\t"
            print "not list2"
        if isinstance(self.expresion, list):
            print 'lista expresion'
            for e in self.expresion:

                print 'lista statement'
                expresion = e.traducir()
                txt += id + " -> " + str(expresion) + "\n\t"
        else:
            expresion = self.expresion.traducir()
            txt += id + " -> " + expresion + "\n\t"
            print "not list2"

        return id


class selection_stmt02(nodo):
    'selection-stmt : IF LPAREN expression RPAREN statement ELSE statement'

    def __init__(self, expression, statement1, statement2, name):
        self.name = name
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2

    def traducir(self):
        global txt
        id = incremetarContador()

        hijo1 = self.expression.traducir()
        hijo2 = self.statement1.traducir()
        hijo3 = self.statement2.traducir()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        txt += id + " -> " + hijo3 + "\n\t"
        return id


class iteration_stmt(nodo):
    'iteration-stmt : WHILE LPAREN expression RPAREN statement'

    def __init__(self, expresion, statement, name):
        self.name = name
        self.expresion = expresion
        self.statement = statement

    def traducir(self):
        global txt
        id = incremetarContador()
        expresion = self.expresion.traducir()
        statement = self.statement.traducir()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"
        txt += id + " -> " + expresion + "\n\t"
        txt += id + " -> " + statement + "\n\t"
        return id


class return_stmt(nodo):
    'return-stmt : RETURN expression SEMICOLON'

    def __init__(self, expresion, name):
        self.name = name
        self.expresion = expresion

    def traducir(self):
        global txt
        id = incremetarContador()
        if self.expresion is not None:
            expresion = self.expresion.traducir()
            txt += id + " -> " + expresion + "\n\t"

        txt += id + "[label= " + self.name + "]" + "\n\t"
        return id


class expression01(nodo):
    'expression : var ASSIGN expression'

    def __init__(self, var, expression, name):
        self.name = name
        self.var = var
        self.expression = expression

    def traducir(self):
        global txt
        id = incremetarContador()

        var = self.var.traducir()
        expression = self.expression.traducir()

        txt += id + "[label= \" " + self.name + "\" ]" + "\n\t"
        txt += id + " -> " + var + "\n\t"
        txt += id + " -> " + expression + "\n\t"

        return id


class var01(nodo):
    'var : ID'

    def __init__(self, var, expresion, name):
        self.name = name
        self.var = var
        self.expresion = expresion

    def traducir(self):
        global txt
        id = incremetarContador()
        # hijo1 = self.var.traducir()

        txt += id + "[label= \"" + self.name + str(self.var) + "\"]" + "\n\t"
        # txt += id + " -> " + hijo1 + "\n\t"
        if self.expresion is not None:
            if isinstance(self.expresion, list):
                print 'lista expresion'
                for e in self.expresion:
                    # print str(e)+'E'
                    print 'lista statement'
                    expresion = e.traducir()
                    txt += id + " -> " + str(expresion) + "\n\t"
            else:
                expresion = self.expresion.traducir()
                txt += id + " -> " + expresion + "\n\t"
                print "not list2"

        return id


class binOP(nodo):
    'simple-expression : additive-expression relop additive-expression'

    def __init__(self, term1, op, term2, name):
        self.name = name
        self.term1 = term1
        self.op = op
        self.term2 = term2

    def traducir(self):
        # print self.op
        global txt
        id = incremetarContador()

        term1 = self.term1.traducir()
        term2 = self.term2.traducir()

        txt += id + "[label= \" " + self.name + " " + str(self.op) + " \" ]" + "\n\t"
        txt += id + " -> " + term1 + "\n\t"
        txt += id + " -> " + term2 + "\n\t"
        return id


class call(nodo):
    'call : ID LPAREN args RPAREN'

    def __init__(self, ID, ARGS, name):
        self.name = name
        self.ID = ID
        self.ARGS = ARGS

    def traducir(self):
        global txt
        id = incremetarContador()
        ARGS = self.ARGS.traducir()

        txt += id + "[label= \"" + self.name + ": " + self.ID + "\"]" + "\n\t"
        txt += id + " -> " + ARGS + "\n\t"

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
