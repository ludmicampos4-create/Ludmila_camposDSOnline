import numpy as np  
class Tablero:
    def __init__(self, tamano=10):
        self.tamano=tamano
        #iniciamos la matriz del tablero con aguao espacios vacios usando Numpy
        self.matriz = np.zeros((tamano, tamano), dtype=object)
    def mostrar(self):
        """muestra el tablero actual por pantalla"""
        print("   " + " ".join([str(i)for i in range(self.tamano)]))
        print("   " + "-" * (self.tamano * 3))
        for i, fila in enumerate(self.matriz):
            elementos_fila =[]
            for celda in fila:
                if celda == 0 or celda == "0":
                    elementos_fila.append("🟦")
                else:
                    elementos_fila.append("🚢")
            fila_formateada = "|".join(elementos_fila)
            print(f"{i} | {fila_formateada}")
    def colocar_barcos(self):
        #logica para posicionar los barcos en el tablero
            #1definimos la flota(tamaño de cada barco)
            # 4 barcos de 1 casilla de eslora 3 barcos de 2 casillas de eslora 2 barcos de 3 casillas de eslora 1 barco de 4 casillas de eslora
        flota= [
            {"nombre": "Portaaviones (eslora 4)", "eslora": 4},
            {"nombre": "Buque 1 (eslora 3)", "eslora": 3},
            {"nombre": "Buque 2 (eslora 3)", "eslora": 3 },
            {"nombre": "Destructor 1 (eslora 2)", "eslora":2},
            {"nombre": "Destructor 2 (eslora 2)", "eslora": 2},
            {"nombre": "Destructor 3 (eslora 2)", "eslora": 2},
            {"nombre": "Lancha 1 (eslora 1)","eslora":1 },
            {"nombre": "Lancha 2 (eslora 1)","eslora":1 },
            {"nombre": "Lancha 3 (eslora 1)","eslora":1 },
            {"nombre": "Lancha 4 (eslora 1)","eslora":1 },
        ]
        total_barcos = len(flota)
        
        for i, barcos in enumerate(flota):
            eslora = barcos["eslora"]
            nombre_barcos = barcos["nombre"]
            barcos_restantes = total_barcos - i 
            
            colocado = False
            while not colocado:
                print(f"======================================")
                print(f"🚢COLOCANDO: {nombre_barcos}")
                print(f"⏳BARCOS RESTANTES: {barcos_restantes} de {total_barcos}")
                print(f"======================================")
                self.mostrar() #muestra el tablero actual para que el jugador vea donde colocar los barcos
                    
                try:
                    fila = int(input("🎯Introduce la fila (0-9): "))
                    columna= int(input("📍Introduce la columna (0-9): "))
                    orientacion = input(" ➡️⬇️Introduce orientación (H para horizontal, V para vertical): ").upper()
                        #validar la horientacion y limites basicos
                    if orientacion not in ["H", "V"]:
                        print("❌😿 Error: La orientacion debe ser 'H' o 'V'.")
                        continue
                    if orientacion == "H" and columna + eslora > self.tamano:
                        print("❌🚢Error: El barco se sale del tablero por la derecha.")
                        continue
                    elif orientacion == "V" and fila + eslora > self.tamano:
                        print("❌⬇️Error: El barco se sale del tablero por abajo.")
                        continue
                
                    espacio_libre = True
                    if orientacion == "H":
                        for j in range(eslora):
                            if self.matriz[fila][columna + j] !=0:
                                espacio_libre = False
                                break
                    else:
                        for j in range(eslora):
                            if self.matriz[fila + j ][columna] !=0:
                                espacio_libre = False
                                break
                    if not espacio_libre:
                        print("❌🚢🚢Eror: Ya hay un barco en esa posicion.")
                        continue
                    if orientacion == "H":
                        for j in range(eslora):
                            self.matriz[fila][columna + j] = "B"
                    else:
                        for j in range(eslora):
                            self.matriz[fila + j ][columna]= "B"
                
                    colocado= True #!Barco colocado con exito!, pasamos al siguente!
                    print("¡Barco colocado correctamente!✅👌")
                except ValueError:
                    print("❌😿Error: Por favor, introduce numeros validos para la fila y la columna.")

    def recibir_disparos(self, fila, columna):
        """Gestionar el impacto de un disparo en una coordenada """
        pass
if __name__ == "__main__":
    mi_tablero = Tablero()
    mi_tablero.colocar_barcos()
