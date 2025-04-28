'''
For = Adequada a momentos de precisão em relação ao range da funcionalidade (quantidade certeira de loops).
While = Adequada em outras hipóteses.
'''

soma = 0

num = int(input("Digite um número inteiro: "))

while num >= 0:
    soma += num
    num = int(input("Digite um número inteiro: "))

print(f"A soma dos números é: {soma}")