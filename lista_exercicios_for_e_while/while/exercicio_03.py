'''
Mostrar todos os inteiros entre dois números digitados pelo usuário.
Exemplo: usuário digita os números 8 e 15, e aparecem em tela: 9, 10, 11, 12, 13, 14.
'''

num1 = int(input("Insira o primeiro valor do intervalo: "))
num2 = int(input("Insira o segundo valor do intervalo: "))
i = 0

if num2 < num1:
    intervalo = num1 - num2
    menor = num2
else:
    intervalo = num2 - num1
    menor = num1

while i < intervalo-1:
    menor += 1
    i += 1

    print(menor)
