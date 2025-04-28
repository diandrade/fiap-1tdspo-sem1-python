# Dicionários em Python

# Criar um dicionário para armazenar dados de um aluno
aluno = {'RM': 566385, 'Nome': "Diego Andrade", 'Curso': "TDS", 'Media_geral': 8.5}

# Exibir o dicionário (forma mais simples)
print(aluno)

# Exibir o curso do aluno
print(f"O curso do aluno é: {aluno['Curso']}")

# Exibir cada item do dicionário separadamente
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
