class Fornecedor: 
    def __init__(self): 

        self.__nFornecedor = ""
        self.__nProduto = ""
        self.__dProduto = ""

    def get_nFornecedor(self):
        return self.__nFornecedor
    def set_nFornecedor(self, nFornecedor):
        self.__nFornecedor = nFornecedor

    def get_nProduto(self):
        return self.__nProduto
    def set_nProduto(self, nProduto):
        self.__nProduto = nProduto

    def get_dProduto(self):
        return self.__dProduto
    def set_dProduto(self, dProduto):
        self.__dProduto = dProduto

    
    def cadastrarFornecedor(self):
        print("Cadastro de fornecedor: \n")
        self.set_nFornecedor(input("Nome do fornecedor: "))
        self.set_nProduto(input("Nome do produto: "))
        self.set_dProduto(input("Descrição do produto: "))

    def listarFornecedor(self):
        print("Lista: \n")
        print("Nome do fornecedor: ", self.get_nFornecedor())
        print("Nome do produto: ", self.get_nProduto())
        print("Descrição do produto: ", self.get_dProduto())