#Exemplo estrutura for
# ver números pares que são entre 1 e 50
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print(' ACABOU ')

for c in range(2, 51, 2):
    print(c, end=' ')
print(' ACABOU ')

