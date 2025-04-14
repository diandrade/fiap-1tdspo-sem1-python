'''
Escreva um programa que contenha o seguinte menu:

Opção 1: Verificar e exibir se um número x é ou não divisível por 6;

Opção 2: Calcular o fatorial do número x;

Opção 3: Exibir todos os inteiros de 1 até um número x.

O programa deverá solicitar ao usuário a leitura de um número x e a opção desejada
até que o usuário digite “N” para encerrar o programa.
OBS: o programa deverá solicitar o número e a opção enquanto do usuário escolha “S”.
'''

menu = """
1 - Verificar e exibir se um número x é ou não divisível por 6
2 - Calcular o fatorial do número x
3 - Exibir todos os inteiros de 1 até um número x
"""

sim_nao = """
S - Continuar loop
N - Finalizar loop
"""

print(menu)
continuar = "S"
while continuar != "N":

    escolha = int((input("Insira o número de escolha de acordo com o menu acima: ")))
    if escolha == 1 or escolha == 2 or escolha == 3:
        num = int(input("Insira um número para realização da operação: "))

        i = 1

        match escolha:
            case 1:
                if num % 6 == 0:
                    print("O valor inserido é divisível por 6")
                else:
                    print("O valor inserido não é divisível por 6.")
            case 2:
                fatorial = 1
                while i <= num:
                    fatorial *= i
                    i += 1
                print(f"O fatorial do valor inserido é: {fatorial}")
            case 3:
                while i <= num:
                    print(i)
                    i += 1

        continuar = str(input(sim_nao))

        while continuar != 'N' and continuar != 'S':
            continuar = str(input(sim_nao))
            break

    else:
        print("Insira um valor entre 1 e 3.")
