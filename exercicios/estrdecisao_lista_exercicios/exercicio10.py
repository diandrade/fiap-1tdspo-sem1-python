'''
Uma livraria resolveu fazer uma promoção, com os seguintes critérios:

o Livros com preços até R$ 10,00 - desconto de 8%

o Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10%

o Livros com preços acima de R$ 60,00 - desconto de 20%

Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto oferecido,
em reais.
'''

preco_sem_desconto = float(input("Insira o valor do livro desejado: "))

if preco_sem_desconto <= 0:
    print("Insira um valor positivo para o livro.")
else:
    if preco_sem_desconto <= 10:
        preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 0.08)
        print(f"O valor do livro com desconto é: {preco_com_desconto:.2f}")

    elif preco_sem_desconto <= 60:
        preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 0.10)
        print(f"O valor do livro com desconto é: {preco_com_desconto:.2f}")

    else:
        preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 0.20)
        print(f"O valor do livro com desconto é: R${preco_com_desconto:.2f}")
