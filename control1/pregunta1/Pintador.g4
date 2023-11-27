grammar Pintador;

// Define lexer rules
PRENDER: 'PRENDER';
APAGAR: 'APAGAR';
MOVER: 'MOVER';
DIBUJAR: 'DIBUJAR';
STATS: 'ESTADISTICAS';
NUMBER: ('-'? DIGIT+);

// Ignore whitespace and newline characters
WS: [ \t\r\n]+ -> skip;

fragment DIGIT: [0-9];

start: comando+ EOF;

comando: argumentos ;

argumentos: ( estados | movimiento |stats | dibujar )+ ;
          

estados: ( PRENDER |APAGAR );

movimiento: MOVER NUMBER NUMBER;

stats: STATS;

dibujar: DIBUJAR;