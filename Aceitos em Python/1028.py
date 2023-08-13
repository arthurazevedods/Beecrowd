def mdc(n1, n2):
	if(n2 == 0):
		return n1
	return mdc(n2,n1%n2)




N = int(input()) #numero de casos de teste
for _ in range(N):
	teste = input()
	t1 , t2 = (int(x) for x in teste.split(" ")) #casos de teste
	if(t1 < t2):
		menor = t1
		maior = t2
	else:
		menor = t2
		maior = t1

	print(mdc(maior,menor))
