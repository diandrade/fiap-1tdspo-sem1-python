'''
Escreva um programa que simule um dicionário inglês/português utilizando o conceito de listas.
Para tanto, crie uma lista para as palavras em inglês e outra para as traduções em português nas respectivas posições.
A inserção das palavras deverá ser executada até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).
Após a inserção, exiba a tradução em português de uma determinada palavra em inglês que o usuário deverá digitar.
'''

'''palavras = []

print("--- Cadastro de Palavras ---")
while True:
    portugues = input("Insira a palavra em Português: ")
    ingles = input("Insira a palavra em Inglês: ")

    novo_par = {'Português': portugues, 'Inglês': ingles}
    palavras.append(novo_par)

    while True:
        saida = int(input("Deseja continuar (1-SIM / 0-NÃO): "))

        if saida == 0 or saida == 1:
            break
        else:
            print("Opção inválida. (1-SIM / 0-NÃO).")

    if saida == 0:
        print("Cadastro finalizado.")
        break

print("\n--- Dicionário Cadastrado ---")

if len(palavras) == 0:
    print("Nenhuma palavra foi cadastrada.")
else:
    for palavra in palavras:
        print(f"Português: {palavra['Português']} | Inglês: {palavra['Inglês']}")
'''

lista_ingles = []
lista_portugues = []

resp = 1

# Loop para adicionar palavras ao dicionário
while resp == 1:
    palavra_ingles = input("Digite a palavra em Inglês: ")
    lista_ingles.append(palavra_ingles)

    palavra_portugues = input("Digite a palavra em Português: ")
    lista_portugues.append(palavra_portugues)

    # Pergunta se deseja continuar - CUIDADO: pode dar erro se digitar algo não numérico
    resp = int(input("Deseja continuar? (1 - SIM, 0 - NÃO): "))

# Loop para buscar traduções
while True: # Adicionado um loop para permitir múltiplas buscas
    palavra_ingles_usr = input("\nDigite a palavra em inglês que deseja saber a tradução (ou digite 'sair' para terminar): ")

    if palavra_ingles_usr.lower() == 'sair': # Opção para sair do loop de busca
        break

    if palavra_ingles_usr in lista_ingles:
        # Encontra o índice da primeira ocorrência da palavra na lista inglesa
        indice = lista_ingles.index(palavra_ingles_usr)
        # Usa o mesmo índice para buscar a palavra correspondente na lista portuguesa
        print(f"A tradução para português é: {lista_portugues[indice]}")
    else:
        # Informa se a palavra não foi encontrada
        print("A palavra não consta no dicionário.")

print("\nPrograma finalizado.")