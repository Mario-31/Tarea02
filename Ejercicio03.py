from abc import ABC, abstractmethod
# Falta salto de lineas suficiente para clases
class DatosAbstractos(ABC):
    @abstractmethod
    def leer_datos(self):
        pass

    @abstractmethod
    def ordenar_datos(self, datos):
        pass

    @abstractmethod
    def buscar(self, consulta):
        pass

class ConsultaTelefonos(DatosAbstractos):
    def __init__(self, archivo):
        self.datos = self.leer_datos(archivo)
        """
        Su atributo de datos es una lista de listas, está bien
        pero lo ideal era tener un objeto que tuviera esos dos atributos.
        """
        self.datos_ordenados = self.ordenar_datos(self.datos)

    """
    Realmente esta parte sería ya del script prueba.
    """
    def leer_datos(self, archivo):
        try:
            with open(archivo, "r") as file:
                # Leer los datos del archivo y devolver una lista de nombres y números de teléfono.
                # Cada entrada podría ser una tupla (nombre, numero).
                return [line.strip().split(",") for line in file.readlines()]
        except FileNotFoundError:
            print("El archivo no se ha encontrado.")
            return []

    """
    Dos problemas aquí, aunque el segundo conlleva al primero.
    Al hacerse búsqueda por nombre o por número, se tiene que tener ordenada
    la lista, por nombre o por número, lo que nos lleva a tener un ordenamiento
    para nombre y uno para número. Eso nos lleva al segundo problema, se tenía
    que usar y modificar algún algortimo de los que vimos para ordenar, no usar
    sorted.
    """
    def ordenar_datos(self, datos):
        # Implementar un algoritmo de ordenamiento recursivo, como Mergesort o Quicksort, para ordenar los datos.
        # Devolver la lista ordenada.
        return sorted(datos, key=lambda x: x[0])  # Ordenar por nombres

    """
    Como se menciona arriba era buscar por número y buscar por nombre, por lo
    que tendría que haber dos algoritmos para buscar o tener alguna
    modificación que aceptara ambas formas.
    """
    def buscar(self, consulta):
        # Implementar la búsqueda binaria para buscar un nombre o número de teléfono en los datos ordenados.
        # Devolver el resultado de la búsqueda.
        lo = 0
        hi = len(self.datos_ordenados) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if consulta == self.datos_ordenados[mid][0]:
                return self.datos_ordenados[mid][1]
            elif consulta < self.datos_ordenados[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1
        return None

def main():
    # No sabemos cual es el archivo de los números de teléfono asi que solo e reemplaza "datos_telefono.txt" por el archivo de datos
    archivo = "datos_telefonos.txt"
    consulta = ConsultaTelefonos(archivo)
    
    while True:
        print("1. Consultar por nombre")
        print("2. Consultar por número de teléfono")
        print("3. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            nombre = input("Ingrese el nombre a buscar: ")
            resultado = consulta.buscar(nombre)
            if resultado:
                print(f"Número de teléfono de {nombre}: {resultado}")
            else:
                print(f"{nombre} no encontrado.")
        elif opcion == 2:
            numero = input("Ingrese el número de teléfono a buscar: ")
            resultado = consulta.buscar(numero)
            if resultado:
                print(f"Nombre correspondiente al número {numero}: {resultado}")
            else:
                print(f"Número {numero} no encontrado.")
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
