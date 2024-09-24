# 1 - Dada la siguiente lista de ingresos horarios:
# [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
# 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

# a) Calcular el promedio de ingresos/hora del 20% que más gana. No es necesario
# ordenar, se puede usar continue y resolver mediante programación estructurada
# usando listas.

lista_horario = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
                  9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

#Calculo del 20% del total de elementos de la lista
porcentaje_pedido = 20
cantidad_elementos = len(lista_horario)
calculo_20p = (porcentaje_pedido * cantidad_elementos)/100
cantidad_20p = int(calculo_20p)

#Busqueda de los Mayores Valores 
c = 0
lista_mayores = [0] * cantidad_20p #Lista con el 20% de los elementos con los mayores valores 

while c != cantidad_20p: 
    max_horario = lista_horario[0] # inicializa el maximo
    for i in range(len(lista_horario)):
        if lista_horario[i] > max_horario and lista_horario[i] not in lista_mayores:
            max_horario = lista_horario[i]
    
    lista_mayores[c] = max_horario #Añade los valores a lista con mayores valores
    c += 1

# Funcion sumar lista
def suma_lista(lista:int) -> int:
    '''
    Suma los elementos de la lista
    Recibe: Lista
    Devuelve: int
    '''
    suma_total = 0
    for numero in lista:
        suma_total += numero
    return suma_total

def calculo_promedio(total_suma:float, total_elementos: int) -> float:
    '''
    Calcula promedios de una la lista
    Recibe: float, int
    Devuelve: float
    '''
    promedio = total_suma / total_elementos
    return promedio

#Calculo de Promedio 

suma_total_20p = suma_lista(lista_mayores)
promedio_20p = calculo_promedio(suma_total_20p, cantidad_20p)
print(f"Promedio 20% que mas gana: {promedio_20p}")


# b) Calcular el promedio de ingresos/hora de todos los respondentes.
suma_total = suma_lista(lista_horario)
promedio = calculo_promedio(suma_total, cantidad_elementos)
print(f"Promedio total ingresos/hora: {promedio}")


# c) Buscar cuál es el valor que más se repite. En caso de ser varios, devolverlos todos.
lista_valores_repetidos = [0] * cantidad_elementos
repetido_max = 0
indice = 0
for numero in lista_horario:
    repetido = 0

    for valor in lista_horario:
        if numero == valor:
            repetido += 1 
    
    if repetido > repetido_max:
        repetido_max = repetido
        lista_valores_repetidos[indice] = numero
        indice = 1
        
    elif repetido == repetido_max and numero not in lista_valores_repetidos:
        lista_valores_repetidos[indice] = numero
        indice += 1

# Crear una nueva lista con solo los elementos válidos
valores_finales = [0] * indice  # Inicializa una lista del tamaño correcto
for i in range(indice):
    valores_finales[i] = lista_valores_repetidos[i]

if valores_finales:
    print("Valores mas repetidos:", valores_finales)
else:
    print("No hay valores repetidos.")
        
# d) Calcular la media geométrica. La media geométrica es la raíz de los productos.
producto = 1
for n in lista_horario:
    producto *= n
    media_geometrica = producto **(1/len(lista_horario))
    
print(f"La media geometrica es : {media_geometrica}")

# e) Crear una función que permita recorrer las listas en ambos sentidos.

def recorrer_lista(lista, direccion= "derecha"):
    '''
    Recorre listas en dos direcciones
    
    Recibe: lista, str
    
    Devuelve: NONE
    '''
    if direccion == "derecha":
        for i in range(len(lista)):
            print(lista[i])  # Recorrer hacia la derecha
    elif direccion == "izquierda":
        for i in range(len(lista)-1 , -1 , -1):
            print(lista[i])  # Recorrer hacia la izquierda
    else:
        print("Error, usa derecha o izquierda")
        
# Recorrer hacia la derecha        
print("Recorrer hacia la derecha:")
recorrer_lista(lista_horario, "derecha")

# Recorrer hacia la izquierda
print("\nRecorrer hacia la izquierda:")
recorrer_lista(lista_horario, "izquierda")