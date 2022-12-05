altura = float(input('Digite sua altura: '))
sexo = input('Homem ou Mulher: ')

peso_homens = (72.7*altura)-58
peso_mulheres = (62.1*altura)-44.7

if sexo == 'Mulher':
    print(f'O peso ideal é igual a {peso_mulheres:.2f}')
elif sexo == 'Homem':
    print(f'O peso ideal é igual a {peso_homens:.2f}')
else:
    print('Digite um dado válido.')
