n = int(input('Digite um numero inteiro: '))
print('Pressione [1] para converter para binario .')
print('Pressione [2] para converter para octal .')
print('Pressione [3] para converter para hexadecimal .')
x = int(input('Digite sua opcao: '))
if   x == 1:
    print('{} convertido para BINARIO e igual a {}'.format(n, bin(n)[2:]))
elif x == 2:
    print('{} convertido para OCTAL e igual a {}'.format(n, oct(n)[2:]))
elif x == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opcao invalida , tente novamente!!!')



