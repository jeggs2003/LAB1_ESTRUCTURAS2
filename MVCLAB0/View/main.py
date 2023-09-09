
from venv.Model.ArbolB import ArbolB

print("---------------------------------------------------------")
print("---- Bienvenido al Sistema de Busqueda de Candidatos ----")

salir = False

arbolB = ArbolB(3)  # Por ejemplo, t=3

while not salir:
    print("---------------------------------------------------------")
    print("1. Insertar Archivo JSON")
    print("2. Busqueda de Candidatos")
    print("3. Salir")
    print("---------------------------------------------------------")
    opc = input("Seleccione una opción: ")

    if opc == "1":
        # Llamar al código para insertar el archivo JSON en el árbol B
        if arbolB is not None:
            try:
                # Leer el archivo JSON
                with open("Users\javie\PycharmProjects\MVCLAB0\venv\View\texto.txt", "r") as file:
                    data = file.readlines()

                    for linea in data:
                        # Analizar el JSON
                        json_data = json.loads(linea)

                        # Realizar operaciones según el tipo (INSERT, PATCH, DELETE)
                        tipo_operacion = json_data["tipo"]
                        data = json_data["data"]

                        if tipo_operacion == "INSERT":
                            # Crear una persona a partir de los datos del JSON
                            persona = Model.Persona()
                            persona.set_nombre(data["name"])
                            persona.set_dpi(data["dpi"])
                            persona.set_fecha(data["dateBirth"])
                            persona.set_direccion(data["address"])

                            # Insertar la persona en el árbol B
                            arbolB.insertar(persona)
                        elif tipo_operacion == "PATCH":
                            # Implementa la lógica para actualizar una persona en el árbol B
                            pass
                        elif tipo_operacion == "DELETE":
                            # Implementa la lógica para eliminar una persona del árbol B
                            pass

                # Realizar otras operaciones o mostrar el estado final del árbol B
            except FileNotFoundError as e:
                print("El archivo 'operaciones.json' no se encuentra.")
            except Exception as e:
                print("Error:", e)

        else:
            print("Debe crear un objeto ArbolB primero.")

    elif opc == "2":
        # Llamar al código para buscar candidatos en el árbol B
        if arbolB is not None:
            # Tu código para buscar candidatos en el árbol B debe ir aquí
            pass
        else:
            print("Debe crear un objeto ArbolB primero.")

    elif opc == "3":
        salir = True
        print("Saliendo del programa.")

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

