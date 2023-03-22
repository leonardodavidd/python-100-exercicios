#calcule todos os números ímpares múltiplos de 3 que se encontram no intervalo de 1 a 500

s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
print(' A soma entre todos os valores é : {} '.format(s))
