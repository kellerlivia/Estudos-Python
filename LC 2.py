nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(sobrenome, nome)



nome = input("Digite seu nome: ")
ano = int(input("Digite seu ano de nascimento: "))

diferenca = 2022 - ano

print (nome, "tem (ou terá)", int(diferenca), "anos")



numA = int(input("Num A: "))
numB = int(input("Num B: "))

soma = numA + numB
multiplicação = numA * numB
divisão = numA // numB
resto = numA % numB

print (soma, multiplicação, divisão, resto)



numX = int(input("Num X: "))
numY = int(input("Num Y: "))

potenciacao = numX ** numY

print ("X ^ Y =", potenciacao)



Raio = int(input("Num Raio: "))

perimetro = Raio * 2 * 3.141592
area = 3.141592 * Raio ** 2

print (area, perimetro)



num = int(input("Digite um numero inteiro de 0 a 99: "))

dezenas = num // 10
unidades = num % 10

print("O dígito das dezenas é", dezenas)
print("O dígito das unidades é", unidades)



X = int(input("Numero de camisas: "))
Y = int(input("Numero de calças: "))
Z = int(input("Numero de pares de sapato: "))

combinacao = X * Y * Z

print(combinacao)



preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto do produto: "))

descontoValor = preco * desconto / 100
precoNovo = preco - descontoValor

print("O valor do desconto é de" , descontoValor , "reais")
print("O preço do produto agora é" , precoNovo , "reais")

preco = int(input("Digite o preço do produto: "))
aumento = int(input("Digite o valor do aumento do produto: "))

aumentoValor = preco * aumento / 100
precoNovo = preco + aumentoValor

print("O valor do aumento é de" , aumentoValor , "reais")
print("O preço do produto agora é" , precoNovo , "reais")




distancia = float(input("Digite a distancia em metros: "))
tempo = float(input("Digite o tempo em segundos: "))

velocidade_em_ms = distancia / tempo
velocidade_em_kmh = velocidade_em_ms * 3.6

print("A velocidade em metros por segundo é" , velocidade_em_ms , "m/s")
print("A velocidade em km/h é" , velocidade_em_kmh , "km/h")



sal_old = float(input("Salário antigo: "))
sal_new = float(input("Salário novo: "))

aux = (sal_new - sal_old) * 100
aumento = aux / sal_old

print("Meu aumento foi de {:.2f}".format(aumento))



rm = int(input("Informe o rm: "))

soma = 0

resto = rm % 10
quoc = rm // 10
soma = soma + resto

resto = quoc % 10
quoc = quoc // 10
soma = soma + resto

resto = quoc % 10
quoc = quoc // 10
soma = soma + resto

resto = quoc % 10
quoc = quoc // 10
soma = soma + resto

resto = quoc % 10
quoc = quoc // 10
soma = soma + resto

print('A soma do RM:', rm, "é", soma)



nac = int(input("Nota nac: "))
am = int(input("Nota am: "))
ps = int(input("Nota ps: "))

media = (2 * nac + 3 * am + 5 * ps) / 10

print(media)



avista = int(input("Digite o valor à vista: "))

parcela = int(input("Digite o valor da parcela: "))

valorParcelas = parcela * 10
desconto = (valorParcelas - avista) * 100

valorDesconto = desconto / avista

print("O percentual de desconto é de {:.2f}".format (valorDesconto))