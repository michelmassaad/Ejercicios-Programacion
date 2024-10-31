from funciones import *

seguir = "si"
caso_1_ocurrido = True
continuar = "si"

while seguir == "si":
    opcion = int(input("Marque la opcion del menu (1-7):"))

    match opcion:
        case 1:
            # 1- Cargar secuencialmente una lista de alumnos, cada alumno
            # debe ser un diccionario con cuatro claves: nombre, apellido, edad y
            # la clave curso que posea de valor una tupla con el curso.
            lista_alumnos = []
            lista_alumnos = cargar_alumnos(lista_alumnos,continuar)
            #Mostrar lista
            for alumno in lista_alumnos:
                print(alumno)
            # Marcamos el caso 1 como ejecutado
            caso_1_ocurrido = True

        case 2:
            lista_curso = []
            continuar = "si"
            while continuar == "si":
                lista_curso = cargar_secuencialmente_cursos(lista_curso)
                continuar = input("\nDesea cargar otro curso (si/no): ")
            #Mostrar lista
            for curso in lista_curso:
                print(curso)

        case 3:
            pass
                
        case 4:
            if caso_1_ocurrido == True:
                #Calculo porque se cargo la lista 
                año = int(input("Ingrese el año del curso: "))
                division = int(input("Ingrese la division del curso: "))                
                curso_buscado = (año, division)
                promedio = obtener_promedio_edad(lista_alumnos, curso_buscado)
            else:
                print("\nCargo la lista ya que no se ha cargado la lista")
                lista_alumnos = []
                lista_alumnos = cargar_alumnos(lista_alumnos,continuar)
                #repito el calculo porque se cargo la lista 
                año = int(input("Ingrese el año del curso: "))
                division = int(input("Ingrese la division del curso: "))                
                curso_buscado = (año, division)
                promedio = obtener_promedio_edad(lista_alumnos, curso_buscado)
                
            #resultado
            if promedio is not None:
                print(f"Promedio de edad del curso {curso_buscado} es:"
                     +f"{promedio:.2f} años")
            else:
                print(f"No hay alumnos en el curso {curso_buscado}.")
        case 5:
            pass

        case 6:
            pass

        case 7:
            pass

        case _:
            opcion = int(input("Error.Marque la opcion del menu (1-7):"))
            
        
    #para salir del bucle
    seguir = input("\nDesea marcar otra opcion (si/no): ")
        
            