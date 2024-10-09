def ordenar_x_burbujeo(matriz: list) -> list:
    '''
    Ordena las listas de lista1 = matriz[0] y lista2 = matriz[1] en paralelo, basándose en matriz[0].
    Recibe dos listas: nombres y edades.
    Devuelve las dos listas ordenadas.
    '''

    if type(matriz[0]) != list or type(matriz[1]) != list:
        print("El parametro de la funcion debe ser una lista")
        return None
    
    n = len(matriz[0])
    
    if n != len(matriz[1]):
        print("Las listas matriz[0] y matriz[1] deben tener la misma longitud")
        return None
    
    for i in range(n):
        intercambio = False
        
        for j in range(0, n - i - 1):
            if matriz[0][j] > matriz[0][j+1]:
                intercambio = True
                #Intercambiar matriz[0]
                menor = matriz[0][j+1]
                matriz[0][j+1] = matriz[0][j]
                matriz[0][j] = menor
                #Intercambiar matriz[1] para que esten enlazadas
                menor2 = matriz[1][j+1]
                matriz[1][j+1] = matriz[1][j]
                matriz[1][j] = menor2
                
        if intercambio == False:
        #     print(f"Dejo de intercambiar en la interacion {i}")
            break
        
        # matriz = [matriz[0], matriz[1]]

    
    return matriz