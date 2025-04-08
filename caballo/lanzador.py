from caballo.caballos import Caballos
import random
import time
import sys
import pygame

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




    # Inicializamos Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimientos del Caballo en el Teclado")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Teclas y sus posiciones en el teclado
TECLAS_POSICIONES = {
    1: (200, 100), 2: (300, 100), 3: (400, 100),
    4: (200, 200), 5: (300, 200), 6: (400, 200),
    7: (200, 300), 8: (300, 300), 9: (400, 300),
    0: (300, 400)
}

# Movimientos posibles del caballo
MOVIMIENTOS = {
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

# Tamaño de los nodos (teclas)
RADIUS = 30

# Función para dibujar los nodos (teclas) y sus conexiones
def dibujar_teclas():
    for tecla, (x, y) in TECLAS_POSICIONES.items():
        pygame.draw.circle(screen, BLUE, (x, y), RADIUS)
        font = pygame.font.SysFont(None, 24)
        texto = font.render(str(tecla), True, WHITE)
        screen.blit(texto, (x - 10, y - 10))  # Dibujar el número en el centro de la tecla

# Función para dibujar las conexiones de los movimientos del caballo
def dibujar_conexiones():
    for tecla, movimientos in MOVIMIENTOS.items():
        x1, y1 = TECLAS_POSICIONES[tecla]
        for destino in movimientos:
            x2, y2 = TECLAS_POSICIONES[destino]
            pygame.draw.line(screen, GREEN, (x1, y1), (x2, y2), 2)

# Función para mostrar los movimientos posibles con un número dado de pasos
def calcular_movimientos_iniciales(num_movimientos):
    # Simular el movimiento del caballo desde todas las teclas
    total_movimientos = 0
    for inicio in range(10):
        total_movimientos += contar_movimientos(inicio, num_movimientos - 1)
    return total_movimientos

# Función recursiva para contar los movimientos válidos desde una tecla
def contar_movimientos(pos, movimientos_restantes):
    if movimientos_restantes == 0:
        return 1
    total_movimientos = 0
    for siguiente_pos in MOVIMIENTOS[pos]:
        total_movimientos += contar_movimientos(siguiente_pos, movimientos_restantes - 1)
    return total_movimientos

# Función para mostrar los resultados en pantalla
def mostrar_resultados(num_movimientos, total):
    font = pygame.font.SysFont(None, 36)
    texto = font.render(f"Movimientos válidos con {num_movimientos} movimiento(s): {total}", True, BLACK)
    screen.blit(texto, (50, 500))

# Bucle principal del juego
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        
        # Dibujar teclas y conexiones
        dibujar_teclas()
        dibujar_conexiones()
        
        # Calcular los movimientos válidos para un número de pasos
        num_movimientos = 2  # Puedes cambiar este número para probar diferentes cantidades de movimientos
        total_movimientos = calcular_movimientos_iniciales(num_movimientos)

        # Mostrar resultados
        mostrar_resultados(num_movimientos, total_movimientos)

        # Detectar eventos de cierre de ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la tasa de refresco
        clock.tick(60)

    pygame.quit()
    sys.exit()

    

