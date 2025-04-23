def decimal_a_binario(n, bits):
                                        # devuelve lista de bits de longitud 'bits'
    resultado = []                      # crea una lista vacía que almacenara los bits
    for i in range(bits):               # se itera 'bits' veces
                                        # se agrega el bit menos significativo (LSB) a la lista resultado
        resultado.append(n % 2)
        n = n // 2
                                        # la lista está al revés (LSB primero)
    return resultado                    # ej. [1,0,1] para 5 en 3 bits


def binario_a_decimal(bits_list):           # convierte una lista de bits a decimal
    total = 0                               # inicializa el total en 0 que almacenara el resultante
    for i in range(len(bits_list)):         # itera sobre la lista de bits
        total += bits_list[i] * (2 ** i)    # en cada interación se suma el valor del bit multiplicado por 2 elevado a la posición del bit 
                                            # el resultado se suma a total
    return total                            # devuleve el numero decimal calculado


