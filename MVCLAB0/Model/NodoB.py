from Model import Persona
import json;
class NodoB:
    def __init__(self, t):
        self.n = 0  # número de claves almacenadas en el nodo
        self.leaf = True  # Si el nodo es hoja (nodo hoja=True; nodo interno=False)
        self.key = [None] * ((2 * t) - 1)  # almacena las claves en el nodo
        self.child = [None] * (2 * t)  # arreglo con referencias a los hijos

    def imprimir(self):
        data = []
        for i in range(self.n):
            item = {
                "name": self.key[i].get_nombre(),
                "dateBirth": self.key[i].get_fecha(),
                "address": self.key[i].get_direccion(),
                "Encriptados": self.key[i].get_enc()
            }
            data.append(item)

        json_data = json.dumps(data, indent=5)
        print(json_data)
