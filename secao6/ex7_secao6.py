soma = 0
for i in range(10):
    num = int(input('Digite um numero: '))
    if num >= 0:
        soma = soma + num
    else:
        break
print(f'A media dos numeros será {soma/10}')
