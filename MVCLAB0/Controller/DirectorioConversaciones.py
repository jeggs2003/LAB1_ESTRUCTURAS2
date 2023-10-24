import os
import re

class DirectorioConversaciones:
    def DirArc(self, dpi):

        directorio = "Conversaciones"
        archivos_coincidentes = []

        # Recorre todos los archivos en el directorio
        for nombre_archivo in os.listdir(directorio):
            # Verificar si el nombre del archivo coincide con el patrón REC-DPI-NUMCARTA.txt
            if re.match(r"CONV-(\d+)-\d+\.txt", nombre_archivo):
                # Obtener el DPI del nombre del archivo
                dpi_archivo = re.search(r"CONV-(\d+)-\d+\.txt", nombre_archivo).group(1)

                # Verificar si el DPI coincide con el DPI a buscar
                if dpi_archivo == dpi:
                    archivos_coincidentes.append(nombre_archivo)
        return archivos_coincidentes

