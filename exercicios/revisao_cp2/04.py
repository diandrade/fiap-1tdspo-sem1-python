impares = 0
i = 0
while True:
    num = int(input("Insira um número (0 para finalizar): "))
    if num == 0:
        print("Programa finalizado.")
        break
    else:
        i += 1
        if num % 2 == 1:
            impares += 1
if impares == 0:
    print("Não foram digitados números ímpares, portanto não há total nem percentual dos mesmos.")
else:
    percentual_impares = impares * 100 / i
    print(f"O total de números ímpares digitados é de: {impares}")
    print(f"O percentual de números ímpares digitados em relação ao total de números é de: {percentual_impares}%")
