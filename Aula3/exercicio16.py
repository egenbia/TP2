import os 
os.system("cls")


count = 0 
while count <= 15:
    
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    if sexo in ("M", "m"):
        print(f"{nome} você precisa fazer o exame, pois seu sexo é masculino.")
    elif sexo in ("F", "f"):
        print(f"{nome} você não precisa fazer o exame, pois seu sexo é feminino.")
    else: 
        print("Sexo digitado incorretamente.")

    count += 1