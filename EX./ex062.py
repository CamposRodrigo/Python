print('Gerador de PA')
print('-=-'*10)
n1 = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
cont = 1
termo = n1
total = 0
x = 10
while x != 0 :
    total += x
    while cont <= total:
        print('{} ->'.format(termo), end= '')
        termo += razao
        cont += 1
    print('PAUSA')
    x = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados.'.format(total))

