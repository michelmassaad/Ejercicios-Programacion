# 1 -Clase para representar un Libro
# Crear una clase Libro que tenga las características título, autor y año de publicación. 
# Del libro se debe poder obtener información, mostrando por mensaje todos sus datos. 
# Se debe crear la clase e implementarla.

class Libro:
    # Constructor que define los atributos de la clase
    def __init__(self, titulo: str, autor: str, año_publicacion: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    # Método para mostrar la información de la clase
    def retornar_descripcion(self) -> str:
        return (f"El nombre del libro es: {self.titulo}\n"
                f"El autor del libro es: {self.autor}\n"
                f"El año de publicación es: {self.año_publicacion}\n")

# Instanciar Objetos
libro_1 = Libro("Harry Potter", "J.K Rowling", 2000)
libro_2 = Libro("Futbol", "Juan Perez", 2012)
libro_3 = Libro("El señor de los anillos", "J. R. R. Tolkien", 1956)

# Llamar a los métodos del objeto
print(libro_1.retornar_descripcion())
print(libro_2.retornar_descripcion())
print(libro_3.retornar_descripcion())
