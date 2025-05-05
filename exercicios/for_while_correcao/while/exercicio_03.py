'''
Mostrar todos os inteiros entre dois números digitados pelo usuário.
Exemplo: usuário digita os números 8 e 15, e aparecem em tela: 9, 10, 11, 12, 13, 14.
'''

inicio = int(input("Insira o primeiro valor do intervalo: "))
final = int(input("Insira o segundo valor do intervalo: "))
i = 0

if final < inicio:
    intervalo = inicio - final
    menor = final
else:
    intervalo = final - inicio
    menor = inicio

while i < intervalo-1:
    menor += 1
    i += 1

    print(menor)
