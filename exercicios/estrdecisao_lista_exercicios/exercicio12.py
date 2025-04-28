'''
Uma frutaria está vendendo frutas com a seguinte tabela de preços:

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg)
de morangos e a quantidade (em Kg) de maças adquiridas e
escreva o valor a ser pago pelo cliente.
'''

kg_morangos = int(input("Insira a quantidade de Morangos: "))
kg_macas = int(input("Insira a quantidade de Maçãs: "))

if kg_morangos <= 5:
    preco_morango = kg_morangos * 2.50
else:
    preco_morango = kg_morangos * 2.20

if kg_macas <= 5:
    preco_maca = kg_macas * 1.80
else:
    preco_maca = kg_macas * 1.50

preco_total = preco_morango + preco_maca

if kg_morangos + kg_macas > 8 or preco_total > 25.00:
    preco_total -= preco_total * 0.10

print(f"Os kilos, do morango e da maçã consecutivamente são {kg_morangos}kg e {kg_macas}kg. Além disso, o preço total a ser pago pelo cliente é de R${preco_total:.2f} ")
