// Generated from /mnt/c/Users/hotal/OneDrive/Documentos/UV/Semestre 8/lenguajes/control1/pregunta1/Pintador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class PintadorLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PRENDER=1, APAGAR=2, MOVER=3, DIBUJAR=4, STATS=5, NUMBER=6, WS=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PRENDER", "APAGAR", "MOVER", "DIBUJAR", "STATS", "NUMBER", "WS", "DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'PRENDER'", "'APAGAR'", "'MOVER'", "'DIBUJAR'", "'ESTADISTICAS'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PRENDER", "APAGAR", "MOVER", "DIBUJAR", "STATS", "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public PintadorLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Pintador.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0007L\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0003\u0005=\b\u0005\u0001\u0005\u0004\u0005"+
		"@\b\u0005\u000b\u0005\f\u0005A\u0001\u0006\u0004\u0006E\b\u0006\u000b"+
		"\u0006\f\u0006F\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0000"+
		"\u0000\b\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\u0000\u0001\u0000\u0002\u0003\u0000\t\n\r\r  \u0001"+
		"\u000009M\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0001\u0011\u0001\u0000\u0000\u0000"+
		"\u0003\u0019\u0001\u0000\u0000\u0000\u0005 \u0001\u0000\u0000\u0000\u0007"+
		"&\u0001\u0000\u0000\u0000\t.\u0001\u0000\u0000\u0000\u000b<\u0001\u0000"+
		"\u0000\u0000\rD\u0001\u0000\u0000\u0000\u000fJ\u0001\u0000\u0000\u0000"+
		"\u0011\u0012\u0005P\u0000\u0000\u0012\u0013\u0005R\u0000\u0000\u0013\u0014"+
		"\u0005E\u0000\u0000\u0014\u0015\u0005N\u0000\u0000\u0015\u0016\u0005D"+
		"\u0000\u0000\u0016\u0017\u0005E\u0000\u0000\u0017\u0018\u0005R\u0000\u0000"+
		"\u0018\u0002\u0001\u0000\u0000\u0000\u0019\u001a\u0005A\u0000\u0000\u001a"+
		"\u001b\u0005P\u0000\u0000\u001b\u001c\u0005A\u0000\u0000\u001c\u001d\u0005"+
		"G\u0000\u0000\u001d\u001e\u0005A\u0000\u0000\u001e\u001f\u0005R\u0000"+
		"\u0000\u001f\u0004\u0001\u0000\u0000\u0000 !\u0005M\u0000\u0000!\"\u0005"+
		"O\u0000\u0000\"#\u0005V\u0000\u0000#$\u0005E\u0000\u0000$%\u0005R\u0000"+
		"\u0000%\u0006\u0001\u0000\u0000\u0000&\'\u0005D\u0000\u0000\'(\u0005I"+
		"\u0000\u0000()\u0005B\u0000\u0000)*\u0005U\u0000\u0000*+\u0005J\u0000"+
		"\u0000+,\u0005A\u0000\u0000,-\u0005R\u0000\u0000-\b\u0001\u0000\u0000"+
		"\u0000./\u0005E\u0000\u0000/0\u0005S\u0000\u000001\u0005T\u0000\u0000"+
		"12\u0005A\u0000\u000023\u0005D\u0000\u000034\u0005I\u0000\u000045\u0005"+
		"S\u0000\u000056\u0005T\u0000\u000067\u0005I\u0000\u000078\u0005C\u0000"+
		"\u000089\u0005A\u0000\u00009:\u0005S\u0000\u0000:\n\u0001\u0000\u0000"+
		"\u0000;=\u0005-\u0000\u0000<;\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000"+
		"\u0000=?\u0001\u0000\u0000\u0000>@\u0003\u000f\u0007\u0000?>\u0001\u0000"+
		"\u0000\u0000@A\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000AB\u0001"+
		"\u0000\u0000\u0000B\f\u0001\u0000\u0000\u0000CE\u0007\u0000\u0000\u0000"+
		"DC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000"+
		"\u0000FG\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0006\u0006"+
		"\u0000\u0000I\u000e\u0001\u0000\u0000\u0000JK\u0007\u0001\u0000\u0000"+
		"K\u0010\u0001\u0000\u0000\u0000\u0004\u0000<AF\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}