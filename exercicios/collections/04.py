'''
Escreva um programa que simule um dicionário inglês/português utilizando o conceito de listas.
Para tanto, crie uma lista para as palavras em inglês e outra para as traduções em português nas respectivas posições.
A inserção das palavras deverá ser executada até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).
Após a inserção, exiba a tradução em português de uma determinada palavra em inglês que o usuário deverá digitar.
'''

palavras = []

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
