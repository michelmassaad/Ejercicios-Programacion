def ordenar_x_burbujeo_iguales(matriz:list) -> list:
    '''
    Ordena las listas de lista1 y lista2 en paralelo, basándose en lista1 
    pero si hay datos iguales fijarse en lista2.
    
    Recibe dos listas: nombres y edades.
    Devuelve las dos listas ordenadas.
    '''
    
    lista1 = matriz[0]
    lista2 = matriz[1]
    
    if type(lista1) != list or type(lista2) != list:
        print("El parametro de la funcion debe ser una lista")
        return None
    
    n = len(lista1)
    
    if n != len(lista2):
        print("Las listas lista1 y lista2 deben tener la misma longitud")
        return None
    
    for i in range(n):
        intercambio = False
        
        for j in range(0, n - i - 1):
            if matriz[0][j] > matriz[0][j+1]:
                intercambio = True
                #Intercambiar lista1
                menor = lista1[j+1]
                lista1[j+1] = lista1[j]
                lista1[j] = menor
                #Intercambiar lista2 para que esten enlazadas
                menor2 = lista2[j+1]
                lista2[j+1] = lista2[j]
                lista2[j] = menor2
                
            elif lista1[j] == lista1[j+1]: # VERIFICO SI SON IGUALES
                if lista2[j] > lista2[j+1]: #Tomo en cuenta la lista 2 ahora
                    #Intercambiar lista2
                    menor2 = lista2[j+1]
                    lista2[j+1] = lista2[j]
                    lista2[j] = menor2
                    #Intercambiar lista1 para que esten enlazadas
                    menor = lista1[j+1]
                    lista1[j+1] = lista1[j]
                    lista1[j] = menor
                
        if intercambio == False:
        #     print(f"Dejo de intercambiar en la interacion {i}")
            break
        
        matriz = [lista1, lista2]

    return matriz
