nota1 = float(input('Nota da primeira prova: '))
nota2 = float(input('Nota da segunda prova: '))
nota3 = float(input('Nota da terceira prova: '))

peso_prova1 = 1
peso_prova2 = 1
peso_prova3 = 2

media_ponderada = ((peso_prova1*nota1) + (peso_prova2*nota2) + (peso_prova3*nota3))/(peso_prova1 + peso_prova2 + peso_prova3)

if media_ponderada >= 60:
    print(f'O aluno foi aprovado com uma nota de {media_ponderada:.2f}')
else:
    print('Aluno reprovado!')
