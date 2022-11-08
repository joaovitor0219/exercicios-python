''''Leia o numero'''
N = int(input('Digite um numero inteiro: '))
'''Definir o contador'''
contador = 0
'''O primeiro numero impar'''
impar = 1

while contador < N:
    '''Printar o valor impar'''
    print(impar)
    '''Adicionar 1 ao contador para seguir o loop'''
    contador = contador + 1
    '''Somar 2 ao valor de impar para printar o proximo valor impar'''
    impar = impar + 2


