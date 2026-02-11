# le damos los valores para la cantidad de filas y columnas que tendra nuestra matriz
filas = 5
columnas = 5
#creamos la matriz principal
matriz = []
#posiciones reales de cada cosa dentro del tablero - posicion inicial
pos_gato = [4, 4]
pos_raton = [1, 1]
pos_queso = [2, 3]

#funciones auxiliares para implementar en minimax
#calculo de distancia manthattan, donde las posiciones de fila y columna se restan y luego ambas se suman
def calc_distancia(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

print(calc_distancia(pos_gato,pos_raton))

#se evaluan todos los movimientos posibles dentro del tablero desde cualquier posicion
def movimientos_posibles(pos):
    movimientos = []
    fila = pos[0]
    col = pos[1]
    if fila > 0:
        movimientos.append([fila -1, col])
    if fila < 4:
        movimientos.append([fila +1, col])
    if col > 0:
        movimientos.append([fila, col -1])
    if col < 4:
        movimientos.append([fila, col +1])
    return(movimientos)

print(movimientos_posibles(pos_gato))

#bucle for para ir agregando puntos en todo el "mapa"
for i in range(filas):
    fila_temporal = []
    for j in range(columnas):
        fila_temporal.append(".")
    matriz.append(fila_temporal)
#interpreta las ubicaciones asignadas anteriormente para que puedan ser agregadas al tablero
matriz[pos_gato[0]][pos_gato[1]] = 'G'
matriz[pos_raton[0]][pos_raton[1]] = 'R'
matriz[pos_queso[0]][pos_queso[1]] = '#'

jugando = True

while jugando:
    #mostrar el tablero del juego con las posiciones ya establecidas antes 
    for fila in matriz:
        for elemento in fila:
            print(elemento,end=" ")
        print("  ")
    #pedimos al usuario el input donde elige la direccion de movimiento del gato
    print("Ingrese el movimiento que quiere realizar: w:arriba, s:abajo, a: izquierda, d: derecha, q: salir")
    direccion = input("Su movimiento: ")
    #se cambia la posicion del gato por el "." cada que se mueve
    matriz[pos_gato[0]][pos_gato[1]] = '.'

    if direccion == "w" and pos_gato[0] > 0: #movimiendo hacia arriba
        pos_gato[0] = pos_gato[0] - 1
    elif direccion == "s" and pos_gato[0] < 4: #movimiento hacia abajo 
        pos_gato[0] = pos_gato[0] + 1
    elif direccion == "a" and pos_gato[1] > 0: #movimiento a la izquierda
        pos_gato[1] = pos_gato[1] - 1
    elif direccion == "d" and pos_gato[1] < 4: #movimiento a la derecha
        pos_gato[1] = pos_gato[1] + 1
    elif direccion == "q":                     #salir del juego
        print("Saliendo del juego...")
        jugando = False
    else:                                      
        print("El movimiento no es valido, o salio del tablero")
    #se va reemplazando la ubicacion de la G al moverse por el tablero
    matriz[pos_gato[0]][pos_gato[1]] = "G"

    if pos_gato[0] == pos_raton[0] and pos_gato[1] == pos_raton[1]:
        print("El gato a atrapado al raton!")
        jugando = False
