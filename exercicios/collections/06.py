'''
§ Escreva um programa em Python que crie uma lista de 10 funcionários, utilizando o conceito de dicionários, contendo os seguintes dados:

o Nome;

o Cargo;

o Salário.

Depois da lista criada, exiba todos os funcionários com seus dados um debaixo do outro.

OBS: o programa deverá solicitar que o usuário informe os dados para alimentar a lista de dicionários.
'''

funcionarios = []

print("--- Dados dos Funcionários ---")
for alunos in range(2):
    nome = input("Insira o nome do funcionário: ")
    cargo = input("Insira seu cargo: ")
    sal = float(input("Insira seu salário: "))

    dicionario = {'Nome': nome, 'Cargo' : cargo, 'Salário': sal}
    funcionarios.append(dicionario)

    print("--- Funcionário Cadastrado ---\n")

if len(funcionarios) == 0:
    print("Nenhum funcionário foi cadastrado.")

else:
    for funcionario in funcionarios:
        print(f"Nome: {funcionario['Nome']} \n| Cargo: {funcionario['Cargo']} \n| Salário: {funcionario['Salário']}\n")
