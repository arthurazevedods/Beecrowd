
def pulo(altura, numero):
	canos = input()
	for x in range(2,numero*2,2):
		if(abs(int(canos[x]) - int(canos[x-2])) > altura):
			return False
	return True

alturaPulo, numeroCanos = input().split()

if pulo (int(alturaPulo), int(numeroCanos) ):
	print("YOU WIN")
else:
	print("GAME OVER")