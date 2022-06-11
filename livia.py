print("Olá Mundo!")


numA = int(input("Num A: "))
numB = int(input("Num B: "))
numC = int(input("Num C: "))
numD = int(input("Num D: "))
numE = int(input("Num E: "))

resposta = numA + numB + numC + numD + numE

print(resposta)



base = float(input("digite o valor da base: "))
altura = float(input("digite o valor da altura: "))

area = base * altura / 2

print("O valor da area é " + str(area))



nome = " FIAP "
print ( nome * 4)



idade = 18
nome = "Lívia"
print ("Meu nome e idade", nome , idade, str("anos"))




endereco = input ("Onde você mora? ")
idade = int("18")

print(endereco, idade)



X = int(input("Numero de camisas: "))
Y = int(input("Numero de calças: "))
Z = int(input("Numero de pares de sapato: "))

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);

combinacao = X * factorial(X-1) * Y * factorial(Y-1) * Z * factorial(Z-1)

print(combinacao)



numbers = ['4', '07', '08', '2017', '364', '675']

numero_maximo = max(numbers, key=int)
print(numero_maximo)




soma = 0

num = int(input("Digite o número a ser somado: "))
soma = soma + num

num = int(input("Digite o número a ser somado: "))
soma = soma + num

num = int(input("Digite o número a ser somado: "))
soma = soma + num

num = int(input("Digite o número a ser somado: "))
soma = soma + num

num = int(input("Digite o número a ser somado: "))
soma = soma + num

num = int(input("Digite o número a ser somado: "))
soma = soma + num

num = int(input("Digite o número a ser somado: "))
soma = soma + num

print("O resultado da soma é" , soma)

media = soma / 7
print("A média é {:.2f}".format(media))



numX = int(input("Digite um número inteiro: "))

if numX % 2 == 0:
    print(numX, "é par")

else:
    print(numX, "é impar")




placarA = int(input("Gols do time A: "))
placarB = int(input("Gols do time B: "))

if placarA == placarB :
    print ("Empate")
elif placarA > placarB :
        print ("Vencedor Time A")
else:
        print ("Vencedor Time B")




num = int(input("Digite um número inteiro: "))

if num == 0 :
    print (str(num), "é igual a zero")
elif num > 0 :
        print (str(num), "é positivo")
else:
        print (str(num), "é negativo")




num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
operador = str(input("Digite um operador matemático: "))

if operador == "+" :
    print (num1 + num2)
elif operador == "/" :
    print (num1 / num2)
elif operador == "*" :
    print (num1 * num2)
elif operador == "-" :
    print (num1 - num2)



numA = int(input("Digite um número inteiro: "))
numB = int(input("Digite um número inteiro: "))
op = str(input("Digite um operador matemático: "))

soma = ( op == "+")
subtracao = ( op == "-")
multiplicacao = ( op == "*")
divisao = ( op == "/")

if soma :
    resultado = numA + numB
elif subtracao :
    resultado = numA - numB
elif multiplicacao :
    resultado = numA * numB
elif divisao :
    resultado = numA / numB

print (" Resp : {:.2f}". format (resultado))




num = int(input("Digite um inteiro positivo: "))
divisor = 1
while divisor <= num:
    if num % divisor == 0:
        print (divisor)
    divisor = divisor + 1




def aumento (valor , percentual):
    novoValor = (1 + percentual / 100) * valor
    print (novoValor)

aumento (30.00 , 15)



def divisao (a , b) :
    return a // b , a % b

res = divisao (5 , 3)
print (res)






def fatorial (n) :
    prod = 1
    while n >= 1:
        prod = prod * n
        n = n - 1

    return prod

fat = fatorial (6)
print (fat)




def decToBin (n ):
    pot = 1
    soma = 0

    while n != 0:
        resto = n % 2
        soma = soma + resto * pot
        pot = pot * 10
        n = n // 2

    return soma

resp = decToBin (8)
print (resp)




st = str(input("Digite uma palavra: "))
n = int(input("Digite um número: "))
n1 = int(input("Digite outro número: "))
n2 = int(input("Digite outro número: "))
print (st [n])
print (st [n1:n2])




st = "DONT WORRY, BE HAPPY"
outra_st = st [5:9]
tam = len (outra_st)
print (outra_st)
print (tam)





#strip: remove espaços em branco da String
#lower: converte os caracteres para minuscula
#upper: converte os caracteres para maiuscula
#replace: substitui uma substring por outra

s = "Just keep swimming"
t = s . strip ()
print (t)
t = s . lower ()
print (t)
t = s . upper ()
print (t)
t = s . replace (" swimm ", " runn ")
print (t)



s = "Lívia"
i = 0
while i < len (s ):
    print (s[i ])
    i = i + 1

for c in s:
    print (c)




for x in range (1 , 100) :
    print (x)






s = " Every journey begins with a single step "
resultado = "th" in s
print (resultado) # True
resultado = not "th" in s
print (resultado) # False