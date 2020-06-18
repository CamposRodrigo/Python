n = str(input('Digite uma frase:')).upper().strip()
print('A letra A apareceu {} vezes na sua frase.'.format(n.count('A')))
print('A primeira letra A apareceu na posicao numero {}'.format(n.find('A')+1))
print('A ultima letra A apareceu na posicao numero {}'.format(n.rfind('A')+1))