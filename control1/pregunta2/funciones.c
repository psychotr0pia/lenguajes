
#include <stdio.h>
#include <stdlib.h>
#define MAX_ROWS 20
#define MAX_COLS 20

struct Puntero {
    int estado;
    double posX;
    double posY;
};

//struct Matrix2D {
//    int rows;
//    int cols;
//    double **data;
//};
/*
int **createMatrix(int rows, int cols) {
    if (rows <= 0 || cols <= 0 || rows > MAX_ROWS || cols > MAX_COLS) {
        printf("Invalid matrix dimensions. Rows and columns must be between 1 and %d.\n", MAX_ROWS);
        exit(EXIT_FAILURE);
    }
    int** matrix = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)malloc(cols * sizeof(int));
    }

    // Initialize the matrix with values
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = 0;
        }
    }

    return matrix;
}
*/
// Function to write a matrix to a CSV file
void writeMatrixToCSV(int matrix[MAX_ROWS][MAX_COLS], const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Failed to open file for writing");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < MAX_ROWS; i++) {
        for (int j = 0; j < MAX_COLS; j++) {
            fprintf(file, "%d", matrix[i][j]);
            if (j < MAX_COLS - 1) {
                fprintf(file, ",");
            }
        }
        fprintf(file, "\n");
    }

    fclose(file);
}

void addPoint(int matrix[MAX_ROWS][MAX_COLS], const struct Puntero *point) {
    if (point->posX >= 0 && point->posX < MAX_ROWS && point->posY >= 0 && point->posY < MAX_COLS) {
        // Check if the point is within the matrix bounds
        int x = (int)point->posX;
        int y = (int)point->posY;

        // Update the value at the specified coordinates
        matrix[x][y] = 1.0; // Set to 1.0 or any value you prefer to represent a point
    } else {
        printf("Point is out of bounds.\n");
    }
}
