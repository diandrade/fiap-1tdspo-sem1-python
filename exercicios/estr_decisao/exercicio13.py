'''
O cardápio de uma casa de lanches é dado pela tabela abaixo:

Escreva um algoritmo que solicite o código do item adquirido pelo consumidor e a quantidade, calculando e mostrando o valor a pagar. Não será necessário exibir o produto e o valor, somente o valor final.

OBS: utilize a estrutura de decisão match...case.
'''

print("-----MENU DE LANCHES-----")
print("100----- Cachorro Quente -----R$1,70")
print("101----- Bauru Simples -----R$1,30")
print("102----- Bauru com Ovo -----R$2,60")
print("103----- Hamburguer -----R$2,40")
print("104----- X-Burguer -----R$2,50")
print("105----- Refrigerante -----R$1,00")

codigo_item = int(input("Insira o código de item (100 a 105): "))

if 100 <= codigo_item <= 105:
    quantidade_item = int(input("Insira a quantidade deste mesmo item: "))
    match codigo_item:
        case 100:
            valor_total = quantidade_item * 1.70
            print(f"Cachorro quente na quantidade de {quantidade_item} no valor de R${valor_total:.2f}")
        case 101:
            valor_total = quantidade_item * 1.30
            print(f"Bauru simples na quantidade de {quantidade_item} no valor de R${valor_total:.2f}")
        case 102:
            valor_total = quantidade_item * 2.60
            print(f"Bauru com ovo na quantidade de {quantidade_item} no valor de R${valor_total:.2f}")
        case 103:
            valor_total = quantidade_item * 2.40
            print(f"Hamburger na quantidade de {quantidade_item} no valor de R${valor_total:.2f}")
        case 104:
            valor_total = quantidade_item * 2.50
            print(f"Cheeseburger na quantidade de {quantidade_item} no valor de R${valor_total:.2f}")
        case 105:
            valor_total = quantidade_item * 1.00
            print(f"Refrigerante na quantidade de {quantidade_item} no valor de R${valor_total:.2f}")
else:
    print("Insira um valor válido!")
