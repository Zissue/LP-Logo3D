grammar logo3d;

//////////////////  
// Parser rules // 
////////////////// 

root : proceD* EOF ;

proceD : 'PROC' IDENT '(' (IDENT (COMMA IDENT)*)? ')' 'IS' stmt+ 'END' ;
//funcName : IDENT ;
//funcParam : (IDENT (COMMA IDENT)*)?;
//funcBody : stmt+ ;

// Statements 
stmt : while_it
     | for_it
     | assignation
     | read
     | write
     | conditional
     | invocation
     ;              //  | expr

assignation : IDENT ':=' expr ;

expr : '(' expr ')'
     | expr EQ  expr
     | expr DIF expr
     | expr LT  expr
     | expr GT  expr
     | expr LTE expr
     | expr GTE expr
     | numExpr
     | TRUE
     | FALSE
     ;

numExpr : '(' numExpr ')'
        | numExpr MUL numExpr
        | numExpr DIV numExpr
        | numExpr ADD numExpr
        | numExpr SUB numExpr
        | NUM
        | IDENT                 // Variable (tipus real)
        ;

read : '>>' IDENT ;

write : '<<' expr ;

conditional : 'IF' expr 'THEN' stmt+ 'END'
            | 'IF' expr 'THEN' stmt+ 'ELSE' stmt+ 'END'
            ;

while_it : 'WHILE' expr 'DO' stmt+ 'END' ;

for_it : 'FOR' IDENT 'FROM' expr 'TO' expr 'DO' stmt+ 'END' ;

invocation : IDENT '(' argsPassed ')' ;
argsPassed : (expr (',' expr)*)? ;


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

//ZERO : '0' ;
//ONE :  '1' ;
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