%{
/* Para compilar:
* bison -d nombre_archivo.y
* gcc -Wall nombre_archivo.tab.c nombre_archivo.tab.h -ll
*/

#include <ctype.h>
#include <stdio.h>

int yylex();

void yyerror(const char *msg){
  fprintf(stderr, "%s\n", msg);
}
%}

%token DIGITO

%%

linea   : '\n'           {printf("Linea en blanco\n");}
        | expr '\n'      { printf("Valor = %d\n",$1); }
	      ;
expr    :  expr '+' term   { $$ = $1 + $3; }
        | expr '-' term    { $$ = $1 - $3; }
	    | term             { $$ = $1; /* puede omitir, lo hace por defecto*/}    ;

term    :  term '*' factor  { $$ = $1 * $3; }
        |  term '/' factor  { $$ = $1 / $3; }
      	| factor
        ;
factor  :  '(' expr ')' 	{ $$ = $2; }
      	| DIGITO            { $$ = $1; }
      	;
%%

/*
*  Esta es nuestra propia definicion del
*  analizador lexico, posteriormente lo 
*  conectaremos con Lex (Flex).
*  isdigit( c ) esta reemplazando el uso de ER para identificar digitos
*/
int yylex() {
  int c;
  c = getchar();
  if (isdigit(c)) {
    yylval = c-'0';
    return DIGITO;
  }
  return c;
}

int main()
{
  yyparse();
}