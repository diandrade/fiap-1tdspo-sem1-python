'''
Faça um programa que verifique se uma "senha” numérica digitada pelo usuário está correta. O programa deve repetir
o pedido até que o usuário escreva o valor correto. A senha correta deve estar definida no próprio programa.
'''

qtdTentativas = 0

senha_usuario = int(input("Insira uma senha: "))
senha_correta = 10

while senha_usuario != senha_correta:
    qtdTentativas += 1
    if qtdTentativas >= 3:
        print("Você atingiu o numero de tentativas existentes.")
        break
    else:
        senha_usuario = int(input("Insira uma senha: "))

if senha_usuario == senha_correta:
    print("Parabéns, você inseriu a senha correta!")
