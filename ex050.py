#Exemplo calcule o IMC e diga se a pessoa está acima do peso ou não
peso = float(input('Digite o seu peso (kg) !'))
altura = float(input('Digite a sua altura (m)'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso !')
elif imc >= 18.5 and imc <=25:
    print('Você está no peso ideal')
elif imc >= 25 and imc <=30:
    print('Você está no sobrepeso')
elif imc >= 30 and imc <=40:
    print('Você está na Obesidade')
else:
    print('Você está com obesidade Morbida')
