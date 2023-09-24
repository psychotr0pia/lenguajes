%{
int caracteres = 0;
int palabras = 0;
int lineas = 0;
int minuscula = 0;
int mayuscula = 0;
int digitos = 0;
int cifra_numerica = 0;

%}

%%
[a-zA-Z][a-zA-Z0-9]* {palabras++; }
[0-9]+.{0,1}[0-9]* { cifra_numerica++; }
\n        {   caracteres++; lineas++; }
.         { caracteres++; }
%%

int main(int argc, char **argv) {
    yylex();
    printf("Palabras: %d\n", palabras);
    printf("Caracteres: %d\n", caracteres);
    printf("Lineas: %d\n", lineas);
    printf("Minusculas: %d\n", minuscula);
    printf("Mayusculas: %d\n", mayuscula);
    printf("Digitos: %d\n", digitos);
    printf("Cifra numerica: %d\n", cifra_numerica);
    
    return 0;
}