# Funções para inserção, e remoção de elementos na lista

lista_nomes = ["Ana", "Pedro", "João", "Antônio", "Maria"]

# Inserção (append: permite inserir um elemento no final da lista)
lista_nomes.append("Diego")
print(lista_nomes)

# Inserção (insert: permite inserir um elemento em um índice definido da lista)
lista_nomes.insert(2, "Ricardo")
print(lista_nomes)

# Remoção (pop: permite remover um elemento da lista)

# Primeira forma:
lista_nomes.pop() # remove o último elemento da lista
print(lista_nomes)

# Segunda forma:
lista_nomes.pop(2) # Remover o terceiro elemento da lista
print(lista_nomes)

