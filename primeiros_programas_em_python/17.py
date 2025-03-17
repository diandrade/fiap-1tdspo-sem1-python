'''
Escreva um programa que solicite 2 números inteiros p e q,
faça a troca de seus valores e, no final, exiba p e q.
(Exemplo: p=5 e q=7; após a troca: p=7 e q=5)
(Corrigir)
'''

p = int(input("Insira P: "))
q = int(input("Insira Q: "))
x = p
p = q
q = x
print(f"P: {p}", f"Q: {q}")