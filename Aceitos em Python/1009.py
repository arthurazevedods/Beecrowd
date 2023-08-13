nome = raw_input()
salario = float(input())
vendas = float(input())

x = 15*vendas/100

print('TOTAL = R$ {:.2f}'.format(salario+x))