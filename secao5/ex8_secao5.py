nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2)/2
if nota1 > 0 and nota1 < 10 and nota2 > 0 and nota2 < 10:
    print(f'A media das notas do aluno foi de {media:.2f}')
else:
    print('Foi informado uma nota inválida')



