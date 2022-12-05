lista = []
pares = 0
for num in range(0, 6):
    num = int(input('Digite um numero par: '))
    if num % 2 == 0:
        lista.append(num)
        print(lista)
    if num % 2 != 0:
        print('Numero inválido')
        break


print('A lista inversa com os valores pares é', lista[::-1])