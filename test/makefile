calc_token: scanner_calc.l calculadora_parser.y
			bison -d calculadora_parser.y
			flex scanner_calc.l
			gcc -Wall -o $@ calculadora_parser.tab.c lex.yy.c -lfl
clean: rm calculadora_parser.tab.* lex.yy.c calc_token
