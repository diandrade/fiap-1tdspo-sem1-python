def inserir_notas_aluno(i):
    for i in range(5):
        nota = float(input("Digite a nota do aluno: "))
        lista_notas.append(nota)

lista_notas = []
inserir_notas_aluno(lista_notas)

print(lista_notas)