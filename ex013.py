# faça um algoritimo que leia o salário de um funcinário e mostre o seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do seu salário: '))
novoSalario = salario * 1.15
print('O seu atual salário é de R${:.3f} e o seu novo salário é de R${:.2f}.'.format(salario, novoSalario))
