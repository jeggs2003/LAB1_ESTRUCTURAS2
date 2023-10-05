import math

class DescifrarTrans:

    def descifrar_transposicion_columnas(self, texto_cifrado, key):
        # Obtener la longitud de la clave
        clave = len(key)

        # Calcular el número de columnas necesario para la matriz de transposición
        numCol = math.ceil(len(texto_cifrado) / clave)

        # Definir el número de filas en la matriz
        numFil = clave

        # Calcular el número de espacios necesarios en la matriz
        numSbox = (numCol * numFil) - len(texto_cifrado)

        # Inicializar una lista para almacenar el texto descifrado por columnas
        texto_des = [""] * numCol

        # Inicializar variables para seguir el recorrido de las columnas y filas
        col = 0
        fil = 0

        # Recorrer cada símbolo en el texto cifrado
        for simbolo in texto_cifrado:
            # Agregar el símbolo actual a la columna correspondiente
            texto_des[col] += simbolo
            col += 1

            # Verificar si hemos llenado la columna actual o si estamos en la última columna
            # y hemos llenado todas las filas necesarias (teniendo en cuenta los huecos)
            if (col == numCol) or (col == numCol - 1) and (fil >= numFil - numSbox):
                col = 0
                fil += 1

        # Unir las columnas para obtener el texto descifrado completo
        return "".join(texto_des)
