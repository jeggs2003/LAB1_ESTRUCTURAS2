import json
from Controller.concatenacion import concatenacion
from Controller.HuffmanTree import HuffmanTree
from Model.NodoB import NodoB
import os
from Controller.DescifrarTrans import DescifrarTrans
from Model.Persona import Persona

class ArbolB:
    def __init__(self, t):
        self.root = NodoB(t)
        self.t = t

    def buscar_clave_mayor(self):
        clave_maxima = self.get_clave_mayor(self.root)
        return clave_maxima

    def get_clave_mayor(self, current):
        if current is None:
            return 0  # Si es cero no existe

        # Mientras no sea una hoja
        while not current.leaf:
            # Se accede al hijo mas a la derecha
            current = current.child[current.n]

        return self.clave_mayor_por_nodo(current)

    def clave_mayor_por_nodo(self, current):
        # Devuelve el valor mayor, el que esta mas a la derecha
        return current.key[current.n - 1].get_dpi()

    def mostrar_claves_nodo_minimo(self):
        temp = self.buscar_nodo_minimo(self.root)

        if temp is None:
            print("Sin mínimo")
        else:
            temp.imprimir()

    def buscar_nodo_minimo(self, nodo_actual):
        if self.root is None:
            return None

        aux = self.root

        # Mientras no sea una hoja
        while not aux.leaf:
            # Se accede al primer hijo
            aux = aux.child[0]

        # Devuelve el nodo menor, el que esta mas a la izquierda
        return aux

    # Busca el valor ingresado y muestra el contenido del nodo que contiene el valor
    def buscar_nodo_por_clave(self, num):
        temp = self.search(self.root, num)

        if temp is None:
            print("No se ha encontrado un nodo con el valor ingresado")
        else:
            self.print(temp)

    # Search
    def search(self, actual, key):
        i = 0  # se empieza a buscar siempre en la primera posición

        # Incrementa el índice mientras el valor de la clave del nodo sea menor
        while i < actual.n and key != actual.key[i].get_nombre():
            i += 1

        # Si la clave es igual, entonces retornamos el nodo
        if i < actual.n and key == actual.key[i].get_nombre():
            return actual

        # Si llegamos hasta aquí, entonces hay que buscar los hijos
        # Se revisa primero si tiene hijos
        if actual.leaf:
            return None
        else:
            # Si tiene hijos, hace una llamada recursiva
            return self.search(actual.child[i], key)




    def insertar(self, persona):
        r = self.root

        # Si el nodo esta lleno lo debe separar antes de insertar
        if r.n == (2 * self.t - 1):
            s = NodoB(self.t)
            self.root = s
            s.leaf = False
            s.n = 0
            s.child[0] = r
            self.split(s, 0, r)
            self.non_full_insert(s, persona)
        else:
            self.non_full_insert(r, persona)


    def split(self, x, i, y):
        # Nodo temporal que sera el hijo i + 1 de x
        z = NodoB(self.t)
        z.leaf = y.leaf
        z.n = self.t - 1

        # Copia las ultimas (t - 1) claves del nodo y al inicio del nodo z
        for j in range(self.t - 1):
            z.key[j] = y.key[j + self.t]

        # Si no es hoja hay que reasignar los nodos hijos
        if not y.leaf:
            for k in range(self.t):
                z.child[k] = y.child[k + self.t]

        # nuevo tamanio de y
        y.n = self.t - 1

        # Mueve los hijos de x para darle espacio a z
        for j in range(x.n, i, -1):
            x.child[j + 1] = x.child[j]

        # Reasigna el hijo (i+1) de x
        x.child[i + 1] = z

        # Mueve las claves de x
        for j in range(x.n, i, -1):
            x.key[j + 1] = x.key[j]

        # Agrega la clave situada en la mediana
        x.key[i] = y.key[self.t - 1]
        x.n += 1

    def non_full_insert(self, x, persona):
        key = persona.get_dpi()

        # Si es una hoja
        if x.leaf:
            i = x.n  # cantidad de valores del nodo
            # busca la posición i donde asignar el valor
            while i >= 1 and key < x.key[i - 1].get_dpi():
                x.key[i] = x.key[i - 1]  # Desplaza los valores mayores a key
                i -= 1

            x.key[i] = persona  # asigna la persona al nodo
            x.n += 1  # aumenta la cantidad de elementos del nodo
        else:
            j = 0
            # Busca la posición del hijo
            while j < x.n and key > x.key[j].get_dpi():
                j += 1

            # Si el nodo hijo esta lleno lo separa
            if x.child[j].n == (2 * self.t - 1):
                self.split(x, j, x.child[j])

                if key > x.key[j].get_dpi():
                    j += 1

            self.non_full_insert(x.child[j], persona)

    def mostrar_arbol_b(self):
        self.print(self.root)

    # Print en preorder
    def print(self, n):
        n.imprimir()

        # Si no es hoja
        if not n.leaf:
            # recorre los nodos para saber si tiene hijos
            for j in range(n.n + 1):
                if n.child[j] is not None:
                    print()
                    self.print(n.child[j])

    def find(self, nombre):
        return self._buscar_en_nodo(self.root, nombre)

    def _buscar_en_nodo(self, nodo, nombre):
        if nodo is None:
            return -1  # Si el nodo es None, el valor no se encontró

        for i in range(nodo.n):
            if nodo.key[i].get_nombre() == nombre:
                compa = nodo.key[i].get_compa()
                encrip = nodo.key[i].get_enc()
                desencriptados =[]
                huf_trees = [HuffmanTree(compa[i]) for i in range(len(compa))]
                for j in range(len(compa)):
                    decoded_text = huf_trees[j].Binario_Texto(encrip[j])
                    desencriptados.append(decoded_text)

                print("---------------------------------------------------------")
                nodo.key[i].set_des(desencriptados)
                data = []

                item = {
                    "name": nodo.key[i].get_nombre(),
                    "dpi": nodo.key[i].get_dpi(),
                    "dateBirth": nodo.key[i].get_fecha(),
                    "address": nodo.key[i].get_direccion(),
                    "Desencriptados": nodo.key[i].get_des(),
                    "Directorios Cartas" : nodo.key[i].get_cartas()
                }
                data.append(item)

                json_data = json.dumps(data, indent=5)
                print(json_data)
                print("---------------------------------------------------------")
        if not nodo.leaf:
            # Si no es una hoja, busca en los hijos recursivamente
            for i in range(nodo.n + 1):
                resultado = self._buscar_en_nodo(nodo.child[i], nombre)
                if resultado != -1:
                    return resultado

        return -1

