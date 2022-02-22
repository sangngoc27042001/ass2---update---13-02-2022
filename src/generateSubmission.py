import os
import shutil
os.system('python run.py gen')
try:
    os.mkdir("../submission")
except:
    print("The folder submission already created")

ASTGenSuite='test/ASTGenSuite.py'
ASTGeneration='main/d96/astgen/ASTGeneration.py'
d96='main/d96/parser/D96.g4'
Lexer = '../target/D96Lexer.py'
Parser = '../target/D96Parser.py'
Visitor = '../target/D96Visitor.py'


shutil.copy(ASTGenSuite,'../submission/ASTGenSuite.py')
shutil.copy(ASTGeneration,'../submission/ASTGeneration.py')
shutil.copy(d96,'../submission/D96.g4')
shutil.copy(Lexer,'../submission/D96Lexer.py')
shutil.copy(Parser,'../submission/D96Parser.py')
shutil.copy(Visitor,'../submission/D96Visitor.py')