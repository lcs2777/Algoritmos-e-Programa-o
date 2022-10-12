# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759
anoAtual = int(input())
anoInicial = 2005
salarioBase= 1000
porcentagem = 0.015
aumentoPorcentagem = 0.01

if anoAtual <= 2005:
    print ("O ano informado deverá ser > 2005!")
else:
    while anoAtual > anoInicial:
        salarioBase = salarioBase + (salarioBase * porcentagem)
        porcentagem = (porcentagem + aumentoPorcentagem)
        anoInicial = anoInicial + 1
        if anoAtual == anoInicial:
            print ("Salário atual: R$%.2f" %salarioBase) 