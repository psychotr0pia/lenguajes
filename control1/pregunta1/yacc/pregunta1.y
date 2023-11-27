%{
//#include "../include/funciones.h"
#include <stdio.h>
#include <math.h>
#include <SDL2/SDL.h>

struct Puntero {
    int estado;
    double posX;
    double posY;
};

struct Puntero puntero = {0, 0, 0};
SDL_Window *window = NULL;
SDL_Renderer *renderer = NULL;

extern int yylex();
extern void yyerror(const char *s);


void drawPoint(double x, double y) {
    SDL_RenderDrawPoint(renderer, (int)x, (int)y);
    //XFlush(display);
}

void drawLine(double x1, double y1, double x2, double y2) {
    SDL_RenderDrawLine(renderer, (int)x1, (int)y1, (int)x2, (int)y2);
    //XFlush(display);
}
void closeGraphics() {
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}

    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        fprintf(stderr, "SDL initialization failed: %s\n", SDL_GetError());
        return 1;
    }

    // Create a window
    SDL_Window* window = SDL_CreateWindow("SDL2 Example", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, SDL_WINDOW_SHOWN);
    if (!window) {
        fprintf(stderr, "Window creation failed: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    // Create a renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        fprintf(stderr, "Renderer creation failed: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

%}

%union {
    double dval;
    int vblno;
}

%token <dval> NUMBER
%token PRENDER APAGAR MOVER DIBUJAR STATS
%token CSV IMPRIMIR

%start comando

%%

comando: argumentos { printf("Se ejecutó el comando!\n"); }
       | /* empty */  { /* Do nothing for an empty line */ }
       ;

argumentos: /* vacio */
          | argumentos estados 
          | argumentos movimiento 
          | argumentos NUMBER  { printf("%.2lf\n", $2); }
          | argumentos misc 
          | argumentos stats 
          ;

estados: PRENDER '\n'{
         printf("Prendiendo puntero...\n");
         puntero.estado = 1;
         printf("Puntero prendido! %d\n", puntero.estado);
       }
       | APAGAR '\n' {
        printf("Apagando puntero...\n");
        puntero.estado = 0;
        printf("Puntero apagado! %d\n", puntero.estado);
       }
       ;

movimiento: MOVER NUMBER NUMBER '\n' {
            //gfx_color(0, 200, 100);
            // Set the drawing color for the point (RGB: Red)
            SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255); // Red
            if (puntero.estado == 0 ) {
                printf("yendo directo al punto %.2lf %.2lf\n", $2, $3);
                puntero.posX = floor($2);
                puntero.posY = floor($3);
                SDL_RenderDrawPoint(renderer, (int)puntero.posX, (int)puntero.posY);
            }
            else {
                printf("haciendo camino hacia al punto %.2lf %.2lf\n", $2, $3);
                drawLine(puntero.posX, puntero.posY, $2, $3);
            }
            SDL_RenderPresent(renderer);
        };

misc: DIBUJAR '\n' {
        
        SDL_RenderPresent(renderer);
    }
    ;
stats: STATS  { printf("ESTADISTICAS command recognized!\n"); }
      ;
%%

int main() {
    
    printf("Hello, World!\n");

    // Event loop
    SDL_Event event;
    int quit = 0;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = 1;
            }
        }

        // Call yylex to start parsing
        if (yyparse() == 0) {
            // Parsing successful, render and present
            SDL_RenderPresent(renderer);
        }
    }

    closeGraphics();  // Close SDL graphics
    return 0;

}