total_compras = 0
i = 0
superior_100 = 0
inferior_50 = 0

for i in range(1, 6):
    compra = float(input(f"Insira o valor da compra do cliente {i}: "))
    total_compras += compra

    if compra > 100:
        superior_100 += 1
    if compra < 50:
        inferior_50 += 1

if total_compras <= 0:
    print("Programa finalizado.")
else:
    media = total_compras / i
    print(f"O valor total pago pelos clientes foi de: R$ {total_compras}")
    print(f"O valor da compra média efetuada pelos clientes foi de: R$ {media:.2f}")
    print(f"O número de clientes que efetuaram compras superiores a 100 reais foi de: {superior_100}")
    print(f"O número de clientes que efetuaram compras inferiores a 50 reais foi de: {inferior_50}")



