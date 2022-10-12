# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733
nome = input()
horasExtra = float(input())

salarioMinimo = float(1192.40)
valorHorExtra = float(10.00)


salarioHoraExtra = horasExtra * valorHorExtra

salarioBruto = 3 * salarioMinimo + salarioHoraExtra

if salarioBruto > 2000:
    inss = salarioBruto * 0.12
else:
    inss = salarioBruto * 0.05

if salarioBruto > 2500:
    leao = salarioBruto * 0.2
else:
    leao = 0

# Conta final
salarioLiquido = salarioBruto - (inss + leao)

print("Nome: %s"%(nome))
print("Salário bruto: R$%.2f"%(salarioBruto))
print("Salário líquido: R$%.2f"%(salarioLiquido))