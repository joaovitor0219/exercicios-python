#Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.
def dobro_numero(numero):
        return numero*2
try:
    print(dobro_numero(int(input('Digite um numero inteiro: '))))
except:
    print('Valor inválido')
