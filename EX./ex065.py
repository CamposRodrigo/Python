numero = media = cont = tot = maior = menor = 0
resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um numero: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    tot += numero
    if cont == 1 :
        maior = menor = numero
    else:
        if numero > maior :
             maior = numero
        if numero < menor :
             menor = numero

media = tot / cont

print('Voce digitou {} numeros e a media foi {:.1f} .'.format(cont, media))
print('O maior numero digitado foi {} e o menor numero foi {}'.format(maior, menor))
