import antlr4
from CALexer import CALexer
from CAParser import CAParser
from CAListener import CAListener

class MainCAListener(CAListener):
    # Override the functions as needed
    def exitStatement(self, ctx):
        print("Custom exitStatement implementation")
        # Add your custom logic here

def main():
    input_stream = antlr4.InputStream("X : 42 Y : 23 Z : 10")
    lexer = CALexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = CAParser(stream)
    tree = parser.start()

    listener = MainCAListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    variables = listener.get_variables()
    print("Final variables:", variables)

if __name__ == '__main__':
    main()
