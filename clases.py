import numpy as np  
class Tablero:
    def __int__(self, tamano=10):
        self.tamano=tamano
        #iniciamos la matriz del tablero con aguao espacios vacios usando Numpy
        self.matriz = np.full((tamano, tamano), "")
        def mostrar(self):
            """muestra el tablero actual por pantalla"""
            print(self.matriz)
        def colocar_barcos(self):
            """logica para posicionar los barcos en el tablero"""
            pass
        def recibir_disparos(self, fila, columna):
            """Gestionar el impacto de un disparo en una coordenada """
            pass
