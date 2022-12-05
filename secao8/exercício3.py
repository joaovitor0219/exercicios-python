'''
Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo,
-1 se negativo e 0 se for igual a 0.
'''

def positivo_ou_negativo(numero):

    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0
try:
    print(positivo_ou_negativo(float(input('Digite um número: '))))

except:
    print('Digite um número!')