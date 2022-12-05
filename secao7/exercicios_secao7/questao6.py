lista = []
cont = 0
maior = 0
menor = 0
while cont < 10:
    valor_lista = int(input('Digite um valor: '))
    lista.append(valor_lista)
    cont += 1
print(max(lista))
print(min(lista))
