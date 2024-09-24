# 11- Programar el algoritmo de búsqueda binaria de forma recursiva

def buscar_binario_recursivo(lista: list, buscado: any, inicio: int, final: int):    
    if inicio > final: #Si esta ordenada la lista significa que se revisaron todos
        return None
    medio = (inicio + final) // 2
    
    if lista[medio] == buscado:
        return medio
    elif lista[medio] < buscado:
        return buscar_binario_recursivo(lista, buscado, medio + 1, final) #coloco donde inicia
    else:
        return buscar_binario_recursivo(lista, buscado, inicio, medio - 1) #coloco donde termina

lista_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_buscado = 5
inicio = 0
final = len(lista_ejemplo) - 1
resultado = buscar_binario_recursivo(lista_ejemplo, valor_buscado, inicio, final)

if resultado == None:
    print(f"Valor {valor_buscado} no encontrado")
else:
    print(f"Valor {valor_buscado} encontrado en el índice: {resultado}")