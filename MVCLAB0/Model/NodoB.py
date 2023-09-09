from Model import Persona

class NodoB:
    def __init__(self, t):
        self.n = 0  # número de claves almacenadas en el nodo
        self.leaf = True  # Si el nodo es hoja (nodo hoja=True; nodo interno=False)
        self.key = [None] * ((2 * t) - 1)  # almacena las claves en el nodo
        self.child = [None] * (2 * t)  # arreglo con referencias a los hijos

    def imprimir(self):
        print("", end="")
        for i in range(self.n):
            if i < self.n - 1:
                print('{"name":','"', self.key[i].get_nombre(),'",','"','dpi":', '"',self.key[i].get_dpi(),'",','"','dateBirth":', '"',self.key[i].get_fecha(),'",','"','address":', '"',self.key[i].get_direccion(),'"}')
            else:
                print('{"name":', '"', self.key[i].get_nombre(), '",', '"', 'dpi":', '"', self.key[i].get_dpi(), '",','"', 'dateBirth":', '"', self.key[i].get_fecha(), '",', '"', 'address":', '"',self.key[i].get_direccion(), '"}')
        print("")

