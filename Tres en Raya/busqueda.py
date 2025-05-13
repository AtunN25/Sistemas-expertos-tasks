"""
# Jugador de Tres en Raya #
"""

import math

X = "X"
O = "O"
EMPTY = None


def estado_inicial():
    """
    Retorna el estado incial del tablero.
    """
    """return [[EMPTY, X, O],
            [O, X, X],
            [X, EMPTY, O]]"""

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def jugador(tablero):
    """
    Retorna el jugador que tiene el turno en el tablero
    """
    # X sera prioridad en este caso

    cantX = sum(fila.count(X) for fila in tablero)
    cantO = sum(fila.count(O) for fila in tablero)

    if cantX > cantO:
        return O  
    else:
        return X  


def acciones(tablero):
    """
    Retorna un set de todas las posibles acciones (i,j) disponibles en el tablero.
    """

    acciones_posibles = set()

    for i in range(3):                     
        for j in range(3):
            if tablero[i][j] == EMPTY :
                acciones_posibles.add((i,j))

    return acciones_posibles


def resultado(tablero, accion):
    """
    Retorna el tablero resultante de aplicar el movimiento (i,j) en el tablero.
    """
    i,j = accion

    if tablero[i][j] != EMPTY:
            raise ValueError("Posición ya ocupada")

    tablero_resultante = []

    for fila in tablero:
        nueva_fila = fila.copy()  
        tablero_resultante.append(nueva_fila)

    tablero_resultante[i][j] = jugador(tablero)

    return tablero_resultante

    


def ganador(tablero):
    """
    Retorna el ganador del juego. Devuelve None si no hay ganador.
    """
    if( 
        (tablero[0][0] == tablero[0][1] == tablero[0][2] == X) or
        (tablero[1][0] == tablero[1][1] == tablero[1][2] == X) or
        (tablero[2][0] == tablero[2][1] == tablero[2][2] == X) or
        (tablero[0][0] == tablero[1][0] == tablero[2][0] == X) or
        (tablero[0][1] == tablero[1][1] == tablero[2][1] == X) or
        (tablero[0][2] == tablero[1][2] == tablero[2][2] == X) or
        (tablero[0][0] == tablero[1][1] == tablero[2][2] == X) or
        (tablero[2][0] == tablero[1][1] == tablero[0][2] == X) 
     ):
     return X
   
    if( 
        (tablero[0][0] == tablero[0][1] == tablero[0][2] == O) or
        (tablero[1][0] == tablero[1][1] == tablero[1][2] == O) or
        (tablero[2][0] == tablero[2][1] == tablero[2][2] == O) or
        (tablero[0][0] == tablero[1][0] == tablero[2][0] == O) or
        (tablero[0][1] == tablero[1][1] == tablero[2][1] == O) or
        (tablero[0][2] == tablero[1][2] == tablero[2][2] == O) or
        (tablero[0][0] == tablero[1][1] == tablero[2][2] == O) or
        (tablero[2][0] == tablero[1][1] == tablero[0][2] == O) 
     ):
     return O

    return None  



def terminal(tablero):
    """
    Retorna True si el juego ha finalizado, Falso de otra forma.
    """

    if ganador(tablero) is not None:
        return True

    for fila in tablero:
        if EMPTY in fila:
             return False

    return True
   


def utilidad(tablero):
    """
    Retorna 1 si X ha ganado el juego ,-1 si 0 ha ganado, 0 de otra forma.
    """
    ganador_tablero = ganador(tablero)

    if(ganador_tablero == X):
        return 1
    
    if(ganador_tablero == O):
        return -1
    
    if(ganador_tablero == None):
        return 0



def minimax(tablero):
    """
    Retorna la acción optima para el jugador actual en el tablero.
    """
    if jugador(tablero) == X:
        _ , accion = max_value(tablero, -math.inf, math.inf)
        return accion
    else:
        _ , accion = min_value(tablero, -math.inf, math.inf)
        return accion



def max_value(state, alpha, beta):
    if terminal(state):
        return utilidad(state),None
    
    v = -math.inf
    mejor_accion = None
    for action in acciones(state):
        valor, _ = min_value(resultado(state,action), alpha, beta)
        if valor > v:
            v = valor  
            mejor_accion = action
            alpha = max(alpha, v)
        
        if alpha >= beta:
            print("MAX poda")
            break

    return v, mejor_accion


def min_value(state, alpha, beta):
    if terminal(state):
        return utilidad(state),None
    
    v = math.inf
    mejor_accion = None
    for action in acciones(state):
        valor, _ = max_value(resultado(state,action), alpha, beta)
        if valor < v:
            v = valor
            mejor_accion = action
            beta = min(v,beta)
        
        if alpha >= beta:
            print("MIN poda")
            break

    return v , mejor_accion



"""
def main():
    # Obtener el estado inicial del tablero
    tablero = estado_inicial()
    
    # Mostrar el tablero inicial
    print("Tablero inicial:")
    for fila in tablero:
        print(fila)

if __name__ == "__main__":
    main()
    """