# Generated from Pintador.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,82,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,4,2,36,8,2,11,2,12,2,37,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,62,8,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,5,8,75,8,8,10,8,12,8,78,9,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,
        12,14,16,18,0,2,1,0,8,9,1,0,6,7,83,0,21,1,0,0,0,2,27,1,0,0,0,4,35,
        1,0,0,0,6,39,1,0,0,0,8,41,1,0,0,0,10,55,1,0,0,0,12,65,1,0,0,0,14,
        67,1,0,0,0,16,69,1,0,0,0,18,79,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,
        0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,
        5,0,0,1,26,1,1,0,0,0,27,28,3,4,2,0,28,3,1,0,0,0,29,36,3,6,3,0,30,
        36,3,10,5,0,31,36,3,12,6,0,32,36,3,14,7,0,33,36,3,8,4,0,34,36,3,
        16,8,0,35,29,1,0,0,0,35,30,1,0,0,0,35,31,1,0,0,0,35,32,1,0,0,0,35,
        33,1,0,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,
        0,38,5,1,0,0,0,39,40,7,0,0,0,40,7,1,0,0,0,41,42,5,13,0,0,42,51,5,
        1,0,0,43,44,5,15,0,0,44,45,5,2,0,0,45,52,5,15,0,0,46,52,5,15,0,0,
        47,48,3,10,5,0,48,49,3,18,9,0,49,50,5,15,0,0,50,52,1,0,0,0,51,43,
        1,0,0,0,51,46,1,0,0,0,51,47,1,0,0,0,52,53,1,0,0,0,53,54,5,3,0,0,
        54,9,1,0,0,0,55,56,5,10,0,0,56,61,5,1,0,0,57,58,5,15,0,0,58,59,5,
        2,0,0,59,62,5,15,0,0,60,62,5,15,0,0,61,57,1,0,0,0,61,60,1,0,0,0,
        62,63,1,0,0,0,63,64,5,3,0,0,64,11,1,0,0,0,65,66,5,12,0,0,66,13,1,
        0,0,0,67,68,5,11,0,0,68,15,1,0,0,0,69,70,5,14,0,0,70,71,5,15,0,0,
        71,76,5,4,0,0,72,75,3,4,2,0,73,75,5,5,0,0,74,72,1,0,0,0,74,73,1,
        0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,17,1,0,0,0,78,
        76,1,0,0,0,79,80,7,1,0,0,80,19,1,0,0,0,7,23,35,37,51,61,74,76
    ]

