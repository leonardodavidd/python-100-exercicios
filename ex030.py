#exemplo22 valor digitado exemplo: 1234  // Como mostrar na tela unidade, dezena, centena e milhar ?
num = int(input('Digite um num inteiro:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando a unidade {}'.format(num))
print('A unidade: {} '.format(u))
print('A dezena é : {}'.format(d))
print('A centena é : {}'.format(c))
print('O milhar é: {}'.format(m))

