# 1 - Calcular mediante recursividad la potencia de un número, mediante una función que
# recibe un número base de tipo entero y un exponente de tipo entero. Utilizar parámetros
# opcionales para definir que si la función no recibe ningún parámetro devolverá 2 al
# cuadrado.

def calcular_potencia(base:int = 2, exponente:int = 2) -> int:
    
    if exponente == 0:
        return 1
    else:
        resultado = base * calcular_potencia(base,exponente-1)
        return resultado

print(calcular_potencia(3,3))
    
    
# 2 - Resolver mediante recursividad el problema de las torres de Hanoi
# https://www.youtube.com/watch?v=vrXue8Lq1Ow
# No utilizar listas, la función solo debe devolver un print con los movimientos.

def demostrar_torres_hanoi(discos:int = 3, A="A", B="B", C="C"):
    if discos == 1:
        print(f"Mover disco {discos} desde poste {A} hasta poste {C}")
        return
    else:
        # Mover los discos menos uno de A a B usando C como auxiliar
        demostrar_torres_hanoi(discos - 1, A, C, B)
        
        # Mover el disco más grande de A a C
        print(f"Mover disco {discos} desde poste {A} hasta poste {C}")
        
        # Mover los discos de B a C usando A como auxiliar
        demostrar_torres_hanoi(discos - 1, B, A, C)

# Llamar a la función para 2 discos
demostrar_torres_hanoi(9)

