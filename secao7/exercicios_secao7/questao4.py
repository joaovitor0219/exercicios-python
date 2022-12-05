lista = []
cont = 0
while cont < 8:
    valor_lista = int(input('Digite um valor para a lista: '))
    lista.append(valor_lista)
    cont += 1

lista.sort()
print(lista)
valorX = int(input('Digite um valor X que corresponda há posição do vetor: '))
valorY = int(input('Digite um valor Y que corresponda há posição do vetor: '))

soma = lista[valorX] + lista[valorY]
print(f'A soma dos valores encontrados nas respectivas posições X e Y é {soma}')
