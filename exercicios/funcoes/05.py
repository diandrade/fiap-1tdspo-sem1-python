'''
uma função chamada somaImposto, que possua dois parâmetros: taxaImposto, que é a quantia de imposto sobre
vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de
custo para incluir o imposto sobre vendas e deve retornar o custo com o imposto.
'''


def soma_imposto(taxa_imposto, custo):
    custo *= taxa_imposto / 100 + 1
    return custo


print(f"O valor do produto após a inserção do imposto é de: R${soma_imposto(15, 1500):.2f}")
