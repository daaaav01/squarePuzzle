import pygame
import random

def dividir_imagen(imagen, ancho_ventana, alto_ventana):  
    tamaño_cuadrado = ancho_ventana // 3  # Define tamaño_cuadrado en función de ancho_ventana

    sub_imagenes = []
    for fila in range(3):
        for columna in range(3):
            sub_imagen = imagen.subsurface(columna * tamaño_cuadrado, fila * tamaño_cuadrado, tamaño_cuadrado, tamaño_cuadrado)
            sub_imagenes.append(sub_imagen)
    random.shuffle(sub_imagenes)  
    return sub_imagenes