class PintadorParser ( Parser ):

    grammarFileName = "Pintador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'FIN'", "'+'", 
                     "'-'", "'PRENDER'", "'APAGAR'", "'MOVER'", "'DIBUJAR'", 
                     "'ESTADISTICAS'", "'ROTAR'", "'REPETIR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PRENDER", "APAGAR", "MOVER", "DIBUJAR", "STATS", 
                      "ROTAR", "REPETIR", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_comando = 1
    RULE_argumentos = 2
    RULE_estados = 3
    RULE_rotar = 4
    RULE_movimiento = 5
    RULE_stats = 6
    RULE_dibujar = 7
    RULE_repetir = 8
    RULE_signos = 9

    ruleNames =  [ "start", "comando", "argumentos", "estados", "rotar", 
                   "movimiento", "stats", "dibujar", "repetir", "signos" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    PRENDER=8
    APAGAR=9
    MOVER=10
    DIBUJAR=11
    STATS=12
    ROTAR=13
    REPETIR=14
    NUMBER=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PintadorParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.ComandoContext)
            else:
                return self.getTypedRuleContext(PintadorParser.ComandoContext,i)


        def getRuleIndex(self):
            return PintadorParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PintadorParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.comando()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 32512) != 0)):
                    break

            self.state = 25
            self.match(PintadorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentos(self):
            return self.getTypedRuleContext(PintadorParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return PintadorParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = PintadorParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.argumentos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estados(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.EstadosContext)
            else:
                return self.getTypedRuleContext(PintadorParser.EstadosContext,i)


        def movimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.MovimientoContext)
            else:
                return self.getTypedRuleContext(PintadorParser.MovimientoContext,i)


        def stats(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.StatsContext)
            else:
                return self.getTypedRuleContext(PintadorParser.StatsContext,i)


        def dibujar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.DibujarContext)
            else:
                return self.getTypedRuleContext(PintadorParser.DibujarContext,i)


        def rotar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.RotarContext)
            else:
                return self.getTypedRuleContext(PintadorParser.RotarContext,i)


        def repetir(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.RepetirContext)
            else:
                return self.getTypedRuleContext(PintadorParser.RepetirContext,i)


        def getRuleIndex(self):
            return PintadorParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)




    def argumentos(self):

        localctx = PintadorParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argumentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 35
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8, 9]:
                        self.state = 29
                        self.estados()
                        pass
                    elif token in [10]:
                        self.state = 30
                        self.movimiento()
                        pass
                    elif token in [12]:
                        self.state = 31
                        self.stats()
                        pass
                    elif token in [11]:
                        self.state = 32
                        self.dibujar()
                        pass
                    elif token in [13]:
                        self.state = 33
                        self.rotar()
                        pass
                    elif token in [14]:
                        self.state = 34
                        self.repetir()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 37 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRENDER(self):
            return self.getToken(PintadorParser.PRENDER, 0)

        def APAGAR(self):
            return self.getToken(PintadorParser.APAGAR, 0)

        def getRuleIndex(self):
            return PintadorParser.RULE_estados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstados" ):
                listener.enterEstados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstados" ):
                listener.exitEstados(self)




    def estados(self):

        localctx = PintadorParser.EstadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_estados)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RotarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROTAR(self):
            return self.getToken(PintadorParser.ROTAR, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(PintadorParser.NUMBER)
            else:
                return self.getToken(PintadorParser.NUMBER, i)

        def movimiento(self):
            return self.getTypedRuleContext(PintadorParser.MovimientoContext,0)


        def signos(self):
            return self.getTypedRuleContext(PintadorParser.SignosContext,0)


        def getRuleIndex(self):
            return PintadorParser.RULE_rotar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRotar" ):
                listener.enterRotar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRotar" ):
                listener.exitRotar(self)




    def rotar(self):

        localctx = PintadorParser.RotarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rotar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(PintadorParser.ROTAR)
            self.state = 42
            self.match(PintadorParser.T__0)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 43
                self.match(PintadorParser.NUMBER)
                self.state = 44
                self.match(PintadorParser.T__1)
                self.state = 45
                self.match(PintadorParser.NUMBER)
                pass

            elif la_ == 2:
                self.state = 46
                self.match(PintadorParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 47
                self.movimiento()
                self.state = 48
                self.signos()
                self.state = 49
                self.match(PintadorParser.NUMBER)
                pass


            self.state = 53
            self.match(PintadorParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MovimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVER(self):
            return self.getToken(PintadorParser.MOVER, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(PintadorParser.NUMBER)
            else:
                return self.getToken(PintadorParser.NUMBER, i)

        def getRuleIndex(self):
            return PintadorParser.RULE_movimiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMovimiento" ):
                listener.enterMovimiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMovimiento" ):
                listener.exitMovimiento(self)




    def movimiento(self):

        localctx = PintadorParser.MovimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_movimiento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(PintadorParser.MOVER)
            self.state = 56
            self.match(PintadorParser.T__0)
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 57
                self.match(PintadorParser.NUMBER)
                self.state = 58
                self.match(PintadorParser.T__1)
                self.state = 59
                self.match(PintadorParser.NUMBER)
                pass

            elif la_ == 2:
                self.state = 60
                self.match(PintadorParser.NUMBER)
                pass


            self.state = 63
            self.match(PintadorParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATS(self):
            return self.getToken(PintadorParser.STATS, 0)

        def getRuleIndex(self):
            return PintadorParser.RULE_stats

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStats" ):
                listener.enterStats(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStats" ):
                listener.exitStats(self)




    def stats(self):

        localctx = PintadorParser.StatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stats)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(PintadorParser.STATS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DibujarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIBUJAR(self):
            return self.getToken(PintadorParser.DIBUJAR, 0)

        def getRuleIndex(self):
            return PintadorParser.RULE_dibujar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDibujar" ):
                listener.enterDibujar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDibujar" ):
                listener.exitDibujar(self)




    def dibujar(self):

        localctx = PintadorParser.DibujarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dibujar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(PintadorParser.DIBUJAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPETIR(self):
            return self.getToken(PintadorParser.REPETIR, 0)

        def NUMBER(self):
            return self.getToken(PintadorParser.NUMBER, 0)

        def argumentos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PintadorParser.ArgumentosContext)
            else:
                return self.getTypedRuleContext(PintadorParser.ArgumentosContext,i)


        def getRuleIndex(self):
            return PintadorParser.RULE_repetir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetir" ):
                listener.enterRepetir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetir" ):
                listener.exitRepetir(self)




    def repetir(self):

        localctx = PintadorParser.RepetirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_repetir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(PintadorParser.REPETIR)
            self.state = 70
            self.match(PintadorParser.NUMBER)
            self.state = 71
            self.match(PintadorParser.T__3)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8, 9, 10, 11, 12, 13, 14]:
                        self.state = 72
                        self.argumentos()
                        pass
                    elif token in [5]:
                        self.state = 73
                        self.match(PintadorParser.T__4)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PintadorParser.RULE_signos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignos" ):
                listener.enterSignos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignos" ):
                listener.exitSignos(self)




    def signos(self):

        localctx = PintadorParser.SignosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_signos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





