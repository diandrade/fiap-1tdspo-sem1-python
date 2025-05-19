'''
GRAZIELLE ALENCAR - RM561529
DIEGO ANDRADE - RM566385
'''

def main():
    lista_alunos = []
    while True:
        print('''
        1 - Insira um aluno.
        2 - Leia as informações do aluno.
        3 - Atualize as informações do aluno.
        4 - Delete um aluno do sistema.
        5 - Exiba todos os alunos inseridos no sistema.
        6 - Exibe um relatório dos alunos do curso de TDS.
        7 - Exibe um relatório dos alunos da disciplina “Python” cuja média dos checkpoints seja maior ou igual a 7.0.
        ''')

        opcao = int(input("Insira o opção desejada: (1 a 7): "))
        if 1 <= opcao <= 7:
            match opcao:
                case 1:
                    inserir_aluno(lista_alunos)
                case 2:
                    codigo_aluno = int(input("Digite o código do aluno que deseja buscar: "))
                    indice = buscar_aluno(lista_alunos, codigo_aluno)
                    if indice != -1:
                        for chave, valor in lista_alunos[indice].items():
                            print(f"{chave}:{valor}")
                    else:
                        print("O código não consta na lista")
                case 3:
                    codigo_aluno = int(input("Digite o código do aluno que deseja alterar os dados: "))
                    indice = buscar_aluno(lista_alunos, codigo_aluno)
                    if indice != -1:
                        atualizar_aluno(lista_alunos, indice)
                    else:
                        print("O código não consta na lista")
                case 4:
                    codigo_aluno = int(input("Digite o código do aluno que deseja excluir os dados: "))
                    indice = buscar_aluno(lista_alunos, codigo_aluno)
                    if indice != -1:
                        remover_aluno(lista_alunos, indice)
                case 5:
                    exibir_alunos(lista_alunos)
                case 6:
                    relatorio_tds(lista_alunos)
                case 7:
                    relatorio_python(lista_alunos)
                case _:
                    print("Insira uma opção válida!")

        else:
            print("Opção Inválida")

        resp = int(input("Deseja continuar? (1-SIM/0-NÃO): "))
        while True:
            if resp != 0 and resp != 1:
                resp = int(input("Deseja continuar? (1-SIM/0-NÃO): "))
            else:
                break
        if resp == 0:
            break

def inserir_aluno(lista_alunos):
    codigo_aluno = int(input("Insira o código do aluno: "))
    nome_aluno = input("Insira o nome do aluno: ")
    curso_aluno = input("Insira o curso do aluno: ")
    disciplina_aluno = input("Insira a disciplina do aluno: ")
    faltas_aluno = int(input("Insira a quantidade de faltas do aluno: "))
    checkpoints_aluno = []
    for i in range(3):
        checkpoints_aluno.append(float(input(f"Insira a nota do Checkpoint {i + 1}: ")))

    aluno = {
        'Código': codigo_aluno,
        'Nome': nome_aluno,
        'Curso': curso_aluno,
        'Disciplina': disciplina_aluno,
        'Faltas': faltas_aluno,
        'Checkpoints': checkpoints_aluno
    }
    lista_alunos.append(aluno)

def buscar_aluno(lista_alunos, codigo):
    indice = -1
    for i in range(len(lista_alunos)):
        if lista_alunos[i]['Código'] == codigo:
            indice = i
    return indice

def atualizar_aluno(lista_alunos, indice):
    print(f"Codigo atual do aluno cadastrado no sistema: {lista_alunos[indice]['Código']}")
    lista_alunos[indice]['Código'] = int(input("Digite o novo código do aluno: "))

    print(f"Nome atual do aluno cadastrado no sistema: {lista_alunos[indice]['Nome']}")
    lista_alunos[indice]['Nome'] = input("Digite o novo nome do aluno: ")

    print(f"Curso atual do aluno cadastrado no sistema: {lista_alunos[indice]['Curso']}")
    lista_alunos[indice]['Curso'] = input("Digite o novo curso cadastrado no perfil do aluno: ")

    print(f"Disciplina atual do aluno cadastrado no sistema: {lista_alunos[indice]['Disciplina']}")
    lista_alunos[indice]['Disciplina'] = input("Digite a nova disciplina cadastrada no perfil do aluno: ")

    print(f"Faltas atuais do aluno cadastrado no sistema: {lista_alunos[indice]['Faltas']}")
    lista_alunos[indice]['Faltas'] = int(input("Digite a nova quantidade de faltas do aluno: "))

    checkpoints_aluno = []
    for i in range(3):
        checkpoints_aluno.append(float(input(f"Digite a nova nota do Checkpoint {i + 1}: ")))
    lista_alunos[indice]['Checkpoints'] = checkpoints_aluno

def remover_aluno(lista_alunos, indice):
    lista_alunos.pop(indice)
    print("Aluno removido com sucesso!")

def exibir_alunos(lista_alunos):
    for aluno in lista_alunos:
        for chave, valor in aluno.items():
            print(f"{chave}: {valor}")
        print("---------------------------")

def relatorio_tds(lista_alunos):
    if len(lista_alunos) == 0:
        print("Registre ao menos 1 aluno.")
    else:
        print("Segue abaixo, relatório em código e em nome dos alunos do curso de TDS"
              " (Caso não apareça nenhuma informação, nenhum aluno se enquadra na lista.): ")
        for aluno in lista_alunos:
            if aluno['Curso'].upper() == 'TDS':
                print(f"Código: {aluno['Código']}, Nome: {aluno['Nome']}")
                print("---------------------------")

def relatorio_python(lista_alunos):
    if len(lista_alunos) == 0:
        print("Registre ao menos 1 aluno.")
    else:
        print("Segue abaixo, relatório em código e em nome dos alunos da disciplina Python com média dos checkpoints maior ou igual a 7.0"
              " (Caso não apareça nenhuma informação, nenhum aluno se enquadra na lista.): ")
        for aluno in lista_alunos:
            if aluno['Disciplina'].upper() == 'PYTHON':
                media = sum(aluno['Checkpoints']) / len(aluno['Checkpoints'])
                if media >= 7.0:
                    print(f"Código: {aluno['Código']}, Nome: {aluno['Nome']}")
                    print("---------------------------")

if __name__ == "__main__":
    main()
