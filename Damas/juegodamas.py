import random
import os
from time import sleep

profundidad = 2

def clear():
    os.system( 'cls' )

def crearMatriz(d):
    global test
    test=[[0 for x in range(d)] for y in range(d)]
    global t
    t=d
    for i in range (d):
        for j in range (d):
            test[i][j]='-'
            
def imprimirMatriz():
    print(end='  ')
    for i in range (t):
        print(i, end=' ')
    print()
    for i in range (t):
        print(i, end=' ') 
        for j in range (t):
            print( test[i][j] , end=' ')
        print('\n')

def imprimirTablero(board):
    for i in range (t):
        for j in range (t):
            print( board[i][j] , end=' ')
        print('\n')

def llenarMatriz_Damas():
    for i in range (t):
        for j in range (t):
            if t==4 and i==0 and j%2!=0:
                test[i][j]='X'
            if t==4 and i==t-1 and j%2==0:
                test[i][j]='O'
            if t==8:
                if i%2==0 and i<3 and j%2!=0:
                    test[i][j]='X'
                if i==1 and j%2==0:
                    test[i][j]='X'
                if i%2!=0 and i>4 and j%2==0:
                    test[i][j]='O'
                if i==6 and j%2!=0:
                    test[i][j]='O'  
def calcularPuntaje(board):
    puntaje = 0
    for i in range (t):
        for j in range (t):
            if board[i][j]=='X':
                puntaje += 1
            elif board[i][j]=='O':
                puntaje -= 1
    return puntaje
def contarFichas(board):
    puntaje = 0
    for i in range (t):
        for j in range (t):
            if board[i][j]=='X':
                puntaje += 1
            elif board[i][j]=='O':
                puntaje += 1
    return puntaje
#----------------------------------------------------------------------------    
def humano_come_izq(x,y,mv,ficha):
    if ficha=='O' and mv==0 and test[x-1][y-1]=='X' and test[x-2][y-2]=='-':
        test[x][y]='-'
        test[x-1][y-1]='-'
        test[x-2][y-2]='O'
        return True
    else:
        return False
    
def humano_come_der(x,y,mv,ficha):
    if ficha=='O' and mv==1 and test[x-1][y+1]=='X' and test[x-2][y+2]=='-':
        test[x][y]='-'
        test[x-1][y+1]='-'
        test[x-2][y+2]='O'
        return True
    
    else:
        return False
        
    
def moverhumano(x,y,mv):
    if mv==0 and test[x-1][y-1]=='-':
        test[x][y]='-'
        test[x-1][y-1]='O'
        return True
    if mv==1 and test[x-1][y+1]=='-': #si esta vacio se pone
        test[x][y]='-'
        test[x-1][y+1]='O'
        return True
    else:
        #print("Esta lleno")
        return False
    
    
def humano(x,y,mv):
    if movimiento_valido_O(x,y,'O')==True:
        if mv==0 and test[x][y]=='O' and y!=0: #izquierda
            if moverhumano(x,y,mv)==False:
                if humano_come_izq(x,y,mv,'O')==True:
                    print("Humano comio")
                else:
                    print("Humano no comio")
            else:
                    print("Humano se movio")
                    
        if mv==1 and test[x][y]=='O' and y!=t-1: #derecha
            if moverhumano(x,y,mv)==False:
                if humano_come_der(x,y,1,'O')==True:
                    print("Humano comio")
                else:
                    print("Humano no comio")
            else:
                    print("Humano se movio")
        return True
    else:
        print("Movimiento no valido")
        return False
            
def movimiento_valido_O(x,y,fch):
    if test[x][y] != fch:
        return False
    if y!=0 and y!=t-1:
        if test[x-1][y-1]==fch and test[x-1][y+1]==fch: #izq der 
            return False
        else:
            return True
    elif y==0:
        if test[x-1][y+1]==fch :
            return False
        else:
            return True
    elif y==t-1:
        if test[x-1][y-1]==fch:
            return False
        else:
            return True 
#----------------------------------------------------------------------------   
def movimiento_valido_X(x,y,fch):
    if y!=0 and y!=t-1:
        if test[x+1][y-1]==fch and test[x+1][y+1]==fch : #izq der 
            return False
        else:
            return True
    elif y==0:
        if test[x+1][y+1]==fch :
            return False
        else:
            return True
    elif y==t-1:
        if test[x+1][y-1]==fch:
            return False
        else:
            return True
    
