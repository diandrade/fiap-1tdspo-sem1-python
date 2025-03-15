'''
Escreva um algoritmo para solicite o número total de eleitores de um município,
o número de votos brancos, nulos e válidos.
Calcular e escrever o percentual que cada um representa em relação ao total de eleitores
'''

votos_brancos = int(input("Insira o número total de votos brancos: "))
votos_nulos = int(input("Insira o número total de votos nulos: "))
votos_validos = int(input("Insira o número de votos válidos: "))
total_votos = votos_nulos + votos_validos + votos_brancos
print(f"Do total de {total_votos:.2f} votos, {(votos_validos * 100)/total_votos:.2f}% são válidos, {(votos_brancos * 100)/total_votos:.2f}% são brancos e {(votos_nulos * 100)/total_votos}% são nulos.")
