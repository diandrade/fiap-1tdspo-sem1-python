#Calcular a média dos 10 números digitados.

soma = 0
cont = 1

while cont <= 10:
    num = int(input("Digite um número inteiro: "))
    soma += num
    cont += 1

media = soma / 10
print("A média dos números é:", media)

