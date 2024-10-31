# Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo:
# Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta
# la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo,
# anilina.

from eje_1 import invertir_cadena

texto = "anilina"

def verificar_palindromo(cadena:str):
    cadena_invertida = invertir_cadena(cadena)
    if cadena == cadena_invertida:
        return True
    else:
        return False

print(f"{texto} es Palindromo: {verificar_palindromo(texto)}")