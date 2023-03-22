#Ler o ano de nascimento de 7 pessoas
#no final mostrar quantas são maiores de idade ou não
from datetime import date
cont = 0
cont2 = 0
for c in range(0, 7):
    data = int(input(' Digite o seu ano de nascimento'))
    calculo = date.today().year - data
    if calculo >= 18:
        cont = cont + 1
    elif calculo < 18:
        cont2 = cont2 + 1
print('Quantidade de pessoas maiores de idade {} , quantidade de pessoas menores de idade {}'.format(cont, cont2))

