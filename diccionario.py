
class nodo():
    def __init__(self, tipo_dato, id, valor):
        self.tipo_dato = tipo_dato
        self.id = id
        self.valor = valor
        self.padre = None
        self.dicc = None

    def getpadre(self):
        return self.padre

    def setpadre(self, new_padre):
        self.padre = new_padre

    def getdicc(self):
        return self.dicc

    def settdicc(self, tabla):
        self.dicc = tabla

    def gettipo(self):
        return self.tipo_dato
    def getid(self):
        return self.id



class diccionario():
    def __init__(self):
        self.list_nodos = []
        self.nivel = 0

        self.list_parametro=[]

    def set_nivel(self, nivel):
        self.nivel = nivel

    def addnodo(self, nodo,padre):
        nodo.setpadre(padre)
        self.list_nodos.append(nodo)

    def getnodos(self):
        return self.list_nodos
    def getparams(self):
        return self.list_parametro
    def addparams(self,parametro):
        self.list_parametro.append(parametro)


def main():
    d = diccionario()
    new_nodo = nodo('int', 'var', 45)
    new2_nodo = nodo('string', 'var2', 'hola')
    #d.addnodo(new_nodo)
    #d.addnodo(new2_nodo)

    print d
    nodos = d.getnodos()
    for n in nodos:
        print n.gettipo()


main()
