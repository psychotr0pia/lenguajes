Instalar Windows Subsystems for Linux, y aplicarlo para vscode https://code.visualstudio.com/docs/cpp/config-wsl
despues, descargar e isntalar los paquetes bison y yacc. Listo ello, descargar las librerias necesaarias en c libbison-dev y libfl-dev
Para correrlo en Linux, uso los siguientes comandos:
yacc -d pregunta1.y; #archivo parser, genera y.tab.c
lex pregunta1.l; #archivo analizador lexico, genera lex.yy.c
cc -o myprogram y.tab.c lex.yy.c funciones.c -ly -lfl -lm 
#se adjunta archivo de funcionesauxiliares, y se linkea a las bicliotecas yacc, lexx y math
