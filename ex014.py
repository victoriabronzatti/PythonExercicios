# escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura em C: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))