

run = True
while(run == True):
	#ENTRADA
	entrada = input()
	G, P = (int(numero) for numero in entrada.split(' ')) #Numero de GP's e de Pilotos
	standings = []
	systems = []
	if (G==0 and P==0):
	   run = False
	else:
		#receber as posições das corridas
		for _ in range(G):
			race = {}
			posicoes = input()
			count = 1
			for pos in posicoes.split(' '):
				race[int(pos)] = count
				#race[int(pos)] = [count,0]
				count = count+1

			standings.append(race)

		

		#receber S, o numero de Sistemas de Pontuações que tem
		s = int(input())
		for _ in range(s):
			pontos = []
			sistema = input()
			for pts in sistema.split(' '):
				pontos.append(int(pts)) #systems.append(pontos) #contém os sistemas de pontuação
			lastToPoint = pontos[0] #ultimo a pontuar
			contagem = [0]
			contagem = contagem*P
			maior = 0
			lider = []
			for corrida in standings:
				for i in range(1,int(lastToPoint)+1):
					
					contagem[corrida[i]-1] = contagem[corrida[i]-1]+pontos[i]
					if(contagem[corrida[i]-1] == maior):
						lider.append(corrida[i])
						
					elif(contagem[corrida[i]-1] > maior):
						maior = contagem[corrida[i]-1]
						lider = [corrida[i]]
						
						
			final = sorted(lider)
			print(*final, sep=' ')


