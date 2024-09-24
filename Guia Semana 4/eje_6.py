# 6 - Desarrollar una función que pida 10 números dentro de un rango especificado, validar
# los números solicitados dentro de ese rango, guardar en una lista y retornarla. El programa
# principal debe invocar a la función y mostrar por pantalla el retorno.

def solicitarNumero():
    '''
    Solicita un numero al usuario
    Retorna = int
    '''
    num = input("Ingrese un numero del 10-100: ")
    num = int(num)
    return num

def validarNumero(num):
    '''
    Valida un numero dentro de un rango
    Retorna = int
    '''
    while num < 10 or num > 100:
        num = input("Error.Ingrese un numero entre (10-100): ")
        num = int(num)
    return num


lista_numero = [0]* 5
for i in range(len(lista_numero)):
    lista_numero[i] = solicitarNumero()
    lista_numero[i] = validarNumero(lista_numero[i])
    
print(lista_numero)