numeros = []
while True:
    numeros.append(int(input('Digite um Valor : ')))
    r = str(input('Deseja continuar? [S/N]: '))
    if r  in 'Nn':
        break
numeros.sort(reverse=True)
print(f'Voce digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente sao {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da Lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')
