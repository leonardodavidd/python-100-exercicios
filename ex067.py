#Calculando o fatorial de qualquer número com a biblioteca math

from math import factorial
n = int(input('Digite um número para calcular o seu fatorial'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

