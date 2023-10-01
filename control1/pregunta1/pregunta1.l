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
"PRENDER" { return PRENDER; }
"APAGAR" { return APAGAR; }
"MOVER" { return MOVER; }
"CSV" { return CSV;  }
"IMPRIMIR" { return IMPRIMIR; }
[ \t\n] ; /* ignore whitespace */
%%

