import os
os.system("cls")

class produto:
    
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    #método mostrar info produtos
    def mostrar(self):
        print("Nome Produto: ", self.nome)
        print("Preço Produto: R$", self.preco)
        print("Quantidade: ", self.qtd)

    #método calcular valor total
    def calcularTotal(self):
        valor_total = self.qtd * self.preco
        print(f"O valor total é: R$ {round(valor_total,2)}")

#instanciar o objeto e chamar os métodos da classe 
prod = produto("abacate", 4.9, 5)
prod.mostrar()
prod.calcularTotal()    