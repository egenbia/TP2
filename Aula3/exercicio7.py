import os 
os.system("cls")

ini = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

count = ini
while count < fim:
    count += 1
    res = count * 4
    print(f"4 * {count} = {res}")