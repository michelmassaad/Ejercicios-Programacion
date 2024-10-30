# 4- Herencia de clases
# Crear una clase Animal que tenga la característica nombre. 
# La clase Perro que herede de  Animal las características y 
# realice el sonido “guau guau”. 
# La clase Gato que herede de Animal las características y realice el sonido “Miau”.
# Del gato y el perro se debe poder mostrar el sonido que realizan. 
# Se debe crear la clase e implementarla.

class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.sonido = "guau guau"
    
    def mostrar_sonido(self) -> str:
        return f"El sonido que hace el Perro {self.nombre} es: {self.sonido}"
        
class Gato(Animal):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.sonido = "Miau"
    
    def mostrar_sonido(self) -> str:
        return f"El sonido que hace el Gato {self.nombre} es: {self.sonido}"

# Instanciar
perro = Perro("Rex")
gato = Gato("Frida")

#Llamada
print(perro.mostrar_sonido())  
print(gato.mostrar_sonido())  
