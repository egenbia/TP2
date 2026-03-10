class Pessoa: 

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    #método calcular idade
    def calcularIdade(self):
        anoatual = int(input("Digite o ano atual: "))
        return anoatual - self.idade

#instanciar objeto da classe Oessoa
p = Pessoa('Luiz', 25)
pe = Pessoa('Igor', 20)
print(p.calcularIdade()) 
print(f"Você, {pe.nome} nasceu em {pe.calcularIdade()}") 