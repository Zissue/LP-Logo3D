###################################### 
###################################### 
### Author: Zixuan Sun 
### [LP] 2020-2021 - Q2 - Logo3D 
### Group: 22 L
###################################### 
###################################### 

import sys
from antlr4 import *
from logo3dLexer import logo3dLexer
from logo3dParser import logo3dParser

from visitor import TreeVisitor

#####################################


if len(sys.argv) <= 1:
    sys.exit("\n[USAGE]: Execute with: python3 script.py [file] (first_procedure_name) (parameters)\n")

# Case: python3 script.py [file] 
if len(sys.argv) >= 2:
    input_stream = FileStream(sys.argv[1])

lexer = logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = logo3dParser(token_stream)
tree = parser.root() 

# For debugging, print the parse tree
#print(tree.toStringTree(recog = parser)) 

# Case: python3 script.py [file] [procedure_name] [parameters]
if len(sys.argv) == 3:
    firstProcedure = sys.argv[2]
    listParameters = []
    visitor = TreeVisitor(firstPROC = firstProcedure, paramInvoc = listParameters)
elif len(sys.argv) > 3:
    firstProcedure = sys.argv[2]
    listParameters = sys.argv[3:]
    for i in range(0, len(listParameters)):
        listParameters[i] = float(listParameters[i])
    visitor = TreeVisitor(firstPROC = firstProcedure, paramInvoc = listParameters)
else:
    visitor = TreeVisitor()

print("\nExecuting '", sys.argv[1], "' Logo3D program...\n\n", sep="")

visitor.visit(tree)