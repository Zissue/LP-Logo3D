import sys
from antlr4 import *
from logo3dLexer import logo3dLexer
from logo3dParser import logo3dParser

from visitor import TreeVisitor
from antlr4.tree.Trees import Trees     # for debugging



#input_stream = InputStream(input('? '))
#input_stream = FileStream(sys.argv[1])

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))


lexer = logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = logo3dParser(token_stream)
tree = parser.root() 


visitor = TreeVisitor()
visitor.visit(tree)


print(Trees.toStringTree(tree, None, parser))
