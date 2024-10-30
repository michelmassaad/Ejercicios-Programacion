# Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra
# en una cadena.

def reemplazar_palabra(cadena:str, palabra_a_cambiar:str, palabra_nueva:str) -> str:
    return cadena.replace(palabra_a_cambiar, palabra_nueva)

texto = "Hola mundo mundo"
print(reemplazar_palabra(texto,"mundo","gente"))