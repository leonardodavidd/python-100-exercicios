ano = int(input('Digite o seu ano de nascimento'))
data = int(input('Digite o ano em que você está agora ! '))

idade = data - ano
if idade <= 9:
    print('Você é mirin')
elif idade <= 14:
    print('Você é infantil')
elif idade <= 19:
    print('Você é junior')
elif idade <= 25:
    print('Você é Senior')
elif idade > 25:
    print('Você é Master')
