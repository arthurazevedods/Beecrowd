run = True
while(run == True):
	n = int(input())
	if(n != 0):
		mag = input().split()
		mag.append(mag[0])
		mag.append(mag[1])
		picos = 0
		if(n == 2 and mag[0]!=mag[1]):
			picos = 2
		else:
			for i in range(1,n+1):

				if(mag[i] < mag[i-1]) and (mag[i] < mag[i+1]):
					picos +=1
				elif mag[i] > mag[i-1] and mag[i] > mag[i+1]:
					picos+=1
		print(picos)
		
	else:
		run = False