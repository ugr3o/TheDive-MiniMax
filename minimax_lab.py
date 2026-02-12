# le damos los valores para la cantidad de filas y columnas que tendra nuestra matriz
filas = 6
columnas = 6
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

#se evaluan todos los movimientos posibles dentro del tablero desde cualquier posicion
def movimientos_posibles(pos):
    movimientos = []   # se crea una lista donde se almaceneran todos los movimientos posibles en cualquier posicion
    fila = pos[0]
    col = pos[1]
    if fila > 0: #si el numero de fila es mayor a 0, esta en fila 1-4
        movimientos.append([fila -1, col]) # se resta una posicion a la fila, ya que es un movimiento posible y eso se agrega a la lista
    if fila < 5: # si la fila es menor a 4, puede estar en 0-3 
        movimientos.append([fila +1, col]) # se le suma una posicion en fila, es un movimiento posible
    if col > 0: # si la columna es mayor a 0, esta en columna 1-4
        movimientos.append([fila, col -1]) # se le resta una posicion, es un movimiento posible
    if col < 5: # si la columna es menor a 4, esta en columna 0-3
        movimientos.append([fila, col +1]) # se le suma una posicion, es un movimiento posible
    return(movimientos) # se retorna los resultados almacenados en la lista movimientos

def minimax(pos_gato, pos_raton,profundidad,turno_gato): #minimax utilizara estos 4 parametros para realizar los calculos

    if profundidad == 0: # condicion de si la profundidad es igual a 0, solo retornara la posicion actual del gato y del raton
        return calc_distancia(pos_gato, pos_raton) #se retorna la posicion actual de gato y el raton
    if turno_gato: # si el turno del gato es True
        max_valor = 999999 # se le da un valor alto 
        movimientos = movimientos_posibles(pos_gato) # se estira los movimientos posibles del gato desde su posicion
        for movimiento in movimientos: # se procede a recorrer entre cada uno de los movimientos dentro de los posibles para que se evaluen
            valor = minimax(movimiento, pos_raton, profundidad - 1, False)#se guarda en la variable "valor" el movimiento con todos los estados, se le da la posicion del raton y la profundidad
            if valor < max_valor: # con la informacion guardada en la variable valor, se evalua cual es el menor valor, porque el gato quiere minimizar la distancia con el raton
                max_valor = valor # el valor maximo pasa a ser igual a el valor obtenido luego de toda la evaluacion
        return max_valor #se retorna el resultado final con el menor valor para el gato
    else: # raton
        max_valor = -999999 # se le asigna un valor muy bajo
        movimientos = movimientos_posibles(pos_raton) # se estira todos los posibles movimientos desde la posicion del raton de la funcion
        for movimiento in movimientos: # se recorre cada uno de los movimientos que estan dentro de la lista movimientos
            valor = minimax(pos_gato, movimiento, profundidad - 1, True) #se guarda en la variable "valor" el movimiento con los estados, posicion del gato profundidad
            if valor > max_valor: #evalua cual es el mayor valor porque el raton quiere maximizar la distancia entre el gato
                max_valor = valor # se guarda el valor en la variable max_valor
        return max_valor # se retorna el valor final con el mayor valor para el raton
    
def mejor_movimiento_raton(pos_gato, pos_raton):
    movimientos = movimientos_posibles(pos_raton)
    mejor_mov = None
    mejor_valor = -999999
    for movimiento in movimientos:
        valor = minimax(pos_gato, movimiento, 5, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = movimiento
    return mejor_mov

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
            print(elemento,end="   ")
        print("   ")
    #pedimos al usuario el input donde elige la direccion de movimiento del gato
    print("Ingrese el movimiento que quiere realizar: w:arriba, s:abajo, a: izquierda, d: derecha, q: salir")
    direccion = input("Su movimiento: ")
    #se cambia la posicion del gato por el "." cada que se mueve
    matriz[pos_gato[0]][pos_gato[1]] = '.'

    if direccion == "w" and pos_gato[0] > 0: #movimiendo hacia arriba
        pos_gato[0] = pos_gato[0] - 1
    elif direccion == "s" and pos_gato[0] < 5: #movimiento hacia abajo 
        pos_gato[0] = pos_gato[0] + 1
    elif direccion == "a" and pos_gato[1] > 0: #movimiento a la izquierda
        pos_gato[1] = pos_gato[1] - 1
    elif direccion == "d" and pos_gato[1] < 5: #movimiento a la derecha
        pos_gato[1] = pos_gato[1] + 1
    elif direccion == "q":                     #salir del juego
        print("Saliendo del juego...")
        jugando = False
    else:                                      
        print("El movimiento no es valido, o salio del tablero")
    #se va reemplazando la ubicacion de la G al moverse por el tablero
    matriz[pos_gato[0]][pos_gato[1]] = "G"

    if direccion != "q":
        matriz[pos_raton[0]][pos_raton[1]]= "." #borra la posicion anterior del raton

        nueva_pos_raton = mejor_movimiento_raton(pos_gato,pos_raton)

        if nueva_pos_raton:
            pos_raton = nueva_pos_raton
        
        matriz[pos_raton[0]][pos_raton[1]] = "R"

        print(f"el raton se movio a: {pos_raton}")

    if pos_gato[0] == pos_raton[0] and pos_gato[1] == pos_raton[1]:
        print("El gato a atrapado al raton!")
        jugando = False
