i = 0
dentro = 0
fora = 0
for i in range(1, 11):
    valor = float(input(f"Insira um valor ({11-i} Restantes): "))
    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1
print(f"Dentro: {dentro}")
print(f"Fora: {fora}")
