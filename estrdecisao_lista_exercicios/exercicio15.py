'''
Um funcionário irá receber um aumento de acordo com o seu plano de trabalho, de acordo com a tabela abaixo:

Plano de trabalho Porcentagem de aumento

A 10%

B 15%

C 20%

Faça um programa que leia o plano de trabalho e o salário atual de um funcionário e calcula e imprime o seu novo salário.

OBS: utilize a estrutura de decisão match...case.
'''

plano_trabalho = input("Insira seu plano de trabalho (entre A, B e C): ").upper()

if plano_trabalho == 'A' or plano_trabalho == 'B' or plano_trabalho == 'C':
    percentual_A = 1.10
    percentual_B = 1.15
    percentual_C = 1.20

    salario_atual = float(input("Insira seu salário atual: "))

    if salario_atual <= 0:
        print("Insira um valor positivo.")

    match plano_trabalho:
        case 'A':
            salario_aumento = percentual_A * salario_atual
            print(f"O salário com acrescimo do funcionário será {salario_aumento:.2f}")
        case 'B':
            salario_aumento = percentual_B * salario_atual
            print(f"O salário com acrescimo do funcionário será {salario_aumento:.2f}")
        case 'C':
            salario_aumento = percentual_C * salario_atual
            print(f"O salário com acrescimo do funcionário será {salario_aumento:.2f}")

else:
    print("Insira um valor entre A, B e C.")



