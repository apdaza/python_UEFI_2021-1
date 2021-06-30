class Instrumento:
    def presentar(self):
        return(str(type(self)).split(".")[1][:-2])
    
    def afinar(self, nota = None):
        pass
    def tocar(self, nota = None):
        pass

class Guitarra(Instrumento):
    def afinar(self, nota = None):
        if nota is None:
            print("Afinando guitarra")
        else:
            print("Afinando guitarra en " + nota)
            
    def tocar(self, nota = None):
        if nota is None:
            print("Tocando guitarra")
        else:
            print("Tocando guitarra en " + nota)

class Bajo(Instrumento):
    def afinar(self, nota = None):
        if nota is None:
            print("Afinando bajo")
        else:
            print("Afinando bajo en " + nota)
            
    def tocar(self, nota = None):
        if nota is None:
            print("Tocando bajo")
        else:
            print("Tocando bajo en " + nota)

class Tiple(Instrumento):
    def afinar(self, nota = None):
        if nota is None:
            print("Afinando tiple")
        else:
            print("Afinando tiple en " + nota)
            
    def tocar(self, nota = None):
        if nota is None:
            print("Tocando tiple")
        else:
            print("Tocando tiple en " + nota)

class Flauta(Instrumento):
    def afinar(self, nota = None):
        if nota is None:
            print("Afinando flauta")
        else:
            print("Afinando flauta en " + nota)
            
    def tocar(self, nota = None):
        if nota is None:
            print("Tocando flauta")
        else:
            print("Tocando flauta en " + nota)            

if __name__ == '__main__':
    i = Guitarra()
    i.afinar()
    i.afinar("Do")
    i.tocar()
    i.tocar("Re")
    

