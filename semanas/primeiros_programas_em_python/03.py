'''
Escreva um programa que solicite o salário de um funcionário,
faça o acréscimo de 20% sobre seu valor e exiba-o.
DICA: para fazer o acréscimo, multiplique o valor do salário por 1,20.
'''

salario_funcionario = float(input("Qual é seu salário? "))
salario_acrescimo = salario_funcionario * 1.20

print(f"O salário do funcionário é {salario_acrescimo:.2f}")
