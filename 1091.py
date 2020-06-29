
run = True
while run == True :
	k = int(input())
	if (k == 0):
		run = False
	else:
		entrada = input()
		n, m = (int(numero) for numero in entrada.split(' '))
		for _ in range(k):
			#se recebe as coordenadas x e y
			#onde x é leste-oeste
			#e y é norte sul
			coordenada = input()
			x,y = (int(num) for num in coordenada.split(' '))
			if(x == n or y == m):
				print("divisa")
			elif(x>n):
				if(y>m):
					print("NE")
				else:
					print("SE")
			elif(x<n):
				if(y>m):
					print("NO")
				else:
					print("SO")
