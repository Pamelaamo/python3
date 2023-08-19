# Faça um algoritmo que leia o salário de um funcionário e mostra seu novo salário, com 15 % de aumento.

print('=' * 90)
salário = float(input('Informe o salário do funcionário: '))
novo = salário + (salário * 20 / 100)
print('O funcionário recebe R${:.2f}, e com o aumento de 20 % , irá passar a ganhar R${:.2f}' .format(salário, novo))
print('=' * 90)
