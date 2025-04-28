'''
Crie um algoritmo que solicite ao usuário seu consumo de energia elétrica (em kWh),
que deve ser uma variável real.
O algoritmo deve, então, calcular o total da conta,
considerando que cada kWh custa R$ 0,20.
'''

kWh_consumido = int(input("Insira a quantidade de energia consumida: "))
total_conta = kWh_consumido * 0.2

print(f"O valor final de sua conta de energia será: R${total_conta:.2f}")
