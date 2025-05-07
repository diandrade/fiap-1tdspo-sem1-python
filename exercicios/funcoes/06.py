'''
uma função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso
e passar estes valores para a função valorPagamento. O cálculo do valor a ser pago é feito da seguinte forma:
para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
A função deverá retornar o valor da prestação.
'''



def valor_pagamento(valor_prestacao, nmr_dias_em_atraso):
    if nmr_dias_em_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * 0.001 * nmr_dias_em_atraso
        return valor_prestacao + multa + juros

valor_prestacao = float(input("Insira o valor da prestação: "))
nmr_dias_em_atraso = float(input("Insira o número de dias em atraso: "))

print(f"Valor a pagar: R${valor_pagamento(valor_prestacao, nmr_dias_em_atraso):.2f}")

