lista_notas = []
media = 0
soma = 0
for notas in range(0, 15):
    notas = float(input('Nota do aluno: '))
    soma = soma + notas
    lista_notas.append(notas)
media = soma/15
print(f'A média das notas foram {media:.2f} pontos')
