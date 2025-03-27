'''
•	A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá
hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que solicite o número
de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido
das horas extras,
caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
'''

jornada_semanal = int(input("Qual é a jornada semanal do funcionário?"))
horas_trabalhadas_mes = int(input("Qual é o número de horas trabalhadas no mês do funcionário? "))
salario_hora = float(input("Qual é o salário por hora do funcionário?"))

salario_semana = jornada_semanal * salario_hora
