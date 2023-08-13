n, qtd, valor = input().split()
n2,qtd2,valor2 = input().split()

x = (float(qtd)*float(valor))+(float(qtd2)*float(valor2))

print('VALOR A PAGAR: R$ {:.2f}'.format(x))