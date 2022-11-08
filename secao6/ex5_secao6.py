soma = 0

for valor_usuario in range(1, 11):
    valor_usuario = float(input('Digite um numero: '))
    soma = soma + valor_usuario
print(f'O valor da soma dos valores é {soma:.2f}')
