tot = 0
h = 0
m = 0
while True:
     print('-' * 30)
     print('     CADASTRE UMA PESSOA ')
     print('-' * 30)
     idade = int(input('Idade: '))
     if idade > 18:
          tot += 1
     sexo = ' '
     while sexo not in 'MF':
          sexo = str(input('Sexo:[M/F] ')).upper().strip()[0]
          if sexo == 'M':
               h += 1
          elif sexo == 'F'and idade < 20:
               m +=1
          decisao = ' '
     while decisao not in 'SN':
          decisao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
     if decisao == 'N':
          print(f'Total de pessoas cadastradas com mais de 18 anos: \033[31m{tot}\033[m')
          print(f'Ao todo temos \033[31m{h}\033[m homens cadastrados.')
          print(f'E temos \033[31m{m}\033[m mulheres com menos de 20 anos.')
          break
print('-'*35)
print('Cadastramento de Pessoas encerrado.')



