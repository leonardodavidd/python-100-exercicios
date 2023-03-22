#leia varios valores , condicao de parada 999, mostrar no final quantos numeros foram digitados e qual foi a soma deles

soma = 0
soma2 = 0
while True:
    r = int(input('Digite um valor'))
    if r == 999:
        break
    soma2 = soma2 + r
    soma = soma + 1
print('A quantidade de valores digitados foi de {}, a soma dos valores digitados foi de {}'.format(soma, soma2))
