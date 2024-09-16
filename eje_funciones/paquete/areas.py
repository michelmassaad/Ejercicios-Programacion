# 1- Elabore un módulo que contenga 3 funciones:
# a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
# que en caso de no recibir un radio el valor del mismo será 3.
import math
def calcular_area_circulo(radio:float = 3):
    area_circulo = math.pi * (radio**2)
    return area_circulo

# b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
# parámetro, sin parámetros opcionales.
def calcular_area_cuadrado(longitud:float)-> float:
    area_cuadrado = longitud * longitud
    return area_cuadrado

# c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
def calcular_area_triangulo(base: float, altura: float) -> float:
    area_triagunlo = (base * altura) / 2
    return area_triagunlo
