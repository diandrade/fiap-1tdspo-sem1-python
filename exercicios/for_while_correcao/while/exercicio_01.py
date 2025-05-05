'''
Desenvolva um programa que solicite números inteiros ao usuário e calcule a soma deles até que o 0 seja digitado.
'''

soma = int(input("Insira um número: "))
num = soma
i = 0

while num != 0:
    num = int(input("Insira um número: "))
    soma += num
    i += 1

if i == 0:
    print("Você fechou o programa antes da soma iniciar.")
else:
    print(f"A soma dos valores dígitados é {soma}")
