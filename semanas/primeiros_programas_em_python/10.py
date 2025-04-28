'''
Escreva um algoritmo para calcular a média aritmética de
3 avaliações que deverão ser informadas.
Por fim, exiba o valor da média.
'''

primeira_avaliacao = float(input("Insira a nota da primeira avaliação: "))
segunda_avaliacao = float(input("Insira a nota da segunda avaliação: "))
terceira_avaliacao = float(input("Insira a nota da terceira avaliação: "))
media_aritmetica = ((primeira_avaliacao + segunda_avaliacao + terceira_avaliacao) / 3)

print(f"A média aritmética das 3 avaliações é: {media_aritmetica:.2f}")
