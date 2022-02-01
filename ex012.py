# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o valor do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('Na liquidação o valor R${:.2f} vai ter desconto de 5% e sai por R${:.2f}'.format(preco, novo))