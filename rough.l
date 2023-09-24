%{ 
/* seccion de declaraciones. */
int count = 0;
%}

%%

\"[a-zA-Z]*[0-9]*\\"\" {printf("string!\n");}
while|WHILE {printf("WHILE\n");}
[ \t] {printf("SPACE!!!\n");}
[>] {printf("mayor\n");}
[<] {printf("menor\n");}
[==] {printf("equals\n");}
[_] {printf("guion bajo!\n");}

.	 {printf("%s not a capital letter\n", yytext);}
\n {return 0;}
%%

int yywrap(){}
int main(){

// Explanation:
// yywrap() - wraps the above rule section
/* yyin - takes the file pointer
		which contains the input*/
/* yylex() - this is the main flex function
		which runs the Rule Section*/
// yytext is the text in the buffer

// Uncomment the lines below
// to take input from file
// FILE *fp;
// char filename[50];
// printf("Enter the filename: \n");
// scanf("%s",filename);
// fp = fopen(filename,"r");
// yyin = fp;

yylex();
printf("\nNumber of Capital letters "
	"in the given input - %d\n", count);

return 0;
}
