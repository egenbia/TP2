import os
os.system("cls")

num = int(input("Digite um número: "))

if num % 2 == 0:
    quad = num ** 2
    print(f"Número par, o quadrado é: {quad}")
else:
    cubo = num ** 3
    print(f"Número ímpar, o cubo é: {cubo}")