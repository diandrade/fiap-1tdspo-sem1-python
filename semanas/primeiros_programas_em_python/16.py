'''
Escreva um algoritmo para solicite o número total de eleitores de um município,
o número de votos brancos, nulos e válidos.
Calcular e escrever o percentual que cada um representa em relação ao total de eleitores
'''

votos_brancos = int(input("Insira o número total de votos brancos: "))
votos_nulos = int(input("Insira o número total de votos nulos: "))
votos_validos = int(input("Insira o número de votos válidos: "))

total_votos = votos_nulos + votos_validos + votos_brancos

percentual_validos = (votos_validos * 100)/total_votos
percental_brancos = (votos_brancos * 100)/total_votos
percentual_nulos = (votos_nulos * 100)/total_votos

print(f"Do total de {total_votos:.2f} votos, {percentual_validos:.2f}% são válidos, {percental_brancos:.2f}% são "
      f"brancos e {percentual_nulos:.2f}% são nulos.")
