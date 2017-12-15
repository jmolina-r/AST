from diccionario import *

txt = " "
cont = 0
tabla_simbolo = diccionario()

def incremetarContador():
    global cont
    cont += 1
    return "%d" % cont



class Null():
    def __init__(self):
        self.type = 'void'

    def traducir(self):
        global txt
        id = incremetarContador()
        txt += id + "[label= " + "nodo_nulo" + "]" + "\n\t"

        return id


class program():
    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self):
        global txt
        id = incremetarContador()
        global tabla_simbolo

        if isinstance(self.hijo1, list):
            for hijo in self.hijo1:
                hijo1 = hijo.traducir(tabla_simbolo)
                txt += str(id) + " -> " + str(hijo1) + "\n\t"
        else:
            hijo1 = self.hijo1.traducir(tabla_simbolo)
            txt += id + "->" + hijo1 + "\n\t"

        txt += id + "[label= " + self.name + "]" + "\n\t"

        return "digraph G {\n\t" + txt + "}"


class var_declaration01():
    'var-declaration : type-specifier ID SEMICOLON'

    def __init__(self, type_var, ID, NUM, name):
        self.name = name
        self.type_var = type_var
        self.ID = ID
        self.NUM = NUM

    def traducir(self,diccionario):
        global txt
        id = incremetarContador()

        if self.NUM is not None:
            txt += id + "[label= \" " + self.name + " " + self.type_var + " " + self.ID + " [" + str(
                self.NUM) + "]\" ]" + "\n\t"

            new_nodo = nodo(self.type_var + "[]", self.ID, None)
        else:
            txt += id + "[label= \" " + self.name + " " + self.type_var + " " + self.ID + "\" ]" + "\n\t"
            new_nodo = nodo(self.type_var, self.ID, self.NUM)

        diccionario.addnodo(new_nodo, diccionario)

        return id


class fun_declaration():
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'

    def __init__(self, type_var, ID, params, compound_stmt, name):
        self.name = name
        self.type_var = type_var
        self.ID = ID
        self.compound_stmt = compound_stmt
        self.params = params

    def traducir(self,diccionari):
        global txt
        id = incremetarContador()
        new_nodo = nodo(self.type_var,self.ID,None)
        new_diccionario = diccionario()

        if isinstance(self.params, list):
            for param in self.params:
                idp = param.traducir(new_diccionario)
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
                txt += str(id) + " -> " + str(idp) + "\n\t"
            new_nodo.settdicc(new_diccionario)
            diccionari.addnodo(new_nodo, diccionari)
        else:
            if self.params == "void":
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
                new_nodo.settdicc(new_diccionario)
                diccionari.addnodo(new_nodo, diccionari)
            else:
                new_nodo.settdicc(new_diccionario)
                diccionari.addnodo(new_nodo, diccionari)
                idp = self.params.traducir(new_diccionario)
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
                txt += id + "->" + str(idp) + "\n\t"


        if self.compound_stmt.local_declar is not None or self.compound_stmt.statement_list is not None:
            if new_nodo.getdicc()is None:
                new_nodo.settdicc(new_diccionario)
                diccionari.addnodo(new_nodo,diccionari)
            compound_stmt = self.compound_stmt.traducir(new_diccionario)
            txt += id + " -> " + compound_stmt + "\n\t"
        return id


class param01():
    'param : type-specifier ID'

    def __init__(self, var_type, ID, isarray, name):
        self.name = name
        self.var_type = var_type
        self.ID = ID
        self.isarray = isarray

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()
        if self.isarray == False:
            txt += id + "[label= \" " + self.name + " " + self.var_type + " " + self.ID + "\"]" + "\n\t"
            new_nodo = nodo(self.var_type, self.ID, None)
        else:
            txt += id + "[label= \" " + self.name + " " + self.var_type + " " + self.ID + "[" + "]\"]" + "\n\t"
            new_nodo = nodo(self.var_type+"[]", self.ID, None)

        diccionar.addnodo(new_nodo, diccionar)
        return id


class compound_stmt():
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'

    def __init__(self, local_declar, statement_list, name):
        self.name = name
        self.local_declar = local_declar
        self.statement_list = statement_list

    def traducir(self,diccionario):
        global txt
        id = incremetarContador()

        if isinstance(self.local_declar, list):
            for hijo in self.local_declar:
                if hijo is not None:
                    hijo1 = hijo.traducir(diccionario)
                    txt += str(id) + " -> " + str(hijo1) + "\n\t"
        else:
            if self.local_declar is not None:
                hijo1 = self.local_declar.traducir(diccionario)
                txt += id + "->" + hijo1 + "\n\t"

        if isinstance(self.statement_list, list):
            for hijo in self.statement_list:
                if hijo is not None:
                    hijo1 = hijo.traducir(diccionario)
                    txt += str(id) + " -> " + str(hijo1) + "\n\t"
        else:
            if self.statement_list is not None:
                hijo2 = self.statement_list.traducir(diccionario)
                txt += id + "->" + hijo2 + "\n\t"

        if self.statement_list is not None or self.local_declar is not None:
            txt += id + "[label= " + self.name + "]" + "\n\t"
        return id



