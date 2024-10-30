# CADENA DE CARACTERES-Métodos
# Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una
# cadena.

def invertir_cadena(cadena: str) -> str:
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida

# cadena = "Hola mundo"
# cadena_invertida = invertir_cadena(cadena)
# print(cadena_invertida)
