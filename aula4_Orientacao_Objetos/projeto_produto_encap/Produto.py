class Produto:
    def __init__(self):
        
        self.__nome = ""
        self.__valor = 0.0
        self.__qtd = 0

    #ENCAPSULAMENTO
    #getter nome
    def get_Nome(self):
        return self.__nome
    #setter nome
    def set_Nome(self,nome):
        self.__nome = nome

    
    def get_Valor(self):
        return self.__valor
 
    def set_Valor(self,valor):
        self.__valor = valor

    
    def get_Qtd(self):
        return self.__qtd
 
    def set_Qtd(self,qtd):
        self.__qtd = qtd

    #método cadastrar
    def cadastrarProduto(self):
        print("\n === Cadastro de Produtos === \n")
        self.set_Nome(input("Nome dp produto: "))
        self.set_Qtd(int(input("Quantidade: ")))
        self.set_Valor(float(input("Valor do produto: R$")))

    #método mostrar
    def mostrarProduto(self):
        print("\n === Dados do produto === \n")
        print("Nome do produto: ", self.get_Nome())
        print("Quantidade do produto: ", self.get_Qtd())
        print("Valor do produto: R$", self.get_Valor())

    #método calcular
    def calcular(self):
        return self.__qtd * self.__valor