grammar logo3dcaca;

//////////////////  
// Parser rules // 
////////////////// 

root : (EOL* proceD EOL*)* EOF ;


proceD : funcheader funcbody funcend ;
//proceD : 'PROC' ident '(' ident (',' ident)* ')' 'IS' ;

// Function related 
funcheader : PROC FUNCNAME '(' funcparams ')' IS ;
funcparams : (PARAM (',' PARAM)*)? ;
funcbody : stmt+ ;
funcend : END ;

// Statements 
stmt : assignation
     | read
     | write
     | conditional
     | while_it
     | for_it
     | invocation
     | expr
     ;

assignation : VARIABLE ':=' expr ;

read : '>>' VARIABLE ;

write : '<<' expr ;

conditional : IF expr THEN stmt+ END
            | IF expr THEN stmt+ ELSE stmt+ END
            ;

while_it : WHILE expr DO stmt+ END ;

for_it : FOR SMALLCHAR+ FROM INT TO INT DO stmt+ END ;

invocation : FUNCNAME '(' argpassed ')' ;
argpassed : (argsaux (',' argsaux)*)? ;
argsaux : expr | ARG ;

expr : boolexpr 
     | numexpr 
     ;

boolexpr : HASVALUE EQ HASVALUE
         | HASVALUE DIFF HASVALUE
         | HASVALUE LT  HASVALUE
         | HASVALUE GT  HASVALUE
         | HASVALUE LTE HASVALUE
         | HASVALUE GTE HASVALUE
         | ZERO
         | ONE
         ;

numexpr : NUM
        | '(' numexpr ')'
        | numexpr ADD numexpr
        | numexpr SUB numexpr
        | numexpr MUL numexpr
        | numexpr DIV numexpr
        ;

ident : SMALLCHAR+ ('_' | SMALLCHAR)* ;

///////////////// 
// Lexer rules // 
///////////////// 

LP : '(' ;
RP : ')' ;

EQ :   '==' ;
DIFF : '!=' ;
LT :   '<' ;
GT :   '>' ;
LTE :  '<=' ;
GTE :  '>=' ;
ZERO : '0' ;
ONE :  '1' ;

ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;

PROC : 'PROC' ;
FUNCNAME : IDENT ;
PARAM : IDENT ;
IS : 'IS' ;

VARIABLE : IDENT ;
CTRLVAR :  IDENT ;

ARG: HASVALUE ;
HASVALUE : VARIABLE 
         | NUM 
         ;

IF : 'IF' ; 
THEN : 'THEN' ; 
ELSE : 'ELSE' ; 

WHILE : 'WHILE' ; 

FOR : 'FOR' ;
FROM : 'FROM' ;
TO : 'TO' ; 

DO : 'DO' ; 
END : 'END' ;

IDENT : SMALLCHAR (SMALLCHAR | '_')* ;        // UPERCASE or INT in names?    (SMALLCHAR)+ ? 

NUM : INT | FLOAT ;
INT : DIGIT+ ;
FLOAT : INT FLOATPART ;
FLOATPART : '.' DIGIT+ ;

DIGIT : '0'..'9' ;
SMALLCHAR : 'a'..'z' ;
BIGCHAR : [A-Z] ;

// SKIP THESE 
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WS : [ \t]+ -> skip ;
EOL : '\r'? '\n' -> skip ;