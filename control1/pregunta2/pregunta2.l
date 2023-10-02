%{
#include <stdio.h>
#include "y.tab.h"
%}

%%
-?([0-9]*[.][0-9]+)  {
    yylval.dval = atof(yytext); // Convert matched text to double and store in yylval
    return NUMBER;
}

-?[0-9]+ {
    yylval.dval = atof(yytext); // Convert matched text to double and store in yylval
    return NUMBER;
}
(?i:prender) { return PRENDER; }
(?i:apagar) { return APAGAR; }
(?i:mover) { return MOVER; }
(?i:csv) { return CSV;  }
(?i:imprimir) { return IMPRIMIR; }
(?i:rotar) { return ROTAR; }
[ \t \n]  ; /* ignore whitespace */
%%

