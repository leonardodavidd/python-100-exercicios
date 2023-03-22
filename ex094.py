#exercicio boletim
lista = []
while True:
    nome = str(input('Digite o nome do aluno'))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    comando = str(input('Quer continuar S/N')).strip().upper()
    if comando == 'N':
        break
print(lista)
while True:
    seila = int(input('Digite o número da chamada do aluno que você quer ver, ou digite 999 para sair !'))
    if seila == 999:
        print('FINALIZANDO...')
        break
    if seila <= len(lista) - 1:
        print(f'A nota do aluno {lista[seila][0]} é : {lista[seila][1]}')





