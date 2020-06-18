n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
soma = 0
multiplicar = 0
maior = 0
opcao = 0

while opcao != 5:
    print('       \033[31mMenu Principal\n'
          '         [1] somar\n'
          '         [2] multiplicar\n'
          '         [3] maior\n'
          '         [4] digitar novos numeros\n'
          '         [5] sair do programa\033[m')
    opcao = int(input('Qual e a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {} .'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicacao entre {} e {} é {} .\n\n'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 < n2 :
            maior = n2
            print('O maior valor digitado e {} .'.format(maior))
        if n1 > n2 :
            maior = n1
            print('O maior valor digitado e {} .'.format(maior))
        else:
            print('Os numeros sao iguais!!!!')
    if opcao == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
print('\033[36m===========>>>>>>>>>>>>>>>>>>Voce saiu do Programa!!! Volte sempre!!!<<<<<<<<<<<<<<<==============\033[m')