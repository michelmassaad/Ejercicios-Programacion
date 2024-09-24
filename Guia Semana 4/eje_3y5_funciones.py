# 5- Realizar una función que permita corregir las listas del ejercicio 3 en caso de ser
# necesario. Para ello se debe poder acceder a una posición particular y cargar nuevos
# valores para el listado con valor incorrecto en dicha posición.

def corregir_datos(posicion, cantidad, nombres, sexos, horas_trabajadas, ingresos_semanales):
    '''
    Corrige un valor especifico dada una posicion
    Recibe = int, int, list,list....
    '''
    if 0 <= posicion < cantidad:
        print(f"\nRespondente {posicion + 1}:")
        nombres[posicion - 1] = input("Ingrese su nombre: ")
        sexos[posicion - 1] = input("Ingrese su sexo (M/F): ")
        horas_trabajadas[posicion - 1] = float(input("Ingrese la cantidad de horas trabajadas: "))
        ingresos_semanales[posicion - 1] = float(input("Ingrese el ingreso semanal: "))
    else:
        print("Posicion invalida")

def recolectar_datos(cantidad, nombres, sexos, horas_trabajadas, ingresos_semanales):
    '''
    Recolecta datos secuencialmente hasta una cantidad pedida
    Recibe = int, list,list....
    '''
    for i in range(cantidad):
        print(f"\nRespondente {i + 1}:")
        nombres[i] = input("Ingrese su nombre: ")
        sexos[i] = input("Ingrese su sexo (M/F): ")
        horas_trabajadas[i] = float(input("Ingrese la cantidad de horas trabajadas: "))
        ingresos_semanales[i] = float(input("Ingrese el ingreso semanal: "))

def mostrar_datos(cantidad, nombres, sexos, horas_trabajadas, ingresos_semanales):
    '''
    Muestras los datos por pantalla
    Recibe = int, list,list....
    '''
    print("\nDatos ingresados:")
    for i in range(cantidad):
        print(f"Respondente {i + 1}: "
            f"\nNombre: {nombres[i]} "
            f"\nSexo: {sexos[i]} "
            f"\nHoras Trabajadas: {horas_trabajadas[i]} "
            f"\nIngreso Semanal: {ingresos_semanales[i]}")