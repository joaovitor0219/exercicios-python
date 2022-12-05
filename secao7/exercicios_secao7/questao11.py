lista = []
'''lista_negativos = []'''
negativos = 0
soma_positivos = 0
for num in range(0, 10):
    num = float(input('Digite um numero: '))
    lista.append(num)
    if num < 0:
        negativos = negativos + 1
        '''lista_negativos.append(negativos)'''
    else:
        soma_positivos = soma_positivos + num
print(sorted(lista))
print(negativos)
print(soma_positivos)
