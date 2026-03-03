opc = int(input("\n 1-Sacar \n 2-Extrato \n 3-Sair \n EScolha a opção: "))

match opc:
#match opc.upper(): - para string
    case 1: 
    #caso eu quisesse usar letras case "A" | "a"
        print("Você escolheu a opção sacar")
        valor = float(input("Digite o valor do saque: "))
        print(f"Sacando da sua conta ... o valor de R${valor}")
        #não precisa de break
    case 2: 
        print("Você escolheu a opção extrato")
        dias = int(input("Digite a quantidade de dias: "))
        print(f"Retirando o extrato de {dias} dias ...")
    case 3: 
        exit
    case _:
        print("Opção inválida")
