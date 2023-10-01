%{
#include "calculadora_parser.tab.h"
%}
/* reconoce tokens para la calculadora */
%%
"+" { return ADD; }
"-" { return SUB; }
"*" { return MUL; }
"/" { return DIV; }
"|" { return ABS; }
"(" 
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
\n { return EOL; }
[ \t] {}
. { printf("OTRO CARACTER %c\n", *yytext); }
%%

