# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760
somaIdade = 0
pessoas90 = 0
p = 0

while p < 4:
    idade = int(input())
    peso = float(input())
    somaIdade += idade
    if(peso > 90):
        pessoas90 += 1
    p += 1
    
print("Qtd pessoas > 90 Kg: %i" % (pessoas90))
print("Idade média: %.2f " % (somaIdade/4))
    