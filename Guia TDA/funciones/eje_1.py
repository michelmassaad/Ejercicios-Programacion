# 1- Cargar secuencialmente una lista de alumnos, cada alumno
# debe ser un diccionario con cuatro claves: nombre, apellido, edad y
# la clave curso que posea de valor una tupla con el curso.

def cargar_alumnos(lista_alumnos, continuar:str) -> list:
    continuar = "si"
    while continuar == "si":
        lista_alumnos = cargar_secuencialmente_alumnos(lista_alumnos)
        continuar = input("\nDesea cargar otro alumno (si/no): ")
    return lista_alumnos

def cargar_secuencialmente_alumnos(lista_alumnos:list) -> list:
    # Recolección de datos del alumno
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    # Para curso, podemos pedir diferentes valores y almacenarlos en una tupla
    año = int(input("Ingrese el año del curso: "))
    division = int(input("Ingrese la division del curso: "))
    
    # Creación del diccionario para el alumno
    Alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "curso": (año, division)
    }
    
    lista_alumnos.append(Alumno)
    
    return lista_alumnos
    
