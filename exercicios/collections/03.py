'''
Desenvolva um programa que preencha um vetor com as idades dos usuários até que o usuário digite um valor negativo,
o valor negativo não deve ser inserido na lista. Ao final, exiba na tela:

- A quantidade de usuários menores de 18 anos;

- A média das idades.
'''

usuarios = []
menores_18 = []

while True:
    idade = int(input("Insira a idade dos usuários: "))

    if idade < 0:
        break

    usuarios.append(idade)

len_usuarios = len(usuarios)
sum_usuarios = sum(usuarios)
media_usuarios = sum_usuarios / len_usuarios

for i in usuarios:
    if i < 18:
        menores_18.append(i)

print(f"A quantidade de usuários menores de 18 anos é de: {len(menores_18)}")
print(f"A média das idades dos usuários é de: {media_usuarios}")
