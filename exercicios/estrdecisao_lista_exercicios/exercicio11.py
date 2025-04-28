'''
Considerando o IMC (índice de massa corpórea),
calculado como peso/(altura*altura),
exiba a situação da pessoa com base na seguinte tabela:
'''

imc = float(input("Insira seu IMC: "))

if imc <= 0:
    print("Insira um valor positivo")
else:
    if imc <= 18.5:
        print("Abaixo do peso.")
    elif imc <= 24.9:
        print("Peso ideal.")
    else:
        print("Acima do peso.")
