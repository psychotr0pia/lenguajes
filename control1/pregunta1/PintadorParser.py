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
        4,1,7,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,4,2,
        28,8,2,11,2,12,2,29,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,
        0,0,7,0,2,4,6,8,10,12,0,1,1,0,1,2,39,0,15,1,0,0,0,2,21,1,0,0,0,4,
        27,1,0,0,0,6,31,1,0,0,0,8,33,1,0,0,0,10,37,1,0,0,0,12,39,1,0,0,0,
        14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,
        0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,22,3,4,2,0,22,
        3,1,0,0,0,23,28,3,6,3,0,24,28,3,8,4,0,25,28,3,10,5,0,26,28,3,12,
        6,0,27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,29,
        1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,5,1,0,0,0,31,32,7,0,0,0,32,
        7,1,0,0,0,33,34,5,3,0,0,34,35,5,6,0,0,35,36,5,6,0,0,36,9,1,0,0,0,
        37,38,5,5,0,0,38,11,1,0,0,0,39,40,5,4,0,0,40,13,1,0,0,0,3,17,27,
        29
    ]

class PintadorParser ( Parser ):

    grammarFileName = "Pintador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PRENDER'", "'APAGAR'", "'MOVER'", "'DIBUJAR'", 
                     "'ESTADISTICAS'" ]

    symbolicNames = [ "<INVALID>", "PRENDER", "APAGAR", "MOVER", "DIBUJAR", 
                      "STATS", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_comando = 1
    RULE_argumentos = 2
    RULE_estados = 3
    RULE_movimiento = 4
    RULE_stats = 5
    RULE_dibujar = 6

    ruleNames =  [ "start", "comando", "argumentos", "estados", "movimiento", 
                   "stats", "dibujar" ]

    EOF = Token.EOF
    PRENDER=1
    APAGAR=2
    MOVER=3
    DIBUJAR=4
    STATS=5
    NUMBER=6
    WS=7

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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.comando()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                    break

            self.state = 19
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
            self.state = 21
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
            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 27
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2]:
                        self.state = 23
                        self.estados()
                        pass
                    elif token in [3]:
                        self.state = 24
                        self.movimiento()
                        pass
                    elif token in [5]:
                        self.state = 25
                        self.stats()
                        pass
                    elif token in [4]:
                        self.state = 26
                        self.dibujar()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 29 
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
            self.state = 31
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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
        self.enterRule(localctx, 8, self.RULE_movimiento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(PintadorParser.MOVER)
            self.state = 34
            self.match(PintadorParser.NUMBER)
            self.state = 35
            self.match(PintadorParser.NUMBER)
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
        self.enterRule(localctx, 10, self.RULE_stats)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
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
        self.enterRule(localctx, 12, self.RULE_dibujar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PintadorParser.DIBUJAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





