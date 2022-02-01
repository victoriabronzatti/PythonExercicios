# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. considere o dolar R$ 5,31
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = dinheiro / 5.31
print('Você tem R${:.2f} em sua carteira. E você pode comprar US${:.2f}.'.format(dinheiro, dolar))
