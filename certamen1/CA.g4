grammar CA;

// Define lexer rules
X: 'X';
Y: 'Y';
Z: 'Z';
LAMBDA: 'LAMBDA';
BETA: 'BETA';
ALPHA: 'ALPHA';
DELTA: 'DELTA';
INFECTADOS: 'INFECTADOS';
NUMBER: ('-'? ('0' | [1-9] DIGIT*) 
        ('.' DIGIT+)?) | ('0' '.' DIGIT+);

// Ignore whitespace and newline characters
WS: [ \t\r\n]+ -> skip;
fragment DIGIT: [0-9];
// PARSER GRAMMAR

start: argumentos+ EOF;

argumentos: ( variable )+ ;
variable: ( X | Y | Z | LAMBDA 
| BETA | ALPHA | DELTA | INFECTADOS ) '=' NUMBER;

