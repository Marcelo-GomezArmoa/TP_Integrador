def and_gate(a, b):
    # a y b son 0 o 1
    if a == 1 and b == 1: # evaluar si ambos son 1
        return 1 # devuelve 1 si ambos son 1
    else:
        return 0 # devuelve 0 si alguno es 0

def or_gate(a, b):
    if a == 1 or b == 1: # evaluar si alguno es 1
        return 1 # devuelve 1 si alguno es 1
    else:
        return 0 # devuelve 0 si ambos son 0

def xor_gate(a, b): 
    # true si son distintos
    if a != b: # evaluar si son distintos
        return 1 # devuelve 1 si son distintos
    else:
        return 0 # devuelve 0 si son iguales

def not_gate(a):
    if a == 0: # evaluar si es 0
        return 1 # devuelve 1 si es 0
    else:
        return 0 # devuelve 0 si es 1

def medio_sumador(a, b): 
    suma = xor_gate(a, b) # suma es XOR de a y b
    acarreo = and_gate(a, b) # acarreo es AND de a y b
    return [suma, acarreo]  # devuelve lista con suma y acarreo

def sumador_completo(a, b, c_in):   # esta función suma 3 bits
# a y b son los bits a sumar, c_in es el acarreo de entrada
    s1, c1 = medio_sumador(a, b)        # suma parcial y acarreo parcial
    s2, c2 = medio_sumador(s1, c_in)    # suma parcial y acarreo parcial
    c_out = or_gate(c1, c2)             # acarreo de salida es OR de los dos acarreo parciales
    return [s2, c_out]          # devuelve lista con suma y acarreo de salida




# Resumen:
# Puertas lógicas: Simulan operaciones básicas como AND, OR, XOR y NOT.
# Medio sumador: Suma dos bits y calcula el acarreo.
# Sumador completo: Suma tres bits (dos bits y un acarreo de entrada) y calcula el acarreo de salida.
