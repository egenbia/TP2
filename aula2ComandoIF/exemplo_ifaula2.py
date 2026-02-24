#Exemplo Estrutura condicional IF - Média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nome = input("Digite seu nome: ")
media = (nota1 + nota2)/2

#Comado IF
if media > 6.0:
    print(f"Aluno Aprovado!, a média é: {media:.2f}") #Se não der tab da erro
    #f para adicionar a string {media}
elif media > 5.0 and media < 6.0: #elif é o ELSE IF
    print(f"Aluno de exame, a média é: {media}")
else: #Se esquecer : no if ou no else dá erro
    print(f"Aluno Reprovado, a média é: {media:.2f}")