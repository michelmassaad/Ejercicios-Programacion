# 2 - Clase para representar un Rectángulo Crear una clase rectángulo que tenga las
# características base y altura. Del rectángulo se debe poder calcular el área y 
# el perímetro. Se debe crear la clase e implementarla.


class Rectangulo:
    # Constructor que define los atributos de la clase
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    # Método para calcular el área del rectángulo
    def calcular_area(self) -> float:
        return self.base * self.altura

    # Método para mostrar la información del área
    def mostrar_area(self) -> None:
        print(f"El área del rectángulo es: {self.calcular_area()}\n")

# Instanciar objeto
rectangulo_1 = Rectangulo(4, 8)
rectangulo_2 = Rectangulo(5, 5)
rectangulo_3 = Rectangulo(4, 4)
rectangulo_4 = Rectangulo(2, 7)

# Llamar al método para mostrar el área
rectangulo_1.mostrar_area()
rectangulo_2.mostrar_area()
rectangulo_3.mostrar_area()
rectangulo_4.mostrar_area()

