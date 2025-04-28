# Exemplo: Cálcular o somatório dos números de 4 até 40

soma = 0 #Inicializando a variável do somatório

for cont in range(4, 41):
    soma += cont

print(f"A soma dos número entre 4 e 40 é: {soma}")