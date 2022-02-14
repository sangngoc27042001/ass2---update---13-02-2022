//1952430
grammar D96;

@lexer::header {
from lexererr import *
}

options {
  language = Python3;
}

//1. Program Structures
program: stmClassDecl+ EOF;
//expLitMethodAccess|expLitAttributeAccess|expLogical|expSign|
// listOfStatement classProgram listOfStatement
//mptype: VOIDTYPE;
//
//body: funcall SEMI;
//
//exp: funcall;
//
//funcall: ID LB exp? RB;

//classProgram: 'Class Program' LCB mainFunc RCB;
//mainFunc: STATIC 'main' LB RB LCB listOfStatement RCB;

// Classes


//Constructor - Destructor
stmConstructorDecl: 'Constructor' LB parameterList RB stmBlockInFunction; // Constructor (<list of parameters>) <block statement>
stmdDestructorDecl: 'Destructor' LB RB stmBlockInFunction; // Destructor () <block statement>


// Methods
parameterList: (oneParam (SEMI oneParam)*)?; // <identifier-list>: <typeData> -> structure of parameters
oneParam:ID (COMMA ID)* COLON typeData;



// Arrays
arrayLiteral: ARRAY LB ((expression)(COMMA (expression))*)? RB ; //Array(1, 5, 7, 12)/ Array() -> structure of array
//arrayDecl: (VAL|VAR) STATIC? variableList COLON typeData SEMI; // var $arr : Array[<typeData>, <size>]; -> syntax of array declaration


//Primitive Types
typeData: INT | FLOAT | BOOLEAN | STR  | arrayType |ID;
typeDataPrimitive:INT | FLOAT | BOOLEAN | STR  | arrayType;
BOOLNUM: TRUE | FALSE;
literal: P_INTLIT|INTLIT | FLOATLIT | STRINGLIT | BOOLNUM| arrayLiteral|NULL  ;
VOIDTYPE: 'void';
arrayType: ARRAY LSB typeDataPrimitive COMMA P_INTLIT RSB; // Array[<typeData>, <size>] -> structure of array

//5. Expression
//Index operators
expIndex: (ID | expStaticAttributeAccess | expInstanceAttributeAccess) canBeIndex;
canBeIndex: LSB expression RSB canBeIndex?;
// Object creation
expObjCreation: NEW ID LB listOfExpressions RB;
//Member access
scalarVariable: expStaticAttributeAccess | expStaticMethodInvocation | expObjCreation |ID | SELF|expIndexFree;
//Index operators
expIndexFree: LB ID  canBeIndexFree RB ;
canBeIndexFree: LSB expression RSB canBeIndexFree?;

expInstanceAttributeAccess: expInstanceAttributeAccess DOT ID|expTemp1;
expTemp1:  scalarVariable |scalarVariable DOT ID LB listOfExpressions RB | LB scalarVariable RB;

expInstanceMethodInvocation: expInstanceMethodInvocation DOT ID (LB listOfExpressions RB)? | expTemp2;
expTemp2: exp_11 | expInstanceAttributeAccess;

// static member access
expStaticAttributeAccess: ID'::'STATICID;
expStaticMethodInvocation:ID'::' STATICID LB listOfExpressions RB;

//Expression and list of expression
listOfExpressions: (expression(COMMA expression)*)?;

expression: exp_0;
exp_0: exp_1 STRCMP exp_1 | exp_1;
exp_1: exp_2 RELATIONAL exp_2 | exp_2;
exp_2: exp_2 LOGICAL exp_3 | exp_3;
exp_3: exp_3 (ADD|MINUS) exp_4 | exp_4;
exp_4: exp_4 MULnDIVnMOL exp_5 | exp_5;
exp_5: NOT exp_5 | exp_6;
exp_6: MINUS exp_6 | exp_7;
exp_7: exp_7 (LSB expression RSB)+ | exp_8;
exp_8: exp_8 DOT ID (LB listOfExpressions RB)? | exp_9;
exp_9: ID DOUBLE_COLON STATICID (LB listOfExpressions RB)? | exp_10;
exp_10: NEW exp_10 LB listOfExpressions RB | exp_11;
exp_11: ID | SELF | NULL | literal | LB expression RB;
//6. Statement
//Variable and Constant Declaration Statement
stmVariableDecl: (VAL|VAR) list_att SEMI;
list_att: (ID|STATICID) (COMMA (ID|STATICID))* COLON typeData|(ID|STATICID) list_att_term expression;
list_att_term: COMMA (ID|STATICID) list_att_term expression COMMA|COLON typeData ASSIGN;

stmVariableDeclInFunction: (VAL|VAR) list_attInFunction SEMI;
list_attInFunction:  ID (COMMA (ID))* COLON typeData |ID list_att_termInFunction expression;
list_att_termInFunction: COMMA ID list_att_term expression COMMA|COLON typeData ASSIGN;

//stmVariableDecl: (VAL|VAR) variableList COLON typeData (ASSIGN expression(COMMA expression)*)? SEMI; //TODO: literal = literal/Epression
//Assignment Statement
lhs: ID | exp_7;
stmAssignment: lhs ASSIGN expression SEMI;
//If statement
stmIf: IF LB expression RB statementInFunction (ELSEIF LB expression RB statementInFunction)* (ELSE statementInFunction)?;
//For/In statement


stmBreak: BREAK SEMI;
stmContinue: CONTINUE SEMI;
stmReturn: RETURN expression? SEMI;
stmMethodInvocation: exp_9 DOT ID LB listOfExpressions RB SEMI|exp_10 DOUBLE_COLON STATICID LB listOfExpressions RB SEMI|exp_8V2 DOT ID (LB listOfExpressions RB)  SEMI;
exp_8V2: exp_8V2 DOT ID (LB listOfExpressions RB)? | exp_9;

