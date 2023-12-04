'''
    [Hecho] Definir una gramática para un lenguaje que permita dibujar utilizando un Puntero.
    [Hecho] Implementar la clase Puntero con la capacidad de dibujar según su movimiento.
    [Hecho] Permitir cambiar la posición del Puntero.
    [Hecho] Manejar el caso en el que el Puntero está "encendido" y dibujar puntos a medida que se mueve.
    [Hecho] Manejar el caso en el que el Puntero está "apagado" y solo dibujar un punto donde llego.
'''
import matplotlib.pyplot as plt
from antlr4 import *
from PintadorLexer import PintadorLexer
from PintadorParser import PintadorParser
from PintadorListener import PintadorListener

class Puntero:
    def __init__(self):
        self.estado = False
        self.posicion = [0, 0]
        self.paths_line = []
        self.paths_point = []

    def __str__(self):
        return f"Estado: {self.estado}, Posicion: {self.posicion}"
    
class CustomListener(PintadorListener):
    def __init__(self):
        self.puntero = Puntero()

    def enterEstados(self, ctx:PintadorParser.EstadosContext):
        if ctx.PRENDER():
            self.puntero.estado = True
            print("Puntero prendido!")
        elif ctx.APAGAR():
            self.puntero.estado = False 
            print("Puntero apagado!")
    def enterMovimiento(self, ctx:PintadorParser.MovimientoContext):
        #conseguimos los tokens NUMBER del texto
        values = [float(ctx.NUMBER(i).getText()) for i in range(2)]
        if self.puntero.estado: #si el punteor esta prendido
            punteroX, punteroY = self.puntero.posicion
            print(f"haciendo camino hacia al punto {values} desde {self.puntero.posicion}")
            linea_x = [punteroX, values[0]] #linea de x
            linea_y = [punteroY, values[1]] #linea de y
            self.puntero.posicion[0] = values[0] #actualizamos la posicion del puntero
            self.puntero.posicion[1] = values[1]
            for x, y in zip(linea_x, linea_y):
                self.puntero.paths_line.append((x, y))
        else:
            print(f"yendo directo al punto {values}")
            self.puntero.posicion[0] = values[0]
            self.puntero.posicion[1] = values[1]
            self.puntero.paths_point.append(tuple(self.puntero.posicion))
    def enterStats(self, ctx:PintadorParser.StatsContext):
        print(self.puntero)

    def enterDibujar(self, ctx:PintadorParser.DibujarContext):
        self.draw()
    
    def draw(self):
        if self.puntero.paths_line:
            positions = list(zip(*self.puntero.paths_line))
            plt.plot(positions[0], positions[1], 'r-')
        if self.puntero.paths_point:
            positions = list(zip(*self.puntero.paths_point))
            plt.plot(positions[0], positions[1], 'bo')
        plt.show()

def main():
    listener = CustomListener()
    while True:
        try:
            user_input = input('Enter your command (Enter "exit" to quit): ')
            if user_input.lower() == "exit":
                break
            lexer = PintadorLexer(InputStream(user_input))
            stream = CommonTokenStream(lexer)
            parser = PintadorParser(stream)
            tree = parser.start()

            walker = ParseTreeWalker()
            walker.walk(listener, tree)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()