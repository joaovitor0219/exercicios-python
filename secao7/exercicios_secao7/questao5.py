lista = []
cont = 0
pares = 0
while cont < 10:
    valor_lista = int(input('Digite um valor: '))
    if valor_lista % 2 == 0:
        pares += 1
    lista.append(valor_lista)
    lista.sort()
    cont += 1
print(lista)
print(f'A quantidade de numeros pares são {pares} números')
