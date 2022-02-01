# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímitros
media = float(input('Digite um valor: '))
centimetros = media * 100
milimetros = media * 1000
print('A media de {}m corresponde a {}c e {}mm'. format(media, centimetros, milimetros))
