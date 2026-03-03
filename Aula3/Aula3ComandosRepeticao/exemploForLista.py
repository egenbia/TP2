import os
os.system('cls')

#exemplo for utilizando lista de valores pré-definida

frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for lista in frutas:
    print(lista)

buscar = 'goiaba'
frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for lista in frutas:
    if lista == buscar:
        print(f"Fruta encontrada: {buscar}")
        break #parar repetição
    else:
        print(f"Fruta não encontrada {buscar}")