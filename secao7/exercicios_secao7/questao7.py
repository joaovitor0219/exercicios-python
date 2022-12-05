lista = []
cont = 0
indice_lista = 0
for numbers in range(1,11):
    numbers = int(input('Digite um numero: '))
    lista.append(numbers)
print(lista)
for indice in enumerate(lista):
    indice_lista = indice

print(max(lista))
print(indice_lista)




