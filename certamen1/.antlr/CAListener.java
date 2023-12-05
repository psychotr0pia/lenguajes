// Generated from /mnt/c/Users/hotal/OneDrive/Documentos/UV/Semestre 8/lenguajes/certamen1/CA.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CAParser}.
 */
public interface CAListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CAParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(CAParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link CAParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(CAParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link CAParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(CAParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link CAParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(CAParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link CAParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(CAParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link CAParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(CAParser.VariableContext ctx);
}