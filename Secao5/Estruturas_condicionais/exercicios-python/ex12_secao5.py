import math
numero = int(input('Digite um nunmero inteiro: '))
if numero > 0:
    logaritmo = math.log10(numero)
    print(f'O logaritmo de {numero} é igual a {logaritmo:.2f}')
else:
    print('Numero inválido')