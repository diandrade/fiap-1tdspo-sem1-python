'''
Faça um programa que solicite dois números e execute as operações listadas a

seguir de acordo com a escolha do usuário:

Escolha do usuário Operação

1 Média entre os números digitados

2 Maior valor dos números digitados

3 Menor valor dos números digitados

4 Divisão inteira dos números digitados

OBS: utilize a estrutura de decisão match...case.
'''

print("1 - Média entre os números digitados")
print("2 - Maior valor dos números digitados")
print("3 - Menor valor dos números digitados")
print("4 - Divisão inteira dos números digitados")
operacao_escolhida = int(input("Insira o modelo de operação escolhida: "))

if 1 <= operacao_escolhida <= 4:
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    match operacao_escolhida:
        case 1:
            media = (num1 + num2) / 2
            print(f"A operação escolhida foi média, e o resultado é {media}")
        case 2:
            maior = max(num1, num2)
            print(f"A operação escolhida foi maior dos números dígitados, e o resultado é {maior}")
        case 3:
            menor = min(num1, num2)
            print(f"A operação escolhida foi menor dos números dígitados, e o resultado é {menor}")
        case 4:
            if num2 == 0:
                print("Erro: divisão por zero!")
            else:
                divisao_inteira = num1 // num2
                print(f"A operação escolhida foi divisão inteira, e o resultado é: " + divisao_inteira)
else:
    print("Insira uma operação válida!")
