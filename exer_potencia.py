n1 = float(input("Digite o primeiro número: "))
exp = float(input("Digite o expoente: "))

# Potência utilizando o operador
pot = n1 ** exp
# Potência utilizando a função math
pote = pow(n1, exp) 

print(f"Resultado da potência pot: {pot}") # operador
print(f"Resultado da potência pote: {pote}") # função math