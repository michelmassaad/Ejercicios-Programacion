# Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.

def capitalizar_palabras(cadena: str) -> str:
    return cadena.title()

texto = "hola mundo"
texto_capitalizado = capitalizar_palabras(texto)
print(texto_capitalizado)

