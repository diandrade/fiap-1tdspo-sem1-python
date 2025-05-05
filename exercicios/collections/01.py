'''Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista. Em seguida, armazene os números
pares na lista PAR e os números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas'''

lista = []
pares = []
impares = []

for i in range(10):
    num = int(input(f"Insira um número inteiro ({10 - i} Faltantes): "))
    lista.append(num)

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(lista)
print(pares)
print(impares)