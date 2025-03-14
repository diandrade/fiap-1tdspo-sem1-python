'''
Escreva um programa que solicite o peso e a altura de uma pessoa,
calcule o IMC (índice de massa corpórea) por meio da fórmula:
IMC = peso/altura*altura. Por fim, exiba o valor do IMC.
'''

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
print(f"O IMC da pessoa é: {peso / (altura * 2)}")
