print("----- TABELA DE CARNES -----")
print("\n")
print("Filé Duplo (F) - Até 5KG = R$4,90")
print("Filé Duplo (F) - Acima de 5KG = R$5,80")

print("\n")

print("Alcatra (A) - Até 5KG = R$5,90")
print("Alcatra (A) - Acima de 5KG = R$6,80")

print("\n")

print("Picanha (P) - Até 5KG = R$6,90")
print("Picanha (P) - Acima de 5KG = R$7,80")

print("\n")

tipo_carne = str(input("Insira o tipo de carne selecionada: (entre F, A e P) ")).upper()
match tipo_carne:
    case "F":
        qtd_carne = float(input("Insira a quantidade de carne comprada: (em KG) "))
        if qtd_carne <= 0:
            print("Insira um valor positivo")
        else:
            forma_pagamento = str(input("Insira sua forma de pagamento: ")).upper()
            match forma_pagamento:
                case "TABAJARA":
                    if qtd_carne > 7:
                        valor_carne = 5.80 * qtd_carne
                        valor_carne_com_desconto = valor_carne - (valor_carne * 0.05)
                        print(f"O valor total da {tipo_carne} é R${valor_carne_com_desconto:.2f}")
                    else:
                        if qtd_carne <= 5:
                            valor_carne = 4.90 * qtd_carne
                            print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                        else:
                            valor_carne = 5.80 * qtd_carne
                            print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                case _:
                    if qtd_carne <= 5:
                        valor_carne = 4.90 * qtd_carne
                        print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                    else:
                        valor_carne = 5.80 * qtd_carne
                        print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")

    case "A":
        qtd_carne = float(input("Insira a quantidade de carne comprada: (em KG) "))
        if qtd_carne <= 0:
            print("Insira um valor positivo")
        else:
            forma_pagamento = str(input("Insira sua forma de pagamento: ")).upper()
            match forma_pagamento:
                case "TABAJARA":
                    if qtd_carne > 7:
                        valor_carne = 6.80 * qtd_carne
                        valor_carne_com_desconto = valor_carne - (valor_carne * 0.05)
                        print(f"O valor total da {tipo_carne} é R${valor_carne_com_desconto:.2f}")
                    else:
                        if qtd_carne <= 5:
                            valor_carne = 5.90 * qtd_carne
                            print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                        else:
                            valor_carne = 6.80 * qtd_carne
                            print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                case _:
                    if qtd_carne <= 5:
                        valor_carne = 5.90 * qtd_carne
                        print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                    else:
                        valor_carne = 6.80 * qtd_carne
                        print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")

    case "P":
        qtd_carne = float(input("Insira a quantidade de carne comprada: (em KG) "))
        if qtd_carne <= 0:
            print("Insira um valor positivo")
        else:
            forma_pagamento = str(input("Insira sua forma de pagamento: ")).upper()
            match forma_pagamento:
                case "TABAJARA":
                    if qtd_carne > 7:
                        valor_carne = 7.80 * qtd_carne
                        valor_carne_com_desconto = valor_carne - (valor_carne * 0.05)
                        print(f"O valor total da {tipo_carne} é R${valor_carne_com_desconto:.2f}")
                    else:
                        if qtd_carne <= 5:
                            valor_carne = 6.90 * qtd_carne
                            print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                        else:
                            valor_carne = 7.80 * qtd_carne
                            print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                case _:
                    if qtd_carne <= 5:
                        valor_carne = 6.90 * qtd_carne
                        print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")
                    else:
                        valor_carne = 7.80 * qtd_carne
                        print(f"O valor total da {tipo_carne} é R${valor_carne:.2f}")

    case _:
        print("Insira um valor entre F, A e P")