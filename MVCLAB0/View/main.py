
from Model.ArbolB import ArbolB
from Model.Persona import Persona
from Model.NodoB import NodoB
from Controller.concatenacion import concatenacion
from Controller.CreDirArc import CreDirArc
from Controller.HuffmanTree import HuffmanTree
from Controller.TransposicionFilas import TransposicionFilas
from Controller.DirectorioConversaciones import DirectorioConversaciones
from Controller.GeneratorKey import GeneratorKey
from Controller.FirmadorRSA import FirmadorRSA
from Controller.RSA import RSA
import os
from Controller.Service import Service

import json
print("---------------------------------------------------------")
print("---- Bienvenido al Sistema de Busqueda de Candidatos ----")

Resclutadores = []
user = ""

salir = False
arbolB = ArbolB(600)  # Por ejemplo, t=600

transF = TransposicionFilas();
Originales = []
servicio = Service();
Originales = servicio.generar_firmas();
Firmas = []

# Ruta de la carpeta de destino
carpeta_destino_firmas = "carpeta_destino_firmas"
# Verificar si la carpeta de destino existe, si no, crearla
if not os.path.exists(carpeta_destino_firmas):
    os.makedirs(carpeta_destino_firmas)

# Ruta de la carpeta de destino
carpeta_destino_firmas_sinh = "carpeta_destino_firmas_sinhuffman"
# Verificar si la carpeta de destino existe, si no, crearla
if not os.path.exists(carpeta_destino_firmas_sinh):
    os.makedirs(carpeta_destino_firmas_sinh)
# Encriptado y Compresion

for nombre, firma in Originales:

    print("Archivo:", nombre)
    byteArrayAsString = ''.join(format(b, '02x') for b in firma)
    firmaencriptdad = transF.cifrar_transposicion_columnas(byteArrayAsString, "JAVIERGODINEZKEY")
    print("Firma Arreglo:", byteArrayAsString)
    print("Firma Encriptada:", firmaencriptdad)
    huf_tree = HuffmanTree(firmaencriptdad)
    # Codificar el texto usando la instancia del árbol Huffman
    binary_output = huf_tree.Texto_Binario(firmaencriptdad)
    print("Firma Comprimida:", binary_output)
    Firmas.append((nombre, binary_output))
    mensaje = str(binary_output)
    # Convierte la cadena en bytes
    bytes_mensaje = mensaje.encode('utf-8')
    firmasinh = firmaencriptdad.encode('utf-8')

    # Guardar el archivo en la carpeta de destino
    nombre_archivo = os.path.join(carpeta_destino_firmas_sinh, nombre)
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(firmasinh)

    # Guardar el archivo en la carpeta de destino
    nombre_archivo = os.path.join(carpeta_destino_firmas, nombre)
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(bytes_mensaje)

