import sys
import readline
if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
    from .logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor

#################################

class ProcL3D:

    def __init__(self, fName = "", fParam = [], fDict = {}, fCode = None):
        self.funcName = fName
        self.listParam = fParam
        self.symDict = fDict
        self.blockofCode = fCode

#################################

class TreeVisitor(logo3dVisitor):

    # Class atributes
    def __init__(self, firstPROC = "main", paramInvoc = []):
        self.__funcList = []
        self.__funcStack = []
        self.__funcDict = {}
        self.__firstProcedure = firstPROC
        self.__paramFirstProcedure = paramInvoc

    # Given a substring find the first index of 
    # the element in the list that contains the substring 
    def index_string_list(self, the_list, substring):
        for i, s in enumerate(the_list):
            if substring in s:
                  return i
        return None

    # Visit root 
    def visitRoot(self, ctx):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        if n <= 1:
            print("\n[WARNING]: No procedures (PROC) in this Logo3D program...\n")
            return

        l.pop()     # removes <EOF> token   

        proceds = [p.getText() for p in l]

        print("=========================\n")
        for tks in proceds:
            print(tks)
        print("=========================\n")

        aux = "PROC"+self.__firstProcedure

        index = self.index_string_list(proceds, aux)

        if index == None:
            print("\n[ERROR]: First procedure '", self.__firstProcedure, "' does not exist...\n", sep="")
            return
        #elif index <= n-2:
        #    sys.exit("[ERROR:]: Unexpected error ocurred!")

        # List of procedures except the first invocation one 
        l2 = l[:]
        l2.pop(index)

        # Visit all the other procedures 
        for procedure in l2:
            fName = self.visit(procedure)

        # Visit the first procedure 
        self.visit(l[index])

        print("\n")


    # Visit a parse tree produced by logo3dParser#proceD.
    def visitProceD(self, ctx:logo3dParser.ProceDContext):
        
        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always 3 tokens


        print("Num. Tokens: ", n)
        print("=========================\n")
        for tks in l:
            print("Token: ", tks.getText())
            #print("\n", dir(tks), "\n\n")
        print("=========================\n")
        
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

        #print("=========================\n")
        #for tks in l:
        #    print(tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("=========================\n")

        fName = l[1].getText()

        if fName not in self.__funcList:
            self.__funcList.append(fName)
            #print("My function name: ", fName)
        else:
            sys.exit("[ERROR]: Procedure name duplicated!")
        
        self.__funcStack.append(fName)

        # Visit functions parameters 
        self.visit(l[3])

        return fName



    # Visit a parse tree produced by logo3dParser#funcParam.
    def visitFuncParam(self, ctx:logo3dParser.FuncParamContext, ):

        #l = [n for n in ctx.getChildren()]
        #n = ctx.getChildCount()

        fN = self.__funcStack[len(self.__funcStack)-1]

        param = [n.getText() for n in ctx.getChildren() 
                 if logo3dParser.IDENT == n.getSymbol().type]

        # Check if there are duplicates parameters 
        # in the procedure header
        if len(param) != len(set(param)):
            sys.exit("[ERROR]: Duplicated parameter name in a procedure header!")

        symD = {}
        for p in param:
            symD[p] = 0.0

        print(symD)

        proc = ProcL3D(fName = fN, fParam = param, fDict = symD)

        self.__funcDict[fN] = proc

        

    # Visit a parse tree produced by logo3dParser#instructions.
    def visitInstructions(self, ctx:logo3dParser.InstructionsContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # At least 1 token

        for stmt in l:
            self.visit(stmt)



    # Visit a parse tree produced by logo3dParser#stmt.
    def visitStmt(self, ctx:logo3dParser.StmtContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        # Visit single statement  
        self.visit(l[0])

    

    # Visit a parse tree produced by logo3dParser#assignation.
    def visitAssignation(self, ctx:logo3dParser.AssignationContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        #print("Num. Tokens: ", n)
        #print("=========================\n")
        #for tks in l:
        #    print("Token: ",tks.getText())
        #    print("\n", dir(tks), "\n\n")
        #print("=========================\n")       

        varName = l[0].getText()
        valueAssign = self.visit(l[2])

        # Get procedure's name from the current procedure 
        fName = self.__funcStack[len(self.__funcStack)-1]

        # Assign float read from input to the variable in the 
        # symbols dictionary
        self.__funcDict[fName].symDict[varName] = valueAssign

        #print(self.__funcDict[fName].symDict)



    # Visit a parse tree produced by logo3dParser#expr.
    def visitExpr(self, ctx:logo3dParser.ExprContext):
        
        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        #print("#Tokens: ", n)
        #print("=========================\n")
        #for tks in l:
        #    print("Token: ", tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("=========================\n")

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

        #print("#Tokens: ", n)
        #print("=========================\n")
        #for tks in l:
        #    print("Token: ", tks.getText())
        #    print("\n", dir(tks), "\n\n")
        #print("=========================\n")

        #if n == 1 and "getRuleIndex" in dir(l[0]):
        #    print("YOOOOOOOOOO: ", l[0].getText())
        #    return self.visit(l[0])

        # When there's a single token:
        # Case: Float number
        if n == 1 and logo3dParser.NUM == l[0].getSymbol().type:
            #print("\n THIS IS JUST A NUMBER: ", l[0].getText())
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

        #print("Num. Tokens: ", n)
        #print("=========================\n")
        #for tks in l:
        #    print("Token: ",tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("=========================\n")        

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

        #print("Num. Tokens: ", n)
        #print("=========================\n")
        #for tks in l:
        #    print("Token: ",tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("=========================\n") 

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

        #print("Num. Tokens: ", n)
        #print("=========================\n")
        #for tks in l:
        #    print("Token: ",tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("=========================\n")

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

        l = [n for n in ctx.getChildren()]
        #n = ctx.getChildCount()     # At least 3 tokens

        #print("Num. Tokens: ", n)
        #print("=========================\n")
        #for tks in l:
        #    print("Token: ",tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("=========================\n")

        invocName = l[0].getText()

        if self.__funcStack[0] != self.__firstProcedure:
            print("YEP!!")
            return
        
        print("Invocating...")

        # Check if the invocation name is a procedure name 
        if invocName not in self.__funcList:
            print("[ERROR]: The procedure '",invocName,"' does not exist!",sep="")
            return

        # List of the parameters tokens 
        l = [n for n in ctx.getChildren() if "getRuleIndex" in dir(n)]
        n = ctx.getChildCount()     

        #print("Num. Tokens: ", n)
        #print("----------------\n")
        #for tks in l:
        #    print("Token: ",tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("----------------\n")

        ## Get procedure's name from the current procedure 
        #fName = self.__funcStack[len(self.__funcStack)-1]

        paramList = self.__funcDict[invocName].listParam

        # Check if the number of arguments is correct 
        if len(paramList) != len(l):
            print("[ERROR]: Wrong number of parameters  of the invocation '",invocName,"'")
            return

        # List of arguments passed evaluated 
        evaluatedArgs = [self.visit(n) for n in l]
        print(evaluatedArgs)

        #if self.__funcStack[len(self.__funcStack)-1] == self.__firstProcedure:

        # Copy of the original table of symbols 
        #copyDict = dict(self.__funcDict[invocName].symDict)
        symDict = self.__funcDict[invocName].symDict

        # Assign the value of the evaluated arguments 
        # to the parameters 
        for i in range(0, len(paramList)):
            varName = paramList[i]
            argVal = evaluatedArgs[i]
            symDict[varName] = argVal
        
        print(symDict)

        #self.__funcStack.append((invocName, copyDict))
        self.__funcStack.append(invocName)

        self.visit(self.__funcDict[invocName].blockofCode)



    ##### Turtle operations 

    # Visit a parse tree produced by logo3dParser#color.
    def visitColor(self, ctx:logo3dParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#home.
    def visitHome(self, ctx:logo3dParser.HomeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#show.
    def visitShow(self, ctx:logo3dParser.ShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#hide.
    def visitHide(self, ctx:logo3dParser.HideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#forward.
    def visitForward(self, ctx:logo3dParser.ForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#backward.
    def visitBackward(self, ctx:logo3dParser.BackwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#up.
    def visitUp(self, ctx:logo3dParser.UpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#down.
    def visitDown(self, ctx:logo3dParser.DownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#left.
    def visitLeft(self, ctx:logo3dParser.LeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#right.
    def visitRight(self, ctx:logo3dParser.RightContext):
        return self.visitChildren(ctx)



 

