#ifndef funciones_h
#define funciones_h

#include <stdio.h>

#define MAX_ROWS 20
#define MAX_COLS 20

struct Puntero {
    int estado;
    double posX;
    double posY;
};

struct Matrix2D {
    int rows;
    int cols;
    double **data;
};

// Function prototypes
//int **createMatrix(int rows, int cols);
void writeMatrixToCSV(int matrix[MAX_ROWS][MAX_COLS], const char *filename);
void addPoint(int matrix[MAX_ROWS][MAX_COLS], const struct Puntero *point);

#endif

