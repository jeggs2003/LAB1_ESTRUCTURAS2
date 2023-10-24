import os
from Controller.GeneratorKey import GeneratorKey
from Controller.FirmadorRSA import FirmadorRSA


class Service:
    def __init__(self):
        self.firmador = FirmadorRSA()

    def generar_firmas(self):
        carpeta_origen_conv = r"C:\Users\javie\PycharmProjects\MVCLAB0\venv\View\Conversaciones"
        archivos = os.listdir(carpeta_origen_conv)
        FirmasCarpeta = "carpeta_destino_Firmas"

        if not os.path.exists(FirmasCarpeta):
            os.makedirs(FirmasCarpeta)

        firmas_lista = []  # Lista para almacenar los nombres de archivo y las firmas

        for archivo in archivos:
            try:
                conca = carpeta_origen_conv + "\\" + archivo
                with open(conca, "r") as arch:
                    contenido = arch.read()
                    message_signed = self.firmador.firmar(contenido)
                    firmas_lista.append((archivo, message_signed))  # Agregar a la lista

            except Exception as e:
                print(e)

        return firmas_lista  # Devolver la lista de nombres de archivo y firmas
