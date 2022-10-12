# https://www.beecrowd.com.br/judge/pt/problems/view/1009
SALARIO = float(input())
VENDAS = float(input())

BONUS = float(VENDAS * 0.15)

TOTAL = SALARIO + BONUS

print("TOTAL = R$ %0.2f" %(TOTAL))
