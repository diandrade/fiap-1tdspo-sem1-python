'''
•	Desenvolva um programa que solicite a idade de um cliente e informe o preço do ingresso de um parque temático de
acordo com as seguintes regras: adultos (18-64 anos) pagam $20, idosos (65 anos ou mais) pagam $15,
e crianças (menos de 18 anos) pagam $10.
'''

idade = int(input("Insira a idade do cliente: "))

if 10 <= idade <= 85:
    print("Insira um valor entre 10 e 85.")
else:
    if idade < 18:
        print("Você pagará R$10,00 (Crianças)")
    elif idade <= 64:
        print("Você pagará R$20,00 (Adultos)")
    else:
        print("Você pagará R$15,00 (Idosos)")
