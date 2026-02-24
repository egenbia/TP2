
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import os
os.system("cls")

alt1 = float(input("Digite a 1° altura: "))
alt2 = float(input("Digite a 2° altura: "))
alt3 = float(input("Digite a 3° altura: "))

if alt1 > alt2 and alt1 > alt3:
    maior = alt1
if alt2 > alt3:
    mediana = alt2
    menor = alt3

if alt2 > alt1 and alt2 > alt3:
    maior = alt2
if alt1 > alt3:
    mediana = alt1
    menor = alt3

else: 
    if alt3 > alt1 and alt3 > alt2:
        maior = alt3
    if alt2 > alt1:
        mediana = alt2
        menor = alt1

print(f"\n Maior: {maior} \n Mediana: {mediana} \n Menor: {menor}")