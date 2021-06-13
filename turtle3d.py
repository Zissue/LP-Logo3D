from vpython import *
import math


class Turtle3D:

    '''
    Aquesta classe es l'API de la clase de Turtle3D 🐢
    per treballar amb la llibreria "vpython" 
    '''

    #   Atributs estatics 

        # paràmetres de l'escena 
    scene.height = 1000
    scene.width = 1000
    scene.autocenter = True
    scene.caption = """\nTo rotate "camera", drag with right button or Ctrl-drag.\nTo zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.\nOn a two-button mouse, middle is left + right.\nTo pan left/right and up/down, Shift-drag.\nTouch screen: pinch/extend to zoom, swipe or two-finger rotate.\n"""

    #   Metodes estatics (amb @staticmethod) 



    #   Constructors
    
    def __init__(self, 
                 colorI = color.red, 
                 originI = vector(0,0,0), 
                 alphaI = 0,
                 betaI = 0,
                 radiusI = 0.5,
                 opactityI = 1, 
                 debug = False):
        
        self.__myColor = colorI
        
        self.__originPoint = originI
        self.__position = originI
        
        self.__alpha = math.radians(alphaI)
        self.__beta = math.radians(betaI)
        self.__facingDir = vector(math.cos(self.__alpha)*math.cos(self.__beta),
                                  math.sin(self.__beta),
                                  math.sin(self.__alpha)*math.cos(self.__beta))
        
        self.__radius = radiusI
        self.__opacity = opactityI

        self.__turtle = sphere(pos=self.__position,
                               radius=self.__radius,
                               opactity=self.__opacity,
                               color=self.__myColor)
        if debug:
            # posa els eixos de coordenades blancs 
            cylinder(pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.1, color=color.white)
            cylinder(pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.1, color=color.white)
            cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.1, color=color.white)



    #   Operacions privades
    
    def __update(self):
        self.__turtle.pos = self.__position
        self.__turtle.radius = self.__radius
        self.__turtle.opactity = self.__opacity
        self.__turtle.color = self.__myColor


    # Operacions publiques

    def left(self, angle):
        self.__alpha += math.radians(-angle)

        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)

        self.__facingDir = vector(newx, newy, newz)

        #self.__update()
        

    def right(self, angle):
        self.__alpha += math.radians(angle)

        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)

        self.__facingDir = vector(newx, newy, newz)
        #self.__update()
        

    def up(self, angle):
        self.__beta += math.radians(angle)
        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)

        self.__facingDir = vector(newx, newy, newz)
        #self.__update()

        

    def down(self, angle):
        self.__beta += math.radians(-angle)
        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)

        self.__facingDir = vector(newx, newy, newz)
        #self.__update()
        

    def forward(self, incre):
        currPos = self.__position
        v = self.__facingDir
        newPos = vector(incre*v.x, incre*v.y, incre*v.z)
        sphere(pos=currPos, radius=0.2, color=self.__myColor)
        cylinder(pos=currPos, axis=newPos, radius=0.2, color=self.__myColor)
        sphere(pos=currPos+newPos, radius=0.2, color=self.__myColor)
        self.__position = currPos+newPos
        self.__turtle.pos = currPos+newPos
        #self.__update()
        

    def backward(self, incre):
        currPos = self.__position
        v = self.__facingDir
        newPos = vector(-incre*v.x, -incre*v.y, -incre*v.z)
        sphere(pos=currPos, radius=0.2, color=self.__myColor)
        cylinder(pos=currPos, axis=newPos, radius=0.2, color=self.__myColor)
        sphere(pos=currPos+newPos, radius=0.2, color=self.__myColor)
        self.__position = currPos+newPos
        self.__turtle.pos = currPos+newPos
        #self.__update()
        

    def hidePaint(self):
        self.__opacity = 0
        self.__update()
        

    def showPaint(self):
        self.__opacity = 1
        self.__update()
        

    def backHome(self):
        self.__position = self.__originPoint
        self.__turtle.pos = self.__position
        self.__turtle = sphere(pos=self.__position,
                               radius=self.__radius,
                               opactity=self.__opacity,
                               color=self.__myColor)        

    def x(self):
        return self.__position.x

    def y(self):
        return self.__position.y

    def z(self):
        return self.__position.z

    def color(self, r, g, b):
        self.__myColor = vector(r,g,b)
        self.__update()

    def setOriginPoint(self, point):
        self.__originPoint = point
        self.__update()

    def setX(self, x):
        self.__position.x = x
        self.__update()



########################



turtle = Turtle3D(debug=True)

for i in range(4):
    turtle.forward(10)
    turtle.right(90)





