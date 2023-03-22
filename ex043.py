#vamos colocar cores
print('\033[1;30;44mOlá Mundo\033[m')

#outro exemplo
a = 5
b = 6
print('Os valores são \033[32m{}\033[m e \033[31m{}'.format(a,b))

#outro exemplo
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Oi gente, {} {} {}'.format(cores['amarelo'], a, cores['amarelo']))