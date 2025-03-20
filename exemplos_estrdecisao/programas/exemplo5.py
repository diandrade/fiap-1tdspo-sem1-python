'''
Criar um menu de opções para o usuário escolher uma das 3 operações
1 - Somar os 2 números inteiros
2 - Subtrair os 2 números inteiros
3 - Multiplicar os 2 números inteiros
4 - Dividir os 2 números inteiros
'''
print("----MENU DE OPÇÕES----")
print("1 - Somar os 2 números inteiros")
print("2 - Subtrair os 2 números inteiros")
print("3 - Multiplicar os 2 números inteiros")
print("3 - Dividir os 2 números inteiros")

opcao = int(input("Digite a opção desejada (1 a 4): "))
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

match opcao:
    case 1:
        soma = num1 + num2
        print(f"A soma dos 2 números é {soma}")
    case 2:
        sub = num1 - num2
        print(f"A subtração dos 2 números é {sub}")
    case 3:
        mult = num1 * num2
        print(f"A multiplicação dos 2 números é {mult}")
    case 4:
        div = num1 / num2
        print(f"A divisão dos 2 números é {div:.2f}")
    case _:
        print("Opção inválida")