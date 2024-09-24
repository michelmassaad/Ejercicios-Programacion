# 7- Dadas las siguientes listas:
lista_nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro",
         "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
lista_edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las personas
# de menor edad (puede ser más de una) y las retorne. El programa principal deberá mostrar
# nombre y edad de los menores.

def buscar_menores(lista:list) -> list:
    '''
    Buscar personas con menor edad en la lista 
    Recibe: list
    Retorna: list(con posiciones)
    '''
    lista_posicion = [0] * len(lista)
    edad_min = lista[0]
    indice = 0
    # Buscar la edad mínima
    for i in range(len(lista)):
        if lista[i] < edad_min:
            edad_min = lista[i]
            lista_posicion[indice] = i
            indice = 1
        elif lista[i] == edad_min:
            lista_posicion[indice] = i
            indice += 1
            
    # Crear una nueva lista con solo los elementos válidos
    lista_posicion_finales = [0] * indice  # Inicializa una lista del tamaño correcto
    for i in range(indice):
        lista_posicion_finales[i] = lista_posicion[i]
    return lista_posicion_finales

lista_posicion_menor = buscar_menores(lista_edades)


#IMPRIMIR DATOS EN PANTALLA
for i in lista_posicion_menor:
    print(f"Nombre: {lista_nombres[i]}")
    print(f"Edad: {lista_edades[i]}\n")
