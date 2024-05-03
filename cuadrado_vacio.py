import pygame
from main import TAMAÑO_CUADRADO

class CuadradoVacio:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO)

    def obtener_adyacente(self, cuadrados, dx, dy):
        x, y = self.rect.topleft[0] + dx, self.rect.topleft[1] + dy
        for cuadrado in cuadrados:
            if cuadrado.rect.topleft == (x, y):
                return cuadrado
        return None
