'''
Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser interrompido quando uma nota negativa for digitada.

Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:

- média abaixo de 3.5 (reprovados direto)

- média entre 3,5 e 7 (exame)

- acima de 7 (aprovados)

Calcule a média aritmética da turma e informe o resultado no final.

E exiba na tela a quantidade de alunos: reprovados direto, exame aprovado.
'''

'''
OBS: Limite de 4 notas por aluno.
i = Quantidade de Notas
j = Quantidade de Médias Incluídas
'''
i = 0
j = 0

soma_aluno = 0
soma_medias = 0
media_aritmetica = 0

nota_aluno = float(input("Insira uma nota (1): "))
if nota_aluno < 0:
    print("Fim do programa")
else:
    while nota_aluno >= 0:
        while i <= 3:
            nota_aluno = float(input(f"Insira a {i + 1}° nota (2): "))
            if nota_aluno < 0:
                break
            else:
                soma_aluno += nota_aluno
                i += 1
        soma_medias += soma_aluno / 4
        j += 1
        i = 0
    media_aritmetica += soma_medias / j
    print(f"A média aritmética é: {media_aritmetica}")
