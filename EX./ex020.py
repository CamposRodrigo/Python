import random
n1 = str(input('Nome do primeiro Aluno: '))
n2 = str(input('Nome do segundo Aluno: '))
n3 = str(input('Nome do terceiro Aluno: '))
n4 = str(input('Nome do quarto Aluno: '))
lista = [n1,n2,n3,n4]
ordem = random.shuffle(lista)
print('A sequencia dos nomes sera: {} .'.format(lista))