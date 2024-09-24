# 3- Programar un algoritmo que permita crear una nueva lista de respondentes de manera
# secuencial. Deberán ingresar su nombre, sexo, cantidad de horas trabajadas e ingreso
# semanal en listas separadas.

import eje_3y5_funciones as fn
cantidad_respondentes = int(input("¿Cuántos respondentes desea ingresar? "))
cantidad_maxima = cantidad_respondentes

#Creacion de las variables listas
nombres = [""] * cantidad_maxima
sexos = [""] * cantidad_maxima
horas_trabajadas = [0] * cantidad_maxima
ingresos_semanales = [0] * cantidad_maxima

#Esta llamada desde eje 5
fn.recolectar_datos(cantidad_maxima, nombres, sexos, horas_trabajadas, ingresos_semanales)

# Mostrar los datos ingresados
fn.mostrar_datos(cantidad_maxima, nombres, sexos, horas_trabajadas, ingresos_semanales)

#Corregir datos ingresados
print("\nCorreccion de datos:")
posicion = int(input("\nIngrese la posición que desea corregir: "))
fn.corregir_datos(posicion-1, cantidad_maxima, nombres, sexos, horas_trabajadas, ingresos_semanales)

# Mostrar los datos corregidos
fn.mostrar_datos(cantidad_maxima, nombres, sexos, horas_trabajadas, ingresos_semanales)
