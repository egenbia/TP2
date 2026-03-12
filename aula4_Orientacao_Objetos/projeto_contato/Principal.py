from Contato import Contato

class Principal:
    @staticmethod
    def main():
     c = Contato()
     c.cadastrarDados()
     c.mostrarDados()

if __name__ == "__main__":
    Principal.main()