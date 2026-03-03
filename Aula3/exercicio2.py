import os
os.system('cls')

indice = int(input("Digite o índice de poluição: "))

match indice:
    case 0 | 1 | 2:
        print("Aceitável")
    case 3 | 4 | 5:
        print("Suspender Atividades - Grupo I")
    case 6 | 7:
        print("Suspender Atividades - Grupo II")
    case _:
        print("Suspender Atividade de todos os grupos")