'''
Um estacionamento cobra R$ 5,00 por hora.
Escreva um algoritmo que pergunte ao usuário
qual foi o período de permanência em horas e calcule o total a pagar.
'''

periodo_de_permanencia_em_horas = int(input("Qual foi o período de permanência no estacionamento em horas? "))
total_pagamento = periodo_de_permanencia_em_horas * 5.00
print(f"O total a pagar é: R${total_pagamento}")
