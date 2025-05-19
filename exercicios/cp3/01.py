'''
GRAZIELLE ALENCAR - RM561529
DIEGO ANDRADE - RM566385
'''

def main():
    lista_funcionarios = []
    while True:
        print('''
        1 - Insira um funcionário.
        2 - Leia as informações de um funcionário.
        3 - Atualize as informações de um funcionário.
        4 - Delete um funcionário do sistema.
        5 - Exiba todos os funcionários inseridos no sistema.
        6 - Exibe um relatório dos funcionários com idade superior a 25 anos.
        7 - Exibe um relatório dos funcionários com idade entre 22 e 35 anos, cujo salário seja maior que R$3700,00.
        ''')

        opcao = int(input("Insira o opção desejada: (1 a 7): "))
        if 1 <= opcao <= 7:
            match opcao:
                case 1:
                    inserir_funcionario(lista_funcionarios)
                case 2:
                    codigo_funcionario = int(input("Digite o código do funcionário que deseja buscar: "))
                    indice = buscar_funcionario(lista_funcionarios, codigo_funcionario)
                    if indice != -1:
                        for chave, valor in lista_funcionarios[indice].items():
                            print(f"{chave}:{valor}")
                    else:
                        print("O código não consta na lista")
                case 3:
                    codigo_funcionario = int(input("Digite o código do funcionário que deseja alterar os dados: "))
                    indice = buscar_funcionario(lista_funcionarios, codigo_funcionario)
                    if indice != -1:
                        atualizar_funcionario(lista_funcionarios, indice)
                    else:
                        print("O código não consta na lista")
                case 4:
                    codigo_funcionario = int(input("Digite o código do funcionário que deseja excluir os dados: "))
                    indice = buscar_funcionario(lista_funcionarios, codigo_funcionario)
                    if indice != -1:
                        remover_funcionario(lista_funcionarios, indice)
                case 5:
                    exibir_funcionarios(lista_funcionarios)
                case 6:
                    relatorio_idade_superior_25(lista_funcionarios)
                case 7:
                    relatorio_faixa_idade_salario(lista_funcionarios)
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

def inserir_funcionario(lista_funcionarios):
    codigo_funcionario = int(input("Insira o código do usuário: "))
    nome_funcionario = input("Insira o nome do funcionário: ")
    idade_funcionario = int(input("Insira a idade do funcionário: "))
    sal_funcionario = float(input("Insira o salário do funcionário: "))

    funcionario = {
        'Código': codigo_funcionario,
        'Nome': nome_funcionario,
        'Idade': idade_funcionario,
        'Salário': sal_funcionario
    }
    lista_funcionarios.append(funcionario)

def buscar_funcionario(lista_funcionarios, codigo):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if lista_funcionarios[i]['Código'] == codigo:
            indice = i
    return indice

def atualizar_funcionario(lista_funcionarios, indice):
    print(f"Codigo atual do funcionário cadastrado no sistema: {lista_funcionarios[indice]['Código']}")
    lista_funcionarios[indice]['Código'] = int(input("Digite o novo código do funcionario: "))

    print(f"Nome atual do funcionário cadastrado no sistema: {lista_funcionarios[indice]['Nome']}")
    lista_funcionarios[indice]['Nome'] = input("Digite o novo nome do funcionario: ")

    print(f"Idade atual do funcionário cadastrado no sistema: {lista_funcionarios[indice]['Idade']}")
    lista_funcionarios[indice]['Idade'] = int(input("Digite a nova idade do funcionario: "))

    print(f"Salário atual do funcionário cadastrado no sistema: {lista_funcionarios[indice]['Salário']}")
    lista_funcionarios[indice]['Salário'] = float(input("Digite o novo salário do funcionário: "))

def remover_funcionario(lista_funcionarios, indice):
    lista_funcionarios.pop(indice)
    print("Funcionário removido com sucesso!")

def exibir_funcionarios(lista_funcionarios):
    for funcionario in lista_funcionarios:
        for chave, valor in funcionario.items():
            print(f"{chave}: {valor}")
        print("---------------------------")

def relatorio_idade_superior_25(lista_funcionarios):
    if len(lista_funcionarios) == 0:
        print("Registre ao menos 1 funcionário.")
    else:
        print("Segue abaixo, relatório de funcionários com idade superior a 25 anos"
              " (Caso não apareça nenhuma informação, nenhum funcionário se enquadra na lista.): ")
        for funcionario in lista_funcionarios:
            if funcionario['Idade'] > 25:
                print(f"Código: {funcionario['Código']}, Nome: {funcionario['Nome']}")
                print("---------------------------")

def relatorio_faixa_idade_salario(lista_funcionarios):
    if len(lista_funcionarios) == 0:
        print("Registre ao menos 1 funcionário.")
    else:
        print("Segue abaixo, relatório de funcionários entre 22 e 35 anos com salário maior do que R$3700,00"
              " (Caso não apareça nenhuma informação, nenhum funcionário se enquadra na lista.): ")
        for funcionario in lista_funcionarios:
            if 22 <= funcionario['Idade'] <= 35 and funcionario['Salário'] > 3700:
                print(f"Código: {funcionario['Código']}, Nome: {funcionario['Nome']}")
                print("---------------------------")

if __name__ == "__main__":
    main()
