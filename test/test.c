#include <SDL2/SDL.h>

int main() {
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

    // Set render draw color (RGB: Red, Green, Blue)
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255); // White

    // Clear the screen
    SDL_RenderClear(renderer);

    // Set the drawing color for the line (RGB: Blue)
    SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255); // Blue

    // Draw a line from (100, 200) to (300, 200)
    SDL_RenderDrawLine(renderer, 100, 200, 300, 200);

    // Set the drawing color for the point (RGB: Red)
    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255); // Red

    // Draw a point at (200, 300)
    SDL_RenderDrawPoint(renderer, 200, 300);

    // Update the screen
    SDL_RenderPresent(renderer);

    // Wait for a few seconds
    SDL_Delay(3000);

    // Clean up resources
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
