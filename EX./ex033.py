a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
#VERIFICANDO QUEM E O MENOR
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#VERIFICANDO QUEM E O MAIOR
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {} .'.format(menor))
print('O maior valor digitado foi {} .'.format(maior))