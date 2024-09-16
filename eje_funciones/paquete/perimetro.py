import math
def calcular_perimetro_circulo(radio:float = 3):
    perimetro_circulo = 2 * math.pi * radio
    return perimetro_circulo

def calcular_perimetro_cuadrado(longitud:float) -> float:
    perimetro_cuadrado = 4 * longitud
    return perimetro_cuadrado

def calcular_perimetro_triangulo(lado_a:float, lado_b:float, lado_c:float) -> float:
    perimetro_triagunlo = lado_a + lado_b + lado_c
    return perimetro_triagunlo
