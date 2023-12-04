// Generated from /mnt/c/Users/hotal/OneDrive/Documentos/UV/Semestre 8/lenguajes/control1/pregunta1/Pintador.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PintadorParser}.
 */
public interface PintadorListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PintadorParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(PintadorParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link PintadorParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(PintadorParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link PintadorParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(PintadorParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PintadorParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(PintadorParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PintadorParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(PintadorParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link PintadorParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(PintadorParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link PintadorParser#estados}.
	 * @param ctx the parse tree
	 */
	void enterEstados(PintadorParser.EstadosContext ctx);
	/**
	 * Exit a parse tree produced by {@link PintadorParser#estados}.
	 * @param ctx the parse tree
	 */
	void exitEstados(PintadorParser.EstadosContext ctx);
	/**
	 * Enter a parse tree produced by {@link PintadorParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void enterMovimiento(PintadorParser.MovimientoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PintadorParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void exitMovimiento(PintadorParser.MovimientoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PintadorParser#stats}.
	 * @param ctx the parse tree
	 */
	void enterStats(PintadorParser.StatsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PintadorParser#stats}.
	 * @param ctx the parse tree
	 */
	void exitStats(PintadorParser.StatsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PintadorParser#dibujar}.
	 * @param ctx the parse tree
	 */
	void enterDibujar(PintadorParser.DibujarContext ctx);
	/**
	 * Exit a parse tree produced by {@link PintadorParser#dibujar}.
	 * @param ctx the parse tree
	 */
	void exitDibujar(PintadorParser.DibujarContext ctx);
}