from antlr4 import *
import sys
from logo3dLexer import logo3dLexer
from logo3dParser import logo3dParser
from TreeVisitor import TreeVisitor
from antlr4.tree.Trees import Trees

#input_stream = InputStream(input('? '))
input_stream = FileStream(sys.argv[1])

lexer = logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = logo3dParser(token_stream)
tree = parser.root() 
visitor = TreeVisitor()
visitor.visit(tree)

print(Trees.toStringTree(tree, None, parser))
