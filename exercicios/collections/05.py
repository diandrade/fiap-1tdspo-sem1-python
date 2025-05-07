'''
Escreva um programa em Python que crie uma lista de 10 alunos, utilizando o conceito de dicionários,
contendo os seguintes dados:

o Nome;

o Curso;

o Disciplina;

o Faltas;

o 3 checkpoints.

Depois da lista criada, exiba todos os funcionários com seus dados um debaixo do outro.

OBS: o programa deverá solicitar que o usuário informe os dados para alimentar a lista de dicionários.
'''
funcionarios = []
total_notas = 0

print("--- Dados dos Funcionários ---")
for alunos in range(10):
    nome = input("Insira o nome do funcionário: ")
    curso = input("Insira o curso do funcionários: ")
    disciplina = input("Insira a disciplina que o funcionário está cadastrado: ")
    faltas = input("Insira as faltas do funcionário: ")

    for i in range(3):
        nota_checkpoint = float(input(f"Insira a nota do checkpoint {i + 1}: "))
        total_notas += nota_checkpoint

    media_notas = total_notas / 3

    dicionario = {'Nome': nome, 'Curso': curso, 'Disciplina': disciplina, 'Faltas': faltas, 'Checkpoint': media_notas}
    funcionarios.append(dicionario)

    print("--- Funcionário Cadastrado ---\n")

if len(funcionarios) == 0:
    print("Nenhum funcionário foi cadastrado.")

else:
    for funcionario in funcionarios:
        print(f"Nome: {funcionario['Nome']} | Curso: {funcionario['Curso']} | Disciplina: {funcionario['Disciplina']} "
              f"| Faltas: {funcionario['Faltas']} | Média Checkpoint: {funcionario['Checkpoint']:.2f}")
