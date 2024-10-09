# Ejercicio 2:
# Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales",
           "Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
           "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100, 98, 80, 25, 87, 38, 64, 42, 28, 91, 66, 35, 49, 57]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
# descendente.

from paquete.funcion_eje2 import *

matriz_desordenada = [Nombres, Puntos]

matriz_ordenada_nombres = ordenar_x_burbujeo_iguales(matriz_desordenada)

# print(f"La lista ordenada por nombre es: \n {matriz_ordenada_nombres}")

print("Lista ordenada")
for i in range(len(Nombres)):
    print([Nombres[i],Puntos[i]])