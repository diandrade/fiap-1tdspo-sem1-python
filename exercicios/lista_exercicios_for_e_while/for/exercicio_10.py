'''
Escreva um programa que calcule o somatório de todos os números pares em um intervalo definido pelo usuário.
Ex: para inicio = 2 e fim = 10 o somatório é 2+4+6+8+10. OBS: utilize o “for”.
'''

n1 = int(input("Insira o valor do primeiro intervalo: "))
n2 = int(input("Insira o valor do segundo intervalo: "))

soma = 0
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        soma += i

print(soma)
