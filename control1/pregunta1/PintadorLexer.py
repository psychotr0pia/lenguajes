# Generated from Pintador.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,76,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,3,5,61,
        8,5,1,5,4,5,64,8,5,11,5,12,5,65,1,6,4,6,69,8,6,11,6,12,6,70,1,6,
        1,6,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,0,1,0,2,3,0,9,
        10,13,13,32,32,1,0,48,57,77,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,17,1,0,0,0,3,
        25,1,0,0,0,5,32,1,0,0,0,7,38,1,0,0,0,9,46,1,0,0,0,11,60,1,0,0,0,
        13,68,1,0,0,0,15,74,1,0,0,0,17,18,5,80,0,0,18,19,5,82,0,0,19,20,
        5,69,0,0,20,21,5,78,0,0,21,22,5,68,0,0,22,23,5,69,0,0,23,24,5,82,
        0,0,24,2,1,0,0,0,25,26,5,65,0,0,26,27,5,80,0,0,27,28,5,65,0,0,28,
        29,5,71,0,0,29,30,5,65,0,0,30,31,5,82,0,0,31,4,1,0,0,0,32,33,5,77,
        0,0,33,34,5,79,0,0,34,35,5,86,0,0,35,36,5,69,0,0,36,37,5,82,0,0,
        37,6,1,0,0,0,38,39,5,68,0,0,39,40,5,73,0,0,40,41,5,66,0,0,41,42,
        5,85,0,0,42,43,5,74,0,0,43,44,5,65,0,0,44,45,5,82,0,0,45,8,1,0,0,
        0,46,47,5,69,0,0,47,48,5,83,0,0,48,49,5,84,0,0,49,50,5,65,0,0,50,
        51,5,68,0,0,51,52,5,73,0,0,52,53,5,83,0,0,53,54,5,84,0,0,54,55,5,
        73,0,0,55,56,5,67,0,0,56,57,5,65,0,0,57,58,5,83,0,0,58,10,1,0,0,
        0,59,61,5,45,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,64,
        3,15,7,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,
        66,12,1,0,0,0,67,69,7,0,0,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,
        0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,6,6,0,0,73,14,1,0,0,0,74,
        75,7,1,0,0,75,16,1,0,0,0,4,0,60,65,70,1,6,0,0
    ]

class PintadorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRENDER = 1
    APAGAR = 2
    MOVER = 3
    DIBUJAR = 4
    STATS = 5
    NUMBER = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'PRENDER'", "'APAGAR'", "'MOVER'", "'DIBUJAR'", "'ESTADISTICAS'" ]

    symbolicNames = [ "<INVALID>",
            "PRENDER", "APAGAR", "MOVER", "DIBUJAR", "STATS", "NUMBER", 
            "WS" ]

    ruleNames = [ "PRENDER", "APAGAR", "MOVER", "DIBUJAR", "STATS", "NUMBER", 
                  "WS", "DIGIT" ]

    grammarFileName = "Pintador.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


