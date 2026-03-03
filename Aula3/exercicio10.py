import os
os.system("cls")

nomes=[]
for i in range(1,8):
    n = input(f"Digite o {i}° nome da lista: ")
    nomes.append(n)
print("Lista: ")
for i in nomes:
    print(i)