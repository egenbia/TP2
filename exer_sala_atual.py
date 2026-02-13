sal = float(input("Digite o seu salário atual: "))
pc = float(input("Digite a porcentagem de aumento: "))

ns = (sal*pc)/100+sal
print(f"Novo salário: R${ns:.2f}")