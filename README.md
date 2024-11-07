# LP - *Logo3D* Project

This is my Compiler project for the "Programming Languages" course, *2020-2021 Q2*.

You can find the original assignment in [this](https://github.com/jordi-petit/lp-logo3d-2021) other GitHub repository.


# Files

- `requirements.txt`: contains the libraries required for the project.

- `README.md`: this file documents the project.

- `logo3d.py`: contains the main program for the interpreter.

- `logo3d.g`: contains the grammar for the **Logo3D** programming language.

- `visitor.py`: contains the *AST* visitor.
  
  -- *Note: This class INHERITS from the template class created by the ANTLR4 compiler. Therefore, it's necessary to compile the grammar with the **-visitor** flag. This means running:* `antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g`

- `turtle3d.py`: contains the *Turtle3D* class for drawing with the `vpython` library.


# Installation

1. Install the required *Python* libraries from `requirements.txt`.

2. [Install](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation) `antlr4`.

3. Compile the `logo3d.g` grammar with the *-visitor* flag to generate `logo3dVisitor.py`. This can be done with the command:
   `antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g` 


# Execution

To run the project, use the following command:

- `python3 logo3d.py programa.l3d`: this command starts execution from the `main()` procedure. If `main()` is not defined, an error will occur.

- You can also start execution from a different procedure than `main()` using:
  `python3 logo3d.py programa.l3d procedure_name [parameters]`. The parameter list can be empty, or they must be integers or floats. For example: `python3 logo3d.py prog_espiral.l3d espiral 5`.

*Note that `programa.l3d` can be any program written in Logo3D.*


---

# LP - Pràctica *Logo3D*

Aquest és el meu projecte de Compiladors de l'asignatura de "Llenguatges de Programació" del curs *2020-2021 Q2*.

Podeu trobar l'enunciat original en [aquest](https://github.com/jordi-petit/lp-logo3d-2021) altre repositori de GitHub.


# Arxius

- Fitxer `requirements.txt` amb les llibreries que utilitza el projecte.

- Fitxer `README.md` aquest fitxer que documenta el projecte.

- Fitxer `logo3d.py` conté el programa principal de l'intèrpret. 

- Fitxer `logo3d.g` conté la gramàtica pel llenguatge de programació **Logo3D**.

- Fitxer `visitor.py` conté el visitador de l'*AST*. 
	
	-- *Atenció:  aquesta clase HEREDA de la classe plantilla creada per el compilador de ANTLR4. Per tant, és necesari compilar la gramàtica amb el flag **-visitor**. És a dir:* `antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g`

- Fitxer `turtle3d.py` conté la classe *Turtle3D* per pintar amb ajuda de la llibrería `vpython`.


# Instalació 

1. Instalar les llibreries de *Python* requerides del fitxer `requirements.txt`.

2. [Instalar](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation) `antlr4`. 

3. Compilar la gramàtica `logo3d.g` amb el flag *-visitor* per generar `logo3dVisitor.py`. Es pot fer amb la comanda:
`antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g` 


# Execució

Per executar només cal utilitzar la comanda:

- `python3 logo3d.py programa.l3d` aquesta comanda comença a executar des del procediment `main()`, si no està definit aquest procediment donará error. 

- També es pot començar a executar des d'un altre procediment diferent al `main()`, amb la comanda:
`python logo3d.py programa.l3d nom_procediment [parametres]`. La llista de paràmetres pot ser buida, o han de ser enters o *floats*. Per exemple: `python3 logo3d.py prog_espiral.l3d espiral 5`.

*Cal notar que `programa.l3d` pot ser qualsevol programa escrit en Logo3D*.
