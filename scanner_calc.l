%{
#include "scanner_calc.tab.h"
int yylval;
void yyerror(char *);
char *p = NULL;
%}
/* reconoce tokens para la calculadora */
%%
"+" { printf("SUMA\n"); return SUMA; }
"-" { printf("RESTA\n"); return RESTA; }
"*" { printf("MULTIPLICACION\n"); return MULTIPLICA; }
"/" { printf("DIVISION\n"); return DIVIDE; }
"|" { printf("ABS\n"); return ABS; }
[0-9]+ { yylval = atoi(yytext); printf("NUMERO %d\n", yylval); return NUMERO; }
\n { printf("NUEVALINEA\n"); return FINLINEA; }
[ \t] {}
. { printf("OTRO CARACTER %c\n", *yytext); }
%%

