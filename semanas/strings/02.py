palavra = input("Digite uma palavra: ")

qtde_letras = len(palavra)
print(f"A palavra {palavra} têm {qtde_letras} letras.")

palavra_minuscula = palavra.lower()
print(f"Palavra com as letras minúsculas: {palavra_minuscula}")

palavra_maiuscula = palavra.upper()
print(f"Palavra com as letras minúsculas: {palavra_maiuscula}")

frase = input("Digite uma frase: ")
palavra_sub = input("Digite a palavra que quer substituir na frase: ")
palavra_sub2 = input(f"Digite a palavra que deseja colocar no lugar de {palavra_sub}: ")

nova_frase = frase.replace(palavra_sub, palavra_sub2)

print(nova_frase)

lista_palavras = frase.split()
print(lista_palavras)

print(f"Segunda palavra da frase: {lista_palavras[1]}")

data = input("Digite uma data no formato dd/mm/aaaa: ")
lista_data = data.split("/")
print(lista_data)

mes_extenso = "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Outubro", "Novembro", "Dezembro"
mes_int = int(lista_data[1])

data_extenso = lista_data[0] + " de " + mes_extenso[mes_int - 1] + " de " + lista_data[2]
print(data_extenso)

palavra_invertida = palavra[:: - 1]
print(palavra_invertida)