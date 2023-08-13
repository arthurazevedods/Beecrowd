alfabeto =  ['a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
alfabetoM = ['A','B','C','D','E','F','G','H','I','J','L','K','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']

def cifrar(i,resposta):

		newLetra = ''
		if(i in alfabeto or i in alfabetoM):
			if(not i.isupper()):
				for letra in range(len(alfabeto)):
					if(alfabeto[letra] == i):
						calc = letra+13
						if((letra+13) > 25):
							calc -= 26							
						newLetra = alfabeto[calc]
						return resposta+newLetra
			else:
				for letra in range(len(alfabeto)):
					if(alfabetoM[letra] == i):
						calc = letra+13
						if((letra+13) > 25):
							calc -= 26
						newLetra = alfabetoM[calc]	
						return resposta+newLetra	
						
			
		else:
			resposta = resposta+i
			return resposta

while True:
	
	try:
		entrada = input()
		resposta = ''
		for i in entrada:
			resposta = cifrar(i, resposta)
		
		print(resposta)
	except:
		break