class expression_stmt():
    'expression-stmt : expression SEMICOLON | SEMICOLON'

    def __init__(self, hijo1, name):
        self.name = name
        self.hijo1 = hijo1

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()

        if self.hijo1 is None:
            txt += id + "[label=\""+ self.name +"\" ]" + "\n\t"
        else:
            hijo1 = self.hijo1.traducir(diccionar)
            txt += id + " -> " + str(hijo1) + "\n\t"
            txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class selection_stmt01():
    'selection-stmt : IF LPAREN expression RPAREN statement'

    def __init__(self, expression, statement, name):
        self.name = name
        self.expression = expression
        self.statement = statement


    def traducir(self,diccionar):
        global txt
        id = incremetarContador()
        new_nodo = nodo("nodo_if","IF",None)
        new_diccinario=diccionario()
        new_nodo.settdicc(new_diccinario)
        diccionar.addnodo(new_nodo,diccionar)
        hijo1 = self.expression.traducir(new_diccinario)
        hijo2 = self.statement.traducir(new_diccinario)


        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"

        return id


class selection_stmt02():
    'selection-stmt : IF LPAREN expression RPAREN statement ELSE statement'

    def __init__(self, expression, statement1, statement2, name):
        self.name = name
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()
        new_nodo = nodo("nodo_if", "IF", None)
        new_diccinario = diccionario()
        new_nodo.settdicc(new_diccinario)
        diccionar.addnodo(new_nodo, diccionar)

        new_nodo = nodo("nodo_else", "else", None)
        new_diccinario2 = diccionario()
        new_nodo.settdicc(new_diccinario2)
        diccionar.addnodo(new_nodo, diccionar)

        hijo1 = self.expression.traducir(new_diccinario)
        hijo2 = self.statement1.traducir(new_diccinario)

        hijo3 = self.statement2.traducir(new_diccinario2)

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"
        txt += id + " -> " + hijo1 + "\n\t"
        txt += id + " -> " + hijo2 + "\n\t"
        txt += id + " -> " + hijo3 + "\n\t"
        return id


class iteration_stmt():
    'iteration-stmt : WHILE LPAREN expression RPAREN statement'

    def __init__(self, expresion, statement, name):
        self.name = name
        self.expresion = expresion
        self.statement = statement

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()

        new_nodo = nodo("nodo_while", "WHILE", None)
        new_diccinario = diccionario()
        new_nodo.settdicc(new_diccinario)

        diccionar.addnodo(new_nodo, diccionar)
        expresion = self.expresion.traducir(new_diccinario)
        statement = self.statement.traducir(new_diccinario)

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"
        txt += id + " -> " + expresion + "\n\t"
        txt += id + " -> " + statement + "\n\t"
        return id


class return_stmt():
    'return-stmt : RETURN expression SEMICOLON'

    def __init__(self, expresion, name):
        self.name = name
        self.expresion = expresion

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()
        if self.expresion is not None:
            expresion = self.expresion.traducir(diccionar)
            txt += id + " -> " + expresion + "\n\t"

        txt += id + "[label= " + self.name + "]" + "\n\t"
        return id


class expression01():
    'expression : var ASSIGN expression'

    def __init__(self, var, expression, name):
        self.name = name
        self.var = var
        self.expression = expression

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()

        var = self.var.traducir(diccionar)
        expression = self.expression.traducir(diccionar)

        txt += id + "[label= \" " + self.name + "\" ]" + "\n\t"
        txt += id + " -> " + var + "\n\t"
        txt += id + " -> " + expression + "\n\t"

        return id


class var01():
    'var : ID'

    def __init__(self, var, expresion, name):
        self.name = name
        self.var = var
        self.expresion = expresion

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()

        txt += id + "[label= \"" + self.name + str(self.var) + "\"]" + "\n\t"
        # txt += id + " -> " + hijo1 + "\n\t"
        if self.expresion is not None:
            if isinstance(self.expresion, list):
                for e in self.expresion:
                    expresion = e.traducir()
                    txt += id + " -> " + str(expresion) + "\n\t"
            else:
                expresion = self.expresion.traducir(diccionar)
                txt += id + " -> " + expresion + "\n\t"

        return id


class binOP():
    'simple-expression : additive-expression relop additive-expression'

    def __init__(self, term1, op, term2, name):
        self.name = name
        self.term1 = term1
        self.op = op
        self.term2 = term2

    def traducir(self,diccionar):

        global txt
        id = incremetarContador()

        term1 = self.term1.traducir(diccionar)
        term2 = self.term2.traducir(diccionar)

        txt += id + "[label= \" " + self.name + " " + str(self.op) + " \" ]" + "\n\t"
        txt += id + " -> " + term1 + "\n\t"
        txt += id + " -> " + term2 + "\n\t"
        return id


class call():
    'call : ID LPAREN args RPAREN'

    def __init__(self, ID, ARGS, name):
        self.name = name
        self.ID = ID
        self.ARGS = ARGS

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()
        if(self.ARGS is not None) :
            ARGS = self.ARGS.traducir(diccionar)

            txt += id + "[label= \"" + self.name + ": " + self.ID + "\"]" + "\n\t"
            txt += id + " -> " + ARGS + "\n\t"

        return id


class num():
    def __init__(self, name):
        self.name = name

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()

        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id


class ID():
    def __init__(self, name):
        self.name = name

    def traducir(self,diccionar):
        global txt
        id = incremetarContador()
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id

def gettabla():
    return tabla_simbolo
