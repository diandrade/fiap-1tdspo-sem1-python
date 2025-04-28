'''
Escreva um programa em Python que solicite 10 valores inteiros ao usuário
e mostre quantos desses valores lidos são negativos.
Para tal, utilize a estrutura de repetição “for”.
'''

negativo = 0
for i in range(1, 11):
    num = int(input("Insira um número: "))
    if num <= 0:
        negativo += 1
print(f"A quantidade de números negativos é: {negativo}")