n = int(input("Digite o número de elementos: "))

cont = 0
num_atual = 0
num_anterior = 0
i = 0

while i < n:
        num = int(input("Digite o número da sequência: "))
        num_atual = num
        if num_atual != num_anterior:
            cont = cont + 1
            num_anterior = num_atual
        i = i + 1

print("O número de segmentos é de", cont)