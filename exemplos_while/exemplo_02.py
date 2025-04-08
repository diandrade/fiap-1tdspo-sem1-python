# Calcular a soma dos números pares de 1 até 30

soma = 0
cont = 1

while cont <= 30:
    if cont % 2 == 0:
        soma += cont
    cont += 1

print(f"A soma dos pares é {soma}")
