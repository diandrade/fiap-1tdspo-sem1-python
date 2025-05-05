'''
Escreva um algoritmo para ler 10 números.
Todos os números lidos com valor inferior a 40 devem ser somados.
Escreva o valor final da soma efetuada.
'''

soma = 0
for i in range(1, 11):
    n = float(input("Insira um número: "))
    if n < 40:
        soma += n
print(f"O valor final da soma é: {soma:.2f}")
