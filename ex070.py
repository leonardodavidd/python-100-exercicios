#leia vários números, final mostrar media e menor e maior número digitado
#perguntar na segunda vez se o usário quer continuar digitando
resp = 's'
cont = 0
soma = 0
maior = 0
cont2 = 0
menor = 1000000
while resp in 'Ss':
    numero = int(input('Digite um número'))
    resp = str(input('Digite S para continuar ou N para sair')).upper().strip()[0]
    soma = soma + numero
    cont = cont + 1
    cont2 = cont2 + 1
    if numero > maior:
        maior = numero
        if numero < menor:
            menor = numero


media = soma / cont
print('A média dos números digitados foi de {}, a quantidade de números digitados foi de {} '.format(media, cont2))
print('O maior número digitado foi de {}, o menor número digitado foi de {}'.format(maior, menor))
