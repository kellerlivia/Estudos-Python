n = int(input("Digite um inteiro positivo: "))

while n < 0:
    n = int(input("Erro! Digite um inteiro positivo: "))

soma = 0;
i = 1
while i <= n:
    soma = soma + i
    i = i + 1

print ("Valor da soma vale", soma )




resp = 's'
while resp == 's':
    n = int(input("Informe qtd de alunos: "))

    soma = 0
    contador = 0
    while contador < n:
        nota = float(input("Digite a nota: "))
        soma = soma + nota
        contador = contador + 1

    media = soma / n
    print("A média da turma foi", media)

    resp = input("Deseja fazer mais médias (s/n): ")




n = int(input("Informe qtd de alunos: "))

soma = 0
contador = 0
conta_azul = 0
conta_vermelho = 0
while contador < n:
    nota = float(input("Digite a nota: "))

    if nota >= 5:
        conta_azul = conta_azul + 1
    else:
        conta_vermelho = conta_vermelho + 1

    soma = soma + nota
    contador = contador + 1

media = soma / n
print("A média da turma foi", media)
print("Qtd de alunos que tiraram mais ou igual a 5: ", conta_azul)
print("Qtd de alunos que tiraram menos do que 5: ", conta_vermelho)




n = int(input("Informe qtd de números: "))

contador = 0
positivo = 0
negativo = 0
while contador < n:
    num = float(input("Digite o número real: "))

    if num >= 0:
        positivo = positivo + 1
    else:
        negativo = negativo + 1

    contador = contador + 1

print("Qtd de números positivos: ", positivo)
print("Qtd de números negativos: ", negativo)




