#Verificar se uma expressão matemática tem o mesmo número de panteses que abrem e fecham
#Ou seja, verificar se a expressão está correta
cont = 0
cont1 = 0
expressao = str(input('Digite a sua expressão!'))
for c in expressao:
    if c == '(':
        cont = cont + 1
    if c == ')':
        cont1 = cont1 + 1
if cont == cont1:
    print('Sua expressão está correta!')
elif cont != cont1:
    print('Sua expressão está incorreta!')
