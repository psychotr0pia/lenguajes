
import math
import matplotlib.pyplot as plt
from antlr4 import *


class Puntero:
    def __init__(self, orientacion=0):
        self.estado = False
        self.orientacion = orientacion
        self.posicion = [0, 0]
        self.paths_line = []
        self.paths_point = []

    def __str__(self):
        return f"Estado: {self.estado}, Posicion: {self.posicion}, Orientacion: {self.orientacion}"

class CustomListener(PintadorListener):
    def __init__(self, ast):
        self.puntero = Puntero()
        self.ast = ast 
        self.repetir_count = 0



    def enterEstados(self, ctx:PintadorParser.EstadosContext):
        if ctx.PRENDER():
            self.puntero.estado = True
            print("Puntero prendido!")
            prender_node = PintarNode("PRENDER")
            self.ast.ast.append(prender_node)
        elif ctx.APAGAR():
            self.puntero.estado = False 
            print("Puntero apagado!")
            apagar_node = ApagarNode("APAGAR")
            self.ast.ast.append(apagar_node)
    def enterMovimiento(self, ctx:PintadorParser.MovimientoContext):
         # Handle MOVER case for only one 
        numbersQty = len(ctx.NUMBER())
        values = [float(ctx.NUMBER(i).getText()) for i in range(numbersQty)]
        if numbersQty == 2: #mover(150, 200) newX = 150, newY = 200 calcular magnitud y orientacion
            target_coordinates = [values[0], values[1]]
            magnitud = self.puntero.calculate_distance(target_coordinates)
            orientacion = self.puntero.calculate_angle(target_coordinates)
            move_node = MoveNode(values[0], values[1])
            self.ast.ast.append(move_node)
        else: #mover(20), magnitud 20, orientacion actual del puntero
            magnitud = values[0]
            orientacion = self.puntero.orientacion
            move_node = MoveNode(magnitud, 0)
            self.ast.ast.append(move_node)
        
        punteroX, punteroY = self.puntero.posicion #coords actuales del puntero
        newX, newY = self.puntero.calculate_endpoint_coordinates(magnitud, orientacion) #nuevas coords

        if self.puntero.estado:  # Si el puntero está prendido
            print(f"Haciendo camino")    
            linea_x = [punteroX, newX]  # Línea de x
            linea_y = [punteroY, newY]  # Línea de y
            self.puntero.posicion[0] = newX  # Actualizamos la posición del puntero
            self.puntero.posicion[1] = newY
            for x, y in zip(linea_x, linea_y):
                self.puntero.paths_line.append((x, y))
        else:
            print(f"Yendo directo al punto {values}")
            self.puntero.posicion[0] = newX
            self.puntero.posicion[1] = newY
            self.puntero.paths_point.append(tuple(self.puntero.posicion))
    
    def enterRotar(self, ctx: PintadorParser.RotarContext):
        # Handle ROTAR case
        numbersQty = len(ctx.NUMBER())
        if numbersQty == 1: #rotar 90. El puntero rota 90 grados.
            angle = float(ctx.NUMBER(0).getText())
            self.puntero.rotar(angle)
            # Print updated state
            print(f"la orientacion del puntero ahora es {self.puntero}")
        else: #rotar(X, Y) //CAMBIAR ORIENTACION HACIA X Y
            values = [float(ctx.NUMBER(i).getText()) for i in range(numbersQty)]
            angle = self.puntero.calculate_angle(values)
            self.puntero.orientacion = angle
            print(f"la orientacion del puntero ahora es {self.puntero}")
        rotate_node = RotateNode(angle)
        self.ast.ast.append(rotate_node)
    def enterStats(self, ctx:PintadorParser.StatsContext):
        print(self.puntero)
        stats_node = StatsNode("ESTADISTICAS")
        self.ast.ast.append(stats_node)
    def enterDibujar(self, ctx:PintadorParser.DibujarContext):
        self.draw()
        dibujar_node = DibujarNode("DIBUJAR")
        self.ast.ast.append(dibujar_node)    
    
    def enterRepetir(self, ctx: PintadorParser.RepetirContext):
        self.repetir_count = int(ctx.NUMBER().getText())

    def exitRepetir(self, ctx: PintadorParser.RepetirContext):
        for _ in range(self.repetir_count):
            print(f"Repetition {_ + 1}")
            for argumentos_ctx in ctx.argumentos():
                print(f"Argumentos: {argumentos_ctx.getText()}")
                self.enterArgumentos(argumentos_ctx)
            
    def draw(self):
        if self.puntero.paths_line:
            positions = list(zip(*self.puntero.paths_line))
            plt.plot(positions[0], positions[1], 'r-')
        if self.puntero.paths_point:
            positions = list(zip(*self.puntero.paths_point))
            plt.plot(positions[0], positions[1], 'bo')
        plt.show()

def main():
    ast = PintadorAST()
    listener = CustomListener(ast)

    while True:
        try:
            user_input = input('Enter your command (Enter "exit" to quit): ')
            if user_input.lower() == "exit":
                for node in ast.ast:
                    print(node)
                break
            lexer = PintadorLexer(InputStream(user_input))
            stream = CommonTokenStream(lexer)
            parser = PintadorParser(stream)
            tree = parser.start()

            walker = ParseTreeWalker()
            walker.walk(listener, tree)

            for node in ast.ast:
                print(node)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()