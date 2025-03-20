'''
Escreva um programa que pergunte em qual mês estamos (1-12) e ao final utilize
uma estrutura de decisão por seleção para escrever o nome do mês por extenso na tela.
'''

mes = int(input("Em qual mês estamos? "))

if 1 <= mes <= 12:
    match mes:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
else:
    print("Insira um mês válido")

