#importar a classe produto

from Produto import Produto

class Principal:
  @staticmethod
  def main():
    #instanciar classe Produto
    prod = Produto()
    #chamar os métodos
    prod.cadastrarProduto()
    prod.mostrarProduto()
    print(f"Valor total = {prod.calcular()}")

#define a inicialização pela classe Principal
if __name__ == "__main__":
  Principal.main()