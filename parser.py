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
    p[0]= var_declaration01(p[1])

def p_declaration02(p):
    'declaration : fun-declaration'
    p[0] = var_declaration02(p[1])


def p_var_declaration01(p):
    'var-declaration : type-specifier ID SEMICOLON'
    p

def p_var_declaration02(p):
    'var-declaration : type-specifier ID LSQUAREBRACKET NUM RSQUAREBRACKET SEMICOLON'


def p_type_specifier01(p):
    'type-specifier : INT'


def p_type_specifier02(p):
    'type-specifier : VOID'


def p_fun_declaration(p):
    'fun-declaration : type-specifier ID LPAREN params RPAREN compound-stmt'


def p_params01(p):
    'params : param-list'


def p_params02(p):
    'params : VOID'


def p_param_list01(p):
    'param-list : param-list COMMA param'


def p_param_list02(p):
    'param-list :  param'


def p_param01(p):
    'param : type-specifier ID'


def p_param02(p):
    'param : type-specifier ID LSQUAREBRACKET  RSQUAREBRACKET'


def p_compound_stmt(p):
    'compound-stmt : LBRACE local-declarations statement-list RBRACE'


def p_local_declarations01(p):
    'local-declarations : local-declarations var-declaration'


def p_local_declarations02(p):
    'local-declarations : empty'


def p_statement_list01(p):
    'statement-list : statement-list statement'


def p_statement_list02(p):
    'statement-list : empty'


def p_statement01(p):
    'statement : expression-stmt'


def p_statement02(p):
    'statement : compound-stmt'


def p_statement03(p):
    'statement : selection-stmt'


def p_statement04(p):
    'statement : iteration-stmt'


def p_statement05(p):
    'statement : return-stmt'


def p_expression_stmt01(p):
    'expression-stmt : expression SEMICOLON'


def p_expression_stmt02(p):
    'expression-stmt : SEMICOLON'


def p_selection_stmt01(p):
    'selection-stmt : IF LPAREN expression RPAREN statement'


def p_selection_stmt02(p):
    'selection-stmt : IF LPAREN expression RPAREN statement ELSE statement'


def p_iteration_stmt(p):
    'iteration-stmt : WHILE LPAREN expression RPAREN statement'


def p_return_stmt01(p):
    'return-stmt : RETURN SEMICOLON'


def p_return_stmt02(p):
    'return-stmt : RETURN expression SEMICOLON'


def p_expression01(p):
    'expression : var ASSIGN expression'


def p_expression02(p):
    'expression : simple-expression'


def p_var01(p):
    'var : ID '


def p_var02(p):
    'var : ID LSQUAREBRACKET expression RSQUAREBRACKET'


def p_simple_expression01(p):
    'simple-expression : additive-expression relop additive-expression'


def p_simple_expression02(p):
    'simple-expression : additive-expression'


def p_relop01(p):
    'relop : MUCHSMALLER'


def p_relop02(p):
    'relop : LESS'


def p_relop03(p):
    'relop : GREATER'


def p_relop04(p):
    'relop : MUCHGREATER'


def p_relop05(p):
    'relop : EQUAL'


def p_relop06(p):
    'relop : UNEQUAL'


def p_additive_expression01(p):
    'additive-expression : additive-expression addop term'


def p_additive_expression02(p):
    'additive-expression : term'


def p_addop01(p):
    'addop : PLUS'


def p_addop02(p):
    'addop :  MINUS'


def p_term01(p):
    'term : term mulop factor'


def p_term02(p):
    'term : factor'


def p_mulop01(p):
    'mulop : TIMES'


def p_mulop02(p):
    'mulop : DIVIDE'


def p_factor01(p):
    'factor :  LPAREN expression RPAREN'


def p_factor02(p):
    'factor : var'


def p_factor03(p):
    'factor : call'


def p_factor04(p):
    'factor : NUM'


def p_call(p):
    'call : ID LPAREN args RPAREN'


def p_args01(p):
    'args : arg-list'


def p_args02(p):
    'args : empty'


def p_arg_list01(p):
    'arg-list : arg-list COMMA expression'


def p_arg_list02(p):
    'arg-list : expression'


def p_empty(p):
    'empty :'
    # pass


def p_error(p):
    print("Syntax error in input!", p)
    print("line: ", str(p.lineno))


def traducir(result):
    graphFile = open('graphviztrhee.vz', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print "El programa traducido se guardo en \"graphviztrhee.vz\""


parser = yacc.yacc()

result = parser.parse(cadena)  # Use raw_input on Python 2

#traducir(result)