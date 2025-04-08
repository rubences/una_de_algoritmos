from caballo.caballos import Caballos

class Lanzador:
    """Clase que representa el lanzador del caballo."""
    def __init__(self):
        # Movimientos posibles del caballo
        self.movimientos = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

    def contar_movimientos(self, pos, movimientos_restantes):
        """Cuenta los movimientos válidos desde una posición inicial."""
        if movimientos_restantes == 0:
            return 1
        total_movimientos = 0
        for siguiente_pos in self.movimientos[pos]:
            total_movimientos += self.contar_movimientos(siguiente_pos, movimientos_restantes - 1)
        return total_movimientos

    def calcular_movimientos_iniciales(self, num_movimientos):
        """Calcula los movimientos válidos desde todas las posiciones iniciales."""
        total_movimientos = 0
        for inicio in range(10):
            total_movimientos += self.contar_movimientos(inicio, num_movimientos - 1)
        return total_movimientos

    def main():
        """Función principal para ejecutar el lanzador del caballo."""
        lanzador = Lanzador()
        num_movimientos = int(input("Introduce el número de movimientos: "))
        total_movimientos = lanzador.calcular_movimientos_iniciales(num_movimientos)
        print(f"Total de movimientos válidos: {total_movimientos}")

    

