'''
Escreva um programa em Python que solicite
3 notas de avaliações, cálcule e mostre a média aritmética dessas avaliações.
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é {media:.1f}")