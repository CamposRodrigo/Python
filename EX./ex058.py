from random import randint
computador = randint(0, 10)
print('\033[31mSou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?\033[31m')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite+= 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez.')
        elif jogador > computador:
            print('Menos..Tente mais uma vez.')
print('=======>>>>>>>>>>>>>>>>>>>> \033[36mAcertou com {} palpite(s).Parabens!!!\033[m '.format(palpite))

