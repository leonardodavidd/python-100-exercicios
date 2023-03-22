#Exercicio - utlização da estrutura FOR
soma = 0
maisvelho = 0
cont = 0
cod = ''
for c in range(0, 4):
    nome = str(input('Digite o sua nome ')).strip()
    idade = int(input('Digite a sua idade '))
    sexo = str(input('Digite o seu sexo M ou F')).strip()
    soma = soma + idade
    if sexo == 'M' or sexo == 'm':
        if idade > maisvelho:
            maisvelho = idade
            cod = nome
    if sexo == 'F' or sexo == 'f':
        if idade < 20:
            cont = cont + 1



media = soma / 4
print('A média de idade do grupo é {:.2f}.'.format(media))
print('A maior idade do homem é de {}, quem tem essa idade tem o nome de {}'.format(maisvelho, cod))
print('Quantidade de mulheres que tem menos de 20 anos {}.'.format(cont))






