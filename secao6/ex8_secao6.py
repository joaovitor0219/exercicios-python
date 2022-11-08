soma = 0
maior = 0
menor = 0
for i in range(3):
    num = float(input('Digite um numero: '))
    if num > maior:
        maior = num
    else:
        print(f'O menor numero é {num}')
print(f'O maior numero é o {maior}')
