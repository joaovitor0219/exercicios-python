import math
num = float(input('Digite um numero: '))
if num > 0:
    raiz = math.sqrt(num)
    print(f'O numero positivo digitado ao quadrado é igual a {num**2} e sua raiz é igual a {raiz}')
else:
    print('Numero inválido!')