# 5- Encapsulamiento Crear una clase Cuenta Bancaria que tenga las características 
# titular y saldo encapsulado. De la cuenta bancaria se puede obtener el saldo, 
# depositar o retirar (en cada caso imprimir que fue exitoso). 
# Se debe crear la clase e implementarla.

class CuentaBancaria:
    def __init__(self, titular:str, saldo: float) -> None:
        self.titular = titular
        self.__saldo = saldo
    
    def mostrar_saldo(self) -> str:
        return f"El saldo de la Cuenta es {self.__saldo}"
    
# Instancio Objetos
cuenta_1 = CuentaBancaria("Michel", 45756.56)

#Prueba de que es un dato privado y no se puede realizar cambios 
cuenta_1.__saldo = 8794531

print(cuenta_1.mostrar_saldo())