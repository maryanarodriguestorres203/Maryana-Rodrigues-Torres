from time import sleep
v = float(input('Qual a velocidade que o carro passou no radar? '))
if v <= 60:
    print('-Velocidade aceita')
else:
    print('-Velocidade de 60Km/h ultrapassada')
    calculo = (v-60) * 7
    sleep(2)
    print('-o valor da multa é de 7 reais por km acima do limite')
    print('calculando...')
    sleep(5)
    print('-O valor da multa é de R${}.'.format(calculo))


