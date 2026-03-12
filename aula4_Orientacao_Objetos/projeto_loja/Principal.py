from Loja import Loja

class Principal: 
    @staticmethod
    def main():
     L = Loja()
     L.inserirDados()
     L.mostrarDados()
     print(f"\nValor total: {L.total()}")

if __name__ == "__main__":
    Principal.main()