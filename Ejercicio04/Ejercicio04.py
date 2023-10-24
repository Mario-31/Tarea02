from abc import ABC
from abc import abstractmethod
# Faltan saltos de línea sufientes para clases y para métodos
class Coleccionx(ABC):
    """
    No se implementa nada en una interfaz (clase abtracta del tad), y menos
    usando un método que hasta el momento es abstracto.
    
    Por otro lado, no se pasa una lista. Simplemente se inicializa una vacía
    para la colección.
    """
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
    """
    Este método no es parte del tad
    """
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
    """
    __eq__
    """
    def eq(self, otra):
        pass
    @abstractmethod
    def imprimir_ascendente(self):
        pass
    @abstractmethod
    def imprimir_descendente(self):
        pass

class Coleccion(Coleccionx):

    """
    No se podía usar len()
    """
    # Método para verificar si la colección está vacía
    def esta_vacia(self):
        return len(self.data) == 0

    # Método para limpiar la colección
    """
    Bien
    """
    def limpiar(self):
        self.data = []

    # Método para obtener el tamaño de la colección
    """
    No se podía usar len()
    """
    def tamanio(self):
        return len(self.data)

    # Método para eliminar el elemento mínimo
    """
    return?
    
    No hace falta buscar el mínimo, porque es una colección ordenada, por lo
    que siempre es el primer valor.
    """
    def eliminar_min(self):
        if self.esta_vacia():
            return
        min_val = min(self.data)
        self.data = [x for x in self.data if x != min_val]

    """
    Mismo comentario que arriba
    """
    # Método para eliminar el elemento máximo
    def eliminar_max(self):
        if self.esta_vacia():
            return
        max_val = max(self.data)
        self.data = [x for x in self.data if x != max_val]
    
    """
    existe el break, por qué usan return como break?
    
    Por otro lado, no se cumple con el single responsability,
    es decir, no sólo se encarga de ingresarlo, el método tiene que
    ser el encargado de buscar la posición que le corresponde al nuevo
    elemento, es complejidad O(n), recorre hasta encontar la posición. En clase
    se vió cómo modificar la búsqueda binaria para poder encontra la posición
    de un nuevo número en la colección
    """
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

    """
    No se pidió un método que se llamara busqueda_binara.
    Para usarlo hay que dejarlo como una clase o función aparte.
    
    Cómo aseguran que el la posición que encuentra sea la primer posición de
    un elemento repetido?
    """
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

    """
    bien
    """
    # Método para buscar un elemento
    def buscar_elemento(self, elemento):
        return self._busqueda_binaria(elemento)

    """
    No podían usar métodos de las listas más que append e insert
    """
    # Método para contar cuántas veces aparece un elemento
    def cuantos(self, elemento):
        return self.data.count(elemento)

    """
    Bien, el detalle realmente viene de buscar_elemento
    Si el de buscar no elige siempre la primer aparición de un elemento
    que se repite entonces esta subcolección es incorrecta.
    """
    # Método para obtener subcolección
    def obtener_subcoleccion(self, elemento):
        index = self.buscar_elemento(elemento)
        if index == -1:
            raise Exception("No existe dicha subcolección.")
        return self.data[index:]

    # Método para obtener subcolección por rango
    """
    Bueno aquí no hay single responsability, primero si ya validan que el
    segundo elemento si sea el último de los repetidos, ese calculo, no debería
    hacerse aquí, el punto es modificar los algortimos de búqueda binaria para
    poder obtener tanto el primero como el último.
    """
    def obtener_subcoleccion_rango(self, primer_elemento, segundo_elemento):
        inicio = self.buscar_elemento(primer_elemento)
        final = self.buscar_elemento(segundo_elemento)
        if inicio == -1 or final == -1:
            raise Exception(f"No se puede obtener la subcolección porque no se encuentra el {primer_elemento} y/o {segundo_elemento}.")
        while final + 1 < len(self.data) and self.data[final + 1] == segundo_elemento:
            final += 1
        return self.data[inicio:final+1]

    # Método para obtener subcolección sin repetición
    """
    bien
    """
    def subcoleccion_sin_repeticion(self):
        subcoleccion = []
        for val in self.data:
            if val not in subcoleccion:
                subcoleccion.append(val)
        return subcoleccion

    # Método para remplazar elementos
    """
    Bueno aquí, si se cambian los elementos evidentemente, pero recordemos
    que la colección siempre es una estructura ordenada. No se vale
    cambiarla así y luego sólo ordenarla con sort
    (que tampoco estaba permitido), porque aunque sea un pequeño momento,
    la colección estuvo desordenada.
    """
    def remplazar(self, elemento, nuevo):
        self.data = [nuevo if x == elemento else x for x in self.data]
        self.data.sort()

    # Método para verificar igualdad entre colecciones
    """
    Aquí aunque no parece están usando otro método que tampoco se podía
    que es justo __eq__ de las listas
    """
    def eq(self, otra):
        if not isinstance(otra, Coleccion):
            return False
        return self.data == otra.data

    """
    No queremos imprimir una lista (crear una lista por medio de la colección),
    queremos imprimir la colección sin None
    """
    # Método para imprimir de forma ascendente
    def imprimir_ascendente(self):
        print([x for x in self.data if x is not None])

    # Método para imprimir de forma descendente
    """
    No se podía usar reversed
    """
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