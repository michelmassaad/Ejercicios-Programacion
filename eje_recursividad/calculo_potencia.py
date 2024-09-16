# 1 - Calcular mediante recursividad la potencia de un número, mediante una función que
# recibe un número base de tipo entero y un exponente de tipo entero. Utilizar parámetros
# opcionales para definir que si la función no recibe ningún parámetro devolverá 2 al
# cuadrado.

def calcular_potencia(base:int = 2, exponente:int = 2) -> int:
    
    if exponente == 0:
        return 1
    else:
        resultado = base * calcular_potencia(base,exponente-1)
        return resultado

print(calcular_potencia(3,3))