# Exemplo 5: Cálcular a média de 10 números dígitados pelo usuário

soma = 0

for cont in range(10): # Cont vai variar de 0 até o 9.
    num = int(input("Digite um número: "))
    soma += num

media = soma / 10
print(f"A média dos 10 números é: {media:.2f}")