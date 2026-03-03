import os
os.system("cls")

#exemplo for utilizando Range, para somar os valore da sequência

total =0
for i in range(1,101):
    # 1 < 101 - não considera o ultimo numero
    # total = total + 1
    total += i
print(f"Soma total: {total}")