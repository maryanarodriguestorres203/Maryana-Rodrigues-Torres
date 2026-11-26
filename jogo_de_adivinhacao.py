from random import randint
from time import sleep
escolha = int(input('adivinhe o número que eu escolhi de 0 a 5: '))
print('-' * 45)
n = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
print('-' * 45)
if escolha == n:
    print('PARABÉNS, VOÇÊ ME VENCEU!!!')
else:
    print('GANHEI! Eu pensei em {}.'.format(n))
print('-' * 45)
print('-fim de jogo-')