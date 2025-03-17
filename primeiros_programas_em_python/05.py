'''
Escreva um programa que solicite o valor da cotação do dólar (em reais) do dia,
faça a conversão de um valor em dólares para reais.
Em seguida, exiba o valor que foi convertido para reais.
'''

valor_cotacao_dolar = float(input("Insira a cotação do dolar no dia atual: "))
quantidade_de_dolares = float(input("Insira a quantidade de dólares que você deseja converter para reais: "))
valor_reais = quantidade_de_dolares * valor_cotacao_dolar

print(
    f"A quantidade de reais convertidos a partir de U${quantidade_de_dolares} doláres é R${valor_reais:.2f}")
