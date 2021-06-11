if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
    from .logo3dVisitor import logo3dVisitor
else:
    from logo3dParser import logo3dParser
    from logo3dVisitor import logo3dVisitor

class TreeVisitor(logo3dVisitor):
    def __init__(self):
        self.nivell = 0

    def visitlogo3d(self, ctx):
            return self.visitChildren(ctx)
del logo3dParser

