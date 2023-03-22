#Crie uma TUPLA com várias palavras
#Depois disso, mostrar as vogais de cada palavra da TUPLA
tupla = ('python', 'leonardo', 'curso em video', 'Vasco', 'Flamengo')
for c in tupla:
    print(f'\nEssa palavra {c} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end='')

