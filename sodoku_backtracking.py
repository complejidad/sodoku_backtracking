#SODOKU utilizando la Técnica de Backtracking

tablero = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# 1. Buscamos posiciones vacias
def encontrar_vacio(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                return (i, j)  # fila, columna

    return None

# 2. Verificamos numeros validos
def valido(tab, num, pos):
    # Verificar fila
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False

    # Verificar columna
    for i in range(len(tab)):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False

    # Verificar Caja
    caja_x = pos[1] // 3
    caja_y = pos[0] // 3

    for i in range(caja_y*3, caja_y*3 + 3):
        for j in range(caja_x * 3, caja_x*3 + 3):
            if tab[i][j] == num and (i,j) != pos:
                return False

    return True


# Repetimos el procedimiento hasta terminar el tablero
def resultado(tab):
    buscar = encontrar_vacio(tab)
    if not buscar:
        return True
    else:
        fila, col = buscar

    for i in range(1,10):
        if valido(tab, i, (fila, col)):
            tab[fila][col] = i

            if resultado(tab):
                return True

            # Backtracking 
            tab[fila][col] = 0

    return False





def print_tablero(tab):
    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")




print()
print("         SODOKU         ")
print()
print("------------------------")
print("    Tablero original    ")
print("________________________")
print()
print_tablero(tablero)
resultado(tablero)
print()
print("------------------------")
print("        Resultado       ")
print("________________________")
print()
print_tablero(tablero)