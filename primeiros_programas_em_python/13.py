'''
O custo de um carro novo ao consumidor é a soma do custo de fábrica
com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
escrever um algoritmo para solicitar ao usuário o custo de fábrica de um carro,
calcular e escrever o custo final ao consumidor.

    A. Informe o custo de fábrica.
	B. Forneça o produto do custo de fábrica por 1.28.
	C. Forneça o produto do produto por 1.45.
	D. Mostre o resultado do produto final.
'''

custo_de_fabrica = float(input("Insira o custo de fabricação: "))
print(f"O custo final ao consumidor é: {(custo_de_fabrica * 1.28) * 1.45}")

