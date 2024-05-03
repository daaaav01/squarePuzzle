import pygame

class Cuadrado:
    def __init__(self, imagen, x, y):
        self.imagen = imagen
        self.rect = imagen.get_rect()
        self.rect.topleft = (x, y)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)
