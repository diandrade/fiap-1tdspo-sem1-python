'''
Escreva um algoritmo para calcular a média aritmética de
3 avaliações que deverão ser informadas.
Por fim, exiba o valor da média.
'''

primeira_avaliacao = int(input("Insira a nota da primeira avaliação: "))
segunda_avaliacao = int(input("Insira a nota da segunda avaliação: "))
terceira_avaliacao = int(input("Insira a nota da terceira avaliação: "))
print(f"A média aritmética das 3 avaliações é: {((primeira_avaliacao + segunda_avaliacao + terceira_avaliacao) / 3):.2f}")
