# Conversor de Moedas
real = float(input('Quando dinheiro você tem na carteira? R$ '))
print('-' * 43)
dolar = real / 4.98
print('Com R${} você pode comprar U${:.2f}' .format(real, dolar))