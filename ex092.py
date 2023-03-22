#Crie um programa que leia uma matrix 3x3 e preencha com valores lidos pelo teclado
#No final mostrar a matriz na tela , com formatação correta
#mostrar a soma de todos os valores pares digitados
#mostrar a soma dos valores da terceira coluna
#mostrar o maior valor da segunda linha
#mostrar qual o menor valor digitado
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = maior = soma = 0
menor = 9223372036854775807
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o [{l}, {c}] valor '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            cont = cont + matriz[l][c]
    print()
for l in range(0, 3):
        soma = soma + matriz[l][2]
for c in range(0, 3):
        if matriz[1][c] > maior:
            maior = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] < menor:
            menor = matriz[l][c]
print(f'O menor valor digitado na Matriz foi de {menor}')
print(f'O maior valor da segunda linha é {maior}')
print(f'A soma dos valores da terceira coluna {soma}')
print(f'A soma dos números pares digitados {cont}')
