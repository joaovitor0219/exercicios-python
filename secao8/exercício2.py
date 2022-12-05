'''Faça uma função que receba a data atual(dia,mês e ano em inteiro) e exiba-a na tela noformato textual por extenso.
Exemplo: Data: 01/01/2000, Imprimeir: 1 de janeiro de 2000.'''


def data_atual(dia, mes, ano):
    return print(f'{dia} de {mes} de {ano}!')


data_atual(int(input('dia: ')), input('mês: '), int(input('Ano: ')))

