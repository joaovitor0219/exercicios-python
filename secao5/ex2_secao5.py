import math
num = float(input('Digite um numero: '))
if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é igual a {raiz}')
else:
    print('Este número é inválido!')