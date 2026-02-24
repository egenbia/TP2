#Comando para limpar a tela na execução
import os
os.system("cls")
10
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    divisao = num1 / num2
    print(f"Resultado: {divisao}")
elif num2 < num1:
    divisao = num2 / num1
    print(f"Resultado: {divisao}")
elif num1 == num2:
    print("Os números são iguais")
