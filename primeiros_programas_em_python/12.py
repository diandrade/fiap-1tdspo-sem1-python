'''
Faça um algoritmo que solicite ao usuário a idade de uma pessoa expressa em
anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
Considerar ano com 365 dias e mês com 30 dias.
Por fim, exiba a idade da pessoa expressa apenas em dias.

	A. Informe quantos anos a pessoa têm.
	B. Informe quantos meses se passaram desde seu último aniversário.
	C. Informe quantos dias se passaram desde o começo do mês atual.
	D. Forneça o produto dos anos por 365.
	E. Forneça o produto dos meses por 30.
	F. Forneça a soma de ambos os produtos e some com os dias restantes.
	G. Mostre o resultado da soma final.
'''

anos = int(input("Quantos anos você têm? "))
meses = int(input("Quantos meses se passaram desde seu último aniversário: "))
dias = int(input("Quantos dias se passaram desde o começo do mês atual? "))

print(f"A idade da pessoa expressa apenas em dias é: {((anos * 365) + (meses * 30)) + dias}")
