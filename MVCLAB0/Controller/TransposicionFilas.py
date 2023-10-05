class TransposicionFilas:

    def cifrar_transposicion_columnas(self, texto_plano, key):
        # Obtener la longitud de la clave
        clave = len(key)

        # Crear una lista de longitud igual a la clave, para almacenar las columnas cifradas
        texto_cifrado = [''] * clave

        # Iterar a través de las columnas de la matriz de transposición
        for col in range(clave):
            pointer = col  # Inicializar un puntero en la posición de la columna actual

            # Mientras el puntero esté dentro del texto plano
            while pointer < len(texto_plano):
                # Agregar el carácter en la posición del puntero a la columna actual
                texto_cifrado[col] += texto_plano[pointer]

                # Mover el puntero hacia abajo en la misma columna
                pointer += clave

        # Unir las columnas cifradas para obtener el texto cifrado completo
        return ''.join(texto_cifrado)




