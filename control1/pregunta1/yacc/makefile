CC = cc
CFLAGS = -Wall -g
LIBS = -lfl -lm -ly -lX11 -lSDL2

all: pregunta1

pregunta1: y.tab.c lex.yy.c ../include/gfx.c
	$(CC) $(CFLAGS) -o pregunta1 y.tab.c lex.yy.c ../include/gfx.c $(LIBS) -I../include

lex.yy.c: pregunta1.l
	lex pregunta1.l

y.tab.c: pregunta1.y
	yacc -d pregunta1.y

clean:
	rm -f pregunta1 y.tab.* lex.yy.c
