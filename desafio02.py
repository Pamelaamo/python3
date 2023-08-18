# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))
dob = n * 2
tri = n * 3
ra = n ** (1/2)
print('O dobro de {} vale {}.' .format(n, dob))
print('O triplo de {} vale {}.' .format(n, tri))
print('E a raiz quadrada de {} vale {:.3f}.' .format(n, ra))