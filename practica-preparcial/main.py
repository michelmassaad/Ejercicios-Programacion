# Una empresa se dedica a la realización de eventos. Para ello cuentan con 3
# salones en CABA, que se encuentran en Puerto Madero, Palermo y San
# Telmo.
# Los salones pueden realizar 4 tipos diferentes de eventos: cumpleaños,
# casamientos, fiestas de 15 y bodas de oro.
# La oficina central, recibe mensualmente una planilla de donde se indican la
# cantidad de eventos realizados en cada salón.
# Realizar un menú de opciones que permita:

from paquete.funciones import *
#creo las listas con los datos 
lista_eventos = ["cumpleaños","casamientos","fiestas de 15","bodas de oro"]
lista_salones = ["Puerto Madero","Palermo","San Telmo"]


# PARA NO CARGAR DATOS DE VUELTA Y HACER PRUEBAS PUSE UNA DE EJM
matriz_datos = [[77,"casamientos","San Telmo"],
                [7,"fiestas de 15","Palermo"],
                [22,"casamientos","Puerto Madero"],
                [55,"bodas de oro","Palermo"],
                [45, "bodas de oro", "Palermo"],
                [15, "casamientos", "San Telmo"]]
# DATOS Para probar ejercicio suponemos una lista, 
# tiene que ser del mismo tamaño que matriz datos
lista_montos = [5000000, 1000, 3000, 7000 ,8000 ,10000]

# region  1. Cargar secuencialmente eventos que contengan un id, un tipo de
# # evento y un salón correspondiente en el main.py

# matriz_datos = [] # Creamos una matriz para agregarle los datos

# #Planilla donde indican la cantidad de eventos (Pedimos que el usuario lo rellene)
# n_eventos = int(input("Ingrese la cantidad de eventos: "))

# # Carga y Validacion de datos
# for i in range(n_eventos):
#     lista_id = int(input(f"\nIngrese un id en la posición {i}: "))
    
#     lista_tipo_evento = input(f"Ingrese un tipo de evento en la posición {i}: ")
#     while lista_tipo_evento not in lista_eventos:
#         lista_tipo_evento = input(f"Error. Ingrese un tipo de evento válido en la posición {i}: ")

#     lista_salon = input(f"Ingrese un salón en la posición {i}: ")
#     while lista_salon not in lista_salones:
#         lista_salon = input(f"Error. Ingrese un salón válido en la posición {i}: ")

#     # Agregar la fila como [id, tipo_evento, salon] a la matriz
#     matriz_datos += [[lista_id, lista_tipo_evento, lista_salon]]

# #MOSTRAR MATRIZ
# print("\nMatriz cargada")
# mostrar_matriz(matriz_datos)

# endregion

# region 2. Calcular por cada salón la cantidad total de fiestas realizadas de cada
# # tipo. Utilizar una función.

matriz_cantidad_evento = []

for salon in lista_salones:  # itera salones
    for evento in lista_eventos: #itera eventos
        cantidad_evento = contar_por_tipo_de_evento(matriz_datos ,salon , evento, 2 , 1)
        matriz_cantidad_evento += [[salon, evento , cantidad_evento]]

#MOSTRAR RESULTADOS CANTIDAD DE EVENTOS POR SALON 
print("\nCANTIDAD DE EVENTOS POR SALON y EVENTO")
mostrar_matriz(matriz_cantidad_evento)

# endregion
   
# region 3. Consultar el nombre del evento más realizado en cada salón. Utilizar
# # función.

resultados = evento_mas_realizado_por_salon(matriz_cantidad_evento,lista_salones,0,1,2)

# # Imprimir resultados
print("\nLista Evento mas realizado por salon")
mostrar_matriz(resultados)

#endregion

#region # 4. Calcular la recaudación de cada salón, teniendo en cuenta que
# disponemos de un vector con los valores de cada tipo de evento.
# Generar una función.

#si quieres para comprobar el programa usando la carga de datos del ejercicio 1
# puedes cargarla de esta manera
# lista_montos = []
# for i in range(n_eventos):
#     lista_montos += [int(input(f"\nIngrese un monto en la posición {i}: "))]

