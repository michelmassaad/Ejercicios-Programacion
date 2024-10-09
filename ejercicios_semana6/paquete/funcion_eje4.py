def busqueda_binaria(lista:list,valor_buscado:str) -> int:
    '''
    Busca en una lista un valor y devuelve la posicion de la lista
    Recibe una lista y un valor buscado str
    devuelve un int con la posicion de la lista
    '''
    inicio = 0
    final = len(lista) - 1
    
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == valor_buscado:
            return medio # devolvemos la posicion de la lista para usarla en otras listas
        elif lista[medio] < valor_buscado: 
            inicio = medio + 1
        else:
            final = medio - 1
    return None