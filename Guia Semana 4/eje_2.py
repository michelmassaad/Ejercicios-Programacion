# 2- Suponiendo que tenemos dos listas en las cuales la posición es la misma en ambas para
# cada respondente:
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", 
                 "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]

# a) Devolver el nombre del respondiente más jóven y del más grande.
bandera = True
for posicion in range(len(lista_nombres)):
    if bandera == True:
        posicion_min_edad = posicion
        min_edad = lista_edad[posicion]
        max_edad = lista_edad[posicion]
        posicion_max_edad = posicion
        bandera = False
    else:
        if lista_edad[posicion] < min_edad:# Verifica el min
            posicion_min_edad = posicion
            min_edad = lista_edad[posicion]
            
        if lista_edad[posicion] > max_edad: # Verifica el max
            max_edad = lista_edad[posicion]
            posicion_max_edad = posicion


print(f"El nombre del Menor es {lista_nombres[posicion_min_edad]} y la edad es {lista_edad[posicion_min_edad]}")
print(f"El nombre del Mayor es {lista_nombres[posicion_max_edad]} y la edad es {lista_edad[posicion_max_edad]}")


# b) Usando break, busque en la lista si hay mayores de 65. En ese caso cortar la
# iteración y mostrar mensaje por pantalla.
# Inicializa una variable para verificar si se encontró un mayor de 65

encontrado = False
for i in range(len(lista_edad)):
    if lista_edad[i] > 65:
        encontrado = True  # Marca que se encontró un mayor de 65
        break  # Cortar la iteración
if encontrado:
    print("Hay mayores de 65 años.")
else:
    print("No hay mayores de 65 años.")

# c) Utilizando continue, calcule la media etaria para mayores de 40 años
suma_edades_mayor_40 = 0
cont = 0
for edad in lista_edad:
    if edad < 40:
        continue
    else:
        suma_edades_mayor_40 += edad
        cont += 1
        
media_etaria = suma_edades_mayor_40 / cont
media_etaria = int(media_etaria)

print(media_etaria)