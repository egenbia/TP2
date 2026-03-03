import os 
os.system('cls')

letra = input("Digite uma letra: ")
match letra.lower():
    case "a":
        print("Vogal")
    case "e":
        print("Vogal")
    case "i":
        print("Vogal")
    case "o":
        print("Vogal")
    case "u":
        print("Vogal")
    case _:
        print("Não vogal")