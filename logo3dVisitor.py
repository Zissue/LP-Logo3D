# Generated from logo3d.g by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
else:
    from logo3dParser import logo3dParser

# This class defines a complete generic visitor for a parse tree produced by logo3dParser.

class logo3dVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by logo3dParser#root.
    def visitRoot(self, ctx:logo3dParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#proceD.
    def visitProceD(self, ctx:logo3dParser.ProceDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#funcName.
    def visitFuncName(self, ctx:logo3dParser.FuncNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#funcParam.
    def visitFuncParam(self, ctx:logo3dParser.FuncParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#funcBody.
    def visitFuncBody(self, ctx:logo3dParser.FuncBodyContext):
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



del logo3dParser