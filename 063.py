#PRIMEIRO EXEMPLO SIMPLES DE COMO FUNCIONA A ESTRUTURA ENQUANTO = WHILE
r = 'S'
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('Quer continuar ? S/N')).upper()
print('Fim')
