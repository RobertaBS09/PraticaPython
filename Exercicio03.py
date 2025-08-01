valor_hora=float(input('Digite o valor da hora:'))
numero_horas=int(input('Digite o numero de horas trabalhadas:'))
porcetagem_INSS=float(input('Digite a porcentagem do INSS:'))

salario_bruto=float(valor_hora*numero_horas)
valor_descontado=(salario_bruto*(porcetagem_INSS/100))
salario_liquido=float(salario_bruto-valor_descontado)

print(f'Salario liquido:{salario_liquido:.2f}')