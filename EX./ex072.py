cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = ' '

while resp not in 'N':
    while True :
        n = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= n <= 20 :
            break
            print('Tente Novamente.\n',end='')
    print(f'Voce digitou o numero {cont[n]}.')
    resp = str(input('Voce quer continuar? [S/N]: ')).upper()
print('Obrigado por utilizar nosso programa!!!!')


