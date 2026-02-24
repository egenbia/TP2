nome = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade comprada: "))
unit = float(input("Digite o preço unitário do produto: "))

total = qtd * unit
print(f"Total a pagar: {total} no produto: {nome}")