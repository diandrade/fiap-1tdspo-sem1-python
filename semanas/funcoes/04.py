'''
CRUD (create, read, update e delete) de funcionarios
'''


# A funcao main serve para conter um menu de opcoes com as chamadas das funcoes
def main():
    lista_funcionarios = []

    resp = 1

    while (resp == 1):
        print("1-Inserir funcionario")
        print("2-Alterar funcionario")
        print("3-Buscar funcionario")
        print("4-Remover funcionario")
        print("5-Exibir todos os funcionarios")
        opcao = int(input("Digite a opcao desejada (1 a 5): "))
        if (opcao >= 1 and opcao <= 5):
            match opcao:
                case 1:
                    inserir_funcionario(lista_funcionarios)
                case 2:
                    nome_func = input("Digite o nome do funcionário que deseja buscar")
                    indice = buscar_funcionario(lista_funcionarios)
        else:
            print("Opcao invalida")

        resp = int(input("Deseja continuar (1-SIM/0-NAO)? "))


# Criar as funcoes do CRUD
def inserir_funcionario(lista_funcionarios):
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salario: "))
    funcionario = {
        'Nome': nome,
        'Cargo': cargo,
        'Salario': salario
    }
    lista_funcionarios.append(funcionario)


def buscar_funcionario(lista_funcionarios, nome):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if lista_funcionarios[i]['Nome'] == nome:
            indice = i
    return indice

def remover_funcionario(lista_funcionarios,indice):
    lista_funcionarios.pop(indice)
    print("Remoção realizada com sucesso!")

def exibir_funcionarios(lista_funcionarios):
    for funcionario in lista_funcionarios:
        for chave,valor in funcionario.items():
            print(f"{chave}: {valor}")
        print("---------------------")



# Boa pratica para chamar a funcao main
if (__name__ == "__main__"):
    main()
