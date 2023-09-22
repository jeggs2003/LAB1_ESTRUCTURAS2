
from Model.ArbolB import ArbolB
from Model.Persona import Persona
from Model.NodoB import NodoB
from Controller.concatenacion import concatenacion
from Controller.HuffmanTree import HuffmanTree

import json
print("---------------------------------------------------------")
print("---- Bienvenido al Sistema de Busqueda de Candidatos ----")

salir = False

arbolB = ArbolB(500)  # Por ejemplo, t=3/

while not salir:
    print("---------------------------------------------------------")
    print("1. Insertar Archivo JSON")
    print("2. Busqueda de Candidatos por Nombre")
    print("3. Busqueda de Candidatos por DPI")
    print("4. Salir")
    print("---------------------------------------------------------")
    opc = input("Seleccione una opción: ")

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

                                    companies = []

                                    conc = concatenacion();
                                    companies = conc.process_companies(data["dpi"],data["companies"])
                                    persona.set_compa(companies)
                                    # Crear una instancia de HuffmanTree para cada cadena de texto
                                    huf_trees = [HuffmanTree(companies[i]) for i in range(len(companies))]

                                    # Codificar y decodificar cada cadena usando las instancias correspondientes
                                    encriptados = []
                                    desencriptados = []
                                    persona.set_des(desencriptados)

                                    for i in range(len(companies)):
                                        binary_output = huf_trees[i].text_to_binary_huffman(companies[i])
                                        encriptados.append(binary_output)

                                    # Insertar la persona en el árbol B
                                    persona.set_enc(encriptados)
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
                                    if address is None or address == "":
                                        arbolB.actualizarDate(name,dpi,fecha)
                                        pass
                                    else:
                                        arbolB.actualizarAdress(name, dpi, address)
                                        pass
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
    elif opc == "2":
        # Llamar al código para buscar candidatos en el árbol B
        if arbolB is not None:

            nombre = input("Ingrese el Nombre de la Persona: ")
            nodo_encontrado = arbolB.find(nombre)

        else:
            print("Debe crear un objeto ArbolB primero.")

    elif opc == "3":
        # Llamar al código para buscar candidatos en el árbol B
        if arbolB is not None:

            dpi = input("Ingrese el DPI de la Persona: ")
            nodo_encontrado = arbolB.finddpi(dpi)

        else:
            print("Debe crear un objeto ArbolB primero.")


    elif opc == "4":


        print("Saliendo del programa.")

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

