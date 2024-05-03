import pygame
import sys

# Tamaño de la ventana
ANCHO_VENTANA = 300
ALTO_VENTANA = 300

# Tamaño de cada cuadrado
TAMAÑO_CUADRADO = ANCHO_VENTANA // 3

class Cuadrado:
    def __init__(self, imagen, x, y):
        self.imagen = imagen
        self.rect = imagen.get_rect()
        self.rect.topleft = (x, y)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)

class CuadradoVacio:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO)

    def obtener_adyacentes(self, cuadrados):
        adyacentes = []
        x, y = self.rect.topleft
        for cuadrado in cuadrados:
            if cuadrado.rect.colliderect(pygame.Rect(x - TAMAÑO_CUADRADO, y, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO)) or \
               cuadrado.rect.colliderect(pygame.Rect(x + TAMAÑO_CUADRADO, y, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO)) or \
               cuadrado.rect.colliderect(pygame.Rect(x, y - TAMAÑO_CUADRADO, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO)) or \
               cuadrado.rect.colliderect(pygame.Rect(x, y + TAMAÑO_CUADRADO, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO)):
                adyacentes.append(cuadrado)
        return adyacentes

def dividir_imagen(imagen):
    sub_imagenes = []
    for fila in range(3):
        for columna in range(3):
            sub_imagen = imagen.subsurface(columna * TAMAÑO_CUADRADO, fila * TAMAÑO_CUADRADO, TAMAÑO_CUADRADO, TAMAÑO_CUADRADO)
            sub_imagenes.append(sub_imagen)
    return sub_imagenes

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Imagen dividida")

    # Carga de la imagen
    imagen_original = pygame.image.load("300x300.jpeg")  # Reemplaza "tu_imagen.jpg" con la ruta de tu imagen
    sub_imagenes = dividir_imagen(imagen_original)

    cuadrados = []
    cuadrado_vacio = None
    for i, sub_imagen in enumerate(sub_imagenes):
        fila = i // 3
        columna = i % 3
        if sub_imagen and (fila != 2 or columna != 2):  # Ignoramos la última sub-imagen para crear el cuadrado vacío
            cuadrado = Cuadrado(sub_imagen, columna * TAMAÑO_CUADRADO, fila * TAMAÑO_CUADRADO)
            cuadrados.append(cuadrado)
        elif not sub_imagen:
            cuadrado_vacio = CuadradoVacio(columna * TAMAÑO_CUADRADO, fila * TAMAÑO_CUADRADO)

    cuadrados.append(cuadrado_vacio)  # Agregamos el cuadrado vacío al final de la lista de cuadrados

    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.fill((255, 255, 255))

        # Dibujar los cuadrados en la pantalla
        for cuadrado in cuadrados:
            if isinstance(cuadrado, Cuadrado):  # Solo dibujamos los cuadrados que son instancias de Cuadrado
                cuadrado.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()
