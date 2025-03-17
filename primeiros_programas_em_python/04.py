'''
Escreva um programa que solicite o peso e a altura de uma pessoa,
calcule o IMC (índice de massa corpórea) por meio da fórmula:
IMC = peso/altura*altura. Por fim, exiba o valor do IMC.
'''

peso_pessoa = float(input("Insira seu peso em KG: "))
altura_pessoa = float(input("Insira sua altura em Metros: "))
imc = peso_pessoa / altura_pessoa ** 2

print(f"O IMC da pessoa é: {imc:.2f}")
