class Matematica:
    def __init__(self):
        self.__nome = ""
        self.__n1 = 0.0
        self.__n2 = 0.0
        self.__media = 0.0

    def getNome(self):
        return self.__nome
    def setNome(self,nome):
        self.__nome = nome

    def getN1(self):
        return self.__n1
    def setN1(self, n1):
        self.__n1 = n1

    def getN2(self):
        return self.__n2
    def setN2(self, n2):
        self.__n2 = n2

    def getMedia(self):
        return self.__media
    def setMedia(self, media):
        self.__media = media

    def inserirNotas(self):
        print("== INSERIR ==")
        self.setNome(input("Nome: "))
        self.setN1(float(input("Nota 1: ")))
        self.setN2(float(input("Nota 2: ")))

    def calcularMedia(self):
        return (self.__n1 + self.__n2) / 2
    
    def mostrarNomeMedia(self):
        print("Seu nome é: ", self.getNome())
        print("Sua nota é:  ", self.calcularMedia())
