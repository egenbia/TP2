class Contato:
    def __init__(self):
        self.__nome = ""
        self.__tel = ""
        self.__end = ""
        self.__cid = ""

    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome

    def getTel(self):
        return self.__tel
    def setTel(self,tel):
        self.__tel = tel

    def getEnd(self):
        return self.__end
    def setEnd(self, end):
        self.__end = end

    def getCid(self):
        return self.__cid
    def setCid(self,cid):
        self.__cid = cid

    def cadastrarDados(self):
        print("== CADASTRO ==")
        self.setNome(input("Nome: "))
        self.setTel(input("Telefone: "))
        self.setEnd(input("Endereço: "))
        self.setCid(input("Cidade: "))

    def mostrarDados(self):
        print("== MOSTRAR ==")
        print("Nome: ", self.getNome())
        print("Telefone: ", self.getTel())
        print("Endereço: ", self.getEnd())
        print("Cidade: ", self.getCid())