def movercpu(board,x,y,mv):
    if mv==0 and test[x+1][y-1]=='-':
        board[x][y]='-'
        board[x+1][y-1]='X'
        return True
    if mv==1 and test[x+1][y+1]=='-': #si esta vacio se pone
        board[x][y]='-'
        board[x+1][y+1]='X'
        return True
    else:
        return False
    
def cpu_come_izq(tab,x,y,mv):  #mv=0
    if mv==0 and test[x+1][y-1]=='O' and test[x+2][y-2]=='-':
        tab[x][y]='-'
        tab[x+1][y-1]='-'
        tab[x+2][y-2]='X'
        return True    
    else:
        return False
def cpu_come_der(tab,x,y): #mv=1
    if mv==1 and test[x+1][y+1]=='O' and test[x+2][y+2]=='-':
        tab[x][y]='-'
        tab[x+1][y+1]='-'
        tab[x+2][y+2]='X'
        return True
    else:
        return False
    
def cpu_formas_comer(tab,x,y):
    c=0
    if cpu_come_izq(tab,x,y,0) and cpu_come_der(tab,x,y,1): # <
        return c+2,'id'
    if cpu_come_der(tab,x,y,1) and cpu_come_izq(tab,x,y,0): # >
        return c+2,'di'
    if cpu_come_izq(tab,x,y,0) and cpu_come_izq(tab,x,y,0): # \\
        return c+2,'ii'
    if cpu_come_der(tab,x,y,1) and cpu_come_der(tab,x,y,1): # //
        return c+2,'dd'
    if cpu_come_izq(tab,x,y) : # \
        return c+1,'i'
    if cpu_come_der(tab,x,y) : # /
        return c+1,'d'
    else:
        return 0,'n'

def buscar_movimientos_validos_en(board, x, y, ficha):
    fichaContraria = ''
    if ficha == 'X': fichaContraria = 'O'
    if ficha == 'O': fichaContraria = 'X'

    movimientos = []
    if ficha == 'X':
        def dentro_de_tablero(val): return 0 <= val and val < t
        if dentro_de_tablero(x + 1) and dentro_de_tablero(y - 1):
            if board[x + 1][y - 1] == '-':
                #añadir a lista de retorno
                boardInstance = get_copia(board)
                boardInstance[x][y] = '-'
                boardInstance[x + 1][y - 1] = ficha
                movimientos.append(boardInstance)
            elif board[x + 1][y - 1] == fichaContraria:
                if dentro_de_tablero(x + 2) and dentro_de_tablero(y - 2):
                    if board[x + 2][y - 2] == '-':
                        #come
                        #añadir a lista de retorno
                        boardInstance = get_copia(board)
                        boardInstance[x][y] = '-'
                        boardInstance[x + 1][y - 1] = '-'
                        boardInstance[x + 2][y - 2] = ficha
                        movimientos.append(boardInstance)

        if dentro_de_tablero(x + 1) and dentro_de_tablero(y + 1):
            if board[x + 1][y + 1] == '-':
                #añadir a lista de retorno
                boardInstance = get_copia(board)
                boardInstance[x][y] = '-'
                boardInstance[x + 1][y + 1] = ficha
                movimientos.append(boardInstance)
            elif board[x + 1][y + 1] == fichaContraria:
                if dentro_de_tablero(x + 2) and dentro_de_tablero(y + 2):
                    if board[x + 2][y + 2] == '-':
                        #come
                        #añadir a lista de retorno
                        boardInstance = get_copia(board)
                        boardInstance[x][y] = '-'
                        boardInstance[x + 1][y + 1] = '-'
                        boardInstance[x + 2][y + 2] = ficha
                        movimientos.append(boardInstance)
    else:
        def dentro_de_tablero(val): return 0 <= val and val < t
        if dentro_de_tablero(x - 1) and dentro_de_tablero(y - 1):
            if board[x - 1][y - 1] == '-':
                #añadir a lista de retorno
                boardInstance = get_copia(board)
                boardInstance[x][y] = '-'
                boardInstance[x - 1][y - 1] = ficha
                movimientos.append(boardInstance)
            elif board[x - 1][y - 1] == fichaContraria:
                if dentro_de_tablero(x - 2) and dentro_de_tablero(y - 2):
                    if board[x - 2][y - 2] == '-':
                        #come
                        #añadir a lista de retorno
                        boardInstance = get_copia(board)
                        boardInstance[x][y] = '-'
                        boardInstance[x - 1][y - 1] = '-'
                        boardInstance[x - 2][y - 2] = ficha
                        movimientos.append(boardInstance)

        if dentro_de_tablero(x - 1) and dentro_de_tablero(y + 1):
            if board[x - 1][y + 1] == '-':
                #añadir a lista de retorno
                boardInstance = get_copia(board)
                boardInstance[x][y] = '-'
                boardInstance[x - 1][y + 1] = ficha
                movimientos.append(boardInstance)
            elif board[x - 1][y + 1] == fichaContraria:
                if dentro_de_tablero(x - 2) and dentro_de_tablero(y + 2):
                    if board[x - 2][y + 2] == '-':
                        #come
                        #añadir a lista de retorno
                        boardInstance = get_copia(board)
                        boardInstance[x][y] = '-'
                        boardInstance[x - 1][y + 1] = '-'
                        boardInstance[x - 2][y + 2] = ficha
                        movimientos.append(boardInstance)
    return movimientos

