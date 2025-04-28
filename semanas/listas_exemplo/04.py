'''
Solicitar que o usuário informe 7 salários de funcionários para criar uma lista. Em seguida,
crie uma nova lista com o acrescimo de 30% sobre os salários da primeira lista.
'''
lista_salarios = [] # Criando uma lista vazia
lista_salarios_acrescimo = []

for i in range(7): # i vai variar de 0 a 6
    salario = float(input("Digite o salário do funcionário para armazenar a lista: "))
    lista_salarios.append(salario)

print(lista_salarios)

# Calcular 30% de acrescimo nos salarios da lista e armazena-los na segunda lista.
for salario in lista_salarios:
    salario_acrescimo = salario * 1.30
    lista_salarios_acrescimo.append(salario_acrescimo)

print(lista_salarios_acrescimo)

# Outra forma de exibir elementos separadamente
for i in range(7):
    print(lista_salarios_acrescimo[i])