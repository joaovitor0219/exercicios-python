salario = float(input('Salário do empregador: '))
emprestimo = float(input('Valor do emprestimo: '))
if emprestimo > 0.2*salario:
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')
