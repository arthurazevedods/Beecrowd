class coordenada:
    def __init__(self):
        self.visitada = False
    
    def marcarVisita(self):
        self.visitada = True

    def seVisitada(self):
        return self.visitada
    
    
def busca(matriz,coordenadas,x,y,winner):

    if (x >= 0 and x < 5 and y >= 0 and y < 5 and winner == 0):
        
        coordenadas[x][y].marcarVisita()
        if (x == 4 and y == 4):
            winner = 1
            return winner
        else:
            #vai para baixo, cima, esquerda ou direita
            if ((x+1 < 5) and (matriz[x+1][y] == 0) and (coordenadas[x+1][y].seVisitada() == False)):
                winner = busca(matriz, coordenadas, x+1,y,winner)
            
            #vai para cima
            if ((x-1 < 5) and (matriz[x-1][y] == 0) and (coordenadas[x-1][y].seVisitada() == False)):
                winner = busca(matriz, coordenadas, x-1,y,winner)
            
            #vai para direita
            if ((y + 1 < 5) and ((matriz[x][y+1]) == 0) and (coordenadas[x][y+1].seVisitada() == False)):
                winner = busca(matriz, coordenadas, x,y+1, winner)
            #vai para esquerda
            
            if ((y-1 < 5) and (matriz[x][y-1] == 0) and (coordenadas[x][y-1].seVisitada() == False)):
                winner = busca(matriz, coordenadas, x,y-1, winner)
            
    return winner

T = int(input())


for i in range(T):
    coluna = 0
    matriz = []
    linha = []
    coordenadas = []
    while coluna < 5:
        
        linha = input().split()
        linha = list(int(i) for i in linha)
        temp = []
        if linha:
            for i in range(len(linha)):
                temp.append(coordenada())
            coordenadas.append(temp)  
            matriz.append(linha)
            coluna +=1

            
    if matriz:
        winner = 0
        winner = busca(matriz,coordenadas,0,0,winner)
        if winner == 0:
            print('ROBBERS')
        else:
            print('COPS')
   
        
