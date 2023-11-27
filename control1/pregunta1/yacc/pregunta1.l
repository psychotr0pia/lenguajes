%{
#include <stdio.h>
#include "y.tab.h"
%}

%%
-?([0-9]*[.][0-9]+)  {
    yylval.dval = atof(yytext);
    return NUMBER;
}

-?[0-9]+ {
    yylval.dval = atof(yytext);
    return NUMBER;
}

"PRENDER" { return PRENDER; }
"APAGAR" { return APAGAR; }
"MOVER" { return MOVER; }
"DIBUJAR" { return DIBUJAR; }
"STATS" { return STATS; }
[\n]        { return '\n'; }
[ \t] ; // Ignore whitespace
. ; // Catch-all rule for any other character
%%

