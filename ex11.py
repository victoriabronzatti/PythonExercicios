# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
altura = float(input('Digita a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = (area / 2)
print('A sua parede tem a dimensão de {}x{}, e a sua área é de {}m². \n Para pintar essa parede, você precisára de {}l de tinta'.format(altura, largura, area, tinta))
