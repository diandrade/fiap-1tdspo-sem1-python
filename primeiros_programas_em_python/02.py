'''
Escreva um programa que solicite a base e a altura de um triângulo,
calcule sua área por meio da fórmula: area = (base x altura)/2.
Por fim, exiba a área do triângulo.
'''

base_triangulo = float(input("Base: "))
altura_triangulo = float(input("Altura: "))
area_triangulo = (base_triangulo * altura_triangulo) / 2

print(f"A área é: {area_triangulo:.2f}")
