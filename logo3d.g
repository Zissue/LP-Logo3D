grammar logo3d;

//////////////////  
// Parser rules // 
////////////////// 

root : proceD* EOF ;

proceD : funcHeader instructions END ;
funcHeader : PROC IDENT LP funcParam RP IS ;
funcParam : (IDENT (COMMA IDENT)*)?;
instructions : stmt+ ;

// Statements 
stmt : while_it
     | for_it
     | assignation
     | read
     | write
     | conditional
     | invocation
     | color
     | home
     | show
     | hide
     | forward
     | backward
     | up
     | down
     | left
     | right
     // | expr
     ;

color : 'color' LP expr COMMA expr COMMA expr RP ;

home : 'home' LP RP ;

show : 'show' LP RP ;

hide : 'hide' LP RP ;

forward : 'forward' LP expr RP ;

backward : 'backward' LP expr RP ;

up : 'up' LP expr RP ;

down : 'down' LP expr RP ;

left : 'left' LP expr RP ;

right : 'right' LP expr RP ;

assignation : IDENT ASGN expr ;

expr : LP expr RP
     | expr EQ  expr
     | expr DIF expr
     | expr LT  expr
     | expr GT  expr
     | expr LTE expr
     | expr GTE expr
     | numExpr
     | TRUE     // == 1
     | FALSE    // == 0
     ;

numExpr : LP numExpr RP
        | numExpr MUL numExpr
        | numExpr DIV numExpr
        | numExpr ADD numExpr
        | numExpr SUB numExpr
        | NUM
        | IDENT                 // Variable (tipus real)
        ;

read : ROP IDENT ;

write : WOP expr ;

conditional : IF expr THEN instructions END
            | IF expr THEN instructions ELSE instructions END
            ;

while_it : WHILE expr DO instructions END ;

for_it : FOR IDENT FROM expr TO expr DO instructions END ;

invocation : IDENT LP argsPassed RP ;
argsPassed : (expr (COMMA expr)*)? ;


///////////////// 
// Lexer rules // 
///////////////// 

LP : '(' ;
RP : ')' ;

ASGN: ':=' ;

EQ :   '==' ;
DIF :  '!=' ;
LT :   '<' ;
GT :   '>' ;
LTE :  '<=' ;
GTE :  '>=' ;

PROC : 'PROC' ;
IS : 'IS' ;
END : 'END' ;

IF : 'IF' ;
THEN : 'THEN' ;
ELSE : 'ELSE' ;

WHILE : 'WHILE' ;
DO : 'DO' ;

FOR : 'FOR' ;
FROM : 'FROM' ;
TO : 'TO' ;

ROP : '>>' ;
WOP : '<<' ;

FALSE: 'False' ;
TRUE : 'True' ;

// Num. Operators
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

// Identifier
IDENT : SMALLCHAR (SMALLCHAR | DIGIT | '_')* ;

NUM : INT | FLOAT ;
INT : DIGIT+ ;
FLOAT : INT FLOATPART ;
FLOATPART : '.' DIGIT+ ;

DIGIT : '0'..'9' ;
SMALLCHAR : 'a'..'z' ;
//BIGCHAR : [A-Z] ;

// SKIP THESE 
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
COMMA : ',' ;
WS : [ \t\n]+ -> skip ;
EOL : '\r'? '\n' -> skip ;