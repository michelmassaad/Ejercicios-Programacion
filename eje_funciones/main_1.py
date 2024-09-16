# 1- Elabore un módulo que contenga 3 funciones:
# a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
# que en caso de no recibir un radio el valor del mismo será 3.
# b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
# parámetro, sin parámetros opcionales.
# c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
# 2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
# de las mismas figuras que el punto 1.
# 3- generar paquete.
# 4- subir a github.

from paquete import areas, perimetro

# Calculando áreas
print("Área del círculo:", areas.calcular_area_circulo(4))
print("Área del cuadrado:", areas.calcular_area_cuadrado(5))
print("Área del triángulo:", areas.calcular_area_triangulo(3, 4))

# Calculando perímetros
print("Perímetro del círculo:", perimetro.calcular_perimetro_circulo(4))
print("Perímetro del cuadrado:", perimetro.calcular_perimetro_cuadrado(5))
print("Perímetro del triángulo:", perimetro.calcular_perimetro_triangulo(3, 4, 5))