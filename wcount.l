%{
int caracteres = 0;
int palabras = 0; 
int lineas = 0;

int nro_car = 0;
int nro_pal = 0;
%} 

%% 

[a-zA-Z0-9]+ { palabras++; caracteres += strlen(yytext); nro_pal++; nro_car+=strlen(yytext); } 
\n 	  { caracteres++; lineas++; printf("\tPalabra = %d - Caracteres = %d\n", nro_pal, nro_car); nro_car = 0; nro_pal = 0;}
. 	  { caracteres++; } 

%% 

main(int argc, char **argv){
  yylex(); 
  printf("Lineas=%8d - Palabras=%8d - Caracteres=%8d\n",
           lineas, palabras, caracteres);
} 

