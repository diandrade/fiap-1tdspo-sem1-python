'''
•	Desenvolva um programa que solicite a idade de um cliente e informe o preço do ingresso de um parque temático de
acordo com as seguintes regras: adultos (18-64 anos) pagam $20, idosos (65 anos ou mais) pagam $15,
e crianças (menos de 18 anos) pagam $10.
'''

idade = int(input("Insira a idade do cliente: "))

if idade <= 0:
    print("Insira um valor positivo e numérico.")

else:
    if idade <= 18:
        print("Você pagará R$10,00")
    elif idade <= 64:
        print("Você pagará R$20,00")
    else:
        print("Você pagará R$15,00")
