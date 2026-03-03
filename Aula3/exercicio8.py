import os
os.system('cls')

nomes = ['Maria', 'João', 'Paulo', 'Magali']
for i in nomes:
    print(i)

buscar = 'Magali'
nomes = ['Maria', 'João', 'Paulo', 'Magali']
for i in nomes:
    if i == buscar:
        print(f"{buscar} existe!")
        break
    else:
        print(f"{buscar} não encontrado")