'''
Cálcular e exibir a média de 3 avaliações para 5 alunos.
'''

for cont in range(5): # Cont varia de 0 a 4
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    print(f"A média do aluno {cont+1} é {media:.1f}")
