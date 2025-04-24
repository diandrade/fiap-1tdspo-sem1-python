# Funções ,aos utilizadas em listas

lista_idades = [20, 21, 19, 23, 30, 15]

# Função que retorna o tamanho da lista
tamanho = len(lista_idades)
print(f"O tamanho da lista é {tamanho}")

# Função que retorna o somatório dos elementos da lista
soma = sum(lista_idades)
print(f"O somatório dos elementos da lista é {soma}")

# Função que retorna o maior elemento da lista
maior = max(lista_idades)
print(f"O maior elemento da lista é {maior}")

# Função que retorna o menor elemento da lista
menor = min(lista_idades)
print(f"O menor elemento da lista é: {menor}")

# Cálcular a média dos elementos da lista
media = sum(lista_idades) / len(lista_idades)
print(f"A média dos elementos da lista é {media:.2f}")

# Função para ordenar os elementos da lista

# Ordem Crescente
lista_crescente = sorted(lista_idades)
print(lista_crescente)

# Ordem Decrescente
lista_decrescente = sorted(lista_idades, reverse=True)
print(lista_decrescente)

# Procurar um elemento na lista
elemento = int(input("Digite um elemento a ser procurado na lista: "))
if elemento in lista_idades:
    print("O elemento pertence a lista.")
else:
    print("O elemento não pertence à lista.")

# Função que retorna o índice de um elemento pertence a lista
if elemento in lista_idades:
    indice = lista_idades.index(elemento)
    print(f"{elemento} está armazenado no índice {indice}")
