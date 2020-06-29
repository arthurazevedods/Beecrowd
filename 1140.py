run = True
while(run == True):
	entrada = raw_input().split()
	if(entrada[0]!='*'):
		letter = entrada[0][0]
		asnwer = 'Y'
		for i in range(len(entrada)):
			if(letter.upper()==entrada[i][0] or letter.lower()==entrada[i][0]):
				asnwer = 'Y'
			else:
				asnwer = 'N'
				break
		print(asnwer)
	else:
		run = False