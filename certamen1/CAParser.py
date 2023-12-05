# Generated from CA.g4 by ANTLR 4.13.1
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
        4,1,11,23,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,4,1,15,8,1,11,1,12,1,16,1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,
        0,1,1,0,2,9,21,0,7,1,0,0,0,2,14,1,0,0,0,4,18,1,0,0,0,6,8,3,2,1,0,
        7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,
        12,5,0,0,1,12,1,1,0,0,0,13,15,3,4,2,0,14,13,1,0,0,0,15,16,1,0,0,
        0,16,14,1,0,0,0,16,17,1,0,0,0,17,3,1,0,0,0,18,19,7,0,0,0,19,20,5,
        1,0,0,20,21,5,10,0,0,21,5,1,0,0,0,2,9,16
    ]

class CAParser ( Parser ):

    grammarFileName = "CA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'X'", "'Y'", "'Z'", "'LAMBDA'", 
                     "'BETA'", "'ALPHA'", "'DELTA'", "'INFECTADOS'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "X", "Y", "Z", "LAMBDA", 
                      "BETA", "ALPHA", "DELTA", "INFECTADOS", "NUMBER", 
                      "WS" ]

    RULE_start = 0
    RULE_argumentos = 1
    RULE_variable = 2

    ruleNames =  [ "start", "argumentos", "variable" ]

    EOF = Token.EOF
    T__0=1
    X=2
    Y=3
    Z=4
    LAMBDA=5
    BETA=6
    ALPHA=7
    DELTA=8
    INFECTADOS=9
    NUMBER=10
    WS=11

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
            return self.getToken(CAParser.EOF, 0)

        def argumentos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CAParser.ArgumentosContext)
            else:
                return self.getTypedRuleContext(CAParser.ArgumentosContext,i)


        def getRuleIndex(self):
            return CAParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = CAParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.argumentos()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1020) != 0)):
                    break

            self.state = 11
            self.match(CAParser.EOF)
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

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CAParser.VariableContext)
            else:
                return self.getTypedRuleContext(CAParser.VariableContext,i)


        def getRuleIndex(self):
            return CAParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)




    def argumentos(self):

        localctx = CAParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_argumentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 13
                    self.variable()

                else:
                    raise NoViableAltException(self)
                self.state = 16 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CAParser.NUMBER, 0)

        def X(self):
            return self.getToken(CAParser.X, 0)

        def Y(self):
            return self.getToken(CAParser.Y, 0)

        def Z(self):
            return self.getToken(CAParser.Z, 0)

        def LAMBDA(self):
            return self.getToken(CAParser.LAMBDA, 0)

        def BETA(self):
            return self.getToken(CAParser.BETA, 0)

        def ALPHA(self):
            return self.getToken(CAParser.ALPHA, 0)

        def DELTA(self):
            return self.getToken(CAParser.DELTA, 0)

        def INFECTADOS(self):
            return self.getToken(CAParser.INFECTADOS, 0)

        def getRuleIndex(self):
            return CAParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = CAParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1020) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 19
            self.match(CAParser.T__0)
            self.state = 20
            self.match(CAParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





