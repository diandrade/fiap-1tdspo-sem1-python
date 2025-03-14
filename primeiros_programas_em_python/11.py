'''
Escreva um programa que solicite a quilometragem parcial de um carro
e a quantidade de litros gastos ele para percorrer esta quilometragem.
Calcule quantos km/l o carro percorreu (autonomia) e exiba na tela.
'''

quilometragem_parcial = float(input("Insira a quilometragem parcial de um carro em determinado espaço: "))
litros_gastos = float(input("Insira quantos litros foram gastos para percorrer esta quilometragem: "))
print(f"A quantidade de km/l que o veículo percorreu é: {quilometragem_parcial/litros_gastos}")