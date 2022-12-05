candidato1 = 0
candidato2 = 0
candidato3 = 0
voto_branco = 0
voto_nulo = 0
contador = 0
voto = int(input('Digite o numero do cadidato: '))

while voto != -1:
    contador = contador + 1

    if voto == 1:
        candidato1 = candidato1 + 1

    elif voto == 2:
        candidato2 = candidato2 + 1

    elif voto == 3:
        candidato3 = candidato3 + 1

    elif voto == 4:
        voto_nulo = voto_nulo + 1

    else:
        voto_branco = voto_branco + 1

    voto = int(input("Digite seu voto ou -1 para sair: "))

if candidato1 > candidato2 and candidato1 > candidato3:
    print(f'O candidato 1 foi o vencedor!{candidato1} votos')

elif candidato2 > candidato1 and candidato2 > candidato3:
    print(f'O candidato 2 foi o vencedor!{candidato2} votos')

else:
    print(f'O candidato 3 foi o vencedor!{candidato3} votos')

print(f'O número de Votos branco foi de {voto_branco}')
print(f'O numero de votos nulos foi de {voto_nulo}')
print(f'O número de eleitores foi de {contador} pessoas')