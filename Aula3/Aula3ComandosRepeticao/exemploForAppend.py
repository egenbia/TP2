import os
os.system("cls")

# exemplo for Append para adicionar os valores a lista
numeros=[]
for i in range(1,5):
    n = int(input(f"Digite o {i}° número da lista: "))
    numeros.append(n)

print("Números digitados: ")
for i in numeros:
    print(i)