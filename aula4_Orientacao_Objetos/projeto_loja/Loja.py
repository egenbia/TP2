class Loja: 
    def __init__(self):
        self.__razao = ""
        self.__cpf = ""
        self.__valor = 0.0
        self.__qtd = 0
        self.__total = 0.0

    def getRazao(self):
        return self.__razao
    def setRazao(self,razao):
        self.__razao = razao

    def getCpf(self):
        return self.__cpf
    def setCpf(self,cpf):
        self.__cpf = cpf

    def getValor(self):
        return self.__valor
    def setValor(self,valor):
        self.__valor = valor
    
    def getQtd(self):
        return self.__qtd
    def setQtd(self,qtd):
        self.__qtd = qtd

    def getTotal(self):
        return self.__total
    def setTotal(self,total):
        self.__total = total

    def inserirDados(self):
        print("== INSERIR DADOS ==")
        self.setRazao(input("Razão: "))
        self.setCpf(input("Cpf: "))
        self.setValor(float(input("Valor: ")))
        self.setQtd(int(input("Quantidade: ")))

    def mostrarDados(self):
        print("== DADOS ==")
        print("Razão: ", self.getRazao())
        print("Cpf: ", self.getCpf())
        print("Valor: ", self.getValor())
        print("Quantidade: ", self.getQtd())

    def total(self):
        return self.__qtd * self.__valor