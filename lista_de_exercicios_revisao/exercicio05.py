'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

- Álcool:

- até 20 litros, desconto de 3% por litro

- acima de 20 litros, desconto de 5% por litro

- Gasolina:

- até 20 litros, desconto de 4% por litro

- acima de 20 litros, desconto de 6% por litro

- Diesel:

- até 20 litros, desconto de 2% por litro

- acima de 20 litros, desconto de 7% por litro


Escreva um programa em Python que solicite ao usuário o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina ou D-Diesel), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 6,09, o preço do litro do álcool é R$ 4,04
e o preço do litro do Diesel é R$ 5,93.
'''

print("----- MENU DE COMBUSTÍVEIS -----")
print("Álcool (A) ----- R$ 4.04")
print("Gasolina (G) ----- R$ 6.09")
print("Diesel (D) ----- R$ 5.93")

combustivel_escolhido = str(input("Insira o combustível de escolha entre A, G e D: ")).upper()
match combustivel_escolhido:
    case "A":
        litros_vendidos = float(input("Insira a quantidade de litros vendidos: "))
        valor_alcool = litros_vendidos * 4.40
        print(f"O preço do combustível ficou R${valor_alcool}")
    case "G":
        litros_vendidos = float(input("Insira a quantidade de litros vendidos: "))
        valor_gasolina = litros_vendidos * 6.09
        print(f"O preço do combustível ficou R${valor_gasolina}")
    case "D":
        litros_vendidos = float(input("Insira a quantidade de litros vendidos: "))
        valor_diesel = litros_vendidos * 5.93
        print(f"O preço do combustível ficou R${valor_diesel}")
    case _:
        print("Insira um valor minúsculo ou maiúsculo entre A, G e D.")



