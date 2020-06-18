dados = {}
dados["Nome"]= str(input('Nome: '))
dados["Media"]= float(input('Media: '))
print('=-'*30)
print(f'- O Nome é igual a {dados["Nome"]}.')
print(f'- A Media foi de {dados["Media"]}')
if dados["Media"] < 7 and dados["Media"] > 5:
    print('- Situacao e igual a Recuperacao.')
elif dados["Media"] >= 7:
    print('- Situacao é igual a Aprovado.')
elif dados["Media"] <= 5:
    print('- Situacao é igual a Reprovado.')
