# Lista de Dicionários

'''
Solicitar que o usuário digite dados de 5 usuários que ir]ao utilizar o sistema. Em seguida, exiba os dados de cada usuário.
'''

lista_usuarios = []

for i in range(5):
    user_name = input("Digite o username do usuário: ")
    user_pwd = input("Digite a senha do usuário: ")
    user_cpf = int(input("Digite o CPF do usuário: "))
    usuario = {
        'User_name' : user_name,
        'User_pwd' : user_pwd,
        'User_CPF' : user_cpf
    }
    lista_usuarios.append(usuario)


# Exibir os usuários da lista
for i in range(5):
    for chave, valor in lista_usuarios[i].items():
        print(f"{chave}: {valor}")
    print("-----------------------------------")