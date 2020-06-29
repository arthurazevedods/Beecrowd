def bingo(N,B,bolas):
	teste = set()
	for i in range(B):
		for j in range(i,B):
			ball = abs(bolas[i]-bolas[j])
			teste.add(ball)
			if(len(teste)>=N+1):
				return 'Y'
	return 'N'


run = True
while run == True:
	entrada = input()
	N,B = (int(n) for n in entrada.split(" ") )
	if(N == 0 and B == 0):
		run =  False
	else:
		bolas = [int(b) for b in input().split()]
		
		print(bingo(N,B,bolas))
		#bingo(N,B,bolas)