class Caballos:
    def __init__(self, origen, destino):
        self.origen = origen  # Posición inicial (tupla: fila, columna)
        self.destino = destino  # Posición final (tupla: fila, columna)

    def __repr__(self):
        return f"Caballo(origen={self.origen}, destino={self.destino})"


