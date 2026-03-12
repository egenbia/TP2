from Matematica import Matematica

class Principal:
    @staticmethod
    def main():
        mat = Matematica()
        mat.inserirNotas()
        mat.calcularMedia()
        mat.mostrarNomeMedia()

if __name__ == "__main__":
    Principal.main()