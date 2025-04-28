'''
Um condomínio possui 20 blocos e para uma correta administração possui dois síndicos:
o sr José que administra os blocos de 1 a 10 e
o sr Hamilton que administra os blocos de 11 a 20.
Escreva um algoritmo que solicite ao usuário em
qual bloco ele mora e escreva na tela qual o síndico responsável.
'''

bloco = int(input("Insira seu bloco: "))
if 1 <= bloco <= 20:
    if bloco <= 10:
        print(f"O usuário mora no bloco {bloco} e seu síndico responsável é o Sr. José.")
    else:
        print(f"O usuário mora no bloco {bloco} e seu síndico responsável é o Sr. Hamilton.")
else:
    print("Insirá um bloco válido.")