#Find para DPI
    def finddpi(self, dpi):
        return self._buscar_en_nododpi(self.root, dpi)

    def _buscar_en_nododpi(self, nodo, dpi):
        if nodo is None:
            return -1  # Si el nodo es None, el valor no se encontró

        for i in range(nodo.n):
            if nodo.key[i].get_dpi() == dpi:
                compa = nodo.key[i].get_compa()
                encrip = nodo.key[i].get_enc()
                desencriptados = []
                huf_trees = [HuffmanTree(compa[i]) for i in range(len(compa))]
                Desenc = DescifrarTrans();
                Desifrados = [];


                for j in range(len(compa)):
                    decoded_text = huf_trees[j].Binario_Texto(encrip[j])
                    desencriptados.append(decoded_text)

                carpeta_origen = r"C:\Users\javie\PycharmProjects\MVCLAB0\venv\View\carpeta_destino"  # Ruta completa de la carpeta de origen
                for nombre_archivo in nodo.key[i].get_cartas():
                    # Construir la ruta completa al archivo de origen
                    ruta_origen = os.path.join(carpeta_origen, nombre_archivo)

                    # Leer el contenido del archivo de origen
                    with open(ruta_origen, "r") as archivo_origen:
                        contenido = archivo_origen.read()
                        descifrado = ""
                        descifrado = Desenc.descifrar_transposicion_columnas(contenido, "JAVIERGODINEZKEY")
                        Desifrados.append(nombre_archivo+": "+descifrado)


                print("---------------------------------------------------------")
                nodo.key[i].set_des(desencriptados)
                data = []

                item = {
                    "name": nodo.key[i].get_nombre(),
                    "dpi": nodo.key[i].get_dpi(),
                    "dateBirth": nodo.key[i].get_fecha(),
                    "address": nodo.key[i].get_direccion(),
                    "Desencriptados": nodo.key[i].get_des(),
                    "Directorios Cartas": nodo.key[i].get_cartas(),
                    "Cartas Decifradas": Desifrados
                }
                data.append(item)

                json_data = json.dumps(data, indent=5)
                print(json_data)
                print("---------------------------------------------------------")

        if not nodo.leaf:
            # Si no es una hoja, busca en los hijos recursivamente
            for i in range(nodo.n + 1):
                resultado = self._buscar_en_nododpi(nodo.child[i], dpi)
                if resultado != -1:
                    return resultado

        return -1




    def actualizarData(self, nombre, dpi, adress ,fecha, Companies, enc, des):

        return self._actualizar_en_nodo_data(self.root, nombre, dpi, fecha, adress,Companies,enc,des)

    def _actualizar_en_nodo_data(self, nodo, nombre, dpi, fecha, adress, compa, enc, des):
        if nodo is None:
            return -1  # Si el nodo es None, el valor no se encontró

        for i in range(nodo.n):
            if nodo.key[i].get_nombre() == nombre:
                if nodo.key[i].get_dpi() == dpi:
                    nodo.key[i].set_fecha(fecha)
                    nodo.key[i].set_direccion(adress)
                    nodo.key[i].set_enc(enc)
                    nodo.key[i].set_des(des)
                    nodo.key[i].set_compa(compa)
                    print(" REGISTRO CON NOMBRE: ", nombre, " // DPI: ", dpi, " ACTUALIZADO CORRECTAMENTE")

        if not nodo.leaf:
            # Si no es una hoja, busca en los hijos recursivamente
            for i in range(nodo.n + 1):
                resultado = self._actualizar_en_nodo_data(nodo.child[i], nombre, dpi, fecha,adress, compa, enc, des)
                if resultado != -1:
                    return resultado

        return -1









    def actualizarDate(self, nombre, dpi, fecha):

        return self._actualizar_en_nodo(self.root, nombre, dpi, fecha)

    def _actualizar_en_nodo(self, nodo, nombre, dpi, fecha):
        if nodo is None:
            return -1  # Si el nodo es None, el valor no se encontró

        for i in range(nodo.n):
            if nodo.key[i].get_nombre() == nombre:
                if nodo.key[i].get_dpi() == dpi:
                    nodo.key[i].set_fecha(fecha)
                    print(" REGISTRO CON NOMBRE: ", nombre, " // DPI: ", dpi, " ACTUALIZADO CORRECTAMENTE")

        if not nodo.leaf:
            # Si no es una hoja, busca en los hijos recursivamente
            for i in range(nodo.n + 1):
                resultado = self._actualizar_en_nodo(nodo.child[i], nombre, dpi, fecha)
                if resultado != -1:
                    return resultado

        return -1

    def actualizarAdress(self, nombre, dpi, adress):

        return self._actualizar_en_nodoA(self.root, nombre, dpi, adress)

    def _actualizar_en_nodoA(self, nodo, nombre, dpi, adress):
        if nodo is None:
            return -1  # Si el nodo es None, el valor no se encontró

        for i in range(nodo.n):
            if nodo.key[i].get_nombre() == nombre:
                if nodo.key[i].get_dpi() == dpi:
                    nodo.key[i].set_direccion(adress)
                    print(" REGISTRO CON NOMBRE: ", nombre, " // DPI: ", dpi, " ACTUALIZADO CORRECTAMENTE")
        if not nodo.leaf:
            # Si no es una hoja, busca en los hijos recursivamente
            for i in range(nodo.n + 1):
                resultado = self._actualizar_en_nodoA(nodo.child[i], nombre, dpi, adress)
                if resultado != -1:
                    return resultado

        return -1


    def eliminar(self, nombre, dpi):
        # Comienza la eliminación en la raíz
        resultado, nueva_raiz = self._eliminar_en_nodo(self.root, nombre, dpi)

        if resultado:
            # Si la eliminación tuvo éxito, actualiza la raíz si es necesario
            if nueva_raiz is not None:
                self.root = nueva_raiz
            print(" REGISTRO CON NOMBRE: ", nombre, " // DPI: ", dpi, " ELIMINADO CORRECTAMENTE")
        else:
            print("No se encontró la persona con el nombre y DPI especificados.")

    def _eliminar_en_nodo(self, nodo, nombre, dpi):
        if nodo is None:
            return False, None  # No se encontró la persona

        for i in range(nodo.n):
            if nodo.key[i].get_nombre() == nombre and nodo.key[i].get_dpi() == dpi:
                # Encontró la persona, elimínala
                for j in range(i, nodo.n - 1):
                    nodo.key[j] = nodo.key[j + 1]
                nodo.key[nodo.n - 1] = None  # Marca la última posición como None
                nodo.n -= 1

                # Si el nodo está en el nivel mínimo y está vacío, necesita ser fusionado o redistribuido
                if nodo == self.root and nodo.n == 0:
                    if nodo.leaf:
                        # Si el nodo es la raíz y es una hoja vacía, simplemente ábrelo
                        self.root = None
                    else:
                        # Si el nodo es la raíz y es un nodo interno vacío, haz que su único hijo sea la nueva raíz
                        self.root = nodo.child[0]
                elif nodo.n < self.t - 1:
                    # Si el nodo tiene menos claves de las requeridas, necesitamos redistribuir o fusionar
                    hermano = None
                    indice_hermano = None

                    # Busca un hermano con al menos t claves
                    for j in range(nodo.n + 1):
                        if (j < nodo.n and nodo.key[j] is not None) or (j == nodo.n and nodo.child[j].n >= self.t):
                            hermano = nodo.child[j]
                            indice_hermano = j
                            break

                    if hermano is not None:
                        # Si encontramos un hermano con al menos t claves, redistribuye
                        if indice_hermano < nodo.n and nodo.key[indice_hermano] is not None:
                            # Hermano es el hermano derecho, toma una clave del hermano
                            hermano.key[hermano.n] = nodo.key[indice_hermano]
                            nodo.key[indice_hermano] = None
                            nodo.n -= 1

                            # Mueve la clave más a la izquierda del hermano al nodo actual
                            nodo.key[nodo.n] = hermano.key[0]
                            hermano.key[0] = None

                            # Mueve el hijo más a la izquierda del hermano al nodo actual si no es una hoja
                            if not hermano.leaf:
                                nodo.child[nodo.n + 1] = hermano.child[0]

                            # Ajusta los punteros de los hermanos
                            for k in range(hermano.n):
                                hermano.key[k] = hermano.key[k + 1]
                                hermano.child[k] = hermano.child[k + 1]
                            hermano.child[hermano.n] = None
                            hermano.key[hermano.n - 1] = None
                            hermano.n -= 1
                        else:
                            # Hermano es el hermano izquierdo, toma una clave del nodo actual
                            hermano.key[hermano.n] = nodo.key[0]
                            nodo.key[0] = None
                            nodo.n -= 1

                            # Mueve la clave más a la izquierda del nodo actual al hermano
                            nodo.key[0] = nodo.child[1].key[0]

                            # Mueve el hijo más a la izquierda del nodo actual al hermano si no es una hoja
                            if not nodo.child[1].leaf:
                                hermano.child[hermano.n + 1] = nodo.child[1].child[0]

                            # Ajusta los punteros de los hermanos
                            for k in range(nodo.child[1].n):
                                nodo.child[1].key[k] = nodo.child[1].key[k + 1]
                                nodo.child[1].child[k] = nodo.child[1].child[k + 1]
                            nodo.child[1].child[nodo.child[1].n] = None
                            nodo.child[1].key[nodo.child[1].n - 1] = None
                            nodo.child[1].n -= 1
                    else:
                        # No se encontró un hermano con al menos t claves, fusiona con un hermano
                        if indice_hermano < nodo.n:
                            # Fusionar con el hermano derecho
                            hermano = nodo.child[indice_hermano + 1]
                            hermano.key[nodo.n - 1] = nodo.key[indice_hermano]
                            hermano.n += 1
                            nodo.key[indice_hermano] = None
                            nodo.n -= 1

                            # Mueve todas las claves y punteros del nodo al hermano derecho
                            for k in range(nodo.n):
                                hermano.key[k + self.t] = nodo.key[k]
                                hermano.child[k + self.t] = nodo.child[k]
                            hermano.child[2 * self.t - 1] = nodo.child[self.t - 1]

                            # Ajusta los punteros de los hermanos
                            for k in range(indice_hermano, nodo.n):
                                nodo.key[k] = nodo.key[k + 1]
                                nodo.child[k + 1] = nodo.child[k + 2]
                            nodo.key[nodo.n] = None
                            nodo.child[nodo.n + 1] = None
                        else:
                            # Fusionar con el hermano izquierdo
                            hermano = nodo.child[indice_hermano - 1]
                            hermano.key[hermano.n - 1] = nodo.key[indice_hermano - 1]
                            hermano.n += 1
                            nodo.key[indice_hermano - 1] = None
                            nodo.n -= 1

                            # Mueve todas las claves y punteros del nodo al hermano izquierdo
                            for k in range(nodo.n):
                                hermano.key[k + self.t] = nodo.key[k]
                                hermano.child[k + self.t] = nodo.child[k]
                            hermano.child[2 * self.t - 1] = nodo.child[self.t - 1]

                            # Ajusta los punteros de los hermanos
                            for k in range(indice_hermano - 1, nodo.n):
                                nodo.key[k] = nodo.key[k + 1]
                                nodo.child[k + 1] = nodo.child[k + 2]
                            nodo.key[nodo.n] = None
                            nodo.child[nodo.n + 1] = None

                return True, None

        if not nodo.leaf:
            # Si no es una hoja, busca en los hijos recursivamente
            for i in range(nodo.n + 1):

                resultado, nueva_raiz = self._eliminar_en_nodo(nodo.child[i], nombre, dpi)
                if resultado:
                    return True, nueva_raiz

        return False, None