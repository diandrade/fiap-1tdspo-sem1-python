'''
Escreva um programa que solicite uma temperatura na escala Fahrenheit,
faça a conversão e exiba a temperatura equivalente em Celsius.
Celsius = 5/9 * (F - 32).
'''

graus_em_fahrenheit = int(input("Informe a quantidade de Fahrenheit: "))
print(f"O valor de {graus_em_fahrenheit} fahrenheit é {((5 / 9) * (graus_em_fahrenheit - 32)):.1f} Celsius.")
