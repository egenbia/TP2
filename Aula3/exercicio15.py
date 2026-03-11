import os
os.system("cls")

buscar = input("Digite o nome da linguagem a buscar: ")
ling = ["python","c#","Visual Basic","C++","Delphi","Cobol","Clipper","PHP","Java"]

for i in ling:
    if i == buscar:
        print(f"Linguagem encontrada: {buscar}")
        break
    else:
        print(f"{buscar} não encontrado.")

for i, ling in enumerate (ling):
    if ling == buscar:
        print(f"{ling} foi localizado na {i} posição")
   
