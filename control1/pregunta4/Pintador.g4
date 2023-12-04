grammar Pintador;

// Define lexer rules
PRENDER: 'PRENDER';
APAGAR: 'APAGAR';
MOVER: 'MOVER';
DIBUJAR: 'DIBUJAR';
STATS: 'ESTADISTICAS';
ROTAR: 'ROTAR';
REPETIR: 'REPETIR';
NUMBER: ('-'? DIGIT+);

// Ignore whitespace and newline characters
WS: [ \t\r\n]+ -> skip;

fragment DIGIT: [0-9];

start: comando+ EOF;

comando: argumentos ;

argumentos: ( estados | movimiento | stats | dibujar | rotar | repetir )+ ;

estados: ( PRENDER | APAGAR );
rotar: ROTAR '(' ( NUMBER ',' NUMBER | NUMBER | movimiento signos NUMBER) ')';
movimiento: MOVER '(' ( NUMBER ',' NUMBER | NUMBER ) ')';

stats: STATS;

dibujar: DIBUJAR;

repetir: REPETIR NUMBER ':' (argumentos | 'FIN')* ;

signos: ('+' | '-');
