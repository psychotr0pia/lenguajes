# Generated from CA.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CAParser import CAParser
else:
    from CAParser import CAParser

# This class defines a complete listener for a parse tree produced by CAParser.
class CAListener(ParseTreeListener):

    # Enter a parse tree produced by CAParser#start.
    def enterStart(self, ctx:CAParser.StartContext):
        pass

    # Exit a parse tree produced by CAParser#start.
    def exitStart(self, ctx:CAParser.StartContext):
        pass


    # Enter a parse tree produced by CAParser#argumentos.
    def enterArgumentos(self, ctx:CAParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by CAParser#argumentos.
    def exitArgumentos(self, ctx:CAParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by CAParser#variable.
    def enterVariable(self, ctx:CAParser.VariableContext):
        pass

    # Exit a parse tree produced by CAParser#variable.
    def exitVariable(self, ctx:CAParser.VariableContext):
        pass



del CAParser