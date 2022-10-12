# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

cliente = int(input())


total_da_compra = float(input())


if cliente == 1:
    print ('valor total a ser pago: R$ %.2f' % total_da_compra)
elif cliente == 2:
    print ('valor total a ser pago: R$ %.2f' % (total_da_compra - (total_da_compra * 0.13)))
elif cliente == 3:
     print ('valor total a ser pago: R$ %.2f' % (total_da_compra - (total_da_compra * 0.07)))
else:
     print ('OPÇÃO INVÁLIDA!')