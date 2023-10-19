class Coleccion:
    def __init__(self):
        self.data = []

    # Método para verificar si la colección está vacía
    def esta_vacia(self):
        return len(self.data) == 0

    # Método para limpiar la colección
    def limpiar(self):
        self.data = []

    # Método para obtener el tamaño de la colección
    def tamanio(self):
        return len(self.data)

    # Método para eliminar el elemento mínimo
    def eliminar_min(self):
        if self.esta_vacia():
            return
        min_val = min(self.data)
        self.data = [x for x in self.data if x != min_val]

    # Método para eliminar el elemento máximo
    def eliminar_max(self):
        if self.esta_vacia():
            return
        max_val = max(self.data)
        self.data = [x for x in self.data if x != max_val]

    # Método para agregar un elemento manteniendo el orden
    def agregar(self, elemento):
        if self.esta_vacia():
            self.data.append(elemento)
            return
        for i, val in enumerate(self.data):
            if elemento <= val:
                self.data.insert(i, elemento)
                return
        self.data.append(elemento)

    # Método de búsqueda binaria
    def _busqueda_binaria(self, elemento):
        inicio, fin = 0, len(self.data) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.data[medio] == elemento:
                return medio
            elif self.data[medio] < elemento:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1

    # Método para buscar un elemento
    def buscar_elemento(self, elemento):
        return self._busqueda_binaria(elemento)

    # Método para contar cuántas veces aparece un elemento
    def cuantos(self, elemento):
        return self.data.count(elemento)

    # Método para obtener subcolección
    def obtener_subcoleccion(self, elemento):
        index = self.buscar_elemento(elemento)
        if index == -1:
            raise Exception("No existe dicha subcolección.")
        return self.data[index:]

    # Método para obtener subcolección por rango
    def obtener_subcoleccion_rango(self, primer_elemento, segundo_elemento):
        inicio = self.buscar_elemento(primer_elemento)
        final = self.buscar_elemento(segundo_elemento)
        if inicio == -1 or final == -1:
            raise Exception(f"No se puede obtener la subcolección porque no se encuentra el {primer_elemento} y/o {segundo_elemento}.")
        while final + 1 < len(self.data) and self.data[final + 1] == segundo_elemento:
            final += 1
        return self.data[inicio:final+1]

    # Método para obtener subcolección sin repetición
    def subcoleccion_sin_repeticion(self):
        subcoleccion = []
        for val in self.data:
            if val not in subcoleccion:
                subcoleccion.append(val)
        return subcoleccion

    # Método para remplazar elementos
    def remplazar(self, elemento, nuevo):
        self.data = [nuevo if x == elemento else x for x in self.data]
        self.data.sort()

    # Método para verificar igualdad entre colecciones
    def eq(self, otra):
        if not isinstance(otra, Coleccion):
            return False
        return self.data == otra.data

    # Método para imprimir de forma ascendente
    def imprimir_ascendente(self):
        print([x for x in self.data if x is not None])

    # Método para imprimir de forma descendente
    def imprimir_descendente(self):
        print([x for x in reversed(self.data) if x is not None])