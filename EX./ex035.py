print('-=-'*20)
print('                     Analisador de Triangulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('\033[1;34;41m Os segmentos acima PODEM FORMAR triangulo.\033[m')
else:
    print('OS segmentos acima NAO PODEM FORMAR triangulo.')
