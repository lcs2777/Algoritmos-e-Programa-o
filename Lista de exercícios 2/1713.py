# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713
ganharPorHora = float(input())
diasTrabalhados = float(input())
# salario total
salarioTotal = ganharPorHora * diasTrabalhados

impostoDeRenda =  salarioTotal * 0.11
inss = salarioTotal * 0.08
sindicato = salarioTotal * 0.05
salarioLiquido = salarioTotal - (impostoDeRenda + inss + sindicato)

print('Salário bruto: R$%.2f' % salarioTotal)
print('Imposto: R$%.2f' % impostoDeRenda)
print('INSS: R$%.2f' % inss)
print('Sindicato: R$%.2f' % sindicato)
print('Líquido: R$%.2f' % salarioLiquido)