while not salir:
    print("---------------------------------------------------------")
    print("1. Insertar Archivo JSON")
    print("2. Busqueda de Candidatos por Nombre")
    print("3. Busqueda de Candidatos por DPI")
    print("4. Salir")
    print("---------------------------------------------------------")

    opc = input()

    if opc == "1":
        print("-----------------------------------------------------------------------")
        # Llamar al código para insertar el archivo JSON en el árbol B
        if arbolB is not None:
            try:
                # Leer el archivo JSON
                with open("texto.txt", "r") as file:
                    data = file.readlines()

                    for linea in data:
                        # Separar la línea en partes usando el punto y coma como separador
                        partes = linea.strip().split(';')

                        # Verificar que haya al menos dos partes (tipo de operación y datos)
                        if len(partes) >= 2:
                            tipo_operacion = partes[0].strip()
                            datos_str = partes[1].strip()

                            if tipo_operacion == "INSERT":
                                # Analizar los datos JSON
                                try:
                                    # Analizar los datos JSON
                                    data = json.loads(datos_str)

                                    # Crear una persona a partir de los datos del JSON
                                    # Json dumps hacerlo a la inversa, genera un string json
                                    # Mandar la informacion directamente al objeto de la persona

                                    persona = Persona()
                                    persona.set_nombre(data["name"])
                                    persona.set_dpi(data["dpi"])
                                    persona.set_fecha(data["datebirth"])
                                    persona.set_direccion(data["address"])
                                    persona.set_reclutador(data["recluiter"])

                                    Resclutadores.append(data["recluiter"])
                                    dpi = data["dpi"]


                    #COMPANIAS
                                    companies = []

                                    conc = concatenacion();
                                    companies = conc.process_companies(dpi,data["companies"])
                                    persona.set_compa(companies)
                                    # Crear una instancia de HuffmanTree para cada cadena de texto
                                    huf_trees = [HuffmanTree(companies[i]) for i in range(len(companies))]

                                    # Codificar y decodificar cada cadena usando las instancias correspondientes
                                    encriptados = []
                                    desencriptados = []
                                    persona.set_des(desencriptados)

                                    for i in range(len(companies)):
                                        binary_output = huf_trees[i].Texto_Binario(companies[i])
                                        encriptados.append(binary_output)

                                    # Insertar la persona en el árbol B
                                    persona.set_enc(encriptados)


                    #TRANSPOSICION CARTAS
                                    dir = []
                                    dirarc = CreDirArc();
                                    dir = dirarc.DirArc(dpi)
                                    persona.set_cartas(dir)


                                    transF = TransposicionFilas();
                                    # Carpeta de destino

                                    carpeta_origen = r"C:\Users\javie\PycharmProjects\MVCLAB0\venv\View\Inputs"  # Ruta completa de la carpeta de origen

                                    # Carpeta de destino
                                    carpeta_destino = "carpeta_destino"  # Reemplaza con la carpeta de destino deseada

                                    # Verificar si la carpeta de destino existe, si no, crearla
                                    if not os.path.exists(carpeta_destino):
                                        os.makedirs(carpeta_destino)

                                    # Recorrer la lista de archivos
                                    for nombre_archivo in dir:
                                        # Construir la ruta completa al archivo de origen
                                        ruta_origen = os.path.join(carpeta_origen, nombre_archivo)

                                        # Leer el contenido del archivo de origen
                                        with open(ruta_origen, "r") as archivo_origen:
                                            contenido = archivo_origen.read()
                                            cifrado = transF.cifrar_transposicion_columnas(contenido, "JAVIERGODINEZKEY")
                                        # Construir la ruta completa al archivo de destino
                                        ruta_destino = os.path.join(carpeta_destino, nombre_archivo)

                                        # Escribir el contenido en el archivo de destino
                                        with open(ruta_destino, "w") as archivo_destino:
                                            archivo_destino.write(cifrado)


                        #FIRMA DIGITAL CONVERSAIONES

                                    dircon = []
                                    dirarccon = DirectorioConversaciones();
                                    dircon = dirarccon.DirArc(dpi)
                                    persona.set_conv(dircon)

                                    carpeta_origen_conv = r"C:\Users\javie\PycharmProjects\MVCLAB0\venv\View\Conversaciones"  # Ruta completa de la carpeta de origen


                                    arbolB.insertar(persona)

                                except json.JSONDecodeError as json_error:
                                    print(f"Error al decodificar JSON en línea: {linea}")
                                    print(f"Mensaje de error: {json_error}")
                                except Exception as e:
                                    print(f"Error inesperado: {e}")
                            elif tipo_operacion == "PATCH":
                                try:
                                    data = json.loads(datos_str)

                                    name = data.get("name")
                                    dpi = data.get("dpi")
                                    fecha = data.get("datebirth")
                                    address = data.get("address")

                                    companies = []

                                    conc = concatenacion();
                                    companies = conc.process_companies(data["dpi"], data["companies"])

                                    huf_trees = [HuffmanTree(companies[i]) for i in range(len(companies))]

                                    # Codificar y decodificar cada cadena usando las instancias correspondientes
                                    encriptados = []
                                    desencriptados = []

                                    for i in range(len(companies)):
                                        binary_output = huf_trees[i].Texto_Binario(companies[i])
                                        encriptados.append(binary_output)

                                    arbolB.actualizarData(name, dpi, address,fecha, companies, encriptados, desencriptados)

                                except json.JSONDecodeError as json_error:
                                    print(f"Error al decodificar JSON en línea: {linea}")
                                    print(f"Mensaje de error: {json_error}")
                                except Exception as e:
                                    print(f"Error inesperado: {e}")

                                pass
                            elif tipo_operacion == "DELETE":
                                try:
                                    data = json.loads(datos_str)

                                    name = data.get("name")
                                    dpi = data.get("dpi")

                                    arbolB.eliminar(name,dpi)
                                except json.JSONDecodeError as json_error:
                                    print(f"Error al decodificar JSON en línea: {linea}")
                                    print(f"Mensaje de error: {json_error}")
                                except Exception as e:
                                    print(f"Error inesperado: {e}")
                                pass
                # Realizar otras operaciones o mostrar el estado final del árbol B
            except FileNotFoundError as e:
                print("El archivo 'operaciones.json' no se encuentra.")
            except Exception as e:
                print("Error:", e)

        else:
            print("Debe crear un objeto ArbolB primero.")
        print("-----------------------------------------------------------------------")
        arbolB.mostrar_arbol_b();


        result = []
        password = []

        for item in Resclutadores:
            if item not in result:
                result.append(item)

        CIFRSA = RSA()

        for item in result:
            contra = item + "123"
            passwordText = CIFRSA.encrypt(contra)
            password.append(passwordText)


        salida = False
        while salida == False:
            print("-----------------------------------------------------------")
            print("--------------Bienvenido al Inicio de Sesion---------------")
            print("-----------------------------------------------------------")
            user = input("Ingrese el Nombre del Reclutador: ")
            print("-----------------------------------------------------------")
            contrase = input("Ingrese la Contraseña del Reclutador: ")
            print("-----------------------------------------------------------")

            if user in result:
                indice_usuario = result.index(user)
                password_desencriptado = CIFRSA.decrypt(password[indice_usuario])
                if contrase == password_desencriptado:
                    print("Inicio de sesión exitoso. Bienvenido, " + user)
                    salida = True

    elif opc == "2":
        # Llamar al código para buscar candidatos en el árbol B
        if arbolB is not None:

            nombre = input("Ingrese el Nombre de la Persona: ")
            nodo_encontrado = arbolB.find(nombre,user)

        else:
            print("Debe crear un objeto ArbolB primero.")

    elif opc == "3":
        # Llamar al código para buscar candidatos en el árbol B
        if arbolB is not None:

            dpi = input("Ingrese el DPI de la Persona: ")
            nodo_encontrado = arbolB.finddpi(dpi,user)

        else:
            print("Debe crear un objeto ArbolB primero.")


    elif opc == "4":


        print("Saliendo del programa.")

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

