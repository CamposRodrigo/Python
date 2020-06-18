from random import randint
print('=-='*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*10)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador +computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador {computador}.Total de {total} ', end='')
    print('Deu PAR'if total %2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!!!!')
            v += 1
        else:
            print('Voce PERDEU!!!')
            break
    elif tipo =='I':
        if total% 2 == 1:
            print('Voce VENCEU!!!')
            v += 1
        else:
            print('Voce PERDEU!!!')
            break
    print('Vamos joga novamente...')
print(f'Game OVER!!! Voce venceu {v} vezes.')

