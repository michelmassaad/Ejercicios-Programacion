# 4- Obtener promedio de edad de un determinado curso.

def obtener_promedio_edad(lista_alumnos, curso_buscado):
    total_edad = 0
    contador = 0
    for alumno in lista_alumnos:
        if alumno["curso"] == curso_buscado:
            total_edad += alumno["edad"]
            contador += 1
    
    if contador > 0:
        return total_edad / contador
    else:
        return None  # Retornamos None si no se encuentran alumnos en el curso   