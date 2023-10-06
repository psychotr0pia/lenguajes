%{
#include <stdio.h>

int yylex();
void yyerror(const char *s){
  fprintf(stderr, "%s\n", s);
}
%} 

/* declaramos los tokens */
%token NUMBER
%token ADD SUB MUL DIV ABS
%token EOL 

%%
linea: /* Coincide con inicio la entrada */
 | linea exp EOL { printf("uwu = %d \n", $2);}
 ; 
exp: factor
 | exp ADD factor { $$ = $1 + $3; }
 | exp SUB factor { $$ = $1 - $3; } ; 
factor: term
 | factor MUL term { $$ = $1 * $3; }
 | factor DIV term { $$ = $1 / $3; } ; 
term: NUMBER
 | ABS term { $$ = $2 >= 0? $2 : - $2; }
 | AP exp CP { $$ = $2; }
 ; 

%%


int main(int argc, char **argv){
  yyparse();
  return 0;
}

