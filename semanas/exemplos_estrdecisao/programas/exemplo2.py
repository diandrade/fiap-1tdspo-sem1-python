# Exemplo: Mostrar se um número inteiro é par ou impar

# OBS: == comparação / = Atribuição

num = int(input("Digite um número inteiro: "))

resto_divisao = num % 2

if (resto_divisao == 0):
    print("O número é par")
else:
    print("O número é ímpar")