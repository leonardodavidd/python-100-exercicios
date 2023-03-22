#faca a tabuada de vários números, e o programa será interrompido quando o usuário digitar um num negativo

cont = 0
while True:
    num = int(input('Digite o número que deseja para realizar a tabuada'))
    if num < 0:
        break
    for c in range(1, 11):
        resultado = num * c
        print('{} x {} = {}'.format(num, c, resultado))













