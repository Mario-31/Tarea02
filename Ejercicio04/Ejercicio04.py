from abc import ABC
from abc import abstractmethod
class Coleccionx(ABC):
    def _init_(self, elementos=[]):
        self.data = []
        for elemento in elementos:
            self.agregar(elemento)
    @abstractmethod
    def esta_vacia(self):
        pass
    @abstractmethod
    def limpiar(self):
        pass
    @abstractmethod
    def tamanio(self):
        pass
    @abstractmethod
    def eliminar_min(self):
        pass
    @abstractmethod
    def eliminar_max(self):
        pass
    @abstractmethod
    def agregar(self, elemento):
        pass
    @abstractmethod
    def _busqueda_binaria(self, elemento):
        pass
    @abstractmethod
    def buscar_elemento(self, elemento):
        pass
    @abstractmethod
    def cuantos(self, elemento):
        pass
    @abstractmethod
    def obtener_subcoleccion(self, elemento):
        pass
    @abstractmethod
    def obtener_subcoleccion_rango(self, primer_elemento, segundo_elemento):
        pass
    @abstractmethod
    def subcoleccion_sin_repeticion(self):
        pass
    @abstractmethod
    def remplazar(self, elemento, nuevo):
        pass
    @abstractmethod
    def eq(self, otra):
        pass
    @abstractmethod
    def imprimir_ascendente(self):
        pass
    @abstractmethod
    def imprimir_descendente(self):
        pass

class Coleccion(Coleccionx):

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



# Crear un objeto de la clase Coleccion
mi_coleccion = Coleccion()

# Agregar elementos a la colección
mi_coleccion.agregar(5)
mi_coleccion.agregar(2)
mi_coleccion.agregar(8)
mi_coleccion.agregar(1)

# Imprimir la colección en orden ascendente
print("Colección en orden ascendente:")
mi_coleccion.imprimir_ascendente()

# Imprimir la colección en orden descendente
print("Colección en orden descendente:")
mi_coleccion.imprimir_descendente()

# Verificar si la colección está vacía
print("¿La colección está vacía?", mi_coleccion.esta_vacia())

# Obtener el tamaño de la colección
print("Tamaño de la colección:", mi_coleccion.tamanio())

# Buscar un elemento en la colección
elemento_a_buscar = 2
posicion = mi_coleccion.buscar_elemento(elemento_a_buscar)
if posicion != -1:
    print(f"El elemento {elemento_a_buscar} se encuentra en la posición {posicion}.")
else:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la colección.")

# Eliminar el elemento mínimo
mi_coleccion.eliminar_min()
print("Colección después de eliminar el elemento mínimo:")
mi_coleccion.imprimir_ascendente()

# Eliminar el elemento máximo
mi_coleccion.eliminar_max()
print("Colección después de eliminar el elemento máximo:")
mi_coleccion.imprimir_ascendente()

coleccion2= Coleccion([1,2,3,4])
coleccion2.imprimir_ascendente()