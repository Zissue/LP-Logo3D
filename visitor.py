import sys
if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
    from .logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor

#################################

class ProcL3D:

    def __init__(self, fName = "", fParam = [], fDict = {}):
        self.funcName = fName
        self.listParam = fParam
        self.symDict = fDict

#################################

class TreeVisitor(logo3dVisitor):

    # Class atributes
    def __init__(self):
        self.__nivell = 1
        self.__funcStack = []
        self.__funcDict = {}


    # Visit root 
    def visitRoot(self, ctx):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        #print("=========================\n")
        #for tks in l:
        #    print(tks.getText())
        #print("=========================\n")

        if n <= 1:
            print("\n[WARNING]: No procedures (PROC) in this Logo3D program...\n")
        else:
            l.pop()     # removes <EOF> token   
            for procedure in l:
                #print(" - " * self.__nivell + procedure.getText())
                self.__nivell += 1
                self.visit(procedure)
                self.__nivell -= 1

        print("\n")

        print(self.__funcDict)
        

    # Visit a parse tree produced by logo3dParser#proceD.
    def visitProceD(self, ctx:logo3dParser.ProceDContext):
        
        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        #print("=========================\n")
        #for tks in l:
        #    print(tks.getText())
        #    #print("\n", dir(tks), "\n\n")
        #print("=========================\n")
        
        if len(l) != 3:
           sys.exit("[ERROR]: Bad procedure declaration...")
            
        symDict = {}

        # Visit function header 
        self.visit(l[0])

        # Visit function body
        self.visit(l[1])

        
        #rules = [n for n in ctx.getChildren() if "getRuleIndex" in dir(n)]
        #for tks in list(ctx.getChildren()):

        #    print(tks.getText())
        #    #if logo3dParser.IDENT
        #    #print(dir(tks))
        #    #print(logo3dParser.symbolicNames[tks.getSymbol().type])


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

        if fName not in self.__funcStack:
            self.__funcStack.append(fName)
            #print("My function name: ", fName)
        else:
            sys.exit("[ERROR]: Procedure name duplicated!")
        
        # Visit functions parameters 
        self.visit(l[3])



    # Visit a parse tree produced by logo3dParser#funcParam.
    def visitFuncParam(self, ctx:logo3dParser.FuncParamContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        fN = self.__funcStack[len(self.__funcStack)-1]

        param = [n.getText() for n in ctx.getChildren() 
                 if logo3dParser.IDENT == n.getSymbol().type]

        symD = {}
        for p in param:
            symD[p] = 0.0

        print(symD)

        proc = ProcL3D(fName = fN, fParam = param, fDict = symD)

        self.__funcDict[fN] = proc

        

    # Visit a parse tree produced by logo3dParser#funcBody.
    def visitFuncBody(self, ctx:logo3dParser.FuncBodyContext):

        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()

        print("=========================\n")
        for tks in l:
            print(tks.getText())
            #print("\n", dir(tks), "\n\n")
        print("=========================\n")

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
       return 




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
            # Recursive case 
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

            # Case: numExpr * numExpr
            if logo3dParser.DIV == l[1].getSymbol().type:
                denom = self.visit(l[2])
                if denom == 0:
                    sys.exit("[ERROR]: Float division by ZERO!")
                return float(self.visit(l[0]) / denom)

            # Case: numExpr * numExpr
            if logo3dParser.ADD == l[1].getSymbol().type:
                return float(self.visit(l[0]) + self.visit(l[2]))

            # Case: numExpr * numExpr
            if logo3dParser.SUB == l[1].getSymbol().type:
                return float(self.visit(l[0]) - self.visit(l[2]))



    # Visit a parse tree produced by logo3dParser#read.
    def visitRead(self, ctx:logo3dParser.ReadContext):


        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#write.
    def visitWrite(self, ctx:logo3dParser.WriteContext):
        
        l = [n for n in ctx.getChildren()]
        n = ctx.getChildCount()     # Always size 2 

        # Visit the expresion first and the print the result returned 
        print("\n[WRITE] ", self.visit(l[1]), " << ", l[1].getText())



    # Visit a parse tree produced by logo3dParser#conditional.
    def visitConditional(self, ctx:logo3dParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#while_it.
    def visitWhile_it(self, ctx:logo3dParser.While_itContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#for_it.
    def visitFor_it(self, ctx:logo3dParser.For_itContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#invocation.
    def visitInvocation(self, ctx:logo3dParser.InvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#argsPassed.
    def visitArgsPassed(self, ctx:logo3dParser.ArgsPassedContext):
        return self.visitChildren(ctx)


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



 

