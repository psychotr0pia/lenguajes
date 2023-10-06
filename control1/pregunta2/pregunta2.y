%{  

    #include "funciones.h"
    #include <stdio.h>
    #include <math.h>
    struct Puntero puntero = {0, MAX_ROWS/2, MAX_COLS/2};
    int matrix[MAX_ROWS][MAX_COLS] = {{0}};
    //struct Matrix2D *matrix = createMatrix(MAX_ROWS, MAX_COLS);
%}

%union {
    double dval;
    int vblno;
}
%token <dval> NUMBER
%token PRENDER APAGAR MOVER ROTAR
%token CSV IMPRIMIR
%token EJECUTAR
%%
comando: argumentos { printf("Se ejecuto el comando! \n"); }
argumentos: /* vacio */
          | argumentos estados
          | argumentos movimiento
          | argumentos NUMBER {printf("%.2lf", $2); }
          | argumentos misc
          //| EJECUTAR { printf("Se ejecuto el comando! \n"); }
          ;
estados: PRENDER {
         printf("Prendiendo puntero... \n");
         puntero.estado = 1;
         printf("Puntero prendido! %d \n", puntero.estado);
       }
       | APAGAR {
        printf("Apagando puntero... \n");
        puntero.estado = 0;
        printf("Puntero apagado! %d \n", puntero.estado);
       }
       ;
movimiento: MOVER NUMBER NUMBER  {
            if (puntero.estado == 0 ) {
                printf("yendo directo al punto %.2lf %.2lf", $2, $3);
                puntero.posX = puntero.posX + floor($2);
                puntero.posY = puntero.posY + floor($3);
                addPoint(matrix, &puntero);
                }
            else {
                printf("haciendo camino hacia al punto %.2lf %.2lf", $2, $3);      
          }
        }
        | ROTAR {
          printf("toy rotanding \n");  
        };
misc: CSV {
            writeMatrixToCSV(matrix, "matrix.csv");
    }
    | IMPRIMIR {
            printf("Impriendo matriz... \n");
    };
%%
/*
int main() {
//    struct Puntero puntero = {0, MAX_ROWS/2, MAX_COLS/2};
    printf("Creando matriz... \n");
    matrix = createMatrix(MAX_ROWS, MAX_COLS);
    printf("Matriz creada! \n");
    yylex();
}
*/
