'''
GRAZIELLE ALENCAR - RM561529
DIEGO ANDRADE - RM566385
'''

def main():
    lista_produtos = []
    while True:
        print('''
        1 - Insira um produto.
        2 - Leia as informações do produto.
        3 - Atualize as informações do produto.
        4 - Delete um produto do sistema.
        5 - Exiba todos os produtos inseridos no sistema.
        6 - Exibe um relatório dos produtos cujo valor esteja entre R$150,00 e R$500,00.
        7 - Exibe um relatório dos produtos com quantidade superior a 100 unidades.
        ''')

        opcao = int(input("Insira o opção desejada: (1 a 7): "))
        if 1 <= opcao <= 7:
            match opcao:
                case 1:
                    inserir_produto(lista_produtos)
                case 2:
                    codigo_produto = int(input("Digite o código do produto que deseja buscar: "))
                    indice = buscar_produto(lista_produtos, codigo_produto)
                    if indice != -1:
                        for chave, valor in lista_produtos[indice].items():
                            print(f"{chave}:{valor}")
                    else:
                        print("O código não consta na lista")
                case 3:
                    codigo_produto = int(input("Digite o código do produto que deseja alterar os dados: "))
                    indice = buscar_produto(lista_produtos, codigo_produto)
                    if indice != -1:
                        atualizar_produto(lista_produtos, indice)
                    else:
                        print("O código não consta na lista")
                case 4:
                    codigo_produto = int(input("Digite o código do produto que deseja excluir os dados: "))
                    indice = buscar_produto(lista_produtos, codigo_produto)
                    if indice != -1:
                        remover_produto(lista_produtos, indice)
                case 5:
                    exibir_produtos(lista_produtos)
                case 6:
                    relatorio_valor_produto(lista_produtos)
                case 7:
                    relatorio_qtd_unidades(lista_produtos)
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

def inserir_produto(lista_produtos):
    codigo_produto = int(input("Insira o código do produto: "))
    descricao_produto = input("Insira a descrição do produto: ")
    qtd_produto = int(input("Insira a quantidade do produto em estoque: "))
    val_produto = float(input("Insira o valor do produto: "))

    produto = {
        'Código': codigo_produto,
        'Descrição': descricao_produto,
        'Quantidade': qtd_produto,
        'Valor': val_produto
    }
    lista_produtos.append(produto)

def buscar_produto(lista_produtos, codigo):
    indice = -1
    for i in range(len(lista_produtos)):
        if lista_produtos[i]['Código'] == codigo:
            indice = i
    return indice

def atualizar_produto(lista_produtos, indice):
    print(f"Codigo atual do produto cadastrado no sistema: {lista_produtos[indice]['Código']}")
    lista_produtos[indice]['Código'] = int(input("Digite o novo código do produto: "))

    print(f"Descrição atual do produto cadastrado no sistema: {lista_produtos[indice]['Descrição']}")
    lista_produtos[indice]['Descrição'] = input("Digite a nova descrição do produto: ")

    print(f"Quantidade atual do produto cadastrado no sistema: {lista_produtos[indice]['Quantidade']}")
    lista_produtos[indice]['Quantidade'] = int(input("Digite a nova quantidade de unidades do produto: "))

    print(f"Valor atual do produto cadastrado no sistema: {lista_produtos[indice]['Valor']}")
    lista_produtos[indice]['Valor'] = float(input("Digite o novo valor do produto: "))

def remover_produto(lista_produtos, indice):
    lista_produtos.pop(indice)
    print("Produto removido com sucesso!")

def exibir_produtos(lista_produtos):
    for produto in lista_produtos:
        for chave, valor in produto.items():
            print(f"{chave}: {valor}")
        print("---------------------------")

def relatorio_valor_produto(lista_produtos):
    if len(lista_produtos) == 0:
        print("Registre ao menos 1 produto.")
    else:
        print("Segue abaixo, relatório em código dos produtos entre R$150,00 e R$500,00"
              " (Caso não apareça nenhuma informação, nenhum produto se enquadra na lista.): ")
        for produto in lista_produtos:
            if 150.00 <= produto['Valor'] <= 500.00:
                print(f"Código: {produto['Código']}")
                print("---------------------------")

def relatorio_qtd_unidades(lista_produtos):
    if len(lista_produtos) == 0:
        print("Registre ao menos 1 produto.")
    else:
        print("Segue abaixo, relatório em código dos produtos com quantidade superior a 100 unidades: "
              " (Caso não apareça nenhuma informação, nenhum produto se enquadra na lista.): ")
        for produto in lista_produtos:
            if produto['Quantidade'] > 100:
                print(f"Código: {produto['Código']}")
                print("---------------------------")

if __name__ == "__main__":
    main()
