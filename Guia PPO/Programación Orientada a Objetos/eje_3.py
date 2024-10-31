# 3- Clase para representar una Calculadora Crear una clase Calculadora que pueda 
# calcular suma, resta, multiplicación y división. 
# Se debe crear la clase e implementarla.


#### PREGUNTAR COMO PASAR MAS NUMEROS
class Calculadora:
    def __init__(self, numero_1:float, numero_2:float) -> None:
        self.numero_1 = numero_1
        self.numero_2 = numero_2
    
    def calcular_suma(self) -> float:
        return self.numero_1 + self.numero_2 
    
    def calcular_resta(self) -> float:
        return self.numero_1 - self.numero_2 
    
    def calcular_multiplicacion(self) -> float:
        return self.numero_1 * self.numero_2 
    
    def calcular_division(self) -> float:
        if self.numero_2 != 0:
            return self.numero_1 / self.numero_2
        else:
            return "Error: División por cero no permitida"


calculadora = Calculadora(10, 5)

print("Suma:", calculadora.calcular_suma())           
print("Resta:", calculadora.calcular_resta())         
print("Multiplicación:", calculadora.calcular_multiplicacion()) 
print("División:", calculadora.calcular_division())   