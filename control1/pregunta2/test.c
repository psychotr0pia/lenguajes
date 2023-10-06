#include <stdio.h>
#include <stdlib.h>
#include "funciones.h" // Include the header file with your functions and structures
int matrix[MAX_ROWS][MAX_COLS] = {{0}};

int main() {
    // Test the createMatrix function
    //matrix = createMatrix(MAX_ROWS, MAX_COLS);

    // Initialize and print the matrix
    printf("Initialized Matrix:\n");
    for (int i = 0; i < MAX_ROWS; i++) {
        for (int j = 0; j < MAX_COLS; j++) {
            matrix[i][j] = (i * MAX_COLS) + j + 1;
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }

    // Test writing the matrix to a CSV file
    writeMatrixToCSV(matrix, "matrix.csv");
    printf("Matrix written to 'matrix.csv'\n");


    return 0;
}

