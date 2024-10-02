class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, elemento):
        """Agrega un elemento a la pila."""
        self.pila.append(elemento)
        print(f"Apilado: {elemento}")

    def desapilar(self):
        """Elimina y devuelve el último elemento de la pila."""
        if not self.esta_vacia():
            elemento = self.pila.pop()
            print(f"Desapilado: {elemento}")
            return elemento
        else:
            print("La pila está vacía.")
            return None

    def ver_tope(self):
        """Devuelve el último elemento sin eliminarlo."""
        if not self.esta_vacia():
            print(f"Tope de la pila: {self.pila[-1]}")
            return self.pila[-1]
        else:
            print("La pila está vacía.")
            return None

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.pila) == 0

    def tamano(self):
        """Devuelve el tamaño de la pila."""
        print(f"Tamaño de la pila: {len(self.pila)}")
        return len(self.pila)


mi_pila = Pila()

mi_pila.apilar("1")
mi_pila.apilar("2")
mi_pila.apilar("3")

mi_pila.ver_tope()

mi_pila.desapilar()

mi_pila.tamano()

mi_pila.desapilar()
mi_pila.desapilar()

mi_pila.desapilar()

mi_pila.esta_vacia()
