'''Uma função com dois parâmetros (a e b) que mostre o maior deles;'''


def maior(a, b):
    if a > b:
        return a
    else:
        return b


num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

print(f"O maior valor entre os dois é: {maior(num1, num2)}")
