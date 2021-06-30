class Calculadora:
    def __init__(self):
        self.__valor_uno__ = 0
        self.__valor_dos__ = 0
        self.__resultado__ = 0

    def __sumar__(self):
        self.__resultado__ = self.__valor_uno__ + self.__valor_dos__

    def __restar__(self):
        self.__resultado__ = self.__valor_uno__ - self.__valor_dos__

    def __multiplicar__(self):
        self.__resultado__ = self.__valor_uno__ * self.__valor_dos__

    def __dividir__(self):
        self.__resultado__ = self.__valor_uno__ // self.__valor_dos__

    def operar(self, v1, v2, op):
        self.__valor_uno__ = v1
        self.__valor_dos__ = v2
        self.__operacion__ = op
        if op == "+":
            self.__sumar__()
        elif op == "-":
            self.__restar__()
        elif op == "*":
            self.__multiplicar__()
        else:
            self.__dividir__()

    def mostrar_resultado(self):
        print("%d %s %d = %d" %(self.__valor_uno__, self.__operacion__,
                                self.__valor_dos__, self.__resultado__))


if __name__ == '__main__':

    c = Calculadora()
    print(type(c))

    v1 = int(input("Ingrese el primer valor: "))
    v2 = int(input("Ingrese el segundo valor: "))
    op = input("ingrese el operador: ")
    
    c.operar(v1, v2, op)
    c.mostrar_resultado()
    
