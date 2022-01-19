# LP - Pràctica *Logo3D*

Aquest és el meu projecte de Compiladors de l'asignatura de "Llenguatges de Programació" del curs *2020-2021 Q2*.

Podeu trobar l'enunciat original [aquí](https://github.com/jordi-petit/lp-logo3d-2021)


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

