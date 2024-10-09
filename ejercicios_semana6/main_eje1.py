# Ejercicio 1:
# Dadas las siguientes listas:
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro"
           ,"Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente.

from paquete.funcion_eje1 import *
matriz_desordenada = [Nombres, Edades]
matriz_ordenada_nombres = ordenar_x_burbujeo(matriz_desordenada)

# print(f"La lista ordenada por nombre es: \n {matriz_ordenada_nombres}")

print("Lista ordenada")
for i in range(len(Nombres)):
    print([Nombres[i],Edades[i]])


