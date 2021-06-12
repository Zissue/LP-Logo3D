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
                 alphaI = -90,
                 betaI = 0,
                 radiusI = 0.5,
                 opactityI = 1, 
                 debug = False):
        
        self.__myColor = colorI
        
        self.__originPoint = originI
        self.__position = originI
        
        self.__alpha = alphaI
        self.__beta = 0
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
        self.__alpha = angle

        self.__turtle.pos.x = math.cos(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.z = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.y = math.sin(self.__beta)
        #self.__update()
        

    def right(self, angle):
        self.__alpha = -angle

        self.__turtle.pos.x = math.cos(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.z = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.y = math.sin(self.__beta)
        #self.__update()
        

    def up(self, angle):
        self.__beta = angle

        self.__turtle.pos.x = math.cos(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.z = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.y = math.sin(self.__beta)
        #self.__update()

        

    def down(self, angle):
        self.__beta = -angle

        self.__turtle.pos.x = math.cos(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.z = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__turtle.pos.y = math.sin(self.__beta)
        #self.__update()
        

    def forward(self, inc):
        #self.__position.
        self.__update()
        

    def backward(self, inc):
        self.__update()
        

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

    def setColor(self, color):
        self.__myColor = color
        self.__update()

    def setOriginPoint(self, point):
        self.__originPoint = point
        self.__update()

    def setX(self, x):
        self.__position.x = x
        self.__update()



########################



turtle = Turtle3D(debug=True)

d = 0.05
#turtle.left(-90)
while True:
    #if turtle.x() > 10 or turtle.x() < 0:
    #    d = -d

    #if turtle.x() > 4 and turtle.x() < 8:
    #    turtle.hidePaint()
    #else:
    #    turtle.showPaint()
    if turtle.x() >= 5: 
        print("\n\nYA LLEGUE\n\n")
        turtle.backHome()
    
    print(turtle.x())
    turtle.setX(turtle.x() + d)
    #turtle.left(90)
    rate(60)

# posa una esfera roja 
#bola = sphere(pos=vector(0, 0, 0), radius=0.5, make_trail=False, color=color.red)

# mou la bola continuament 
#d = 0.1
#while True:
#    # si arriba als límits, canvia de direcció 
#    if bola.pos.x > 10 or bola.pos.x < 0:
#        d = -d
#
#    # canvia posició 
#    bola.pos.x += d
#    if bola.pos.x >= 5 and bola.pos.x <=8:
#        rad = 1
#        bola.make_trail=True
#    else:
#        rad = 0
#        bola.make_trail=False
#    #sphere(pos=vector(bola.pos.x, bola.pos.y, bola.pos.z), radius=0.3, make_trail=True, color=color.red)
#
#    rate(5)


