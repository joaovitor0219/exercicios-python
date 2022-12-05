num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    diferenca = num1 - num2
    print(f'O numero 1 ({num1}) é maior que o numero 2({num2}) com diferença de {diferenca}')
else:
    diferenca = num2 - num1
    print(f'O numero 2 ({num2}) é maior que o numero 1({num1}) com diferença de {diferenca}')