# LP - *Logo3D* Project

This is my Compiler project for the "Programming Languages" course, *2020-2021 Q2*.

You can find the original assignment in [this](https://github.com/jordi-petit/lp-logo3d-2021) other GitHub repository.

## Overview

**Logo3D** is an interpreter for a 3D turtle graphics programming language. It extends the classic Logo/Turtle graphics to three dimensions, allowing you to create beautiful 3D drawings and animations using simple commands. The interpreter is built using ANTLR4 for parsing and VPython for 3D visualization.

## Features

- **3D Turtle Graphics**: Control a 3D turtle to draw in three-dimensional space
- **Movement Commands**: `forward()`, `backward()` for linear movement
- **Rotation Commands**: `left()`, `right()` for horizontal rotation, `up()`, `down()` for vertical rotation
- **Visual Control**: `show()`, `hide()`, `color()`, `home()` for display management
- **Programming Constructs**: Variables, procedures, conditionals (`IF-THEN-ELSE`), loops (`FOR`, `WHILE`)
- **I/O Operations**: Read input (`>>`) and write output (`<<`)
- **Arithmetic & Logic**: Full support for arithmetic and boolean expressions

## Examples

### Example 1: 3D Spiral

This program creates a 3D spiral by drawing circles at increasing heights:

```logo3d
PROC cercle(mida, costats) IS
    FOR i FROM 1 TO costats DO
        forward(mida)
        left(360 / costats)
    END
END

PROC espiral(cercles) IS
    IF cercles > 0 THEN
        cercle(1, 12)
        up(5)
        espiral(cercles - 1)
    END
END

PROC main() IS
    espiral(5)
END
```

**What it does**: This creates a 3D spiral with 5 circles stacked vertically, each circle made of 12 segments. The turtle rotates around and moves upward, creating a spring-like structure in 3D space.

Run it with:
```bash
python3 logo3d.py inputs_tests/espiral.l3d
```

### Example 2: 3D Cube

This program draws a cube using turtle graphics:

```logo3d
PROC square(size) IS
    FOR i FROM 1 TO 4 DO
        forward(size)
        left(90)
    END
END

PROC cube(size) IS
    square(size)           // Draw bottom square
    up(90)
    forward(size)
    down(90)
    square(size)           // Draw top square
    // ... (connect with vertical edges)
END

PROC main() IS
    color(0.2, 0.8, 1.0)  // Cyan color
    cube(5)
END
```

**What it does**: Creates a 3D cube by drawing two squares (top and bottom) and connecting them with vertical edges. The turtle navigates in 3D space using `up()` and `down()` commands to change elevation while drawing.

Run it with:
```bash
python3 logo3d.py inputs_tests/cube.l3d
```

### Example 3: Pyramid

```logo3d
PROC triangle(size) IS
    FOR i FROM 1 TO 3 DO
        forward(size)
        left(120)
    END
END

PROC pyramid(levels) IS
    IF levels > 0 THEN
        triangle(levels * 2)
        up(30)
        forward(1)
        down(30)
        pyramid(levels - 1)
    END
END

PROC main() IS
    color(1.0, 0.8, 0.2)  // Golden color
    pyramid(8)
END
```

**What it does**: Creates a pyramid structure by recursively drawing triangles of decreasing size while moving upward. Each level is slightly tilted and smaller, creating a stepped pyramid effect.

Run it with:
```bash
python3 logo3d.py inputs_tests/pyramid.l3d
```

### Example 4: Basic Turtle Commands

```logo3d
PROC main() IS
    color(1, 0.4, 0.2)  // Set color to orange
    home()               // Return to origin
    show()               // Make drawing visible
    forward(10)          // Move forward 10 units
    left(90)             // Turn left 90 degrees
    up(45)               // Tilt up 45 degrees
    forward(10)          // Move forward in 3D space
END
```

**What it does**: Demonstrates basic turtle commands by drawing an L-shaped path in 3D space. The turtle starts horizontally, turns left, tilts upward, and continues, creating a three-dimensional corner.

Run it with:
```bash
python3 logo3d.py inputs_tests/turtle.l3d
```

## Visual Examples

When you run these programs, VPython opens an interactive 3D window where you can:
- **Rotate the view**: Drag with right mouse button or Ctrl-drag
- **Zoom**: Use scroll wheel or drag with middle button
- **Pan**: Shift-drag to move the view around

The turtle draws colored lines in 3D space as it moves, creating beautiful geometric patterns and structures. Each program generates a different 3D shape or pattern that you can view from any angle.

### Screenshot Gallery

Screenshots of the example programs can be found in the `images/` directory. To generate your own screenshots:

1. Run a Logo3D program
2. Position the 3D view to your preference in the VPython window
3. Capture the screen using your system's screenshot tool

See `images/README.md` for more details on the expected visual outputs.

## Files

- `requirements.txt`: contains the libraries required for the project.
- `README.md`: this file documents the project.
- `logo3d.py`: contains the main program for the interpreter.
- `logo3d.g`: contains the grammar for the **Logo3D** programming language.
- `visitor.py`: contains the *AST* visitor.
  
  *Note: This class INHERITS from the template class created by the ANTLR4 compiler. Therefore, it's necessary to compile the grammar with the **-visitor** flag. This means running:* `antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g`

- `turtle3d.py`: contains the *Turtle3D* class for drawing with the `vpython` library.
- `inputs_tests/`: directory containing example Logo3D programs for testing.

## Installation

1. Install the required *Python* libraries from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. [Install](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation) `antlr4`.

3. Compile the `logo3d.g` grammar with the *-visitor* flag to generate `logo3dVisitor.py`:
   ```bash
   antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g
   ```

## Execution

To run the project, use the following command:

```bash
python3 logo3d.py programa.l3d
```

This command starts execution from the `main()` procedure. If `main()` is not defined, an error will occur.

You can also start execution from a different procedure than `main()`:

```bash
python3 logo3d.py programa.l3d procedure_name [parameters]
```

The parameter list can be empty, or they must be integers or floats. For example:

```bash
python3 logo3d.py inputs_tests/espiral.l3d espiral 5
```

*Note that `programa.l3d` can be any program written in Logo3D.*

## Language Reference

### Turtle Commands

- `forward(distance)` - Move the turtle forward by the specified distance
- `backward(distance)` - Move the turtle backward by the specified distance
- `left(degrees)` - Rotate the turtle left (counterclockwise) by the specified degrees
- `right(degrees)` - Rotate the turtle right (clockwise) by the specified degrees
- `up(degrees)` - Tilt the turtle up by the specified degrees
- `down(degrees)` - Tilt the turtle down by the specified degrees
- `color(r, g, b)` - Set the drawing color (RGB values from 0 to 1)
- `show()` - Make the turtle and its trail visible
- `hide()` - Make the turtle and its trail invisible
- `home()` - Return the turtle to the origin position

### Control Structures

- `IF condition THEN ... END`
- `IF condition THEN ... ELSE ... END`
- `WHILE condition DO ... END`
- `FOR variable FROM start TO end DO ... END`

### I/O Operations

- `>> variable` - Read input into a variable
- `<< expression` - Write output


---

# LP - Pràctica *Logo3D*

Aquest és el meu projecte de Compiladors de l'asignatura de "Llenguatges de Programació" del curs *2020-2021 Q2*.

Podeu trobar l'enunciat original en [aquest](https://github.com/jordi-petit/lp-logo3d-2021) altre repositori de GitHub.

## Resum

**Logo3D** és un intèrpret per a un llenguatge de programació de gràfics tortuga 3D. Estén el clàssic Logo/Turtle graphics a tres dimensions, permetent crear dibuixos i animacions 3D boniques utilitzant comandes simples. L'intèrpret està construït utilitzant ANTLR4 per a l'anàlisi sintàctic i VPython per a la visualització 3D.

## Característiques

- **Gràfics Tortuga 3D**: Controla una tortuga 3D per dibuixar en espai tridimensional
- **Comandes de Moviment**: `forward()`, `backward()` per moviment lineal
- **Comandes de Rotació**: `left()`, `right()` per rotació horitzontal, `up()`, `down()` per rotació vertical
- **Control Visual**: `show()`, `hide()`, `color()`, `home()` per gestió de visualització
- **Construccions de Programació**: Variables, procediments, condicionals (`IF-THEN-ELSE`), bucles (`FOR`, `WHILE`)
- **Operacions I/O**: Llegir entrada (`>>`) i escriure sortida (`<<`)
- **Aritmètica i Lògica**: Suport complet per expressions aritmètiques i booleanes

## Exemples

### Exemple 1: Espiral 3D

Aquest programa crea una espiral 3D dibuixant cercles a altades creixents:

```logo3d
PROC cercle(mida, costats) IS
    FOR i FROM 1 TO costats DO
        forward(mida)
        left(360 / costats)
    END
END

PROC espiral(cercles) IS
    IF cercles > 0 THEN
        cercle(1, 12)
        up(5)
        espiral(cercles - 1)
    END
END

PROC main() IS
    espiral(5)
END
```

**Què fa**: Això crea una espiral 3D amb 5 cercles apilats verticalment, cada cercle fet de 12 segments. La tortuga rota al voltant i es mou cap amunt, creant una estructura tipus molla en espai 3D.

Executa'l amb:
```bash
python3 logo3d.py inputs_tests/espiral.l3d
```

### Exemple 2: Cub 3D

Aquest programa dibuixa un cub utilitzant gràfics tortuga:

```logo3d
PROC square(size) IS
    FOR i FROM 1 TO 4 DO
        forward(size)
        left(90)
    END
END

PROC cube(size) IS
    square(size)           // Dibuixar quadrat inferior
    up(90)
    forward(size)
    down(90)
    square(size)           // Dibuixar quadrat superior
    // ... (connectar amb arestes verticals)
END

PROC main() IS
    color(0.2, 0.8, 1.0)  // Color cian
    cube(5)
END
```

**Què fa**: Crea un cub 3D dibuixant dos quadrats (superior i inferior) i connectant-los amb arestes verticals. La tortuga navega en espai 3D utilitzant les comandes `up()` i `down()` per canviar l'elevació mentre dibuixa.

Executa'l amb:
```bash
python3 logo3d.py inputs_tests/cube.l3d
```

### Exemple 3: Piràmide

```logo3d
PROC triangle(size) IS
    FOR i FROM 1 TO 3 DO
        forward(size)
        left(120)
    END
END

PROC pyramid(levels) IS
    IF levels > 0 THEN
        triangle(levels * 2)
        up(30)
        forward(1)
        down(30)
        pyramid(levels - 1)
    END
END

PROC main() IS
    color(1.0, 0.8, 0.2)  // Color daurat
    pyramid(8)
END
```

**Què fa**: Crea una estructura piramidal dibuixant recursivament triangles de mida decreixent mentre es mou cap amunt. Cada nivell està lleugerament inclinat i és més petit, creant un efecte de piràmide escalonada.

Executa'l amb:
```bash
python3 logo3d.py inputs_tests/pyramid.l3d
```

### Exemple 4: Comandes Bàsiques de Tortuga

```logo3d
PROC main() IS
    color(1, 0.4, 0.2)  // Establir color a taronja
    home()               // Tornar a l'origen
    show()               // Fer visible el dibuix
    forward(10)          // Moure endavant 10 unitats
    left(90)             // Girar a l'esquerra 90 graus
    up(45)               // Inclinar cap amunt 45 graus
    forward(10)          // Moure endavant en espai 3D
END
```

**Què fa**: Demostra les comandes bàsiques de la tortuga dibuixant un camí en forma d'L en espai 3D. La tortuga comença horitzontalment, gira a l'esquerra, s'inclina cap amunt i continua, creant un racó tridimensional.

Executa'l amb:
```bash
python3 logo3d.py inputs_tests/turtle.l3d
```

## Exemples Visuals

Quan executeu aquests programes, VPython obre una finestra 3D interactiva on podeu:
- **Rotar la vista**: Arrossegueu amb el botó dret del ratolí o Ctrl-arrossegueu
- **Zoom**: Utilitzeu la roda de desplaçament o arrossegueu amb el botó del mig
- **Panoràmica**: Shift-arrossegueu per moure la vista

La tortuga dibuixa línies de colors en espai 3D mentre es mou, creant patrons i estructures geomètriques boniques. Cada programa genera una forma o patró 3D diferent que podeu veure des de qualsevol angle.

### Galeria de Captures de Pantalla

Les captures de pantalla dels programes d'exemple es poden trobar al directori `images/`. Per generar les vostres pròpies captures de pantalla:

1. Executeu un programa Logo3D
2. Posicioneu la vista 3D a la vostra preferència a la finestra VPython
3. Captureu la pantalla utilitzant l'eina de captura de pantalla del vostre sistema

Consulteu `images/README.md` per a més detalls sobre les sortides visuals esperades.

## Arxius

- `requirements.txt`: conté les llibreries requerides pel projecte.
- `README.md`: aquest fitxer que documenta el projecte.
- `logo3d.py`: conté el programa principal de l'intèrpret.
- `logo3d.g`: conté la gramàtica pel llenguatge de programació **Logo3D**.
- `visitor.py`: conté el visitador de l'*AST*.
  
  *Atenció: aquesta classe HEREDA de la classe plantilla creada pel compilador de ANTLR4. Per tant, és necessari compilar la gramàtica amb el flag **-visitor**. És a dir:* `antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g`

- `turtle3d.py`: conté la classe *Turtle3D* per pintar amb ajuda de la llibreria `vpython`.
- `inputs_tests/`: directori que conté programes Logo3D d'exemple per a proves.

## Instal·lació 

1. Instal·lar les llibreries de *Python* requerides del fitxer `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. [Instal·lar](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation) `antlr4`.

3. Compilar la gramàtica `logo3d.g` amb el flag *-visitor* per generar `logo3dVisitor.py`:
   ```bash
   antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g
   ```

## Execució

Per executar el projecte, utilitzeu la comanda següent:

```bash
python3 logo3d.py programa.l3d
```

Aquesta comanda comença a executar des del procediment `main()`. Si no està definit aquest procediment, donarà error.

També es pot començar a executar des d'un altre procediment diferent al `main()`:

```bash
python3 logo3d.py programa.l3d nom_procediment [parametres]
```

La llista de paràmetres pot ser buida, o han de ser enters o *floats*. Per exemple:

```bash
python3 logo3d.py inputs_tests/espiral.l3d espiral 5
```

*Cal notar que `programa.l3d` pot ser qualsevol programa escrit en Logo3D*.

## Referència del Llenguatge

### Comandes de Tortuga

- `forward(distancia)` - Moure la tortuga endavant per la distància especificada
- `backward(distancia)` - Moure la tortuga enrere per la distància especificada
- `left(graus)` - Rotar la tortuga a l'esquerra (antihorari) pels graus especificats
- `right(graus)` - Rotar la tortuga a la dreta (horari) pels graus especificats
- `up(graus)` - Inclinar la tortuga cap amunt pels graus especificats
- `down(graus)` - Inclinar la tortuga cap avall pels graus especificats
- `color(r, g, b)` - Establir el color de dibuix (valors RGB de 0 a 1)
- `show()` - Fer visible la tortuga i el seu rastre
- `hide()` - Fer invisible la tortuga i el seu rastre
- `home()` - Retornar la tortuga a la posició d'origen

### Estructures de Control

- `IF condicio THEN ... END`
- `IF condicio THEN ... ELSE ... END`
- `WHILE condicio DO ... END`
- `FOR variable FROM inici TO final DO ... END`

### Operacions I/O

- `>> variable` - Llegir entrada en una variable
- `<< expressio` - Escriure sortida
