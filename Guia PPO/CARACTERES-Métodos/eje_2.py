# Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.

def cuenta_palabras(cadena:str) -> int:
    lista_palabras = cadena.split()  #divide en una lista las palabras
    return len(lista_palabras)

print(cuenta_palabras("soy una cadena"))