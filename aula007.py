#Exemplo27
nome = str(input('Qual é o seu nome'))
print('Prazer em te conhecer{:^20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
mod = n1 % n2
print('A soma é {}, multiplicação é {}, divisão é {}, divisão inteira é {}'.format(s, m, d, di), end = ' ')
print('A potência é {:.2f}, o resto da divisão é {}'.format(e, mod))


