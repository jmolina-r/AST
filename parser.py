#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc
import re
import os
from scanner import tokens, cadena
import codecs
import sys
from diccionario import *
from AST import *


def p_program(p):
    'program : declaration-list'
    p[0] = program(p[1], "program")


def p_declaration_list01(p):
    '''declaration-list : declaration-list declaration
                          | declaration'''
    # p[0] = declaration_list01(p[1], p[2], "declaration_list01")
    if len(p) == 3:
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[2], list):
            p[0].extend(p[2])
        else:
            p[0].extend([p[2]])
    else:
        p[0] = p[1]


def p_declaration01(p):
    'declaration : var-declaration'
    p[0] = p[1]


def p_declaration02(p):
    'declaration : fun-declaration'
    p[0] = p[1]


def p_var_declaration01(p):
    'var-declaration : type-specifier ID SEMICOLON'
    p[0] = var_declaration01(p[1], p[2], None, "var_declaration01")


def p_var_declaration02(p):
    'var-declaration : type-specifier ID LBRACE NUM RBRACE SEMICOLON'
    p[0] = var_declaration01(p[1], p[2], p[4], "var_declaration02")


def p_type_specifier01(p):
    'type-specifier : INT'
    p[0] = p[1]


def p_type_specifier02(p):
    'type-specifier : VOID'
    p[0] = p[1]


def p_fun_declaration(p):
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'
    p[0] = fun_declaration(p[1], p[2], p[4], p[6], "Funcion:")


def p_params01(p):
    'params : param-list'
    p[0] = p[1]


def p_params02(p):
    'params : VOID'
    p[0] = p[1]


def p_param_list01(p):
    '''param-list : param-list COMMA param
    | param'''
    # p[0] = param_list01(p[1], p[3], "param_list01")
    if len(p) == 4:
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[3], list):
            p[0].extend(p[3])
        else:
            p[0].extend([p[3]])
    else:
        p[0] = p[1]


def p_param01(p):
    'param : type-specifier ID'
    p[0] = param01(p[1], p[2], False, "parametro: ")


def p_param02(p):
    'param : type-specifier ID LBRACE RBRACE'
    p[0] = param01(p[1], p[2], True, "parametro: ")


def p_compound_stmt(p):
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'
    p[0] = compound_stmt(p[2], p[3], "compound_stmt")


def p_local_declarations01(p):
    '''local-declarations : local-declarations var-declaration
                            | empty'''
    if len(p) == 3:
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[2], list):
            p[0].extend(p[2])
        else:
            p[0].extend([p[2]])
    else:
        p[0] = None


def p_statement_list01(p):
    '''statement-list : statement-list statement
                        | empty'''

    if len(p) == 3:
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[2], list):
            p[0].extend(p[2])
        else:
            p[0].extend([p[2]])
    else:
        p[0] = None


def p_statement01(p):
    'statement : expression-stmt'
    p[0] = p[1]


def p_statement02(p):
    'statement : compound-stmt'
    p[0] = p[1]


def p_statement03(p):
    'statement : selection-stmt'
    p[0] = p[1]


def p_statement04(p):
    'statement : iteration-stmt'
    p[0] = p[1]


def p_statement05(p):
    'statement : return-stmt'
    p[0] = p[1]


def p_expression_stmt01(p):
    'expression-stmt : expression SEMICOLON'
    p[0] = expression_stmt(p[1], 'Expresion')


def p_expression_stmt02(p):
    'expression-stmt : SEMICOLON'
    p[0] = expression_stmt(None, "e")


def p_selection_stmt01(p):
    'selection-stmt : IF LPAREN expression RPAREN statement'
    p[0] = selection_stmt01(p[3], p[5], "IF")


def p_selection_stmt02(p):
    'selection-stmt : IF LPAREN expression RPAREN statement ELSE statement'
    p[0] = selection_stmt02(p[3], p[5], p[7], "IF-ELSE")


def p_iteration_stmt(p):
    'iteration-stmt : WHILE LPAREN expression RPAREN statement'
    p[0] = iteration_stmt(p[3], p[5], "WHILE: ")


def p_return_stmt01(p):
    'return-stmt : RETURN SEMICOLON'
    p[0] = return_stmt(None, "RETURN")


def p_return_stmt02(p):
    'return-stmt : RETURN expression SEMICOLON'
    p[0] = return_stmt(p[2], "RETURN")


def p_expression01(p):
    'expression : var ASSIGN expression'
    p[0] = expression01(p[1], p[3], "ASSIGN")


def p_expression02(p):
    'expression : simple-expression'
    p[0] = p[1]


def p_var01(p):
    'var : ID '
    p[0] = var01(p[1], None, "var: ")


def p_var02(p):
    'var : ID LBRACE expression RBRACE'
    p[0] = var01(p[1], p[3], "var: ")


def p_simple_expression01(p):
    'simple-expression : additive-expression relop additive-expression'
    p[0] = binOP(p[1], p[2], p[3], "binop")


def p_simple_expression02(p):
    'simple-expression : additive-expression'
    p[0] = p[1]


def p_relop01(p):
    'relop : MUCHSMALLER'
    p[0] = p[1]


def p_relop02(p):
    'relop : LESS'
    p[0] = p[1]


def p_relop03(p):
    'relop : GREATER'
    p[0] = p[1]


def p_relop04(p):
    'relop : MUCHGREATER'
    p[0] = p[1]


