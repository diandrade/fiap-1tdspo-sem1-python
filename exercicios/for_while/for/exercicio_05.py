'''
Faça um programa em C que mostre na tela os números divisíveis por 6 compreendidos entre 50 e 100.
(Considere os números 50 e 100 e utilize estruturas de repetição).
'''

print (50)
for i in range(50, 100):
    if i % 6 == 0:
        print(i)
print (100)