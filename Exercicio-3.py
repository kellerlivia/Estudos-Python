x = int(input("Digite o valor da cédula: ")) 
a = int(input("Digite o valor de uma moeda: "))
b = int(input("Digite o valor da outra moeda: "))

moedaQuantity = 1

z = x - a
y = x - b

if (x % a) == 0 or (x % b) == 0 or (z % b) == 0 or (y % a) == 0:
    if (x % a) == 0:
        print("Possível:", (x // a), "moeda(s) de", a, "e 0 moedas de", b)

    elif (x % b) == 0:
        print("Possível:", (x // b), "moeda(s) de", b, "e 0 moedas de", a)

    elif (z % b) == 0:
        print("Possível:", moedaQuantity, "moeda(s) de", a, "e", (z // b), "moeda(s) de", b)

    elif (y % a) == 0:
        print("Possível:", moedaQuantity, "moeda(s) de", b, "e", (y // a), "moeda(s) de", a)

    elif (a > b):
        while (z % b) != 0:
            z = z - a
            moedaQuantity = moedaQuantity + 1
            if z // b:
                print("Possível:", moedaQuantity, "moeda(s) de", a, "e", (z // b), "moeda(s) de", b)

    elif (b > a):
         while (y % a) != 0:
            y = y - b
            moedaQuantity = moedaQuantity + 1
            if y // a:
                print("Possível:", moedaQuantity, "moeda(s) de", b, "e", (y // a), "moeda(s) de", a)
    
else:
    print("Não é possível fazer a troca")