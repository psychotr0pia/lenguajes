# Generated from Pintador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PintadorParser import PintadorParser
else:
    from PintadorParser import PintadorParser

# This class defines a complete listener for a parse tree produced by PintadorParser.
class PintadorListener(ParseTreeListener):

    # Enter a parse tree produced by PintadorParser#start.
    def enterStart(self, ctx:PintadorParser.StartContext):
        pass

    # Exit a parse tree produced by PintadorParser#start.
    def exitStart(self, ctx:PintadorParser.StartContext):
        pass


    # Enter a parse tree produced by PintadorParser#comando.
    def enterComando(self, ctx:PintadorParser.ComandoContext):
        pass

    # Exit a parse tree produced by PintadorParser#comando.
    def exitComando(self, ctx:PintadorParser.ComandoContext):
        pass


    # Enter a parse tree produced by PintadorParser#argumentos.
    def enterArgumentos(self, ctx:PintadorParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by PintadorParser#argumentos.
    def exitArgumentos(self, ctx:PintadorParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by PintadorParser#estados.
    def enterEstados(self, ctx:PintadorParser.EstadosContext):
        pass

    # Exit a parse tree produced by PintadorParser#estados.
    def exitEstados(self, ctx:PintadorParser.EstadosContext):
        pass


    # Enter a parse tree produced by PintadorParser#movimiento.
    def enterMovimiento(self, ctx:PintadorParser.MovimientoContext):
        pass

    # Exit a parse tree produced by PintadorParser#movimiento.
    def exitMovimiento(self, ctx:PintadorParser.MovimientoContext):
        pass


    # Enter a parse tree produced by PintadorParser#stats.
    def enterStats(self, ctx:PintadorParser.StatsContext):
        pass

    # Exit a parse tree produced by PintadorParser#stats.
    def exitStats(self, ctx:PintadorParser.StatsContext):
        pass


    # Enter a parse tree produced by PintadorParser#dibujar.
    def enterDibujar(self, ctx:PintadorParser.DibujarContext):
        pass

    # Exit a parse tree produced by PintadorParser#dibujar.
    def exitDibujar(self, ctx:PintadorParser.DibujarContext):
        pass



del PintadorParser