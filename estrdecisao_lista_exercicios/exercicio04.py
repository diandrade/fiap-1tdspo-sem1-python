'''
Um estacionamento cobra R$ 5,00 por hora porém possui
um teto de cobrança máxima de R$ 35,00,
independente do número de horas. Escreva um algoritmo que pergunte ao usuário
qual foi o período de permanência em horas e escreva na tela o total a pagar.
'''

permanencia_em_horas = int(input("Insira o tempo de permanência em horas: "))
if permanencia_em_horas >= 1:
    if permanencia_em_horas <= 7:
        total_pagar = permanencia_em_horas * 5
        print(f"O total a pagar é: R${total_pagar:.2f}")
    else:
        print("O total a pagar é R$35,00")
else:
    print("Insira um número positivo")