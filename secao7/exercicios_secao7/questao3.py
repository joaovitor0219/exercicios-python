lista1 = []
cont = 0
lista2 = []
while cont < 10:
    valor_lista = int(input('Digite um valor: '))
    lista1.append(valor_lista)
    quadrado_valor_lista = valor_lista**2
    lista2.append(quadrado_valor_lista)
    cont += 1

lista1.sort()
lista2.sort()
print(lista1)
print(lista2)
