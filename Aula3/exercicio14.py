import os
os.system("cls")

ling = ["python","c#","Visual Basic","C++","Delphi","Cobol"]
for i in ling:
    if len(i) > 3:
        print(f"O nome da linguagem que possui mais de 3 caracteres é: {i}")

for i in ling:
    qtd = len(i)
    print(f"a linguagem {i} possui {qtd} caracteres")