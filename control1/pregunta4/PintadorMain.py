
import math
import matplotlib.pyplot as plt
from antlr4 import *
from PintadorLexer import PintadorLexer
from PintadorParser import PintadorParser
from PintadorListener import PintadorListener

class Puntero:
    def __init__(self, orientacion=0):
        self.estado = False
        self.orientacion = orientacion
        self.posicion = [0, 0]
        self.paths_line = []
        self.paths_point = []

    def __str__(self):
        return f"Estado: {self.estado}, Posicion: {self.posicion}, Orientacion: {self.orientacion}"

    def rotar(self, angle):
        self.orientacion += angle
        # Normalize the orientation to be within [0, 360) degrees
        self.orientacion %= 360
    
    def calculate_distance(self, target_coordinates):
        x1, y1 = self.posicion
        x2, y2 = target_coordinates
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

    def calculate_angle(self, target_coordinates):
        x1, y1 = self.posicion
        x2, y2 = target_coordinates
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        return angle
    
    def calculate_endpoint_coordinates(self, magnitude, angle):
        x1, y1 = self.posicion
        x2 = x1 + magnitude * math.cos(math.radians(angle))
        y2 = y1 + magnitude * math.sin(math.radians(angle))
        return x2, y2

#clases para construir el AST
class ASTNode:
    def __str__(self, level=0):
        ret = "\t" * level + f"{self.__class__.__name__}\n"
        for child in self.__dict__:
            if isinstance(self.__dict__[child], ASTNode):
                ret += self.__dict__[child].__str__(level + 1)
            else:
                ret += "\t" * (level + 1) + f"{child}: {self.__dict__[child]}\n"
        return ret

class CommandNode(ASTNode):
    def __init__(self, command):
        self.command = command

class PintarNode(CommandNode):
    pass

class ApagarNode(CommandNode):
    pass

class StatsNode(CommandNode):
    pass

class DibujarNode(CommandNode):
    pass

class MoveNode(ASTNode):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RotateNode(ASTNode):
    def __init__(self, angle):
        self.angle = angle

class PintadorAST:
    def __init__(self):
        self.ast = []

    def __str__(self):
        ret = ""
        for node in self.ast:
            ret += node.__str__(1)  # Start at level 1 to provide initial indentation
        return ret


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

    def enterArgumentos(self, ctx: PintadorParser.ArgumentosContext):
        if ctx.estados():
            self.enterEstados(ctx.estados())
        elif ctx.movimiento():
            self.enterMovimiento(ctx.movimiento())
        elif ctx.rotar():
            self.enterRotar(ctx.rotar())
        elif ctx.stats():
            self.enterStats(ctx.stats())
        elif ctx.dibujar():
            self.enterDibujar(ctx.dibujar())
            
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