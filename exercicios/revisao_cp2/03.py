print('''
------------- MENU -------------
01 -  PORÇÃO DE FRITAS - R$ 35.00
02 - PORÇÃO DE PASTÉIS - R$ 25.00
03 -  TÁBUA DE FRIOS   - R$ 40.00
04 -  PORÇÃO DE PEIXES - R$ 55.00
05 -      CERVEJA      - R$ 18.00
''')

comanda = 0
valor_comanda = 0
total_comanda = 0

while True:
    continuar = int(input("Deseja iniciar ou continuar o programa? (0 para Não e 1 para Sim): "))
    if continuar == 0:
        break
    elif continuar != 1:
        print("Insira um valor entre 0 e 1.")
    else:
        comanda += 1
        print(f"---------------- Comanda {comanda} -------------------")
        while True:
            codigo = int(input("Insira o código da refeição desejada: "))
            match codigo:
                case 0:
                    break
                case 1:
                    valor_comanda += 35.00
                case 2:
                    valor_comanda += 25.00
                case 3:
                    valor_comanda += 40.00
                case 4:
                    valor_comanda += 55.00
                case 5:
                    valor_comanda += 18.00
                case _:
                    print("Insira um código válido.")
        print(f"O valor total da comanda {comanda} é de R$ {valor_comanda}")
        total_comanda += valor_comanda
        valor_comanda = 0
print(f"O valor total de todas as comandas recebidas durante o dia foi de: R$ {total_comanda}")
