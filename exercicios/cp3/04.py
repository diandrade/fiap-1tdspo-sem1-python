'''
GRAZIELLE ALENCAR - RM561529
DIEGO ANDRADE - RM566385
'''

def main():
    lista_clientes = []
    while True:
        print('''
        1 - Insira um cliente.
        2 - Leia as informações de um cliente.
        3 - Atualize as informações de um cliente.
        4 - Delete um cliente do sistema.
        5 - Exiba todos os clientes inseridos no sistema.
        6 - Exibe um relatório dos clientes com limite de crédito inferior a R$5000,00.
        7 - Exibe um relatório dos clientes com idade entre 25 e 45 anos e limite superior a R$2000.
        ''')

        opcao = int(input("Insira a opção desejada: (1 a 7): "))
        if 1 <= opcao <= 7:
            match opcao:
                case 1:
                    inserir_cliente(lista_clientes)
                case 2:
                    codigo = int(input("Digite o código do cliente que deseja buscar: "))
                    indice = buscar_cliente(lista_clientes, codigo)
                    if indice != -1:
                        for chave, valor in lista_clientes[indice].items():
                            print(f"{chave}: {valor}")
                    else:
                        print("O código não consta na lista")
                case 3:
                    codigo = int(input("Digite o código do cliente que deseja alterar: "))
                    indice = buscar_cliente(lista_clientes, codigo)
                    if indice != -1:
                        atualizar_cliente(lista_clientes, indice)
                    else:
                        print("O código não consta na lista")
                case 4:
                    codigo = int(input("Digite o código do cliente que deseja remover: "))
                    indice = buscar_cliente(lista_clientes, codigo)
                    if indice != -1:
                        remover_cliente(lista_clientes, indice)
                case 5:
                    exibir_clientes(lista_clientes)
                case 6:
                    relatorio_limite(lista_clientes)
                case 7:
                    relatorio_idade_limite(lista_clientes)
        else:
            print("Opção inválida.")

        resp = int(input("Deseja continuar? (1-SIM/0-NÃO): "))
        while True:
            if resp != 0 and resp != 1:
                resp = int(input("Deseja continuar? (1-SIM/0-NÃO): "))
            else:
                break
        if resp == 0:
            break

def inserir_cliente(lista_clientes):
    codigo = int(input("Insira o código do cliente: "))
    nome = input("Insira o nome do cliente: ")
    cpf = input("Insira o CPF do cliente: ")
    idade = int(input("Insira a idade do cliente: "))
    endereco = input("Insira o endereço do cliente: ")
    limite = float(input("Insira o limite de crédito do cliente: "))
    cliente = {
        'Código': codigo,
        'Nome': nome,
        'CPF': cpf,
        'Idade': idade,
        'Endereço': endereco,
        'Limite': limite
    }
    lista_clientes.append(cliente)

def buscar_cliente(lista_clientes, codigo):
    indice = -1
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['Código'] == codigo:
            indice = i
    return indice

def atualizar_cliente(lista_clientes, indice):
    print(f"Código atual do cliente cadastrado no sistema: {lista_clientes[indice]['Código']}")
    lista_clientes[indice]['Código'] = int(input("Digite o novo código do cliente: "))

    print(f"Nome atual do cliente cadastrado no sistema: {lista_clientes[indice]['Nome']}")
    lista_clientes[indice]['Nome'] = input("Digite o novo nome do cliente: ")

    print(f"Curso atual do cliente cadastrado no sistema: {lista_clientes[indice]['Curso']}")
    lista_clientes[indice]['CPF'] = input("Digite o novo CPF do cliente: ")

    print(f"Disciplina atual do cliente cadastrado no sistema: {lista_clientes[indice]['Disciplina']}")
    lista_clientes[indice]['Idade'] = int(input("Digite a nova idade do cliente: "))

    print(f"Faltas atuais do cliente cadastrado no sistema: {lista_clientes[indice]['Faltas']}")
    lista_clientes[indice]['Endereço'] = input("Digite o novo endereço do cliente: ")

    print(f"Limite atual de crédito do cliente cadastrado no sistema: {lista_clientes[indice]['Limite']}")
    lista_clientes[indice]['Limite'] = float(input("Digite o novo limite de crédito do cliente: "))

def remover_cliente(lista_clientes, indice):
    lista_clientes.pop(indice)
    print("Cliente removido com sucesso!")

def exibir_clientes(lista_clientes):
    for cliente in lista_clientes:
        for chave, valor in cliente.items():
            print(f"{chave}: {valor}")
        print("---------------------------")

def relatorio_limite(lista_clientes):
    if len(lista_clientes) == 0:
        print("Registre ao menos 1 cliente.")
    else:
        print("Segue abaixo, relatório dos clientes em código e nome com limite de crédito inferior a R$5000,00."
              " (Caso não apareça nenhuma informação, nenhum cliente se enquadra na lista.): ")
        for cliente in lista_clientes:
            if cliente['Limite'] < 5000:
                print(f"Código: {cliente['Código']}, Nome: {cliente['Nome']}, Limite: R${cliente['Limite']:.2f}")
                print("---------------------------")

def relatorio_idade_limite(lista_clientes):
    if len(lista_clientes) == 0:
        print("Registre ao menos 1 cliente.")
    else:
        print("Segue abaixo, relatório dos clientes em código e nome com idade entre 25 e 45 anos e limite superior a R$2000:"
              " (Caso não apareça nenhuma informação, nenhum cliente se enquadra na lista.): ")
        for cliente in lista_clientes:
            if 25 <= cliente['Idade'] <= 45 and cliente['Limite'] > 2000:
                print(f"Código: {cliente['Código']}, Nome: {cliente['Nome']}")
                print("---------------------------")

if __name__ == "__main__":
    main()
