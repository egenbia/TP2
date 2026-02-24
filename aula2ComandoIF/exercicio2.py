#Comando para limpar a tela na execução
import os
os.system("cls")

nome1 = input("Digite o nome da pessoa 1: ")
peso1 = float(input("Digite o peso da pessoa 1: "))

nome2 = input("Digite o nome da pessoa 2: ")
peso2 = float(input("Digite o peso da pessoa 2: "))

if peso1 > peso2:
    print(f"{nome1} é mais pesado que {nome2}.")
elif peso2 > peso1:
    print(f"{nome2} é mais pesado que {nome1}.")
elif peso1 == peso2:
    print(f"{nome1} e {nome2} tem o mesmo peso.")
