num = int(input("Digite um número inteiro: "))

if num > 10:
    print(num, "é maior que dez")



num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

if num1 == num2 :
    print("empate")
elif num1 > num2 :
    print(num1, "é maior que", num2)
else :
    print(num2, "é maior que", num1)




nome1 = str(input("Digite o nome do time 1: "))
num1 = int(input("Digite o número de gols dos time 1: "))
nome2 = str(input("Digite o nome do time 2: "))
num2 = int(input("Digite o número de gols dos time 2: "))

if num1 == num2 :
    print("empate")
elif num1 > num2 :
    print(nome1, "ganhou")
else :
    print(nome2, "ganhou")




dias_uteis = int(input("Digite a quantidade de dias úteis: "))
horas = float(input("Digite o total de horas trabalhadas: "))
valor = float(input("Digite o valor que recebe por hora: "))

jornada = dias_uteis * 8

hora_extra = 0

if horas > jornada:
    hora_extra = (valor / 2) + valor
    qtd_horas_extras = horas - jornada

salario = jornada * valor + (hora_extra * qtd_horas_extras)
print("O trabalhador receberá {:.2f}".format(salario))

if hora_extra > 0:
    print("E recebeu {:.2f} relativo às horas-extras".format(hora_extra * qtd_horas_extras))





numA = int(input("Digite o número inteiro A: "))
numB = int(input("Digite o número inteiro B: "))

divisao = numA % numB

if divisao == 0:
    print (numA, "é divisível por", numB)





import math

num = int(input("Digite o número inteiro: "))

if num > 0:
    raiz = math.sqrt(num)
    print (raiz)




num = int(input("Idade: "))

if 5 <= num <= 7:
    print ("infatil")

elif 8 <= num <= 10:
    print ("Juvenil")

elif 11 <= num <= 15:
    print ("Adolescente")

elif 16 <= num <= 30:
    print ("Adulto")

elif num > 30:
    print ("Senior")





num_a = float(input("Digite 1º número: "))
num_b = float(input("Digite 2º número: "))

op = input("Operador (+-*/): ")

if op == '+':
    print("resultado", num_a + num_b)
elif op == '-':
    print("resultado", num_a - num_b)
elif op == '*':
    print("resultado", num_a * num_b)    
elif op == "/":
    if num_b != 0:
        print("resultado", num_a / num_b)    
    else:
        print("Impossível divisão por 0")
else:
    print("Operador não identificado!")




import math

a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = b * b - (4 * a * c)

if delta > 0:
    x1 = (-(b) - math.sqrt(delta)) / 2 * a
    x2 = (-(b) + math.sqrt(delta)) / 2 * a
    print("Raíz 1: ", x1)
    print("Raíz 2: ", x2)





preco = float(input("Informe o valor do produto: "))
escolha = int(input("Informe a forma de pagto: "))

if escolha == 1:
    print("10% de desconto")
    print("valor: {:.2f}".format(preco * 0.9))
elif escolha == 2:
    print("5% de desconto")
    print("valor: {:.2f}".format(preco * 0.95))
elif escolha == 3:
    print("2 vezes")    
    print("valor: {:.2f}".format(preco / 2))
elif escolha == 4:
    print("4 vezes com juros de 7%")
    print("valor: {:.2f}".format(preco * 1.07 / 4))    
else:
    print("Opção de pagamento inválida!")





media1 = float(input("Informe a média do primeiro semestre: "))
media2 = float(input("Informe a média do segundo semestre: "))
aulas = int(input("Informe o número de aulas ministradas: "))
assistidas = int(input("Informe o número de aulas assistidas: "))

if (media1 * 0.4) + (media2 * 0.6) >= 6.0 and assistidas >= aulas - (aulas * 0.3):
    print("Aprovado")
else:
    print("Reprovado")





dia = int(input("Dia: "))
mes = int(input("Mês: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Data inválida!")
elif mes == 2 and dia > 28:
    print("Data inválida!")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Data inválida!")
else:
    print("Data válida!")

ano = int(input("Ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("é bissexto!")
else:
    print("não é bissexto!")