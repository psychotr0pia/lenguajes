%option noyywrap nodefault yylineno case-insensitive
%{
/* Una palabra */
struct symbol {
  char *name;
  struct ref *reflist;
};

/* Ocurrencias de cada palabra (lista enlazada)*/
struct ref {
  struct ref *next;
  char *filename;
  int flags;
  int lineno;
};

/* Tabla de Simbolos simple (de tamanio fijo) */
#define NHASH 9997
struct symbol symtab[NHASH];
struct symbol *lookup(char*);
void addref(int, char*, char*,int);
char *curfilename; /* Nombre del archivo de entrada */
%}
%%
 /* En comentarios en la zona de reglas es
 /* importante el espacio inicial */
 /* Reglas */
 /* Descartar palabras basura (stopwords) como preposiciones y/o articulos */
a |
ante |
bajo |
cabe |
con |
contra |
de |
desde |
en |
entre |
el |
la |
los |
las |
un |
uno |
una |
unos |
unas   /* ignore */

[a-z]+ { addref(yylineno, curfilename, yytext, 0); }
.|\n  /* ignora lo demas */
%% 

/* Agrega unb simbolo (al hash) */
static unsigned symhash(char *sym) {
  unsigned int hash = 0;
  unsigned c;
  while(c = *sym++)
      hash = hash*9 ^ c;
  return hash;
}

struct symbol * lookup(char* sym) {
  struct symbol *sp = &symtab[symhash(sym)%NHASH];
  int scount = NHASH;     /* cuantos simbolos hemos buscado */
  while(--scount >= 0) {
    if(sp->name && !strcmp(sp->name, sym))
      return sp;

    if(!sp->name){ /* nueva entrada */
      sp->name = strdup(sym);
      sp->reflist = 0;
      return sp;
    }

    if(++sp >= symtab+NHASH)
      sp = symtab; /* prueba en la siguiente entrada */
  }
  fputs("overflow de la tabla de simbolos\n", stderr);
  abort(); /* tabla llena */
}

void addref(int lineno, char *filename, char *word, int flags) {
  struct ref *r;
  struct symbol *sp = lookup(word);

  /* No duplicar la misma linea y el mismo archivo */
  if(sp->reflist && sp->reflist->lineno == lineno && sp->reflist->filename == filename)
    return;
  
  r = malloc(sizeof(struct ref));
  
  if(!r) {
    fputs("out of space\n", stderr);
    abort();
  }
  
  r->next = sp->reflist;
  r->filename = filename;
  r->lineno = lineno;
  r->flags = flags;
  sp->reflist = r;
}

/* funcion auxiliar para ordenar */
static int symcompare(const void *xa, const void *xb) {
  const struct symbol *a = xa;
  const struct symbol *b = xb;
  
  if(!a->name) {
    if(!b->name)
      return 0; /* ambos vacios */
    return 1; /* pone los vacios al final */
  }

  if(!b->name)
    return -1;

  return strcmp(a->name, b->name);
}

/* Imprime las referencias
* Ordena la tabla alfabeticamente
* luego da vuelta cada entrada en la lista/tabla de referencias
* y las imprime
*/

void printrefs() {
  struct symbol *sp;
  qsort(symtab, NHASH, sizeof(struct symbol), symcompare); /* ordena la tabla de simbolos */

  for(sp = symtab; sp->name && sp < symtab+NHASH; sp++) {
    char *prevfn = NULL; /* ultimo nombre de archivo impreso, se salta los duplicados */

    /* reversa la lista de referencias */
    struct ref *rp = sp->reflist;
    struct ref *rpp = 0; /* previous ref */
    struct ref *rpn;     /* next ref */
    do {
      rpn = rp->next;
      rp->next = rpp;
      rpp = rp;
      rp = rpn;
    } while(rp);

    /* Imprime la palabra y sus referencias */
    printf("%10s", sp->name);
    for(rp = rpp; rp; rp = rp->next) {
      if(rp->filename == prevfn){
        printf(" %d", rp->lineno);
      }else{
        printf(" %s:%d", rp->filename, rp->lineno);
        prevfn = rp->filename;
      }
  }
  printf("\n"); }
}

main(int argc, char **argv){
  int i;
  if(argc < 2) { /* Lee desde la entrada estandar */
    curfilename = "(stdin)";
    yylineno = 1;
    yylex();
    }
    else
      for(i = 1; i < argc; i++) {
        FILE *f = fopen(argv[i], "r"); /*lee desde archivo*/
        if(!f) {
          perror(argv[1]);
          return (1);
        }
        curfilename = argv[i];
        yyrestart(f);
        yylineno = 1;
        yylex();
        fclose(f);
      }
  printrefs();
}