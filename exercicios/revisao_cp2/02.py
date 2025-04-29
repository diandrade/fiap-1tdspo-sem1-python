habitantes_participantes = 0
qtd_total_salario = 0
qtd_total_filhos = 0
maior_salario = 0
habitantes_inferior_a_150 = 0

while True:
    salario = float(input("Insira o salário do habitante participante da pesquisa: "))
    if salario < 0:
        break
    else:
        habitantes_participantes += 1
        filhos = int(input("Insira o número de filhos do habitante participante da pesquisa: "))
        if filhos <= 0:
            filhos = 0
        else:
            qtd_total_salario += salario
            qtd_total_filhos += filhos
            if salario > maior_salario:
                maior_salario = salario
            if salario < 150.00:
                habitantes_inferior_a_150 += 1

if qtd_total_salario > 0:
    media_salario = qtd_total_salario / habitantes_participantes
else:
    media_salario = 0

if qtd_total_filhos > 0:
    media_filhos = qtd_total_filhos / habitantes_participantes
else:
    media_filhos = 0

if habitantes_inferior_a_150 > 0:
    percentual_150 = habitantes_inferior_a_150 * 100 / habitantes_participantes
else:
    percentual_150 = 0

print(f"A média salárial da população entrevistada é: R$ {media_salario:.2f}")
print(f"A média do número de filhos da população entrevistada é: {media_filhos:.2f}")
print(f"O maior salário entre a população entrevistada foi de: R$ {maior_salario}")
print(f"O percentual da população entrevistada com salário menor que R$ 150,00 foi de: {percentual_150:.2f}%")