statement:stmAssignment|stmdDestructorDecl|stmConstructorDecl|stmMethodInvocation|stmVariableDecl|stmIf|stmBreak|stmContinue|stmReturn|stmForEach|stmBlock;
listOfStatement: statement*;
stmBlock:LCB listOfStatement RCB;

stmBlockInFunction:LCB (stmVariableDeclInFunction|stmMethodInvocation|stmAssignment|stmIf|stmBreak|stmContinue|stmReturn|stmForEach|stmBlockInFunction)* RCB;
statementInFunction:stmVariableDeclInFunction|stmMethodInvocation|stmAssignment|stmIf|stmBreak|stmContinue|stmReturn|stmForEach|stmBlockInFunction;
//For each Statement
stmForEach:FOREACH LB ID IN expression DOUBLE_DOT expression (BY expression)? RB stmBlockInFunction;
//Class statement
stmClassDecl: CLASS (ID) (COLON ID)? classBody; //Chưa có constructor, destructor
classBody:LCB  (stmMethodDecl|stmVariableDecl|stmConstructorDecl|stmdDestructorDecl)*  RCB;
stmMethodDecl: (STATICID|ID) LB parameterList RB stmBlockInFunction;

//addition
STRCMP:(CONCAT | '==.');
MULnDIVnMOL:MULTIPLY|DEVIDE|MODULO;


//2. Lexical Structures
// Keywords
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT:'Int';
FLOAT:'Float';
BOOLEAN:'Boolean';
STR: 'String';
NULL: 'Null';
RETURN: 'Return';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF:'Self';

// Operators
ADD: '+';
CONCAT:'+.';
MINUS: '-';
MULTIPLY: '*';
DEVIDE: '/';
MODULO: '%';
NOT: '!';
ASSIGN: '=';
LOGICAL: '&&' | '||';
RELATIONAL: '<' | '>' | '<=' | '>=' | '==' | '!=' ;
NEWOP: NEW;
DOUBLE_COLON: '::';
DOUBLE_DOT:'..';



//Separators
fragment DOUBLEQUOTE: '"';
SEMI: ';';
COMMA: ',';
COLON: ':';
DOT: '.';
LB: '('; // bracket open
RB: ')'; // bracket close
LSB: '['; // square bracket open
RSB: ']'; // square bracket close
LCB: '{'; // curly bracket open
RCB: '}'; // curly bracket close

//Identifier
ID: [a-zA-Z_][a-zA-Z0-9_]*;
fragment STATIC: '$';
STATICID:STATIC [a-zA-Z0-9_]+;

// Possitive Int literal
fragment P_INT_BIN: '0'[bB]([1]([_]?[01])*);
fragment P_INT_DEC: [1-9]([_]?[0-9])*; // 0123141
fragment P_INT_HEX: '0'[xX]([1-9A-F]([_]?[0-9A-F])*);
fragment P_INT_OCT: '0'([1-7]([_]?[0-7])*);
P_INTLIT:  (P_INT_BIN | P_INT_DEC | P_INT_HEX | P_INT_OCT){self.text = self.text.replace("_","")};

// Int literal
fragment INT_BIN: '0'[bB]('0'|[1]([_]?[01])*);
fragment INT_DEC: [0]|[1-9]([_]?[0-9])*; // 0123141
fragment INT_HEX: '0'[xX]('0'|[1-9A-F]([_]?[0-9A-F])*);
fragment INT_OCT: '0'('0'|[1-7]([_]?[0-7])*);
INTLIT:  (INT_BIN | INT_DEC | INT_HEX | INT_OCT) {self.text = self.text.replace("_","")};
// Float literal
fragment DIGIT: [0-9];
fragment FLOAT_EXP: [eE]('-'|'+')? DIGIT+;
fragment FLOAT_DEC: '.' DIGIT*; //-10.25, -10e25, 10E25, 10.25e03
FLOATLIT:  (INT_DEC (FLOAT_DEC | FLOAT_EXP | FLOAT_DEC FLOAT_EXP) |FLOAT_DEC FLOAT_EXP ) {self.text = self.text.replace("_","")};



// STRINGLIT -> chưa xong
fragment QUOTE_IN_STR: [']["];
ESC_SEQ: '\\'[bfrnt'\\]; // \r \b \n \f \t \' \\
fragment CHAR_STRING: ~[\b\f\n\r\t\\"] | ESC_SEQ | QUOTE_IN_STR|[ ]; //
STRINGLIT: DOUBLEQUOTE CHAR_STRING* DOUBLEQUOTE
{
  content = str(self.text)
  self.text = content[1:-1]
}
;

// Comments
fragment LEGAL_COMMENT_STRING: .*?;
fragment COMMENT_SIGN: '##';
COMMENT: COMMENT_SIGN LEGAL_COMMENT_STRING COMMENT_SIGN -> skip;
WS: [ \t\r\n\b\f]+ -> skip; // skip spaces, tabs, newlines


UNCLOSE_STRING: DOUBLEQUOTE (CHAR_STRING*)
   {
       text = str(self.text)
       raise UncloseString(text[1:])
   };
ERROR_CHAR: .
   {
       raise ErrorToken(self.text)
   };
ILLEGAL_ESCAPE: DOUBLEQUOTE CHAR_STRING* '\\' ~[btnfr\\]
   {
       raise IllegalEscape(self.text[1:])
   };





