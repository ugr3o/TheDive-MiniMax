filas = 7 # cantidad de filas del tablero
columnas = 7 # cantidad de columnas del tablero
matriz = [] # lista de listas que representa el tablero
pos_gato = [4,3] # posicion inicial del gato [fila, columna]
pos_raton = [0, 0] # posicion inicial del raton
pos_salida = [6,6] # posicion de la salida

for i in range(filas):
    fila_temporal = []
    for j in range(columnas):
        fila_temporal.append("⬜") # cada celda inicia vacia
    matriz.append(fila_temporal)

matriz[pos_gato[0]][pos_gato[1]] = '🐱' # se ubica el gato en la matriz
matriz[pos_raton[0]][pos_raton[1]] = '🐁' # se ubica el raton en la matriz
matriz[pos_salida[0]][pos_salida[1]] = '🚪' # se ubica la salida en la matriz

def calc_distancia(p1, p2): # distancia Manhattan: pasos horizontales + verticales
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def movimientos_posibles(pos): # retorna los movimientos validos desde una posicion
    movimientos = []
    fila = pos[0]
    col = pos[1]
    if fila > 0: # verifica que no este en el borde superior
        movimientos.append([fila -1, col]) # movimiento hacia arriba
    if fila < filas -1: # verifica que no este en el borde inferior
        movimientos.append([fila +1, col]) # movimiento hacia abajo
    if col > 0: # verifica que no este en el borde izquierdo
        movimientos.append([fila, col -1]) # movimiento hacia la izquierda
    if col < columnas -1: # verifica que no este en el borde derecho
        movimientos.append([fila, col +1]) # movimiento hacia la derecha
    return(movimientos)

def minimax(pos_gato, pos_raton,pos_salida,profundidad,turno_gato):

    if pos_raton[0] == pos_salida[0] and pos_raton[1] == pos_salida[1]: # caso base: raton llego a la salida
        return 999999
    if pos_gato[0] == pos_raton[0] and pos_gato[1] == pos_raton[1]: # caso base: gato atrapo al raton
        return -999999
    if profundidad == 0: # caso base: evalua el estado actual con la heuristica
        return calc_distancia(pos_gato, pos_raton) - 5 * calc_distancia(pos_raton, pos_salida)
    if turno_gato: # gato es el minimizador: busca reducir la distancia con el raton
        min_valor = 999999
        movimientos = movimientos_posibles(pos_gato)
        for movimiento in movimientos:
            valor = minimax(movimiento, pos_raton, pos_salida, profundidad - 1, False)
            if valor < min_valor: # guarda el menor valor encontrado
                min_valor = valor
        return min_valor
    else: # raton es el maximizador: busca alejarse del gato y llegar a la salida
        max_valor = -999999
        movimientos = movimientos_posibles(pos_raton)
        for movimiento in movimientos:
            valor = minimax(pos_gato, movimiento, pos_salida, profundidad - 1, True)
            if valor > max_valor: # guarda el mayor valor encontrado
                max_valor = valor
        return max_valor
    
def mejor_movimiento_raton(pos_gato, pos_raton, pos_salida): # decide el movimiento optimo del raton
    movimientos = movimientos_posibles(pos_raton)
    mejor_mov = None
    mejor_valor = -999999
    for movimiento in movimientos:
        if movimiento[0] == pos_gato[0] and movimiento[1] == pos_gato[1]: # descarta moverse al gato
            continue
        valor = minimax(pos_gato, movimiento,pos_salida, 2, True)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = movimiento
    return mejor_mov

jugando = True
while jugando:
    for fila in matriz:
        for elemento in fila:
            print(elemento,end="   ")
        print("   ")
    
    print("Ingrese el movimiento que quiere realizar: w:arriba, s:abajo, a: izquierda, d: derecha, q: salir")
    opcion = input("Su movimiento: ")

    if opcion == "": # valida que no este vacia la entrada
        print("MOVIMIENTO INVALIDO o estas intentando salir del tablero.")
        continue
    pos_anterior = [pos_gato[0],pos_gato[1]] # guarda la posicion anterior para limpiar la celda
    if pos_gato == pos_salida: # si el gato estaba sobre la salida, la restaura
        matriz[pos_anterior[0]][pos_anterior[1]] = '🚪'
    else:
        matriz[pos_anterior[0]][pos_anterior[1]] = '⬜'

    if opcion == "q":
        print("Saliendo del juego...")
        jugando = False
        continue
    elif opcion == "w" and pos_gato[0] > 0: # mueve arriba si no esta en el borde
        pos_gato[0] = pos_gato[0] - 1
    elif opcion == "s" and pos_gato[0] < filas -1: # mueve abajo si no esta en el borde
        pos_gato[0] = pos_gato[0] + 1
    elif opcion == "a" and pos_gato[1] > 0: # mueve izquierda si no esta en el borde
        pos_gato[1] = pos_gato[1] - 1
    elif opcion == "d" and pos_gato[1] < columnas -1: # mueve derecha si no esta en el borde
        pos_gato[1] = pos_gato[1] + 1
    else:
        print("Estas en el limite del tablero.")
        matriz[pos_gato[0]][pos_gato[1]] = "🐱" # redibuja el gato antes del continue
        continue

    matriz[pos_gato[0]][pos_gato[1]] = "🐱" # actualiza la nueva posicion del gato en la matriz
    
    if pos_raton[0] == pos_gato[0] and pos_raton[1] == pos_gato[1]:
        print("El gato a atrapado al raton!")
        jugando = False

    if pos_raton != pos_gato:
        matriz[pos_raton[0]][pos_raton[1]]= "⬜" # limpia la posicion anterior del raton

    nueva_pos_raton = mejor_movimiento_raton(pos_gato, pos_raton, pos_salida)

    if nueva_pos_raton:
        pos_raton = nueva_pos_raton

    if pos_raton[0] == pos_salida[0] and pos_raton[1] == pos_salida[1]:
        print("El raton escapo del gato")
        jugando = False
    matriz[pos_raton[0]][pos_raton[1]] = "🐁" # actualiza la nueva posicion del raton en la matriz