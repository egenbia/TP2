import os 
os.system("cls")
opc = int(input("\n 1-Tensão \n 2-Resistência \n 3-Corrente \n Escolha a opção: "))

match opc:
    case 1:
        U = int(input("Digite a tensão: "))
        R = int(input("Digite a resistencia: "))
        i = int(input("Digite a corrente: "))
        volt = U = R * i
        print(f"Resultado: {volt} volts")
    case 2:
        U = int(input("Digite a tensão: "))
        R = int(input("Digite a resistencia: "))
        i = int(input("Digite a corrente: "))
        ohm = R = U / i 
        print(f"Resultado: {ohm} ohms")
    case 3:
        U = int(input("Digite a tensão: "))
        R = int(input("Digite a resistencia: "))
        i = int(input("Digite a corrente: "))
        ampere = i = U / R
        print(f"Resultado: {ampere} ampéres")