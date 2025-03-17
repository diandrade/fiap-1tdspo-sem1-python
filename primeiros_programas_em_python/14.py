'''
Uma revendedora de carros usados paga a seus funcionários vendedores
um salário fixo por mês, mais uma comissão também fixa para cada carro vendido
e mais 5% do valor das vendas por ele efetuadas.
Escrever um algoritmo que solicite ao usuário o número de carros por ele vendidos,
o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido.
Calcule e escreva o salário final do vendedor.

    A. Informe a quantidade de carros vendidos
	B. Informe o valor de cada venda.
	C. Informe o salário fixo do vendedor.
	D. Informe o valor da comissão por venda.
	E. Forneça o produto da quantidade dos carros vendidos pela comissão do funcionário em número decimal.
	F. Forneça a soma do salário fixo pelo produto resultante.
	G. Mostre o resultado da soma final.
'''

quantidade_de_carros_vendidos = int(input("Insira a quantidade de carros vendidos: "))
valor_total_vendas = float(input("Insira o valor total das vendas: "))
salario_fixo_do_vendedor = float(input("Insira o valor do salário fixo: "))
valor_por_carro = float(input("Insira o valor fixo da comissão por carro vendido: "))

comissao_carro = quantidade_de_carros_vendidos * valor_por_carro
comissao_vendas = valor_total_vendas * 0.5

salario_final = salario_fixo_do_vendedor + comissao_carro + comissao_vendas

print(f"O salário final do vendedor será: {salario_final:.2f}")
