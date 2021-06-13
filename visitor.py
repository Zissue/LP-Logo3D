###################################### 
###################################### 
### Author: Zixuan Sun 
### [LP] 2020-2021 - Q2 - Logo3D 
### Group: 22 L
###################################### 
###################################### 

import sys      # To exit the program in case of errors
import readline # To read input
from turtle3d import Turtle3D   # Turtle3D API

if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
    from .logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor

#####################################

class ProcL3D:

    '''
    Aquesta clase es per guardar els "atributs"
    d'un procediment.
    '''

    def __init__(self, fName = "", fParam = [], fDict = {}, fCode = None):
        
        # Atribut que guarda el nom del procediment 
        self.funcName = fName

        # Atribut que guarda el nom dels parametres 
        self.listParam = fParam

        # Diccionari que guarda la variable amb el
        # seu valor
        self.symDict = fDict
        
        # Atribut que guarda el bloc de codi del
        # procediment com un token sencer
        self.blockofCode = fCode

#################################

class TreeVisitor(logo3dVisitor):

    '''
    Aquesta clase hereda de la clase logo3dVisitor creada
    per el compilador de antlr4.
    '''

    # Class constructor and atributes
    def __init__(self, firstPROC = "main", paramInvoc = [], turtleI = None):

        # Atribut per guardar el nom de totes les funcions
        self.__funcList = []
        # Atribut per guardar el nom de les funcions invocades
        # es a dir, es com una pila de les funcions invocades
        self.__funcStack = []
        # Atribut que guarda com a clau el nom de la funcio, i
        # com a valor un instancia de la classe anterior ProcL3D 
        self.__funcDict = {}

        # Atribut per guardar el nom del procediment pel
        # qual es comenca a executar, per defecte, es el
        # "main"
        self.__firstProcedure = firstPROC
        # Atribut per guardar la llista dels valors del
        # primer procediment
        self.__paramFirstProcedure = paramInvoc

        # Atribut per instanciar Turtle3D
        self.__turtle = turtleI
        # Atribut que indica si hi ha una instancia 
        # de la finestra grafica o no
        self.__enableTurt = False



    # Donat una llista de strings i un string,
    # retorna l'index del primer element del qual 
    # conte el substring del parametre 
    def index_string_list(self, the_list, substring):
        for i, s in enumerate(the_list):
            if substring in s:
                  return i
        return None



    # Visit a parse tree produced by logo3dParser#root.
    def visitRoot(self, ctx):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()
        
        # Warning per indicar que no hi ha cap procediment
        # en el programa, pero es correcte 
        if n <= 1:
            print("\n[WARNING]: No procedures (PROC) in this Logo3D program...\n")
            return

        l.pop()     # removes <EOF> token   

        # Obtenim la llista de funcions, i mirem si
        # existeix el primer procediment
        proceds = [p.getText() for p in l]
        aux = "PROC"+self.__firstProcedure+"("
        index = self.index_string_list(proceds, aux)
        if index == None:
            print("\n[ERROR]: First procedure '", self.__firstProcedure, "' does not exist...\n", sep="")
            return

        # List of procedures except the first invocation one 
        l2 = l[:]
        l2.pop(index)

        # Visit all the other procedures
        # to complete self.__funcDict
        for procedure in l2:
            fName = self.visit(procedure)

        # Visit the first procedure 
        self.visit(l[index])

        print("\n")



    # Visit a parse tree produced by logo3dParser#proceD.
    def visitProceD(self, ctx:logo3dParser.ProceDContext):
        
        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always 3 tokens


        if len(l) != 3:
           sys.exit("[ERROR]: Bad procedure declaration...")
            
        symDict = {}

        # Visit function header and get the procedure name 
        fName = self.visit(l[0])

        # Save the block of code of the procedure 
        self.__funcDict[fName].blockofCode = l[1]

        # Visit function body 
        self.visit(l[1])

        lastElem = len(self.__funcStack)-1
        self.__funcStack.pop(lastElem)

        return fName



    # Visit a parse tree produced by logo3dParser#funcHeader.
    def visitFuncHeader(self, ctx:logo3dParser.FuncHeaderContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        # Procedure name
        fName = l[1].getText()

        # Check if the procedure is already defined 
        if fName not in self.__funcList:
            self.__funcList.append(fName)
        else:
            sys.exit("[ERROR]: Procedure name duplicated!")
        
        self.__funcStack.append(fName)

        # Visit functions parameters 
        self.visit(l[3])

        return fName



    # Visit a parse tree produced by logo3dParser#funcParam.
    def visitFuncParam(self, ctx:logo3dParser.FuncParamContext, ):

        fN = self.__funcStack[len(self.__funcStack)-1]

        param = [n.getText() for n in ctx.getChildren() 
                 if logo3dParser.IDENT == n.getSymbol().type]

        # Check if there are duplicates parameters 
        # in the procedure header
        if len(param) != len(set(param)):
            sys.exit("[ERROR]: Duplicated parameter name in a procedure header!")

        # Set all variables to 0.0  
        symD = {}
        for p in param:
            symD[p] = 0.0

        # Check first invocation number of parameters 
        if self.__funcStack[0] == self.__firstProcedure:
            
            definedParams = self.__paramFirstProcedure
            if len(param) != len(definedParams):
                sys.exit("[ERROR]: Wrong number of arguments for the first invocation!")

            # Set the values of the first invocation 
            for i in range(0,len(param)):
                varName = param[i]
                argValue = definedParams[i]
                symD[varName] = argValue

        # Create an instance of class ProcL3D 
        proc = ProcL3D(fName = fN, fParam = param, fDict = symD)
        self.__funcDict[fN] = proc

        

    # Visit a parse tree produced by logo3dParser#instructions.
    def visitInstructions(self, ctx:logo3dParser.InstructionsContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # At least 1 token 

        # Visit every statement
        for stmt in l:
            self.visit(stmt)



    # Visit a parse tree produced by logo3dParser#stmt.
    def visitStmt(self, ctx:logo3dParser.StmtContext):

        l = [n for n in ctx.getChildren()]

        # Visit the single statement  
        self.visit(l[0])

    

    # Visit a parse tree produced by logo3dParser#assignation.
    def visitAssignation(self, ctx:logo3dParser.AssignationContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        varName = l[0].getText()
        valueAssign = self.visit(l[2])

        # Get procedure's name from the current procedure 
        fName = self.__funcStack[len(self.__funcStack)-1]

        # Assign float read from input to the variable in the 
        # symbols dictionary
        self.__funcDict[fName].symDict[varName] = valueAssign




    # Visit a parse tree produced by logo3dParser#expr.
    def visitExpr(self, ctx:logo3dParser.ExprContext):
        
        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        if n == 1:
            # Recursive case: numExpr 
            if "getRuleIndex" in dir(l[0]):
                return self.visit(l[0])
            else:
                # Case: True 
                if logo3dParser.TRUE == l[0].getSymbol().type:
                    return float(1.0) 
                # Case: False 
                else:
                    return float(0.0)
        
        if n == 3:
            # Case: ( expr ) 
            if "getRuleIndex" in dir(l[1]) and logo3dParser.LP == l[0].getSymbol().type:
                return self.visit(l[1])

            # Case: expr == expr
            if logo3dParser.EQ == l[1].getSymbol().type:
                return float(self.visit(l[0]) == self.visit(l[2]))

            # Case: expr != expr
            if logo3dParser.DIF == l[1].getSymbol().type:
                return float(self.visit(l[0]) != self.visit(l[2]))

            # Case: expr < expr
            if logo3dParser.LT == l[1].getSymbol().type:
                return float(self.visit(l[0]) < self.visit(l[2]))

            # Case: expr > expr
            if logo3dParser.GT == l[1].getSymbol().type:
                return float(self.visit(l[0]) > self.visit(l[2]))

            # Case: expr <= expr
            if logo3dParser.LTE == l[1].getSymbol().type:
                return float(self.visit(l[0]) <= self.visit(l[2]))

            # Case: expr >= expr
            if logo3dParser.GTE == l[1].getSymbol().type:
                return float(self.visit(l[0]) >= self.visit(l[2]))



    # Visit a parse tree produced by logo3dParser#numExpr.
    def visitNumExpr(self, ctx:logo3dParser.NumExprContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        # When there's a single token:
        # Case: Float number
        if n == 1 and logo3dParser.NUM == l[0].getSymbol().type:
            return float(l[0].getText())

        # Case: A variable 
        elif n == 1 and logo3dParser.IDENT == l[0].getSymbol().type:

            fName = self.__funcStack[len(self.__funcStack)-1]
            varName = l[0].getText()

            if varName in self.__funcDict[fName].symDict:
                return self.__funcDict[fName].symDict[varName]
            else:
                self.__funcDict[fName].symDict[varName] = 0.0
                return float(0.0)

        # When there are 3 tokens
        if n == 3:
            # Case: ( numExpr ) 
            if "getRuleIndex" in dir(l[1]):
                return self.visit(l[1])

            # Case: numExpr * numExpr
            if logo3dParser.MUL == l[1].getSymbol().type:
                return float(self.visit(l[0]) * self.visit(l[2]))

            # Case: numExpr / numExpr
            if logo3dParser.DIV == l[1].getSymbol().type:
                denom = self.visit(l[2])
                if denom == 0:
                    sys.exit("[ERROR]: Float division by ZERO!")
                return float(self.visit(l[0]) / denom)

            # Case: numExpr + numExpr
            if logo3dParser.ADD == l[1].getSymbol().type:
                return float(self.visit(l[0]) + self.visit(l[2]))

            # Case: numExpr - numExpr
            if logo3dParser.SUB == l[1].getSymbol().type:
                return float(self.visit(l[0]) - self.visit(l[2]))



    # Visit a parse tree produced by logo3dParser#read.
    def visitRead(self, ctx:logo3dParser.ReadContext):

        # Ignore pre-process reads
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always size 2 

        varName = l[1].getText()

        auxPrompt = "[READ]: " + varName + " << "

        # Only read an input that can be casted to float 
        while True:
            try:
                floatRead = float(input(auxPrompt))
            except ValueError:
                print("[ERROR]: Please introduce a single (float) number to READ!")
                continue
            else:
                # Successfully read a float 
                break

        # Get procedure's name from the current procedure 
        fName = self.__funcStack[len(self.__funcStack)-1]

        # Assign float read from input to the variable in the 
        # symbols dictionary
        self.__funcDict[fName].symDict[varName] = floatRead



    # Visit a parse tree produced by logo3dParser#write.
    def visitWrite(self, ctx:logo3dParser.WriteContext):
        
        # Ignore pre-process writes 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always size 2 

        # Visit the expresion first and the print the result returned 
        print("[WRITE]: ", self.visit(l[1]), " << ", l[1].getText())



    # Auxiliar function to check whether a number is True or False 
    # -1e-6  <=   number   <=  1e-6    then    number == False 
    def isFalse(self, floatNumber):
        if floatNumber >= (-1e-6) and floatNumber <= 1e-6:
            return True
        else:
            return False



    # Visit a parse tree produced by logo3dParser#conditional.
    def visitConditional(self, ctx:logo3dParser.ConditionalContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always 5 or 7 tokens

        # Check if the condition is False or True 
        conditionR = self.isFalse(self.visit(l[1]))

        # If conditionR is True,
        # we execute the 'THEN' block of code 
        if not conditionR:
            self.visit(l[3])

        # If conditionR is False and we have 'ELSE',
        # we execute the 'ELSE' block of code 
        elif conditionR and n == 7:
            self.visit(l[5])



    # Visit a parse tree produced by logo3dParser#while_it.
    def visitWhile_it(self, ctx:logo3dParser.While_itContext):
        
        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always 5 tokens

        # Check if the condition is False or True 
        conditionR = self.isFalse(self.visit(l[1]))

        # If conditionR is True,
        # we execute the 'DO' block of code 
        while not conditionR:
            self.visit(l[3])
            conditionR = self.isFalse(self.visit(l[1]))



    # Visit a parse tree produced by logo3dParser#for_it.
    def visitFor_it(self, ctx:logo3dParser.For_itContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always 9 tokens

        # Get procedure's name from the current procedure 
        fName = self.__funcStack[len(self.__funcStack)-1]

        # 'For' induction variable 
        inducVar = l[1].getText()

        startValue = self.visit(l[3])
        finalValue = self.visit(l[5])

        # Create a temporary induction variable in the 
        # table of symbols of the procedure 
        self.__funcDict[fName].symDict[inducVar] = startValue

        i = startValue
        while i <= finalValue:
            # Executed the 'DO' block of code 
            self.visit(l[7])
            # Update the induction variable, it may changed 
            i = self.__funcDict[fName].symDict[inducVar] 
            # Next iteration
            i += 1
            # Update the increment in the table of symbols
            self.__funcDict[fName].symDict[inducVar] = i

        # Delete the temporary induction variable created 
        del self.__funcDict[fName].symDict[inducVar]



    # Visit a parse tree produced by logo3dParser#invocation.
    def visitInvocation(self, ctx:logo3dParser.InvocationContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren()]

        invocName = l[0].getText()

        # Check if the invocation name is a procedure name 
        if invocName not in self.__funcList:
            saux = "[ERROR]: The procedure '"+invocName+"' does not exist!"
            sys.exit(saux)
            return

        # List of the parameters tokens 
        l = [n for n in ctx.getChildren() if "getRuleIndex" in dir(n)]
        n = ctx.getChildCount()     


        paramList = self.__funcDict[invocName].listParam

        # Check if the number of arguments is correct 
        if len(paramList) != len(l):
            print("[ERROR]: Wrong number of parameters in the invocation '", invocName, "'", sep="")
            return

        # List of arguments passed evaluated 
        evaluatedArgs = [self.visit(n) for n in l]

        # Taula de simbols amb els valors de les variables 
        symDict = self.__funcDict[invocName].symDict

        # Assign the value of the evaluated arguments 
        # to the parameters 
        for i in range(0, len(paramList)):
            varName = paramList[i]
            argVal = evaluatedArgs[i]
            symDict[varName] = argVal
        
        # Empilem el nom del procediment
        self.__funcStack.append(invocName)

        # Crida recursiva per executar el bloc de codi invocat 
        self.visit(self.__funcDict[invocName].blockofCode)

        # Desempilem el nom del procediment
        self.__funcStack.pop(len(self.__funcStack)-1)



    ##### Turtle operations 

    # Visit a parse tree produced by logo3dParser#color.
    def visitColor(self, ctx:logo3dParser.ColorContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() if "getRuleIndex" in dir(n)]
        n = ctx.getChildCount()     
        
        # Avaluem cada expresio r g b 
        rgb = [float(self.visit(n)) for n in l]

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.color(rgb[0],rgb[1],rgb[2])
        print("[Turtle3D]: Color set to rgb", rgb , " successfully!", sep="")



    # Visit a parse tree produced by logo3dParser#home.
    def visitHome(self, ctx:logo3dParser.HomeContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.home()
        print("[Turtle3D]: Home position!", sep="")


    # Visit a parse tree produced by logo3dParser#show.
    def visitShow(self, ctx:logo3dParser.ShowContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.show()
        print("[Turtle3D]: Showing paint!", sep="")


    # Visit a parse tree produced by logo3dParser#hide.
    def visitHide(self, ctx:logo3dParser.HideContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.hide()
        print("[Turtle3D]: Hiding paint!", sep="")


    # Visit a parse tree produced by logo3dParser#forward.
    def visitForward(self, ctx:logo3dParser.ForwardContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Avaluem la expresio del argument
        arg = float(self.visit(l[2]))

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.forward(arg)
        print("[Turtle3D]: Moved forward ", arg, " units successfully!", sep="")


    # Visit a parse tree produced by logo3dParser#backward.
    def visitBackward(self, ctx:logo3dParser.BackwardContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Avaluem la expresio del argument
        arg = float(self.visit(l[2]))

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.backward(arg)
        print("[Turtle3D]: Moved backward ", arg, " units successfully!", sep="")


    # Visit a parse tree produced by logo3dParser#up.
    def visitUp(self, ctx:logo3dParser.UpContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Avaluem la expresio del argument
        arg = float(self.visit(l[2]))

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.up(arg)
        print("[Turtle3D]: Turned ", arg, " degrees upward successfully!", sep="")


    # Visit a parse tree produced by logo3dParser#down.
    def visitDown(self, ctx:logo3dParser.DownContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Avaluem la expresio del argument
        arg = float(self.visit(l[2]))

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.down(arg)
        print("[Turtle3D]: Turned ", arg, " degrees downward successfully!", sep="")


    # Visit a parse tree produced by logo3dParser#left.
    def visitLeft(self, ctx:logo3dParser.LeftContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Avaluem la expresio del argument
        arg = float(self.visit(l[2]))

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.left(arg)
        print("[Turtle3D]: Turned ", arg, " degrees to the left successfully!", sep="")


    # Visit a parse tree produced by logo3dParser#right.
    def visitRight(self, ctx:logo3dParser.RightContext):

        # Ignore pre-process invocations 
        if self.__funcStack[0] != self.__firstProcedure:
            return

        l = [n for n in ctx.getChildren() ]
        n = ctx.getChildCount()     

        # Avaluem la expresio del argument
        arg = float(self.visit(l[2]))

        # Check if the graphic window is 
        # already initialized from before 
        if not self.__enableTurt:
            self.initializeTurtle()

        # Cridem a la API de Turtle3D
        self.__turtle.right(arg)
        print("[Turtle3D]: Turned ", arg, " degrees to the right successfully!", sep="")


    # To start a graphic window 
    def initializeTurtle(self):
        # Instanciem de la classe Turtle3D
        # NOTA: per veuere els eixos de coordenades
        # cal posar debug a True
        self.__turtle = Turtle3D(debug=True)
        self.__enableTurt = True

