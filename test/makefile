CC = gcc
CFLAGS = -Wall -Wextra
LDFLAGS = -lSDL2

TARGET = sdl_example

all: $(TARGET)

$(TARGET): test.c
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS)

.PHONY: clean

clean:
	rm -f $(TARGET)
