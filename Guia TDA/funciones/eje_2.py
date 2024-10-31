# 2- Cargar secuencialmente una lista de cursos, cada curso debe
# ser un diccionario con dos claves: una tupla que contenga año y
# división, debe tener cargada como valor la cantidad de alumnos y
# el preceptor a cargo.

def cargar_secuencialmente_cursos(lista_cursos:list) -> list:
    año = int(input("Ingrese el año del curso: "))
    division = int(input("Ingrese la división del curso: "))
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    preceptor = input("Ingrese el nombre del preceptor a cargo: ")
    
    # Creación de la tupla curso y del diccionario para el curso
    curso = (año, division)
    datos_curso = {
        "curso": curso,
        "cantidad_alumnos": cantidad_alumnos,
        "preceptor": preceptor
    }
    
    lista_cursos.append(datos_curso)
    
    return lista_cursos