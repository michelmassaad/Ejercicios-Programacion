# 9- Desarrollar una función que permita cargar nuevos valores a una lista cualquiera. Se
# debe poder validar el tipo de datos que contiene la lista.

######
# Tengo un Problema con este: Siempre que pido el dato por input me lo regresa como cadena
# por lo tanto no puedo comprobar el tipo de dato 
# #########

def solicitarValor():
    """
    Solicita un valor al usuario y lo retorna.
    """
    return input("Ingrese un nuevo valor: ")

def validarDato(lista: list, nuevo_valor):
    """
    Valida si el nuevo valor tiene el mismo tipo que los elementos de la lista.
    Retorna bool 
    """
    if len(lista) > 0 and type(nuevo_valor) != type(lista[0]):
        return False
    return True

#llamadas de funciones
cantidad_valores_agregados = int(input("Ingrese cuantos valores va a agregar: "))

#Crear lista con nuevos valores
nuevos_valores = [0] * cantidad_valores_agregados
for i in range(cantidad_valores_agregados):
    nuevos_valores[i] = solicitarValor() 
print(nuevos_valores)

#lista ejemplo
lista_ejemplo = [1, 2, 3] 
validar = validarDato(lista_ejemplo, nuevos_valores)

#Resultado de Comprobar tipo de datos
if validar == True:
    lista_ejemplo += nuevos_valores  # Crear nueva lista con los nuevos valores
    print(f"Lista final: {lista_ejemplo}")
else:
    print("El tipo de dato no coincide con la lista original.")