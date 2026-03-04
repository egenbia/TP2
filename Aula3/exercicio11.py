import os
os.system('cls')

numeros=[]
for i in range(0,10):
    n=int(input(f"Digite o {i}° número: "))
    numeros.append(n)

    if n % 2 == 0:
        print(f"{i} é PAR")
    else: 
        print(f"{i} é ÍMPAR")