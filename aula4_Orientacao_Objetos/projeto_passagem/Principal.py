import os
os.system("cls")

from Passagem import Passagem

class Principal:
    @staticmethod
    def main():
     p = Passagem()
     p.cadastrarPassageiro()
     p.cadastrarPassagem()
     p.mostrarPassageiro()
     p.mostrarPassagem()

if __name__ == "__main__":
   Principal.main()