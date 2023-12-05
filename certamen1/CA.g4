grammar CA;

// Define lexer rules
X: 'X' ':' NUMBER;
Y: 'Y' ':' NUMBER;
Z: 'Z' ':' NUMBER;
LAMBDA: 'LAMBDA' ':' '0.' NUMBER;
BETA: 'BETA' ':' '0.' NUMBER;
ALPHA: 'ALPHA' ':' '0.' NUMBER;
DELTA: 'DELTA' ':' '0.' NUMBER;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: ('0'..'9')+;

// Ignore whitespace and newline characters
WS: [ \t\r\n]+ -> skip;

// PARSER GRAMMAR

start: argumentos+ EOF;


argumentos: ( variable )+ ;
variable: (X | Y | Z | LAMBDA | BETA | ALPHA | DELTA);

