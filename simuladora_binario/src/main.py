# from logica import sumador_completo # importar función de sumador completo
from binario import decimal_a_binario, binario_a_decimal # importar funciones de conversión entre decimal y binario
from logica import sumador_completo # importar función de sumador completocomo

def sumar_n_bits(a_dec, b_dec, bits=4): # función para sumar dos números decimales
    a_bits = decimal_a_binario(a_dec, bits) 
    b_bits = decimal_a_binario(b_dec, bits)
    resultado = [] # lista para almacenar el resultado
    c_in = 0 # acarreo inicial
    # iterar cada posición de los bits de a y b 

    for i in range(bits):                                              # desde el bit menos significativo (LSB) al más significativo (MSB) 
        suma_bit, c_in = sumador_completo(a_bits[i], b_bits[i], c_in)  # llamar a la función de sumador completo para cada bit 
        resultado.append(suma_bit)                                     # almacenar el resultado de la suma en la lista resultado 
    # añadir acarreo final a la lista resultado 
    resultado.append(c_in)                                             # el acarreo final se añade al final de la lista resultado
    # convertir a decimal para mostrar
    return binario_a_decimal(resultado), resultado                     # devolver el resultado en decimal y en binario 

def generar_tabla_verdad(funcion, n_entradas):  # función para generar la tabla de verdad de una función lógica
    tabla = {}                                  # diccionario para almacenar la tabla de verdad
    for i in range(2 ** n_entradas):            # iterar sobre todas las combinaciones posibles de entradas 
        bits = decimal_a_binario(i, n_entradas) # convertir el número decimal a binario
        tabla[tuple(bits)] = funcion(*bits)     # llamar a la función con los bits como argumentos 
    return tabla                                # devolver la tabla de verdad como un diccionario

def generar_tabla_verdad_operaciones(): # función para generar la tabla de verdad de operaciones lógicas
    print("Seleccione una operación lógica:") 
    print("1. AND")
    print("2. OR")
    print("3. XOR")
    print("4. NOT (solo para una entrada)")
    
    opcion = int(input("Ingrese el número de la operación: ")) 
    
    if opcion == 1:
        operacion = lambda A, B: A and B # función lambda para la operación AND
        # la función lambda toma dos argumentos A y B y devuelve el resultado de la operación AND entre ellos
        # la función lambda se utiliza para definir funciones de una sola línea sin necesidad de definir una función completa
        n_entradas = 2  # número de entradas para la operación AND
                        # la variable n_entradas se utiliza para indicar cuántas entradas tiene la operación lógica
    
    elif opcion == 2:
        operacion = lambda A, B: A or B # función lambda para la operación OR
        n_entradas = 2          # número de entradas para la operación OR 

    elif opcion == 3:           # función lambda para la operación XOR
                                # la operación XOR devuelve True si exactamente uno de los operandos es True
        operacion = lambda A, B: A ^ B  # función lambda para la operación XOR
        n_entradas = 2                  # número de entradas para la operación XOR

    elif opcion == 4:       # función lambda para la operación NOT
        operacion = lambda A: not A     # función lambda para la operación NOT
        n_entradas = 1            # número de entradas para la operación NOT

    else:
        print("Opción no válida.")  # mensaje de error si la opción no es válida 
        return # salir de la función si la opción no es válida

    # Generar tabla de verdad
    tabla = generar_tabla_verdad(operacion, n_entradas)
    
    # Mostrar tabla de verdad
    print("\nTabla de Verdad:")  
    for entradas, salida in tabla.items():  # iterar sobre los elementos de la tabla de verdad
        # entradas es una tupla que contiene los valores de las entradas y salida es el resultado de la operación lógica
        # la función items() devuelve una vista de los elementos del diccionario como pares clave-valor
        print(f"{entradas} -> {salida}") # imprimir las entradas y la salida de la operación lógica

if __name__ == "__main__":  # bloque principal del programa
    print("Bienvenido al generador de tablas de verdad.") 
    generar_tabla_verdad_operaciones() # llamar a la función para generar la tabla de verdad de operaciones lógicas

    x = int(input("Ingrese primer número: "))
    y = int(input("Ingrese segundo número: "))
    suma_dec, suma_bits = sumar_n_bits(x, y, bits=4) # llamar a la función para sumar dos números decimales 
    
    print(f"Suma en decimal: {suma_dec}")
    # Indica que la representación binaria del resultado se muestra desde el bit menos significativo (LSB) al más significativo (MSB).
    print(f"Suma en binario (LSB→MSB): {suma_bits}")