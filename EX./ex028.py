from random import randint
from time import sleep
computador = randint(0,5)# faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um numero de 0 a 5!!!! Tente Adivinhar...  ')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? '))# JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(3)
if jogador==computador:
    print('Parabens vc acertou!!!')
else:
    print('Voce errou,pensei no numero {} tente novamente'.format(computador))