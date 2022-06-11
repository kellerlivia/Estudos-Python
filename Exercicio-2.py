n = int(input("Deseja ver os aumentos de quantos produtos? "))

aumento_percentual_anterior = 0
aumento_reais_anterior = 0
aumento_percentual_atual = 0
aumento_reais_atual = 0
i = 0

while i < n:
    antigo = float(input("Preço antigo: "))
    reajustado = float(input("Preço reajustado: "))

    aumento_percentual_anterior = ((reajustado - antigo) * 100) / antigo
    aumento_reais_anterior = reajustado - antigo

    if (i < 1):
       aumento_percentual_atual = aumento_percentual_anterior
       aumento_reais_atual = aumento_reais_anterior

    if aumento_percentual_anterior > aumento_percentual_atual:
        aumento_percentual_atual = aumento_percentual_anterior

    if aumento_reais_anterior > aumento_reais_atual:
        aumento_reais_atual = aumento_reais_anterior
    
    i = i + 1

print("O maior aumento porcentual foi de {:.2f}".format(aumento_percentual_atual), "%")
print("O maior aumento em reais foi de {:.2f}".format(aumento_reais_atual), "reais")