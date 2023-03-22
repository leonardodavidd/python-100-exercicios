#Exemplo de utilização de estrutura for
i = int(input('Digite o inicio'))
f = int(input('Digite o fim'))
p = int(input('Digite a quantidade de passos'))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0,3):
    n = int(input('Digite o valor'))
    s = s + n
print(' O somatório de todos os valores é : {} '.format(s))
print('fim')
