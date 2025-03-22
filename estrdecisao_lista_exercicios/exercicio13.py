'''
O cardápio de uma casa de lanches é dado pela tabela abaixo:

Escreva um algoritmo que solicite o código do item adquirido pelo consumidor e a quantidade, calculando e mostrando o valor a pagar. Não será necessário exibir o produto e o valor, somente o valor final.

OBS: utilize a estrutura de decisão match...case.
'''

codigo_item = int(input("Insira o código de item: "))

if 100 <= codigo_item <= 105:
    quantidade_item = int(input("Insira a quantidade deste mesmo item: "))
    match codigo_item:
        case 100:
            print(f"Cachorro quente na quantidade de {quantidade_item} no valor de R${quantidade_item * 1.70}")
        case 101:
            print(f"Bauru simples na quantidade de {quantidade_item} no valor de R${quantidade_item * 2.30}")
        case 102:
            print(f"Bauru com ovo na quantidade de {quantidade_item} no valor de R${quantidade_item * 2.60}")
        case 103:
            print(f"Hamburger na quantidade de {quantidade_item} no valor de R${quantidade_item * 2.40}")
        case 104:
            print(f"Cheeseburger na quantidade de {quantidade_item} no valor de R${quantidade_item * 2.50}")
        case 105:
            print(f"Refrigerante na quantidade de {quantidade_item} no valor de R${quantidade_item * 1.00}")
else:
    print("Insira um valor válido!")
