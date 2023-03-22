#Verificando o número se ele é primo ou não
num = int(input(' Digite o número'))
totaldivisiveis = 0

for c in range(1, num + 1):
    if num % c == 0:
        totaldivisiveis = totaldivisiveis + 1
if totaldivisiveis == 2:
    print(' Este número é primo')
else:
    print(' Este número não é primo')