#Crie um programa que leia uma matrix 3x3 e preencha com valores lidos pelo teclado
#No final mostrar a matriz na tela , com formatação correta
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o [{l}, {c}] valor '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()


