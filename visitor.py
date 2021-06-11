if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
    from .logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor

class TreeVisitor(logo3dVisitor):

    # Class atributes
    def __init__(self):
        self.nivell = 0

    # Visit root 
    def visit(self, ctx):
        print("\n\nCalled visit() method:\n")

        self.nivell += 1
        self.visitlogo3d(ctx)
        self.nivell -= 1


        print("\nEND of visit() method\n\n")

    def visitlogo3d(self, ctx):

        #print("==============================================")
        #print(dir(ctx))

        if 'getSymbol' in dir(ctx):
            print(" - " * self.nivell + logo3dParser.symbolicNames[ctx.getSymbol().type])

        if 'getChildren' in dir(ctx):

            l = list(ctx.getChildren())

            for obj in l:
                print(" - " * self.nivell + obj.getText())

            self.nivell += 1
            for obj in l:
                self.visitlogo3d(obj)
            self.nivell -= 1


    # Visit a parse tree produced by logo3dParser#proceD.
    def visitProceD(self, ctx:logo3dParser.ProceDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#stmt.
    def visitStmt(self, ctx:logo3dParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#assignation.
    def visitAssignation(self, ctx:logo3dParser.AssignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#expr.
    def visitExpr(self, ctx:logo3dParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#numExpr.
    def visitNumExpr(self, ctx:logo3dParser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#read.
    def visitRead(self, ctx:logo3dParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#write.
    def visitWrite(self, ctx:logo3dParser.WriteContext):
        return self.visitChildren(ctx)


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
 

