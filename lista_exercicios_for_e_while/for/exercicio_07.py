'''
Escreva um algoritmo que solicite dois números e devolva quantos pares e ímpares há entre esses dois números.
Exemplo: entre 7 e 10 há 2 números pares e 2 números ímpares
'''

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

pares = 0
impares = 0

for i in range (n1, n2+1):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}")
print(f"Impares: {impares}")
