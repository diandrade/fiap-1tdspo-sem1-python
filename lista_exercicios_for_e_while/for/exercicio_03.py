'''
Desenvolva um programa que receba:

- taxa de abatimento em porcentagem;

- número de prestações;

- valor da primeira prestação.

Seu programa deverá exibir na tela os valores das prestações na forma decrescente, dado que a cada mês
o valor da prestação diminui do valor da prestação do mês anterior
(utilize a taxa de abatimento fornecida pelo usuário para realizar esse cálculo). OBS: utilize o “for”.
'''

taxa_abatimento = float(input("Insira a taxa de abatimento em porcentagem: "))
numero_prestacoes = int(input("Insira a quantidade de prestações: "))
primeira_prestacao = float(input("Insira o valor da primeira prestação: "))

conversao_taxa = taxa_abatimento / 100
decimal_subtraido = 1 - conversao_taxa

print(f"O valor da prestação 1 é: {primeira_prestacao:.2f}")
for i in range(1, numero_prestacoes, 1):
    primeira_prestacao *= decimal_subtraido
    print(f"O valor da prestação {i+1} é: {primeira_prestacao:.2f}")
