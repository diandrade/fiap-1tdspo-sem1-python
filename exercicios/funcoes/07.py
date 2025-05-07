'''
uma função que tenha um parâmetro “n” e que calcule e retorne a média de todos os pares de 1 até N.
'''

def media(n):
    soma_pares = 0
    qtd_pares = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            soma_pares += i
            qtd_pares += 1
    if qtd_pares == 0:
        return 0
    return soma_pares / qtd_pares

print(media(6))
