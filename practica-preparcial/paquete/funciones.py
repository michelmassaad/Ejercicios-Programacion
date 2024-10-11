def mostrar_matriz(matriz:list)-> None:
    # #MOSTRAR LISTA
    for fila in matriz:
        print(fila)


def contar_por_tipo_de_evento(matriz:list, tipo_salon:str , tipo_de_evento:str, 
                             col_salon:int, col_evento:int) -> int:
    '''
    Suma el tipo de evento dado cuantas veces aparezca por salon
    Recibe list, str
    Devuelve int(n apariciones)
    '''
    cantidad_evento = 0
    for i in range(len(matriz)):
        if matriz[i][col_salon] == tipo_salon and matriz[i][col_evento] == tipo_de_evento:
            cantidad_evento += 1
    return cantidad_evento

#EJERCICIO 3
# Función para consultar el evento más realizado en cada salón
def evento_mas_realizado_por_salon(matriz:list, lista_salones:list, col_salon:int, 
                                   col_evento:int, col_cantidad:int)-> list:
    '''
    Busca el evento mas repetido por salon
    recibe list, str, int, int, int
    devuelve list
    '''
    matriz_evento_max = []  # Matriz para el resultado final
    
    for salon in lista_salones:    
        cantidad_max = 0  # reiniciar el máximo por cada salon
            
        for i in range(len(matriz)):
            if matriz[i][col_salon] == salon:  #verifica el salon
                if matriz[i][col_cantidad] > cantidad_max:  # buscar la mayor cantidad
                    cantidad_max = matriz[i][col_cantidad]  
                    evento_max = matriz[i][col_evento] 

        matriz_evento_max += [[salon, evento_max , cantidad_max]]

    return matriz_evento_max

#EJERCICIO 4
def sumar_recaudacion_evento(matriz:list, tipo_salon:str , tipo_de_evento:str, 
                             col_salon:int, col_evento:int, col_monto:int) -> float:
    '''
    Suma el tipo de evento dado cuantas veces aparezca
    Recibe list, str
    Devuelve float
    '''
    total = 0
    for i in range(len(matriz)):
        if matriz[i][col_salon] == tipo_salon and matriz[i][col_evento] == tipo_de_evento:
            total += matriz[i][col_monto]
    return total

#EJERCICIO 5
def sumar_recaudacion_salon(matriz:list, tipo_salon:str) -> float:
    '''
    Suma la recaudacion de todos los eventos por salon
    Recibe list, str
    Devuelve int
    '''
    total = 0
    for i in range(len(matriz)):
        if matriz[i][1] == tipo_salon:
            aux = matriz[i][2]
            total += aux
    return total 

#EJERCICIO 6
def porcentaje_boda_oro(matriz:list , tipo_de_evento:str, lista_salones:list) -> float:
    '''
    Calcula el porcentaje por salon de un evento especifico
    recibe list, str, list
    devuelve float
    '''
    n = len(matriz)
    resultados_porcentaje = []
    
    for salon in lista_salones:
        total_eventos_salon = 0
        cont_evento = 0
        for i in range(n):
            if matriz[i][0] == salon:  
                total_eventos_salon += matriz[i][2]  
                if matriz[i][1] == tipo_de_evento: 
                    cont_evento = matriz[i][2]  
        
        # Calcular porcentaje
        total_porcentaje = (cont_evento * 100) / total_eventos_salon
        
        resultados_porcentaje += [[salon, total_porcentaje]]
    
    return resultados_porcentaje

#EJERCICIO 7
def ordenar_burbujeo(matriz:list)->list:
    '''
    Ordena descente una lista
    recibe list
    devueleve list
    '''
    n = len(matriz)
    for i in range(n):
        for j in range(0,n - i - 1):
            if matriz[j][1] < matriz[j+1][1]:
                aux = matriz[j]
                matriz[j]= matriz[j+1]
                matriz[j+1] = aux
    return matriz