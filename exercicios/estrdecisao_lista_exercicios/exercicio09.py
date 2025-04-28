'''
Escreva um programa que leia um ano qualquer e verifique se o mesmo está
entre 1000 e 2999, caso não esteja apresentar uma mensagem de erro.
Caso esteja nessa faixa verificar se o ano é bissexto. Um ano é bissexto caso seja
divisível por 4 mas não por 100. Um ano também é bissexto se for divisível por 400.
'''

ano = int(input("Insira um ano qualquer entre 1000 e 2999: "))

if 1000 <= ano <= 2999:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")
else:
    print("Insira um valor entre 1000 e 2999")