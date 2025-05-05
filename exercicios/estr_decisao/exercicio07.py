'''
Escreva um programa que pergunte ao usuário
qual foi a média anual de um aluno e ao final diga se ele está aprovado,
reprovado ou de exame.
Considere que o aluno está aprovado caso a média seja maior ou igual a 6.0;
de exame com a média entre 3.0 e 5.9 e reprovado com média menor do que 3.0.
'''

media_aluno = float(input("Insira sua média anual: "))
if 0 <= media_aluno <= 10:
    if media_aluno <= 3:
        print("Reprovado.")
    elif media_aluno <= 5.9:
        print("De Exame.")
    else:
        print("Aprovado.")
else:
    print("Insira uma média entre 0 e 10.")