def p_relop05(p):
    'relop : EQUAL'
    p[0] = p[1]


def p_relop06(p):
    'relop : UNEQUAL'
    p[0] = p[1]


def p_additive_expression01(p):
    '''additive-expression : additive-expression addop term
                            | term'''
    # p[0] = binOP(p[1], p[2], p[3], "BinOP")
    if len(p) == 4:
        p[0] = binOP(p[1], p[2], p[3], "BinOP")

    else:
        p[0] = p[1]


def p_addop01(p):
    'addop : PLUS'
    p[0] = p[1]


def p_addop02(p):
    'addop :  MINUS'
    p[0] = p[1]


def p_term01(p):
    'term : term mulop factor'
    p[0] = binOP(p[1], p[2], p[3], "BinOp")


def p_term02(p):
    'term : factor'
    p[0] = p[1]


def p_mulop01(p):
    'mulop : TIMES'
    p[0] = p[1]


def p_mulop02(p):
    'mulop : DIVIDE'
    p[0] = p[1]


def p_factor01(p):
    'factor :  LPAREN expression RPAREN'
    p[0] = p[2]


def p_factor02(p):
    'factor : var'
    p[0] = p[1]


def p_factor03(p):
    'factor : call'
    p[0] = p[1]


def p_factor04(p):
    'factor : NUM'
    p[0] = num(p[1])


def p_call(p):
    'call : ID LPAREN args RPAREN'
    p[0] = call(p[1], p[3], "call")


def p_args01(p):
    'args : arg-list'
    p[0] = p[1]


def p_args02(p):
    'args : empty'
    p[0] = None


def p_arg_list01(p):
    '''arg-list : arg-list COMMA expression
                | expression'''
    # p[0] = arg_list01(p[1], p[3], "arg_list01")
    if len(p) == 4:
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]

        if isinstance(p[3], list):
            p[0].extend(p[3])
        else:
            p[0].extend([p[3]])
    else:
        p[0] = p[1]


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Error de sintaxis!", p)


def traducir(result):
    graphFile = open('graphviztrhee.vz', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print "El AST abstracto se guardo en \"graphviztrhee.vz\"\n"


def check_def_var(tabla_simbolo):
    if len(tabla_simbolo.getnodos()) != 0:
        lista_nodos = tabla_simbolo.getnodos()
        for nodo in lista_nodos:
            dato = nodo.getid()
            comparacion = 0

            # compara el identidicador con las variables de su ambiente
            for i in lista_nodos:
                if dato == i.getid() and dato != "IF" and dato != "WHILE" and dato != "ELSE":
                    comparacion = comparacion + 1
            # si se encuentra mas de una vez el id objetivo (variable), se imprime aviso
            if comparacion > 1 and nodo.getdicc() is None:
                print "ERROR: Variable" + nodo.gettipo() + " " + nodo.getid() + " " + "Duplicada"

            # llamado recursivo a nodo que contenga un diccionario asociado
            if nodo.getdicc() is not None:
                check_def_var(nodo.getdicc())

def check_def_funcion(tabla_simbolo):
    nodos = tabla_simbolo.getnodos()
    lista_funcion =[]

    # se seleccionan los nodos funciones
    for nodo in nodos :
        if nodo.getdicc() is not None:
            #print "funcion encontrada.."
            lista_funcion.append(nodo)

    # se verifica tipo e identificador por cada funcion
    for n in lista_funcion:
        nod = n
        contador = 0
        #comparacion con las otras funciones
        for i in lista_funcion:
            temp = i
            #print temp.gettipo()
            #funcion con id y tipo identicos
            if nod.getid()==temp.getid() and nod.gettipo()==temp.gettipo():

                contador=contador+1
                if contador==2:
                    #print "iguales"
                    lista1 = nod.getdicc().getparams()
                    lista2 = temp.getdicc().getparams()

                    #misma cantidad de parametros
                    print len(lista1)
                    if len(lista1) == len(lista2):
                        match = 0
                        #comparación de tipos:
                        for x in range(len(lista1)):
                            print x
                            print lista1[x].gettipo()
                            print lista2[x].gettipo()
                            if lista1[x].gettipo() ==lista2[x].gettipo():
                                match=match+1
                        #print match
                        if(match == len(lista1)):
                            print "ERROR: Funcion "+i.getid()




parser = yacc.yacc()
result = parser.parse(cadena, debug=0)

# se imprime AST Abstracto
traducir(result)

# Se obtiene la tabla de simbolos
tabla_sim = gettabla()
print "Tabla de simbolos construida...\n"
# lista_t=tabla_sim.getnodos()
# for x in lista_t:
#    print x.gettipo()+x.getid()
#    if x.getdicc()is not None:
#        print "NUEVO DICCIONARIO CREADO"
#        dic = x.getdicc()
#        list_newdic=dic.getnodos()
#        for y in list_newdic:
#            print y.gettipo()+y.getid()
#            if y.getdicc() is not None:
#                print "NUEVO DICCIONARIO CREADO2"
#                dic2 = y.getdicc()
#                list2_dic = dic2.getnodos()
#                for a in list2_dic:
#                    print a.gettipo()

# se verifica Identificador de variable duplicado
print "Verificando Identificadores de variables duplicado..."
check_def_var(tabla_sim)
print "Check"
#check_def_funcion(tabla_sim)

