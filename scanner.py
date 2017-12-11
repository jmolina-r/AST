#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ply.lex as lex
import re
import codecs
import os
import sys

# lista de los nombres de los tokens

reserved = {
    'else': 'ELSE',
    'if': 'IF',
    'int': 'INT',
    'void': 'VOID',
    'return': 'RETURN',
    'while': 'WHILE'
}

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LSQUAREBRACKET',
    'RSQUAREBRACKET',
    'LESS',
    'GREATER',
    'MUCHSMALLER',
    'MUCHGREATER',
    'EQUAL',
    'UNEQUAL',
    'COMMA',
    'SEMICOLON',
    'ASSIGN',
    'MULTCOMMMENT',
    'LINECOMMENT',
    'ID',
    'NUM'
)

tokens = tokens + tuple(reserved.values())

# Reglas de las expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_LESS = r'<'
t_GREATER = r'\>'
t_MUCHSMALLER = r'\<='
t_MUCHGREATER = r'\>='
t_EQUAL = r'\=='
t_UNEQUAL = r'\<>'
t_COMMA = r','
t_SEMICOLON = r';'
t_ASSIGN = r'='

# t_MULTCOMMMENT = r'<\/(\s*|.*?)*\/>'
t_LINECOMMENT = r'(\?|!).*'

# Regla que contiene caracteres ignorados (espacios y tabs)
t_ignore = ' [\t\'\n]*'


def t_ID(t):
    r'([A-Za-z](_?[a-zA-Z0-9]+)*_?([a-z0-9])+|[a-z])|(?i)else|(?i)if|(?i)int|(?i)void|(?i)return|(?i)while'
    # El método get () devuelve el 'valor' para la 'key' dada. Si la key no está disponible en el diccionario,
    # entonces devuelve el valor predeterminado 'ID'.
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


# Regla de manejo de errores
list_error = []


def t_error(t):
    print("Caracter Ilegal, '%s'" % t.value[0])
    list_error.append(str(t.value[0]))  # agrega el valor del error a una lista
    t.lexer.skip(1)


def t_NUM(t):
    r'(0[0-9])|[1-9][0-9]+'
    t.value = int(t.value)
    t.type = 'NUM'
    return t


def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print str(cont) + ". " + file
        cont = cont + 1

    while respuesta == False:
        numArchivo = raw_input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print "Has escogido \"%s\"" % files[int(numArchivo) - 1]

    return files[int(numArchivo) - 1]


directorio = 'C:/Users/jmoli/PycharmProjects/Taller_compiladores/test_file/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

# Construir el lexer
lexer = lex.lex()

# Dar al analizador léxico algún input
lexer.input(cadena)

while True:
    tok = lexer.token()
    if not tok:
        break  # no hay mas input
    print(tok)
