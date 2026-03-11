from Fornecedores import Fornecedor

class Principal:
    @staticmethod
    def main():
        forn = Fornecedor()
        forn.cadastrarFornecedor()
        forn.listarFornecedor()
        print(f"\n Finalizado!")

if __name__ == "__main__":
    Principal.main()