class Passagem:
    def __init__(self):
        self.__nome = ""
        self.__tel = ""
        self.__rg =""
        self.__loc = ""
        self.__data = ""
        self.__hora = ""
        self.__polt = ""

    def getNome(self):
        return self.__nome
    def setNome(self,nome):
        self.__nome = nome
    
    def getTel(self):
        return self.__tel
    def setTel(self,tel):
        self.__tel = tel

    def getRg(self):
        return self.__rg
    def setRg(self,rg):
        self.__rg = rg

    def getLoc(self):
        return self.__loc
    def setLoc(self,loc):
        self.__loc = loc

    def getData(self):
        return self.__data
    def setData(self,data):
        self.__data = data

    def getHora(self):
        return self.__hora
    def setHora(self,hora):
        self.__hora = hora

    def getPolt(self):
        return self.__polt
    def setPolt(self,polt):
        self.__polt = polt

    def cadastrarPassageiro(self):
        print("\n == Dados Passageiro == \n")
        self.setNome(input("Nome: "))
        self.setTel(input("Telefone: "))
        self.setRg(input("RG: "))
       

    def mostrarPassageiro(self):
        print("\n == Dados Passageiro == \n")
        print("Nome: ", self.getNome())
        print("Telefone: ", self.getTel())
        print("RG: ", self.getRg())

    #############################################

    def cadastrarPassagem(self):
        print("== Dados Passagem == \n")
        self.setLoc(input("Local: "))
        self.setData(input("Data: "))
        self.setHora(input("Hora: "))
        self.setPolt(input("N° poltrona: "))
       

    def mostrarPassagem(self):
        print("== Dados Passagem == \n")
        print("Loc: ", self.getLoc())
        print("Data: ", self.getData())
        print("Hora: ", self.getHora())
        print("N° poltrona: ", self.getPolt())