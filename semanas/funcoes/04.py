'''
CRUD de funcionários

A função main servirá para conter o menu de opções
'''

# Função para inserir um novo funcionário na lista
def inserir_funcionario(lista_funcionarios):
    print("\n--- Inserir Funcionário ---")
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    # ATENÇÃO: Se digitar texto aqui, o programa vai parar com erro!
    salario = float(input("Salário: "))

    funcionario = {
        'Nome': nome,
        'Cargo': cargo,
        'Salário': salario
    }
    lista_funcionarios.append(funcionario)
    print("Funcionário inserido com sucesso!")

# Função para exibir todos os funcionários
def exibir_funcionarios(lista_funcionarios):
    print("\n--- Lista de Funcionários ---")
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    # enumerate gera o índice (i) e o item (funcionario) da lista
    for i, funcionario in enumerate(lista_funcionarios):
        print(f"--- Funcionário {i+1} ---") # Mostra um número sequencial
        print(f"  Nome: {funcionario['Nome']}")
        print(f"  Cargo: {funcionario['Cargo']}")
        print(f"  Salário: R$ {funcionario['Salário']:.2f}")
    print("-" * 28)

# Função principal com o menu
def main():
    lista_funcionarios = []
    resp = 1

    while resp == 1:
        print("\n--- Menu Principal ---")
        print("1 - Inserir Funcionário")
        print("2 - Alterar Funcionário (Não implementado)")
        print("3 - Buscar Funcionário (Não implementado)")
        print("4 - Remover Funcionário (Não implementado)")
        print("5 - Exibir todos os Funcionários")
        print("0 - Sair")

        # ATENÇÃO: Se digitar texto aqui, o programa vai parar com erro!
        opcao = int(input("Digite a opção desejada: "))

        if 0 <= opcao <= 5:
            match opcao:
                case 1:
                    inserir_funcionario(lista_funcionarios)
                case 5:
                    exibir_funcionarios(lista_funcionarios)
                case 0:
                    print("Saindo do programa...")
                    resp = 0 # Define resp como 0 para sair do loop principal
                case _: # Casos 2, 3, 4
                    print("Opção ainda não implementada.")
        else:
            print("Opção Inválida (escolha entre 0 e 5).")

        # Se o usuário já escolheu sair (opcao 0), não pergunta para continuar
        if resp == 0:
            break # Sai imediatamente do loop while resp == 1

        # Pergunta se deseja realizar outra operação
        # ATENÇÃO: Se digitar texto aqui, o programa vai parar com erro!
        resp_input = int(input("\nDeseja realizar outra operação? (1 - Sim | 0 - Não): "))

        if resp_input == 0:
            resp = 0 # Define resp como 0 para sair do loop principal
            print("Saindo do programa...")
        elif resp_input != 1:
             # Se não for 0 nem 1, informa que é inválido, mas continua (resp ainda é 1 por padrão)
             print("Opção inválida para continuar, mas seguindo...")
             # Ou você poderia forçar a saída se quisesse ser mais rigoroso:
             # resp = 0
             # print("Opção inválida. Saindo...")

# Boa prática para chamar a função main
# Correção principal que faz o código rodar: __main__
if __name__ == "__main__":
    main()