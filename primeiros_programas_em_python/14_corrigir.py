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

quantidade_de_carros_vendidos = float(input("Insira a quantidade de carros vendidos: "))
valor_da_venda = float(input("Insira o valor por venda: "))
salario_fixo_do_vendedor = float(input("Insira o valor do salário fixo: "))
comissao_por_venda = float(input("Insira o valor da comissão por venda (em número decimal Ex: 10% -> 0.10): "))
print(f"O salário final do vendedor será: {((quantidade_de_carros_vendidos * valor_da_venda) * comissao_por_venda) + salario_fixo_do_vendedor}")