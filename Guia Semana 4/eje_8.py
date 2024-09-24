# 8- Desarrollar una función que verifique si todos los elementos de una lista son del mismo
# tipo. En ese caso que devuelva el tipo que contiene, en caso contrario que informe qué tipos
# de elementos contiene.

#funciones
def crear_lista_tipos(lista: list):
    '''
    Crea una lista del tipo de dato que contiene la lista recibida 
    Recibe: list
    Retorna: list
    '''
    lista_tipos = [0] * len(lista)  
    for i in range(len(lista)):
        lista_tipos[i] = type(lista[i])
    return lista_tipos

def verificar_tipo(lista_tipos: list):
    '''
    verifica si todos los datos de la lista son iguales o no  
    Recibe: list
    Retorna: bool o list
    '''
    for i in range(1,len(lista_tipos)):
        if lista_tipos[i] != lista_tipos[0]:
            return False
    return lista_tipos[0]
        
#Llamado de funciones
lista_ejemplo = [1, 2, 3.0]
lista_tipos = crear_lista_tipos(lista_ejemplo)
resultado = verificar_tipo(lista_tipos) 

#Resultados por pantalla
if resultado == False:
    print("Tipos de datos NO son Iguales\n")
    print(f"Los tipos de datos son {lista_tipos}\n")
else:
    print("Tipos de datos son Iguales")
    print(f"Los tipos de datos son {resultado}\n")
    
