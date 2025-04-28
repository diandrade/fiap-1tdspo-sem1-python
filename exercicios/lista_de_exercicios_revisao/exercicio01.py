'''
•	Com a volta das aulas presenciais, a mãe de um aluno do ensino fundamental necessita saber quanto gastará
com material escolar.
Para fazer uma simulação, ela foi a uma livraria com o objetivo de simular a compra dos seguintes itens básicos:
canetas, lápis e cadernos.
Um ponto a se considerar é que essa livraria está com um programa de desconto de 20% nos preços dos cadernos
e 5% nas canetas.
Assim sendo, escreva um programa em Python que solicite as quantidades dos itens, preços e calcule o
total da compra simulada.
'''

qtd_caneta = int(input("Quantas canetas a mãe irá comprar? "))
if qtd_caneta < 1:
    print("O valor não pode ser inferior a 1.")
else:
    qtd_caderno = int(input("Quantos cadernos a mãe irá comprar? "))
    if qtd_caderno < 1:
        print("O valor não pode ser inferior a 1.")
    else:
        qtd_lapis = int(input("Quantos lapis a mãe irá comprar? "))
        if qtd_lapis <1:
            print("O valor não pode ser inferior a 1.")
        else:
            valor_caneta = float(input("Qual é o valor da caneta? "))
            if valor_caneta < 0:
                print("O valor não pode ser inferior a 0.")
            else:
                valor_caderno = float(input("Qual é o valor do caderno? "))
                if valor_caderno < 0:
                    print("O valor não pode ser inferior a 0.")
                else:
                    valor_lapis = float(input("Qual é o valor do lapis? "))
                    if valor_lapis < 0:
                        print("O valor não pode ser inferior a 0.")
                    else:
                        desconto_caderno = valor_caderno - (valor_caderno * 0.20)
                        desconto_caneta = valor_caneta - (valor_caneta * 0.05)

                        total_caneta = qtd_caneta * desconto_caneta
                        total_caderno = qtd_caderno * desconto_caderno
                        total_lapis = qtd_lapis * valor_lapis

                        valor_total = total_lapis + total_caderno + total_caneta

                        print(f"A soma total da compra simulada é R${valor_total:.2f}")

