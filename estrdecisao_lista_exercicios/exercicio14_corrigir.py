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

operacao_escolhida = int(input("Insira o modelo de operação escolhida (1 - Média entre os números digitados, "
                               "2 - Maior valor dos números digitados, 3 - Menor valor dos números digitados, "
                               "4 - Divisão inteira dos números digitados): "))

if 1 <= operacao_escolhida <= 4:
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    media = (num1 + num2) / 2
    divisao_inteira = f"{num1/num2:.0f}"
    if num1 < num2:
        ordem = f"{num2} maior que {num1}"
    elif num1 == num2:
        ordem = f"{num2} igual a {num1}"
    else:
        ordem = f"{num2} menor que {num1}"

    match operacao_escolhida:
        case 1:
            print(f"A operação escolhida foi média, e o resultado é {media}")
        case 2:
            print(f"A operação escolhida foi maior dos números dígitados, e o resultado é {ordem}")
        case 3:
            print(f"A operação escolhida foi menor dos números dígitados, e o resultado é {ordem}")
        case 4:
            print(f"A operação escolhida foi divisão inteira, e o resultado é: " + divisao_inteira)
else:
    print("Insira uma operação válida!")
