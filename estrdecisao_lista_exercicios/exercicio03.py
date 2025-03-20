'''
Escreva um algoritmo que solicite o valor de uma mercadoria
e qual o valor que o usuário tem em mãos e
diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria.
'''

valor_mercadoria = float(input("Qual é o valor da mercadoria? "))
valor_na_conta = float(input("Qual valor o usuário têm em mãos atualmente? "))

if valor_na_conta >= valor_mercadoria:
    print("É possível realizar a compra da mercadoria")
else:
    print("Infelizmente, não foi possível realizar a compra.")