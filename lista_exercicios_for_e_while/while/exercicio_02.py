'''
Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser interrompido quando uma nota negativa for digitada.

Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:

- média abaixo de 3.5 (reprovados direto)

- média entre 3,5 e 7 (exame)

- acima de 7 (aprovados)

Calcule a média aritmética da turma e informe o resultado no final.

E exiba na tela a quantidade de alunos: reprovados direto, exame aprovado.
'''

qtd_notas = 0
media_aluno = 0
media_final = 0
aprovados = 0
reprovados = 0
exame = 0
qtd_alunos = 0

nota = float(input("Insira a nota do aluno entre 0 e 10: "))
if nota < 0:
    print("Insira um valor entre 0 e 10.")
else:
    while 0 <= nota <= 10:
        nota += float(input("Insira a nota do aluno: "))
        qtd_notas += 1

        if qtd_notas == 4:
            media_aluno = nota / qtd_notas
            if media_aluno < 3.5:
                reprovados += 1
            elif media_aluno < 7:
                exame += 1
            else:
                aprovados += 1

        media_final += media_aluno
        qtd_alunos += 1
        qtd_notas = 0
        nota = 0

        media_final /= qtd_alunos
        print(
            f"A quantidade de aprovados foi de {aprovados}, de exame foram {exame} e de reprovados foram {reprovados}.")
        print(f"A média final da turma foi de {media_final:.2f}")
