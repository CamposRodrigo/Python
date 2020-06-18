cont = soma = n= 0
while True:
    n = int(input('Digite um numero. [999 para parar]:'))
    if n == 999:
        break
    soma += n
    cont += 1

print('Voce digitou {} numeros e a soma e {} .'.format(cont, soma))

