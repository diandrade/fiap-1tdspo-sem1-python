'''
Desenvolva um programa para calcular a média salarial dos funcionários da empresa XXX, para isso seu programa
deverá solicitar o nome e salário dos 5 funcionários que trabalham nessa empresa. Ao final seu programa deverá calcular
a média dos salários e exibir na tela as seguintes informações: (use 2 casas decimais na exibição dos números)

o A média salarial dos funcionários da empresa XXX é _______

o O nome e o salário do funcionário que recebe o menor salário

o O nome e o salário do funcionário que recebe o maior salário
'''

i = 0
soma = 0
menor = 0
maior = 0
maior_nome = ""
menor_nome = ""

for i in range(0, 5):
    nome = str(input("Insira o nome do funcionário: "))
    sal = float(input("Insira o salário do funcionário: "))

    soma += sal

    if sal > maior:
        maior_nome = nome
        maior = sal

    if i == 0:
        menor_nome = nome
        menor = sal
    else:
        if sal < menor:
            menor_nome = nome
            menor = sal

media = soma/i
print(f"A média salárial dos funcionários da empresa XXX é: {media:.2f}")
print(f"O nome e o salário do funcionário que recebe o maior salário é: {maior_nome} com R${maior} de salário.")
print(f"O nome e o salário do funcionário que recebe o menor salário é: {menor_nome} com R${menor} de salário.")


