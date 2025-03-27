'''
•	Um grupo de amigos resolveu fazer um happy hour em um bar após o horário de trabalho.
Na ocasião eles pediram porções de batatas fritas, pastéis e cervejas para acompanhar.
Escreva um programa em Python que calcule o total do pedido baseado nas quantidades de porções e cervejas consumidas
tendo como referência a tabela abaixo.
Além disso, calcule o valor individual da conta de acordo com o número de amigos.
'''

porcao_fritas = 35.00
porcao_pasteis = 25.00
cervejas = 18.00

qtd_amigos = int(input("Quantos amigos participaram do happy hour? "))
if qtd_amigos <= 0:
    print("O número de amigos deve ser maior que 0.")
else:
    qtd_fritas = int(input("Insira a quantidade de porções de batata frita: "))
    if qtd_fritas < 0:
        print("O número de amigos deve ser maior que 0.")
    else:
        qtd_pasteis = int(input("Insira a quantidade de pastéis pedidos: "))
        if qtd_pasteis < 0:
            print("O número de amigos deve ser maior que 0.")
        else:
            qtd_cervejas = int(input("Insira a quantidade de cervejas pedidas: "))
            if qtd_cervejas < 0:
                print("O número de amigos deve ser maior que 0.")
                exit()

            total_fritas = porcao_fritas * qtd_fritas
            total_pasteis = porcao_pasteis * qtd_pasteis
            total_cervejas = cervejas * qtd_cervejas

            valor_total = total_cervejas + total_fritas + total_pasteis
            valor_individual = valor_total / qtd_amigos

            print(f"O valor total da conta é {valor_total:.2f}")
            print(f"O valor individual da conta é {valor_individual:.2f}")
