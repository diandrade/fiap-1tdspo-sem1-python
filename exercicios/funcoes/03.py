'''
Uma função com um parâmetro n que verifique e mostre se ele é par ou ímpar;
'''


def par(n):
    if n % 2 == 0:
        return "Par."
    return "Impar."


num = float(input("Insira um número: "))
print(par(num))
