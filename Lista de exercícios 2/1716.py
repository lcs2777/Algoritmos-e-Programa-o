# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716
tipoFuncionario = (input())
salarioAtual = float(input())

if tipoFuncionario == 'A':
    print ('Novo salário: R$%.2f' % (salarioAtual + (salarioAtual * 0.10)))
elif tipoFuncionario == 'B':
    print ('Novo salário: R$%.2f' % (salarioAtual + (salarioAtual * 0.15)))
elif tipoFuncionario == 'C':
    print ('Novo salário: R$%.2f' % (salarioAtual + (salarioAtual * 0.20)))
    