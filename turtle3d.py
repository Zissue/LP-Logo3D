from vpython import *

# paràmetres de l'escena
scene.height = scene.width = 1000
scene.autocenter = True
scene.caption = """\nTo rotate "camera", drag with right button or Ctrl-drag.\nTo zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.\n  On a two-button mouse, middle is left + right.\nTo pan left/right and up/down, Shift-drag.\nTouch screen: pinch/extend to zoom, swipe or two-finger rotate.\n"""

# posa els eixos de coordenades blancs
cylinder(pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.1, color=color.white)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.1, color=color.white)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.1, color=color.white)

# posa una esfera roja
bola = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.red)

# mou la bola continuament
d = 0.1
while True:
    # si arriba als límits, canvia de direcció
    if bola.pos.x > 10 or bola.pos.x < 0:
        d = -d
    # canvia posició
    bola.pos.x += d
    rate(60)
