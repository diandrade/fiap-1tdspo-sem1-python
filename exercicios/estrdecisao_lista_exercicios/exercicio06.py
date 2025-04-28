'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
e R$ 1,00 se forem compradas pelo menos 12.
Escreva um programa que solicite o número de maçãs compradas,
calcule e escreva o custo total da compra.
'''

macas = int(input("Informe o número de maçãs: "))
if macas >= 1:
    if macas < 12:
        macas *= 1.30
        print(f"O custo total da compra foi R${macas:.2f}")
    else:
        macas *= 1.00
        print(f"O custo total da compra foi R${macas:.2f}")
else:
    print("Insira um número positivo")