def buscar_estados_posibles(board, ficha):
    
    l=[]
    for i in range (t):
        for j in range (t):
            if board[i][j] == ficha:
                l += buscar_movimientos_validos_en(board, i, j, ficha)
    
    return l

def buscar_ficha_Movimiento(board,ficha):
    f=0
    l=[]
    for i in range (t):
        for j in range (t):
            if board[i][j]==ficha:
                if ficha=='X':
                    if movimiento_valido_X(i,j,'X')==True:
                        l.append(i)
                        l.append(j)
                else:
                   if movimiento_valido_O(i,j,'O')==True:
                    l.append(i)
                    l.append(j)
    return l

def computadora():
    asd = MINMAX(test, profundidad, True)
    for i in range(t):
        for j in range(t):
            test[i][j] = asd[0][i][j]
    

        
def get_copia(board):
    copy=[[0 for x in range(t)] for y in range(t)]
    for i in range(t):
      for j in range(t):
        copy[i][j]=board[i][j]
    return copy
#----------- MIN MAX ---- MIN MAX ----- MIN MAX --------- MIN MAX -------------
def MINMAX(board, nivel, minMaxVal):
    #maximizar es para computadora, ficha="X"
    ficha = ''
    if minMaxVal: ficha = 'X'
    else: ficha = 'O'
    if nivel == 0:
        return [board, calcularPuntaje(board), contarFichas(board)]
    estados = buscar_estados_posibles(board, ficha)
    p = int()
    q = t*t
    returnBoard = []
    if minMaxVal:
        #-inf
        p = t*t*-1
    else:
        #+inf
        p = t*t

    for posibleTablero in estados:
        tmp = MINMAX(posibleTablero, nivel - 1, not minMaxVal)
        
        if minMaxVal:
            if tmp[1] > p:
                returnBoard = posibleTablero
                p = tmp[1]
                q = tmp[2]
            elif tmp[1] == p:
                if tmp[2] < q:
                    returnBoard = posibleTablero
                    p = tmp[1]
                    q = tmp[2]
        else:
            if tmp[1] < p:
                returnBoard = posibleTablero
                p = tmp[1]
                q = tmp[2]
            elif tmp[1] == p:
                if tmp[2] < q:
                    returnBoard = posibleTablero
                    p = tmp[1]
                    q = tmp[2]

    
    return [returnBoard, p, contarFichas(board)]
   





#----------------------------------------------------------------------------
def main():
    movimientos=0
    crearMatriz(8)
    llenarMatriz_Damas()
    global profundidad
    profundidad = input("Dificultad(MinMax depth): ")
    profundidad = int(profundidad)
    while True:
        imprimirMatriz()   
        print('\n')
        if movimientos%2==0:
            print("Humano \n")
            y=input("Pos x: ")
            y=int(y)
            x=input("Pos y: ")
            x=int(x)
            v=input("Movimiento 0(↑←), 1(↑→): ")
            v=int(v)
            valido = humano(x,y,v)
            if not valido:
                movimientos-=1
        else:
            print("CPU \n")
            computadora() 
            
        movimientos=movimientos+1
        sleep(1)
        #os.system( 'cls' )
    

main()          

