entrada = input()
a,b,c,d = (int(numero) for numero in entrada.split(" "))
accept = False
if(b>c and d>a):
	if(c+d>a+b):
		if(c>0 and d>0):
			if(a%2 == 0):
				accept = True

if(accept == True):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")