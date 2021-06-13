###################################### 
###################################### 
### Author: Zixuan Sun 
### [LP] 2020-2021 - Q2 - Logo3D 
### Group: 22 L
###################################### 
###################################### 

from vpython import *
import math

######################################


class Turtle3D:

    '''
    Aquesta classe es l'API de la clase de Turtle3D
    per treballar amb la llibreria "vpython" 
    '''

    #   Atributs estatics 

    # parametres de l'escena 
    scene.height = 1000
    scene.width = 1000

    scene.autocenter = True
    scene.caption = """\nTo rotate "camera", drag with right button or Ctrl-drag.\nTo zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.\nOn a two-button mouse, middle is left + right.\nTo pan left/right and up/down, Shift-drag.\nTouch screen: pinch/extend to zoom, swipe or two-finger rotate.\n"""


    #   Constructors
    
    def __init__(self, 
                 colorI = color.red, 
                 originI = vector(0,0,0), 
                 alphaI = 0,
                 betaI = 0,
                 radiusI = 0.17,
                 opactityI = 1, 
                 debug = False):

        '''
        Constructor de la classe Turtle3D, amb els seguents
        atributs privats:
        - color de quan es pinta
        - punt d'origen, per el home()
        - angles alfa i beta, per definir el vector
        de direccio
        - radi del cilindre i l'esfera
        - opacitat, per el show() i hide()
        - instancia de tipus esfera, per pintar la posició 
        actual
        '''

        
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
        
        # NOTA: Utilitzar el parametre debug com True per veure els eixos de 
        # coordenades
        if debug:
            # posa els eixos de coordenades blancs 
            cylinder(pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.1, color=color.white)
            cylinder(pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.1, color=color.white)
            cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.1, color=color.white)



    #   Operacions privades
    
    def __update(self):
        '''
        Actualitza els parametres de la tortuga
        amb correspondencia dels atributs
        '''
        self.__turtle.pos = self.__position
        self.__turtle.radius = self.__radius
        self.__turtle.opactity = self.__opacity
        self.__turtle.color = self.__myColor


    # Operacions publiques

    def left(self, angle):
        '''
        Donat un angle en graus, calcula el nou vector
        de la direccio amb un gir cap a l'esquerra
        '''
        self.__alpha += math.radians(-angle)
        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__facingDir = vector(newx, newy, newz)
        

    def right(self, angle):
        '''
        Donat un angle en graus, calcula el nou vector
        de la direccio amb un gir cap a la dreta
        '''
        self.__alpha += math.radians(angle)
        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__facingDir = vector(newx, newy, newz)
        

    def up(self, angle):
        '''
        Donat un angle en graus, calcula el nou vector
        de la direccio amb un gir cap a d'alt
        '''
        self.__beta += math.radians(angle)
        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__facingDir = vector(newx, newy, newz)
    

    def down(self, angle):
        '''
        Donat un angle en graus, calcula el nou vector
        de la direccio amb un gir cap a baix
        '''
        self.__beta += math.radians(-angle)
        newx = math.cos(self.__alpha)*math.cos(self.__beta)
        newy = math.sin(self.__beta)
        newz = math.sin(self.__alpha)*math.cos(self.__beta)
        self.__facingDir = vector(newx, newy, newz)
        

    def forward(self, incre):
        '''
        Donat un desplacament cap endavant, pintem el desplacament 
        (un cilindre) desde la posicio actual fins a la final amb 
        dos esferes als extrems
        '''
        currPos = self.__position
        v = self.__facingDir
        incPos = vector(incre*v.x, incre*v.y, incre*v.z)

        cylinder(pos=currPos, axis=incPos, radius=self.__radius*0.85, color=self.__myColor, opacity=self.__opacity)

        sphere(pos=currPos, radius=self.__radius*0.85, color=self.__myColor, opacity=self.__opacity)
        sphere(pos=currPos+incPos, radius=self.__radius*0.85, color=self.__myColor, opacity=self.__opacity)

        self.__position = currPos+incPos
        self.__update()
        

    def backward(self, incre):
        '''
        Donat un desplacament cap enrere, pintem el desplacament 
        (un cilindre) desde la posicio actual fins a la final amb 
        dos esferes als extrems
        '''
        currPos = self.__position
        v = self.__facingDir
        incPos = vector(-incre*v.x, -incre*v.y, -incre*v.z)

        cylinder(pos=currPos, axis=incPos, radius=self.__radius*0.85, color=self.__myColor, opacity=self.__opacity)

        sphere(pos=currPos, radius=self.__radius*0.85, color=self.__myColor, opacity=self.__opacity)
        sphere(pos=currPos+incPos, radius=self.__radius*0.85, color=self.__myColor, opacity=self.__opacity)

        self.__position = currPos+incPos
        self.__update()
        

    def hide(self):
        '''
        Metode per deixar de pintar
        '''
        self.__opacity = 0
        self.__update()
        
    def show(self):
        '''
        Metode per tornar a pintar
        '''
        self.__opacity = 1
        self.__update()

    def home(self):
        '''
        Metode per moure la tortuga a la posicio
        d'origen
        '''
        self.__position = self.__originPoint
        self.__update()        

    def x(self):
        '''
        Retorna la component X de la posicio actual
        de la tortuga
        '''
        return self.__position.x

    def y(self):
        '''
        Retorna la component Y de la posicio actual
        de la tortuga
        '''
        return self.__position.y

    def z(self):
        '''
        Retorna la component Z de la posicio actual
        de la tortuga
        '''
        return self.__position.z

    def color(self, r, g, b):
        '''
        Donat 3 components r,g,b amb
        rang de [0-1], cambiem el color el qual 
        utilitzarem per pintar
        '''
        self.__myColor = vector(r,g,b)
        self.__update()

    def setOriginPoint(self, x, y, z):
        '''
        Cambiem el punt d'origen
        '''
        self.__originPoint = vector(x,y,z)

    def setX(self, x):
        '''
        Cambiem la component X de la posicio actual
        de la tortuga
        '''
        self.__position.x = x
        self.__update()

    def setY(self, y):
        '''
        Cambiem la component X de la posicio actual
        de la tortuga
        '''
        self.__position.y = y
        self.__update()

    def setZ(self, z):
        '''
        Cambiem la component X de la posicio actual
        de la tortuga
        '''
        self.__position.z = z
        self.__update()

    def setRadius(self, r):
        '''
        Cambiem el radi del cilindre, i les esferes
        de la tortuga
        '''
        self.__radius = r
        self.__update()