'''
Desenvolva um programa que recebe as notas dos alunos de uma turma. Seu programa deverá ser interrompido quando uma nota negativa for digitada.

Durante o processamento seu programa deverá contar o número de alunos nas seguintes condições:

- média abaixo de 3.5 (reprovados direto)

- média entre 3,5 e 7 (exame)

- acima de 7 (aprovados)

Calcule a média aritmética da turma e informe o resultado no final.

E exiba na tela a quantidade de alunos: reprovados direto, exame aprovado.

(OBS: Pedi auxílio de IA para compreender alguns conceitos de reincialização e de parada).
'''

'''
OBS: Limite de 4 notas por aluno.
i = Quantidade de Notas
j = Quantidade de Médias Incluídas
'''
i = 0
j = 0

'''
nota_aluno = 0
soma_aluno = 0
soma_medias = 0
media_aritmetica = 0
media_aluno = 0

reprovado = 0
aprovado = 0
exame = 0

inicio = input("Iniciar programa (S - início): ").upper()
if inicio == "S":
    while True:
        soma_aluno = 0  # Reinicializa para cada aluno
        i = 0
        while i < 4:
            nota_aluno = float(input(f"Insira a {i + 1}° nota: "))
            if nota_aluno < 0:
                break
            soma_aluno += nota_aluno
            i += 1

        if nota_aluno < 0:  # Verifica se saiu por nota negativa
            break

        if i > 0:  # Só calcula se tiver pelo menos uma nota válida
            media_aluno = soma_aluno / i
            soma_medias += media_aluno
            j += 1

            if media_aluno < 3.5:
                reprovado += 1
            elif media_aluno <= 7:
                exame += 1
            else:
                aprovado += 1

    if j > 0:  # Evita divisão por zero
        media_aritmetica = soma_medias / j
        print(f"A média aritmética da turma é: {media_aritmetica}")
        print(f"""
Reprovados : {reprovado}
De Exame: {exame}
Aprovados: {aprovado}
""")
    else:
        print("Nenhum aluno válido foi inserido.")
else:
    print("Fim do programa")
'''

soma_notas = 0
qtde_notas = 0
qtde_reprovados = 0
qtde_exame = 0
qtde_aprovados = 0

nota = float(input("Digite a nota do aluno (nota negativa para sair)"))

while nota >= 0:
    soma_notas += nota
    qtde_notas += 1
    if nota < 3.5:
        qtde_reprovados += 1
    elif nota <= 7.0:
        qtde_exame += 1
    else:
        qtde_aprovados += 1
    nota = float(input("Digite a nota do aluno (nota negativa para sair)"))

media_turma = soma_notas / qtde_notas
print(f"A média da turma é: {media_turma}")
print(f"A quantidade de aprovados é: {qtde_aprovados}")
print(f"A quantidade de reprovados é: {qtde_reprovados}")
print(f"A quantidade de alunos em exame é: {qtde_exame}")

