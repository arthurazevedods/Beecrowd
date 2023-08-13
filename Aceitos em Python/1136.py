def bingo(N,B,bolas):
	teste = set() #coleção que guardará os números de 0 a N
	#laço para fazer os calculos entre os números
	for i in range(B):
		for j in range(i,B):
			ball = abs(bolas[i]-bolas[j]) #valor absoluto, se dê negativo, serve para o positivo
			teste.add(ball)
			if(len(teste)==N+1): #se for igual N, então quer dizer tem a possibilidade de sair todos os números de 0 a N 
				return 'Y'
	return 'N'


run = True
while run == True:
	entrada = input()
	N,B = (int(n) for n in entrada.split(" ") ) #receber a entrada do N e do B
	if(N == 0 and B == 0): 
		run =  False
	else:
		bolas = [int(b) for b in input().split()] #recebe as bolas que ficarão no bingo
		
