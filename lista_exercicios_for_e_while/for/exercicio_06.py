'''
Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive).
Considere que o N será sempre maior que ZERO.
'''

n = int(input("Insira um valor inteiro: "))

if n <= 0:
    print("Insira um número positivo")
else:
    for i in range(1, n+1):
        print(i)