// Generated from /mnt/c/Users/hotal/OneDrive/Documentos/UV/Semestre 8/lenguajes/certamen1/CA.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CALexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, X=2, Y=3, Z=4, LAMBDA=5, BETA=6, ALPHA=7, DELTA=8, INFECTADOS=9, 
		NUMBER=10, WS=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "X", "Y", "Z", "LAMBDA", "BETA", "ALPHA", "DELTA", "INFECTADOS", 
			"NUMBER", "WS", "DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'X'", "'Y'", "'Z'", "'LAMBDA'", "'BETA'", "'ALPHA'", "'DELTA'", 
			"'INFECTADOS'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "X", "Y", "Z", "LAMBDA", "BETA", "ALPHA", "DELTA", "INFECTADOS", 
			"NUMBER", "WS"
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


	public CALexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CA.g4"; }

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
		"\u0004\u0000\u000bk\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0003\tF\b"+
		"\t\u0001\t\u0001\t\u0001\t\u0005\tK\b\t\n\t\f\tN\t\t\u0003\tP\b\t\u0001"+
		"\t\u0001\t\u0004\tT\b\t\u000b\t\f\tU\u0003\tX\b\t\u0001\t\u0001\t\u0001"+
		"\t\u0004\t]\b\t\u000b\t\f\t^\u0003\ta\b\t\u0001\n\u0004\nd\b\n\u000b\n"+
		"\f\ne\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0000\u0000\f\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\u0000\u0001\u0000\u0003\u0001\u0000"+
		"19\u0003\u0000\t\n\r\r  \u0001\u000009q\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0001"+
		"\u0019\u0001\u0000\u0000\u0000\u0003\u001b\u0001\u0000\u0000\u0000\u0005"+
		"\u001d\u0001\u0000\u0000\u0000\u0007\u001f\u0001\u0000\u0000\u0000\t!"+
		"\u0001\u0000\u0000\u0000\u000b(\u0001\u0000\u0000\u0000\r-\u0001\u0000"+
		"\u0000\u0000\u000f3\u0001\u0000\u0000\u0000\u00119\u0001\u0000\u0000\u0000"+
		"\u0013`\u0001\u0000\u0000\u0000\u0015c\u0001\u0000\u0000\u0000\u0017i"+
		"\u0001\u0000\u0000\u0000\u0019\u001a\u0005=\u0000\u0000\u001a\u0002\u0001"+
		"\u0000\u0000\u0000\u001b\u001c\u0005X\u0000\u0000\u001c\u0004\u0001\u0000"+
		"\u0000\u0000\u001d\u001e\u0005Y\u0000\u0000\u001e\u0006\u0001\u0000\u0000"+
		"\u0000\u001f \u0005Z\u0000\u0000 \b\u0001\u0000\u0000\u0000!\"\u0005L"+
		"\u0000\u0000\"#\u0005A\u0000\u0000#$\u0005M\u0000\u0000$%\u0005B\u0000"+
		"\u0000%&\u0005D\u0000\u0000&\'\u0005A\u0000\u0000\'\n\u0001\u0000\u0000"+
		"\u0000()\u0005B\u0000\u0000)*\u0005E\u0000\u0000*+\u0005T\u0000\u0000"+
		"+,\u0005A\u0000\u0000,\f\u0001\u0000\u0000\u0000-.\u0005A\u0000\u0000"+
		"./\u0005L\u0000\u0000/0\u0005P\u0000\u000001\u0005H\u0000\u000012\u0005"+
		"A\u0000\u00002\u000e\u0001\u0000\u0000\u000034\u0005D\u0000\u000045\u0005"+
		"E\u0000\u000056\u0005L\u0000\u000067\u0005T\u0000\u000078\u0005A\u0000"+
		"\u00008\u0010\u0001\u0000\u0000\u00009:\u0005I\u0000\u0000:;\u0005N\u0000"+
		"\u0000;<\u0005F\u0000\u0000<=\u0005E\u0000\u0000=>\u0005C\u0000\u0000"+
		">?\u0005T\u0000\u0000?@\u0005A\u0000\u0000@A\u0005D\u0000\u0000AB\u0005"+
		"O\u0000\u0000BC\u0005S\u0000\u0000C\u0012\u0001\u0000\u0000\u0000DF\u0005"+
		"-\u0000\u0000ED\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FO\u0001"+
		"\u0000\u0000\u0000GP\u00050\u0000\u0000HL\u0007\u0000\u0000\u0000IK\u0003"+
		"\u0017\u000b\u0000JI\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000"+
		"LJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000"+
		"\u0000NL\u0001\u0000\u0000\u0000OG\u0001\u0000\u0000\u0000OH\u0001\u0000"+
		"\u0000\u0000PW\u0001\u0000\u0000\u0000QS\u0005.\u0000\u0000RT\u0003\u0017"+
		"\u000b\u0000SR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000US\u0001"+
		"\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VX\u0001\u0000\u0000\u0000"+
		"WQ\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000Xa\u0001\u0000\u0000"+
		"\u0000YZ\u00050\u0000\u0000Z\\\u0005.\u0000\u0000[]\u0003\u0017\u000b"+
		"\u0000\\[\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\\\u0001\u0000"+
		"\u0000\u0000^_\u0001\u0000\u0000\u0000_a\u0001\u0000\u0000\u0000`E\u0001"+
		"\u0000\u0000\u0000`Y\u0001\u0000\u0000\u0000a\u0014\u0001\u0000\u0000"+
		"\u0000bd\u0007\u0001\u0000\u0000cb\u0001\u0000\u0000\u0000de\u0001\u0000"+
		"\u0000\u0000ec\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fg\u0001"+
		"\u0000\u0000\u0000gh\u0006\n\u0000\u0000h\u0016\u0001\u0000\u0000\u0000"+
		"ij\u0007\u0002\u0000\u0000j\u0018\u0001\u0000\u0000\u0000\t\u0000ELOU"+
		"W^`e\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}