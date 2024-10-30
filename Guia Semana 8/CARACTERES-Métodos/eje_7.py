# Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número 
# (1 o -1). Se debe retornar el string ordenado de manera ascendente 
# (si recibió 1 por parámetros) o descendente (si recibió -1)
# Nota: Determinar parámetros y retornos de manera que las funciones sean
# genéricas y reutilizables.

def ordenar(cadena:str, orden: int) -> str:
    lista_caracteres = list(cadena)
    if orden == 1:
        lista_caracteres.sort()
    elif orden == -1:
        lista_caracteres.sort(reverse=True)
    else:
        return("ERROR. Elija orden valido (1 o -1) ")

    return ''.join(lista_caracteres)
        
cadena = "hola mundo"

print(ordenar(cadena,1))
print(ordenar(cadena,-1))
print(ordenar(cadena,100))