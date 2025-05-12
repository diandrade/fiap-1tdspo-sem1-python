'''
CRUD (create, read, update e delete) de funcionarios
'''

# A funcao main serve para conter um menu de opcoes com as chamadas das funcoes
def main():
    lista_funcionarios = []

    resp = 1

    while resp == 1:
        print("1-Inserir funcionario")
        print("2-Alterar funcionario")
        print("3-Buscar funcionario")
        print("4-Remover funcionario")
        print("5-Exibir todos os funcionarios")
        print("6-Relatorio dos funcionarios por cargo")
        opcao = int(input("Digite a opcao desejada (1 a 6): "))
        if 1 <= opcao <= 6:
            match opcao:
                case 1:
                    inserir_funcionario(lista_funcionarios)
                case 2:
                    nome_func = input("Digite o nome do funcionario que deseja alterar os dados: ")
                    indice = buscar_funcionario(lista_funcionarios,nome_func)
                    if indice != -1:
                        alterar_funcionario(lista_funcionarios, indice)
                    else:
                        print("O nome nao consta na lista")
                case 3:
                    nome_func = input("Digite o nome do funcionario que deseja buscar: ")
                    indice = buscar_funcionario(lista_funcionarios, nome_func)
                    if indice != -1:
                        for chave, valor in lista_funcionarios[indice].items():
                            print(f"{chave}:{valor}")
                    else:
                        print("O nome nao consta na lista")
                case 4:
                    nome_func = input("Digite o nome do funcionario que deseja remover: ")
                    indice = buscar_funcionario(lista_funcionarios, nome_func)
                    if indice != -1:
                        remover_funcionario(lista_funcionarios, indice)
                    else:
                        print("O nome nao consta na lista")
                case 5:
                    exibir_funcionarios(lista_funcionarios)
                case 6:
                    cargo = input("Digite o cargo para gerar o relatorio: ")
                    exibir_funcionarios_cargo(lista_funcionarios, cargo)

        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))

# Criar as funcoes do CRUD
def inserir_funcionario(lista_funcionarios):
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salario: "))
    funcionario = {
        'Nome':nome,
        'Cargo':cargo,
        'Salario':salario
    }
    lista_funcionarios.append(funcionario)

# Funcao para buscar um funcionario na lista pelo nome
'''
Retorno da funcao: 
- se o nome estiver na lista, a funcao 
deve retornar o indice onde o dicionario esta armazenado
- se o nome nao estiver na lista, a funcao deve retornar -1
'''
def buscar_funcionario(lista_funcionarios,nome):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if lista_funcionarios[i]['Nome'] == nome:
            indice = i
    return indice

def alterar_funcionario(lista_funcionarios,indice):
    print(f"Nome do funcionario: {lista_funcionarios[indice]['Nome']}")
    lista_funcionarios[indice]['Nome'] = input("Digite o novo nome do funcionario: ")
    print(f"Cargo do funcionario: {lista_funcionarios[indice]['Cargo']}")
    lista_funcionarios[indice]['Cargo'] = input("Digite o novo cargo do funcionario: ")
    print(f"Salario do funcionario: {lista_funcionarios[indice]['Salario']}")
    lista_funcionarios[indice]['Salario'] = float(input("Digite o novo salario do funcionario: "))
    print("Alteracao realizada com sucesso!")

def remover_funcionario(lista_funcionarios,indice):
    lista_funcionarios.pop(indice)
    print("Remocao realizada com sucesso!")

def exibir_funcionarios(lista_funcionarios):
    for funcionario in lista_funcionarios:
        for chave,valor in funcionario.items():
            print(f"{chave}: {valor}")
        print("---------------------------")

def exibir_funcionarios_cargo(lista_funcionarios,cargo):
    for funcionario in lista_funcionarios:
        if funcionario['Cargo'] == cargo:
            for chave, valor in funcionario.items():
                print(f"{chave}: {valor}")
            print("---------------------------")

# Boa pratica para chamar a funcao main
if __name__ == "__main__":
    main()
