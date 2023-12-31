%{
    #undef input
    #undef output
    int input(void);
    void unput(int ch);
    unsigned verbose;
    char *progName;
%}

%%
-h |
"-?" |
-help {
    printf("usage is: %s [-help | -h | -? ] [-verbose | -v]" "[(-file| -f) filename]\n", progName);
}
-v | 
-verbose { printf("verbose mode is on\n"); verbose = 1; }
%%

int main(argc, argv) 
int argc;
char **argv;
{
    progName = *argv;
    yylex();
}
