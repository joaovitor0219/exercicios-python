import math
num = float(input('Digite um numero: '))
if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')
else:
    print(f'O valor do numero ao quadrada é {num**2}')