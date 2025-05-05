'''
Desenvolva um programa que receba 10 números inteiros e os armazene em uma lista. Em seguida, o programa deve encontrar
o maior elemento e exibir sua posição (índice) na lista.
'''

lista = []

for i in range(10):
    num = int(input(f"Insira um número inteiro ({10 - i} Faltantes): "))
    lista.append(num)

maior_elemento = max(lista)
if maior_elemento in lista:
    indice = lista.index(maior_elemento)
    print(f"{maior_elemento} está armazenado no índice {indice}")
