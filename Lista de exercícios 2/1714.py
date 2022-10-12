# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714
produto = float(input())
if produto < 20: 
    print ('Valor de venda: R$%.2f' % (produto+(produto * 0.45)))

else:
    print ('Valor de venda: R$%.2f' % (produto+(produto * 0.30)))