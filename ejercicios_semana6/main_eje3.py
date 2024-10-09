# Ejercicio 3:
# Dadas las siguientes listas:
Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria",
               "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez",
             "Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8, 4, 9, 10, 8, 6, 4, 8, 7, 5, 6, 7, 10 ,4 , 8]

# Desarrollar una función que realice el ordenamiento de las listas por apellido de
# manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
# ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
# descendente

from paquete.funcion_eje3 import *

matriz_desordenada = [Estudiantes, Apellidos, Nota]
matriz_ordenada_nombres = ordenar_x_burbujeo_3_condiciones(matriz_desordenada)


print("Lista ordenada")
for i in range(len(Estudiantes)):
    print([Estudiantes[i],Apellidos[i], Nota[i]])
    
