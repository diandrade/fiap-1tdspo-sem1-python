'''
Escreva um programa que solicite uma temperatura na escala Fahrenheit,
faça a conversão e exiba a temperatura equivalente em Celsius.
Celsius = 5/9 * (F - 32).
'''

graus_em_fahrenheit = float(input("Informe a quantidade de Fahrenheit: "))
conversao_em_celsius = 5 / 9 * (graus_em_fahrenheit - 32)
print(f"O valor de {graus_em_fahrenheit} Fahrenheit é {conversao_em_celsius:.2f} Celsius.")
