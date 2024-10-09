# Ejercicio 4:
# Generar una función que mediante búsqueda binaria permite devolver una nota ingresando
# un apellido para las listas del ejercicio 3.

Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria",
               "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez",
             "Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8, 4, 9, 10, 8, 6, 4, 8, 7, 5, 6, 7, 10 ,4 , 8]


from paquete.funcion_eje3 import *
from paquete.funcion_eje4 import *

#Ordenamos las listas
matriz_desordenada = [Estudiantes, Apellidos, Nota]
matriz_ordenada_nombres = ordenar_x_burbujeo_3_condiciones(matriz_desordenada)

#una vez ordenada buscamos los valores pedidos
apellido_buscado = input("Ingrese un apellido: ")
posicion_valor_buscado = busqueda_binaria(Apellidos,apellido_buscado)
p = posicion_valor_buscado

#Mostramos el valor buscado
if p == None:
    print("No existe ningun apellido en la lista")
else:
    print([Estudiantes[p],Apellidos[p], Nota[p]])
