#Exemplo de media de notas.
n1 = float(input('Digite a sua primeira nota ! '))
n2 = float(input('Digite a sua segunda nota ! '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi de {:.2f} e você está REPROVADO'.format(media))
elif media >=5 and media <= 6.9:
    print('A sua média foi de {:.2f} e você está de RECUPERAÇÃO'.format(media))
elif media >= 7:
    print('A sua média foi de {:.2f} e você foi APROVADO!'.format(media))

