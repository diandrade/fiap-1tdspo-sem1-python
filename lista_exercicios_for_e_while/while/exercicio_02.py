'''
Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser interrompido quando uma nota negativa for digitada.

Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:

- média abaixo de 3.5 (reprovados direto)

- média entre 3,5 e 7 (exame)

- acima de 7 (aprovados)

Calcule a média aritmética da turma e informe o resultado no final.

E exiba na tela a quantidade de alunos: reprovados direto, exame aprovado.
'''

nota = float(input("Insira uma nota: "))

soma_individual = 0
soma_coletiva = 0
media_coletiva = 0

reprovados = 0
aprovados = 0
exame = 0

i = 0
j = 0

while nota >= 0:
    if nota > 10:
        print("Insira uma nota entre 0 e 10.")
        break
    else:
        if i == 4:
            media_individual = soma_individual / i
            print(f"A média individual do aluno é {media_individual:.2f}")

            soma_coletiva += media_individual
            if media_individual <= 3.5:
                reprovados += 1
            elif media_individual <= 7:
                exame += 1
            else:
                aprovados += 1

            i = 0
            j += 1
            media_coletiva = soma_coletiva / j
        else:
            soma_individual += nota
            nota = float(input("Insira uma nota: "))

            i += 1

if media_coletiva > 0:
    print(
        f"A quantidade de aprovados foi de {aprovados}, de exame foi de {exame} e de reprovados foram de {reprovados}, "
        f"além disso, a média aritmética das notas da turma foi de: {media_coletiva}")
else:
    print("Insira algum valor!")
