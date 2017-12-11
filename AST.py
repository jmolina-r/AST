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
                print type(hijo)
                txt += str(id) +" -> " + str(hijo1) + "\n\t"
        else:
            print "hola"
            hijo1=self.hijo1.traducir()
            txt += id + "->" + hijo1 + "\n\t"

        txt += id + "[label= " + self.name + "]" + "\n\t"
        #txt += id + "->" + hijo1 + "\n\t"

        return "digraph G {\n\t" + txt + "}"


class var_declaration01(nodo):
    'var-declaration : type-specifier ID SEMICOLON'

    def __init__(self, type_var, ID, NUM, name):
        self.name = name
        self.type_var = type_var
        self.ID = ID
        self.NUM =NUM

    def traducir(self):
        global txt
        id = incremetarContador()
        #hijo1 = self.type2.traducir()
        #hijo2 = self.hijo2.traducir()

        if self.NUM is not None:
            txt += id + "[label= \" "+ self.name + " " + self.type_var +" "+ self.ID +" ["+str(self.NUM) +"]\" ]" + "\n\t"
        else:
            txt += id + "[label= \" "+ self.name + " " + self.type_var + " " + self.ID +  "\" ]" + "\n\t"
        #txt += id + " -> " + hijo1 + "\n\t"
        #txt += id + " -> " + hijo2 + "\n\t"

        return id



class fun_declaration(nodo):
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'

    def __init__(self, type_var, ID, params, compound_stmt,name):
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
                txt += str(id) +" -> " + str(idp) + "\n\t"
        else:
            print "no lista"
            if self.params == "void":
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
            else:
                idp=self.params.traducir()
                txt += id + "[label= \"" + self.name + " " + self.type_var + " " + self.ID + "\"]" + "\n\t"
                txt += id + "->" + str(idp) + "\n\t"

        txt += id + " -> " + compound_stmt + "\n\t"

        return id


class param01(nodo):
    'param : type-specifier ID'

    def __init__(self, var_type,ID,array, name):
        self.name = name
        self.var_type= var_type
        self.ID =ID
        self.array = array

    def traducir(self):
        global txt
        id = incremetarContador()
        if self.array == False:
            txt += id + "[label= \" " + self.name +" "+self.var_type+" "+self.ID+"\"]" + "\n\t"
        else:
            txt += id + "[label= \" " + self.name +" "+ self.var_type+" "+ self.ID +"["+"]\"]" + "\n\t"

        return id




class compound_stmt(nodo):
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'

    def __init__(self, local_declar,statement_list,name):
        self.name = name
        self.local_declar = local_declar
        self.statement_list = statement_list

    def traducir(self):
        global txt
        id = incremetarContador()

        if isinstance(self.local_declar, list):
            for hijo in self.local_declar:
                hijo1 = hijo.traducir()
                txt += str(id) +" -> " + str(hijo1) + "\n\t"
        else:
            hijo1=self.local_declar.traducir()
            txt += id + "->" + hijo1 + "\n\t"

        if isinstance(self.statement_list, list):
            print self.statement_list
            for hijo in self.statement_list:
                hijo1 = hijo.traducir()
                txt += str(id) +" -> " + str(hijo1) + "\n\t"
        else:
            print "stament"
            hijo2=self.statement_list.traducir()
            txt += id + "->" + hijo2 + "\n\t"

        txt += id + "[label= " + self.name + "]" + "\n\t"

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
        if self.hijo2 ==";":
            hijo1 = self.hijo1.traducir()
            #hijo2 = self.hijo2.traducir()
            txt += id + "[label= " + self.name + "]" + "\n\t"
            txt += id + " -> " + hijo1 + "\n\t"
            #txt += id + " -> " + hijo2 + "\n\t"
        else:
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

    def __init__(self, expresion, statement, name):
        self.name = name
        self.expresion = expresion
        self.statement = statement


    def traducir(self):
        global txt
        id = incremetarContador()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        if isinstance(self.statement,list):
            print 'lista stamentr'
        else:
            print "not list1"
        if isinstance(self.expresion,list):
            print 'lista expresion'
        else:
            expresion = self.expresion.traducir()
            txt += id + " -> " + expresion + "\n\t"
            print "not list2"


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

    def __init__(self, var, expression, name):
        self.name = name
        self.var = var
        self.expression = expression

    def traducir(self):
        global txt
        id = incremetarContador()

        var = self.var.traducir()
        expression = self.expression.traducir()

        txt += id + "[label= \" " + self.name +"\" ]" + "\n\t"
        txt += id + " -> " + var + "\n\t"
        txt += id + " -> " + expression + "\n\t"

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

    def __init__(self, var, name):
        self.name = name
        self.var = var

    def traducir(self):
        global txt
        id = incremetarContador()
        hijo1 = self.var.traducir()

        txt += id + "[label= " + self.name +str(var)+ "]" + "\n\t"
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