'''
Desenvolva um programa que solicite ao usuário números positivos até que o valor 0 seja pressionado.
Em seguida, calcule a média aritmética de todos os números recebidos (exceto o número 0). Além disso,
apresente o maior e o menor número digitado.
'''

num = float(input("Insira um número positivo (0 para parar): "))

maior = num
menor = num
soma = 0
i = 0

while num != 0:
    soma += num

    if num < menor:
        menor = num

    if num > maior:
        maior = num

    num = float(input("Insira um número positivo (0 para parar): "))
    i += 1

media = soma / i
print(
    f"O maior número digitado foi: {maior}, o menor foi: {menor} "
    f"e a média aritmética de todos os números inseridos foi de: {media}")
