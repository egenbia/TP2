#Criar Classe Carro

class Carro:
    #construtor da classe
    def __init__(self, nome): # self - que esta contruindo o contrutor da própria classe
        self.nome = nome

    # método da classe Carro
    def acelerar(self): # def - define método
        print(self.nome, "Está acelerando...")

# instâmciando o objeto car da classe Carro
car = Carro('Fusca')
print(car.nome)
car.acelerar()

c = Carro('Uno')
print(c.nome)
c.acelerar()