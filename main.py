import pygame
import sys
from cuadrado import Cuadrado
from cuadrado_vacio import CuadradoVacio
from imagen import dividir_imagen

# Tamaño de la ventana
ANCHO_VENTANA = 300
ALTO_VENTANA = 300
TAMAÑO_CUADRADO = ANCHO_VENTANA // 3

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Imagen dividida")

    # Carga de la imagen
    imagen_original = pygame.image.load("300x300.jpeg")  # Reemplaza "tu_imagen.jpg" con la ruta de tu imagen
    sub_imagenes = dividir_imagen(imagen_original, ANCHO_VENTANA, ALTO_VENTANA)

    cuadrados = []
    cuadrado_vacio = CuadradoVacio(0, 0)  # Inicializamos cuadrado_vacio

    for i, sub_imagen in enumerate(sub_imagenes):
        fila = i // 3
        columna = i % 3
        if sub_imagen:  # Si hay una sub-imagen
            cuadrado = Cuadrado(sub_imagen, columna * TAMAÑO_CUADRADO, fila * TAMAÑO_CUADRADO)
            cuadrados.append(cuadrado)
            if fila == 2 and columna == 2:  # Si es el último cuadrado
                cuadrado_vacio = CuadradoVacio(columna * TAMAÑO_CUADRADO, fila * TAMAÑO_CUADRADO)

    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    adyacente = cuadrado_vacio.obtener_adyacente(cuadrados, 0, -TAMAÑO_CUADRADO)
                    if adyacente:
                        cuadrado_vacio.rect.move_ip(0, -TAMAÑO_CUADRADO)
                        adyacente.rect.move_ip(0, TAMAÑO_CUADRADO)
                elif evento.key == pygame.K_DOWN:
                    adyacente = cuadrado_vacio.obtener_adyacente(cuadrados, 0, TAMAÑO_CUADRADO)
                    if adyacente:
                        cuadrado_vacio.rect.move_ip(0, TAMAÑO_CUADRADO)
                        adyacente.rect.move_ip(0, -TAMAÑO_CUADRADO)
                elif evento.key == pygame.K_LEFT:
                    adyacente = cuadrado_vacio.obtener_adyacente(cuadrados, -TAMAÑO_CUADRADO, 0)
                    if adyacente:
                        cuadrado_vacio.rect.move_ip(-TAMAÑO_CUADRADO, 0)
                        adyacente.rect.move_ip(TAMAÑO_CUADRADO, 0)
                elif evento.key == pygame.K_RIGHT:
                    adyacente = cuadrado_vacio.obtener_adyacente(cuadrados, TAMAÑO_CUADRADO, 0)
                    if adyacente:
                        cuadrado_vacio.rect.move_ip(TAMAÑO_CUADRADO, 0)
                        adyacente.rect.move_ip(-TAMAÑO_CUADRADO, 0)

        pantalla.fill((255, 255, 255))

        # Dibujar los cuadrados en la pantalla
        for cuadrado in cuadrados:
            if isinstance(cuadrado, Cuadrado):  # Solo dibujamos los cuadrados que son instancias de Cuadrado
                cuadrado.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()
