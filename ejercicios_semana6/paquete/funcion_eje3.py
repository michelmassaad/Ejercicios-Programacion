
def ordenar_x_burbujeo_3_condiciones(matriz_desordenada:list)->list:

    for i in range(len(matriz_desordenada[0])):
        for j in range(0,len(matriz_desordenada[0]) - i - 1):
            if matriz_desordenada[1][j] > matriz_desordenada[1][j+1]: #ordena ascendente por apellido
                ordenar_ascendente(matriz_desordenada,j)
            
            elif matriz_desordenada[1][j] == matriz_desordenada[1][j+1]: #verifica si apellidos iguales
                if matriz_desordenada[0][j] > matriz_desordenada[0][j+1]: #ordena ascendete por nombre
                    ordenar_ascendente(matriz_desordenada,j)

                elif matriz_desordenada[0][j] == matriz_desordenada[0][j+1]: #verifica si nombre y apellido iguales
                    if matriz_desordenada[2][j] < matriz_desordenada[2][j+1]: #ordena por nota descendente
                        ordenar_descendente(matriz_desordenada,j)

    return matriz_desordenada

def ordenar_ascendente(matriz_desordenada,j):
    # Itera por cada fila de la matriz es como (fila = matriz_desordenada[i])
    for fila in matriz_desordenada:
        menor = fila[j+1]
        fila[j+1] = fila[j]
        fila[j] = menor

def ordenar_descendente(matriz_desordenada,j): #OTRA MANERA DE HACERLO
    for i in range(len(matriz_desordenada)): # Itera por cada fila de la matriz
        mayor = matriz_desordenada[i][j]  
        matriz_desordenada[i][j] = matriz_desordenada[i][j+1]
        matriz_desordenada[i][j+1] = mayor