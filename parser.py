#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.yacc as yacc
import os
from scanner import tokens, cadena
import codecs
import sys
from AST import *

precedence = (
    ('right', 'ELSE', 'IF', 'INT', 'VOID', 'RETURN', 'WHILE'),
    ('right', 'ID'),
    ('right', 'ASSIGN'),
    ('left', 'UNEQUAL'),
    ('left', 'LESS', 'MUCHSMALLER', 'GREATER', 'MUCHGREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
)


def p_program(p):
    'program : declaration-list'
    p[0] = program(p[1], "program")


def p_declaration_list01(p):
    'declaration-list : declaration-list declaration'
    p[0] = declaration_list01(p[1], p[2], "declaration_list01")


def p_declaration_list02(p):
    'declaration-list : declaration'
    p[0] = declaration_list02(p[1], "declaration_list02")


def p_declaration01(p):
    'declaration : var-declaration'
    p[0] = declaration01(p[1], "declaration01")


def p_declaration02(p):
    'declaration : fun-declaration'
    p[0] = declaration02(p[1], "declaration02")


def p_var_declaration01(p):
    'var-declaration : type-specifier ID SEMICOLON'
    p[0] = var_declaration01(p[1], ID(p[2]), "var_declaration01")


def p_var_declaration02(p):
    'var-declaration : type-specifier ID LSQUAREBRACKET NUM RSQUAREBRACKET SEMICOLON'
    p[0] = var_declaration02(p[1], ID(p[2]),num(p[4]), "var_declaration02")


def p_type_specifier01(p):
    'type-specifier : INT'
    p[0] = type_specifier01(INT(p[1]), "specifier01")


def p_type_specifier02(p):
    'type-specifier : VOID'
    p[0] = type_specifier02(VOID(p[1]), "specifier01")

def p_fun_declaration(p):
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'
    p[0] = fun_declaration(p[1], ID(p[2]), p[4], p[6], "fun_declaration")


def p_params01(p):
    'params : param-list'
    p[0] = params01(p[1], "params01")


def p_params02(p):
    'params : VOID'
    p[0]=VOID(p[1])

def p_param_list01(p):
    'param-list : param-list COMMA param'
    p[0] = param_list01(p[1], p[3], "param_list01")


def p_param_list02(p):
    'param-list :  param'
    p[0] = param_list02(p[1],"param_list02")


def p_param01(p):
    'param : type-specifier ID'
    p[0] = param01(p[1], ID(p[2]), "param01")

def p_param02(p):
    'param : type-specifier ID LSQUAREBRACKET RSQUAREBRACKET'
    p[0] = param02(p[1], ID(p[2]), "param02")

def p_compound_stmt(p):
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'
    p[0] = compound_stmt(p[2], p[3], "compound_stmt")

def p_local_declarations01(p):
    'local-declarations : local-declarations var-declaration'
    p[0] = local_declarations01(p[1], p[2], "local_declarations01")

def p_local_declarations02(p):
    'local-declarations : empty'
    p[0] = Null()

def p_statement_list01(p):
    'statement-list : statement-list statement'
    p[0] = statement_list01(p[1], p[2], "statement_list01")

def p_statement_list02(p):
    'statement-list : empty'
    p[0] = Null()

def p_statement01(p):
    'statement : expression-stmt'
    p[0] = statement01(p[1], "statement01")

def p_statement02(p):
    'statement : compound-stmt'
    p[0] = statement02(p[1], "statement02")

def p_statement03(p):
    'statement : selection-stmt'
    p[0] = statement03(p[1], "statement03")

def p_statement04(p):
    'statement : iteration-stmt'
    p[0] = statement04(p[1], "statement04")

def p_statement05(p):
    'statement : return-stmt'
    p[0] = statement05(p[1], "statement05")

def p_expression_stmt01(p):
    'expression-stmt : expression SEMICOLON'
    p[0] = expression_stmt01(p[1], "expression_stmt01")

def p_expression_stmt02(p):
    'expression-stmt : SEMICOLON'


def p_selection_stmt01(p):
    'selection-stmt : IF LPAREN expression RPAREN statement'
    p[0] = selection_stmt01(IF(p[1]),p[3], p[5], "selection_stmt01")

def p_selection_stmt02(p):
    'selection-stmt : IF LPAREN expression RPAREN statement ELSE statement'
    p[0] = selection_stmt02(IF(p[1]),p[3], p[5],p[7],"selection_stmt02")

def p_iteration_stmt(p):
    'iteration-stmt : WHILE LPAREN expression RPAREN statement'
    p[0] = iteration_stmt(p[3], p[5], "iteration_stmt")

def p_return_stmt01(p):
    'return-stmt : RETURN SEMICOLON'


def p_return_stmt02(p):
    'return-stmt : RETURN expression SEMICOLON'
    p[0] = return_stmt02(p[2], "return_stmt02")

def p_expression01(p):
    'expression : var ASSIGN expression'
    p[0] = expression01(p[1], ASSIGN(p[2]), p[3], "expression01")

def p_expression02(p):
    'expression : simple-expression'
    p[0] = expression02(p[1], "expression02")

def p_var01(p):
    'var : ID '
    p[0] = var01(ID(p[1]), "var01")

def p_var02(p):
    'var : ID LSQUAREBRACKET expression RSQUAREBRACKET'
    p[0] = var02(ID(p[1]), p[3], "var02")

def p_simple_expression01(p):
    'simple-expression : additive-expression relop additive-expression'
    p[0] = simple_expression01(p[1],p[2], p[3], "simple_expression01")

def p_simple_expression02(p):
    'simple-expression : additive-expression'
    p[0] = simple_expression02(p[1], "simple_expression02")
def p_relop01(p):
    'relop : MUCHSMALLER'
    p[0] = relop01(MUCHSMALLER(p[1]), "relop01")

def p_relop02(p):
    'relop : LESS'
    p[0] = relop02(LESS(p[1]), "relop02")

def p_relop03(p):
    'relop : GREATER'
    p[0] = relop03(GREATER(p[1]), "relop03")


def p_relop04(p):
    'relop : MUCHGREATER'
    p[0] = relop04(MUCHGREATER(p[1]), "relop04")

def p_relop05(p):
    'relop : EQUAL'
    p[0] = relop05(EQUAL(p[1]), "relop05")


def p_relop06(p):
    'relop : UNEQUAL'
    p[0] = relop06(UNEQUAL(p[1]), "relop06")


def p_additive_expression01(p):
    'additive-expression : additive-expression addop term'
    p[0] = additive_expression01(p[1],p[2],p[3],"additive_expression01")

def p_additive_expression02(p):
    'additive-expression : term'
    p[0] = additive_expression02(p[1],"additive_expression02")

def p_addop01(p):
    'addop : PLUS'
    p[0] = addop01(p[1], "addop01")

def p_addop02(p):
    'addop :  MINUS'
    p[0] = addop02(p[1], "addop02")

def p_term01(p):
    'term : term mulop factor'
    p[0] = term01(p[1], p[2], p[3], "term01")

def p_term02(p):
    'term : factor'
    p[0] = term02(p[1], "term02")

def p_mulop01(p):
    'mulop : TIMES'
    p[0] = mulop01(TIMES(p[1]), "mulop01")

def p_mulop02(p):
    'mulop : DIVIDE'
    p[0] = mulop02(DIVIDE(p[1]), "mulop02")


def p_factor01(p):
    'factor :  LPAREN expression RPAREN'
    p[0] = factor01(p[2], "factor01")

def p_factor02(p):
    'factor : var'
    p[0] = factor02(p[1], "factor02")

def p_factor03(p):
    'factor : call'
    p[0] = factor03(p[1], "factor03")

def p_factor04(p):
    'factor : NUM'
    p[0] = factor04(num(p[1]), "factor04")

def p_call(p):
    'call : ID LPAREN args RPAREN'
    p[0] = call(ID(p[1]),p[3], "call")

def p_args01(p):
    'args : arg-list'
    p[0] = args01(p[1], "args01")

def p_args02(p):
    'args : empty'
    p[0] = Null()

def p_arg_list01(p):
    'arg-list : arg-list COMMA expression'
    p[0]=arg_list01(p[1],p[3], "arg_list01")

def p_arg_list02(p):
    'arg-list : expression'
    p[0] = arg_list02(p[1], "arg_list02")

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Error de sintaxis!", p)


def traducir(result):
    graphFile = open('graphviztrhee.vz', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print "El programa traducido se guardo en \"graphviztrhee.vz\""


parser = yacc.yacc()

result = parser.parse(cadena)  # Use raw_input on Python 2


traducir(result)