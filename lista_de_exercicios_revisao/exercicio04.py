'''
•	A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá
hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que solicite o número
de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido
das horas extras,
caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
'''

horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas de um funcionário: "))
if horas_trabalhadas < 0:
    print("Não são válidos números menores que 0.")
else:
    valor_hora_regular = float(input("Insira o salário por hora de um funcionário: "))
    if valor_hora_regular < 0:
        print("Não são válidos números menores que 0.")
    else:
        qtd_extras = (horas_trabalhadas - 40)
        qtd_regular = horas_trabalhadas - qtd_extras
        salario_regular = valor_hora_regular * qtd_regular

        if qtd_extras > 0:
            valor_hora_extra = valor_hora_regular * 1.50
            salario_adicional = valor_hora_extra * qtd_extras
            salario_final = salario_adicional + salario_regular
            print(f"O salário final do funcionário a partir do total de {horas_trabalhadas} "
                  f"horas trabalhadas será de R${salario_final:.2f}")
        else:
            print(f"O salário final do funcionário a partir do total de {horas_trabalhadas} "
                  f"horas trabalhadas será de R${salario_regular:.2f}")
