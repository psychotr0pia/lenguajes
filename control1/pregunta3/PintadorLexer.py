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
        4,0,13,104,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,3,11,
        89,8,11,1,11,4,11,92,8,11,11,11,12,11,93,1,12,4,12,97,8,12,11,12,
        12,12,98,1,12,1,12,1,13,1,13,0,0,14,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,0,1,0,2,3,0,9,10,13,13,32,
        32,1,0,48,57,105,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,29,1,0,0,0,
        3,31,1,0,0,0,5,33,1,0,0,0,7,35,1,0,0,0,9,37,1,0,0,0,11,39,1,0,0,
        0,13,47,1,0,0,0,15,54,1,0,0,0,17,60,1,0,0,0,19,68,1,0,0,0,21,81,
        1,0,0,0,23,88,1,0,0,0,25,96,1,0,0,0,27,102,1,0,0,0,29,30,5,40,0,
        0,30,2,1,0,0,0,31,32,5,44,0,0,32,4,1,0,0,0,33,34,5,41,0,0,34,6,1,
        0,0,0,35,36,5,43,0,0,36,8,1,0,0,0,37,38,5,45,0,0,38,10,1,0,0,0,39,
        40,5,80,0,0,40,41,5,82,0,0,41,42,5,69,0,0,42,43,5,78,0,0,43,44,5,
        68,0,0,44,45,5,69,0,0,45,46,5,82,0,0,46,12,1,0,0,0,47,48,5,65,0,
        0,48,49,5,80,0,0,49,50,5,65,0,0,50,51,5,71,0,0,51,52,5,65,0,0,52,
        53,5,82,0,0,53,14,1,0,0,0,54,55,5,77,0,0,55,56,5,79,0,0,56,57,5,
        86,0,0,57,58,5,69,0,0,58,59,5,82,0,0,59,16,1,0,0,0,60,61,5,68,0,
        0,61,62,5,73,0,0,62,63,5,66,0,0,63,64,5,85,0,0,64,65,5,74,0,0,65,
        66,5,65,0,0,66,67,5,82,0,0,67,18,1,0,0,0,68,69,5,69,0,0,69,70,5,
        83,0,0,70,71,5,84,0,0,71,72,5,65,0,0,72,73,5,68,0,0,73,74,5,73,0,
        0,74,75,5,83,0,0,75,76,5,84,0,0,76,77,5,73,0,0,77,78,5,67,0,0,78,
        79,5,65,0,0,79,80,5,83,0,0,80,20,1,0,0,0,81,82,5,82,0,0,82,83,5,
        79,0,0,83,84,5,84,0,0,84,85,5,65,0,0,85,86,5,82,0,0,86,22,1,0,0,
        0,87,89,5,45,0,0,88,87,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,92,
        3,27,13,0,91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,
        0,94,24,1,0,0,0,95,97,7,0,0,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,
        1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,6,12,0,0,101,26,1,0,
        0,0,102,103,7,1,0,0,103,28,1,0,0,0,4,0,88,93,98,1,6,0,0
    ]

class PintadorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    PRENDER = 6
    APAGAR = 7
    MOVER = 8
    DIBUJAR = 9
    STATS = 10
    ROTAR = 11
    NUMBER = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "'+'", "'-'", "'PRENDER'", "'APAGAR'", 
            "'MOVER'", "'DIBUJAR'", "'ESTADISTICAS'", "'ROTAR'" ]

    symbolicNames = [ "<INVALID>",
            "PRENDER", "APAGAR", "MOVER", "DIBUJAR", "STATS", "ROTAR", "NUMBER", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "PRENDER", "APAGAR", 
                  "MOVER", "DIBUJAR", "STATS", "ROTAR", "NUMBER", "WS", 
                  "DIGIT" ]

    grammarFileName = "Pintador.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