#creo una matriz recaudacion para Poder comprobar usando matriz_datos
matriz_recaudacion = []
for i in range(len(matriz_datos)):  #= [evento, salon, montos]
    matriz_recaudacion += [[matriz_datos[i][1], matriz_datos[i][2], lista_montos[i]]]

# mostrar_matriz(matriz_recaudacion)

#Recaudacion tomando en cuenta por salon
resultados_recaudacion_salon = []
for salon in lista_salones:  # itera salones
    total_recaudacion_salon = sumar_recaudacion_salon(matriz_recaudacion,salon)
    resultados_recaudacion_salon += [[salon, total_recaudacion_salon]]

print("\nRecaudacion por salon") 
mostrar_matriz(resultados_recaudacion_salon)

#endregion

#region 5. Calcular la cantidad de salones que hayan recaudado más de
# $5.000.000 en casamientos.
# matriz_total_recaudacion_salon = []

n_recaudacion_salon_evento = []
for salon in lista_salones:  # itera salones
    for evento in lista_eventos: #itera eventos
        total_recaudacion_evento = sumar_recaudacion_evento(matriz_recaudacion,
                                                            salon,evento,1,0,2)
        n_recaudacion_salon_evento += [[salon, evento , total_recaudacion_evento]]
        
# print("\nRecaudacion por salon y evento") 
# mostrar_matriz(n_recaudacion_salon_evento)  #para ver lista creada

matriz_total_recaudacion_salon = []
for salon in lista_salones:  # itera salones
        total_recaudacion_salon = sumar_recaudacion_evento(n_recaudacion_salon_evento,
                                                           salon,"casamientos",0,1,2)
        matriz_total_recaudacion_salon += [[salon, "casamientos" , total_recaudacion_salon]]

# print("\nRecaudacion por salon y evento especifico") 
# mostrar_matriz(matriz_total_recaudacion_salon)  #Para ver resultados de lista completa

#RESULTADOS ejercicio 5
print("\nRecaudacion por salon y evento especifico") 
for fila in matriz_total_recaudacion_salon:
    if fila[2] > 5000000: #mostrar solo mayores
        print([fila[0],fila[1],fila[2]])
    else:
        print(f"No hay recaudacion en casamientos en {fila[0]} mayor a $5.000.000")

#endregion

#region 6. Calcular el porcentaje de bodas de oro realizadas en cada salón.
# Mostrar el que haya realizado el mayor porcentaje.

#SE USA LA matriz_cantidad_evento DEL EJERCICIO 2 [[salon, evento , cantidad_evento]]

resultados_porcentaje_boda_oro = porcentaje_boda_oro(matriz_cantidad_evento, "bodas de oro",
                                                     lista_salones)

# mostrar_matriz(resultados_porcentaje_boda_oro)  #Para comprobar solamente

# Mostrar el salón con el mayor porcentaje de "bodas de oro"
print("\nMayor porcentaje de bodas de oro por salón")
max_porcentaje = 0
salon_max = ""
#Buscamos el mayor porcentaje en la fila de la matriz resultados_porcentaje_boda_oro
for fila in resultados_porcentaje_boda_oro:
    if fila[1] > max_porcentaje: 
        max_porcentaje = fila[1]
        salon_max = fila[0]

print(f"Salón con mayor porcentaje de bodas de oro: {salon_max} ({max_porcentaje}%)")

#endregion

#region 7. Generar un informe con la recaudación de cada salón, ordenada de
# mayor a menor, mediante una función que utilice ordenamiento por
# burbuja.

#USAMOS LA MATRIZ resultados_recaudacion_salon DEL EJERCICIO 4 
# [[salon, total_recaudacion_salon]]

matriz_recaudacion_salon_ordenada = ordenar_burbujeo(resultados_recaudacion_salon)
print("\nMatriz recaudacion por salon ordenada")
mostrar_matriz(matriz_recaudacion_salon_ordenada)

#endregion