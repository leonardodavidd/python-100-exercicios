#Crie um programa que leia nome, sexo e idade de um número indeterminado de pessoas. guardando estes
#dados em um dicionário e todos os dicionarios em uma lista. no final mostre: quantas pessoas cadastradas,
#a media de idade, uma lista com mulheres, uma lista com idade acima da media
dic = {}
galera = []
cont1 = 0
cont = 0
print('Inicializando ....xd')
continuar = 'S'
while continuar != 'N':
    dic['nome'] = str(input('Digite seu nome: '))
    dic['sexo'] = str(input('Digite o seu sexo : ')).upper()[0]
    for c in dic['nome']:
        if dic['sexo'] in 'Ff':
            galera.append(dic['nome'])
    if dic['sexo'] not in 'MmFf':
        print('ERROR ! Digite um sexo válido')
        dic['sexo'] = str(input('Digite o seu sexo : ')).upper()[0]
    dic['idade'] = int(input('Digite a sua idade '))
    cont1 = cont1 + dic['idade']
    cont = cont + 1
    continuar = str(input('Deseja continuar S para sim ou N para não')).upper()[0]
    if continuar == 'N':
        break
    if continuar not in 'SsNn':
        print('ERROR! Digite um dígito válido ! ')
        continuar = str(input('Deseja continuar S para sim ou N para não')).upper()[0]
media = (cont1 / cont)
print(f'Quantas pessoas foram cadastradas -> {cont}')
print(f'Média das idades de todas as pessoas cadastradas {media:.2f}')
print('Todas as mulheres cadrastadas no sistema', list(dict.fromkeys(galera)))






