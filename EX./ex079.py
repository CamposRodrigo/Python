numeros = list()
while True:
    n = int(input('Digite um Valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com Sucesso...')
    else:
        print('Valor duplicado!! Nao vou adicionar...')
    r = str(input('Quer continuar? [S/N] : '))
    if r not in 'NnSs':
        print('Esse comando nao existe tente novamente....')
    if r in 'Nn':
        break
numeros.sort()
print(f'Voce digitou os valores {numeros}')