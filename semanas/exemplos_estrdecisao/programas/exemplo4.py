'''
Mostrar o tipo de modalidade da natação

- idade entre 5 e 12 anos: infantil
- idade entre 13 e 18 anos: juvenil
- idade entre 19 e 59 anos: adulta
- idade maior que 59 anos: senil

IMPORTANTE: o atleta deve ter idade entre 5 e 80 anos
'''

'''
Operadores lógicos:

- and (e): verdadeiro se todas as condições forem verdade
- or (ou): verdadeiro se pelo menos uma condição for verdade
'''

idade_atleta = int(input("Digite a idade do atleta: "))

if (idade_atleta >= 5 and idade_atleta <= 80):
    if (idade_atleta <= 12):
        print("Modalidade infantil")
    elif (idade_atleta <= 18):
        print("Modalidade juvenil")
    elif (idade_atleta <= 59):
        print("Modalidade adulta")
    else:
        print("Modalidade senil")
else:
    print("Idade não permitida para a competição")