import os
os.system("cls")

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (M/F): ")

if sexo == "m":
    pid = (72.7*altura)-58
    print(f"Seu peso ideal é: {pid}")
if sexo == "f":
    pid = (62.1*altura)-44.7
    print(f"Seu peso ideal é: {pid}")