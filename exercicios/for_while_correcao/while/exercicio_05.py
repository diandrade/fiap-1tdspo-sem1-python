'''
Desenvolva um programa que solicite ao usuário números positivos até que o valor 0 seja pressionado.
Em seguida, calcule a média aritmética de todos os números recebidos (exceto o número 0). Além disso,
apresente o maior e o menor número digitado.
'''

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
'''

soma_positivos = 0
qtde_positivos = 0

while True:
    num = int(input("Digite um número positivo (0 para sair): "))
    if num == 0:
        break
    elif num > 0:
        soma_positivos += num
        qtde_positivos += 1

        if qtde_positivos == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    else:
        print("Você deve digitar um número positivo!")

media = soma_positivos / qtde_positivos
print(f"A média dos números é {media:.2f}")
print(maior)
print(menor)

