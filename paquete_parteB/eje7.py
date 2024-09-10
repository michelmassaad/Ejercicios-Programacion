# Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
# productos con impuestos para una determinada empresa:
# La respuesta de chatgpt es:
# def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
# = 15):
# resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
# resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
# resultado_final = resultado_nacional + resultado_exportaciones
# return resultado_final
# ¿Considera que cumple con los objetivos de una función?
# Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
# documente y denomine correctamente

def calcular_ventas_exportaciones(valor_exportaciones :float, retenciones :float = 15 ) -> float:
    '''
    Calcula ventas por exportaciones con las retenciones.
    
    Parámetros:
    -----------
        valor_exportaciones: El valor total de las exportaciones.
        retenciones (float): Porcentaje de retención a aplicar.
        
    Retorna:
    ---------
        Valor de exportaciones tras aplicar retenciones.
    '''
    resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
    return resultado_exportaciones

def calcular_ventas_nacionales(valor_ventas_nacionales :float, iva:int = 21) -> float:
    '''
    Calcula ventas nacionales con IVA aplicado.
    
    Parámetros:
    -----------
        valor_ventas_nacionales (float): Valor total de las ventas nacionales.
        iva (int): Porcentaje de iva.
                
    Retorna:
    ---------
        El valor de las ventas nacionales con IVA.
    '''
    resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    return resultado_nacional

def calculo_impuestos(resultado_nacional:float,resultado_exportaciones:float) -> float:
    '''
    Suma los resultados de ventas nacionales y exportaciones.
    
    Parámetros:
    -----------
        resultado_nacional: Ventas nacionales con IVA.
        resultado_exportaciones: Exportaciones con retenciones.
                
    Retorna:
    ---------
        El total de ventas nacionales y exportaciones con sus impuestos.
    '''
    resultado_final = resultado_nacional + resultado_exportaciones
    return resultado_final  
