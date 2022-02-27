import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """Class main { }"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_301(self):
        input = """Class main { } Class main2 {}"""
        expect = str(Program([ClassDecl(Id("main"),[]),ClassDecl(Id("main2"),[])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_302(self):
        input = """Class main {} Class main2 : main {}"""
        expect = str(Program([ClassDecl(Id("main"),[]),ClassDecl(Id("main2"),[],Id("main"))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = """Class Program { main() {}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """Class Program { main() {Val a:Int;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([ConstDecl(Id('a'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = """Class Program { main() {Val a,b:Int;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([ConstDecl(Id('a'), IntType()), ConstDecl(Id('b'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = """Class Program { main() {Val a:Int = 2;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = """Class Program { main() {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2)),ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = """Class Program { main() {Var a:Int;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([VarDecl(Id('a'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = """Class Program { main() {Var a,b:Int;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([VarDecl(Id('a'), IntType()), VarDecl(Id('b'), IntType())]))])]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = """Class Program { main() {Var a:Int = 2;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([VarDecl(Id('a'), IntType(), IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = """Class Program { main() {Var a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([VarDecl(Id('a'), IntType(), IntLiteral(2)),VarDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = """Class Program { main() {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2)),ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = """Class Rectangle {Var length: Int;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Instance(),VarDecl(Id("length"),IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = """Class Rectangle {Val length: Int;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Instance(),ConstDecl(Id("length"),IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = """Class Rectangle {Val $length: Int;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = """Class Rectangle {Val $length: Int = 1;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType(),IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = """Class Rectangle {Val $length, $width: Int = 1, 2;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType(),IntLiteral(1))),AttributeDecl(Static(),ConstDecl(Id("$width"),IntType(),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """Class Rectangle {Val $length, width: Int = 1, 2;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType(),IntLiteral(1))),AttributeDecl(Instance(),ConstDecl(Id("width"),IntType(),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """Class Rectangle {Val $length: Int = 0x123;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType(),IntLiteral(0x123)))])]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """Class Rectangle {Val $length: Int = 0b1101;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType(),IntLiteral(0b1101)))])]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """Class Rectangle {Val $length: Int = 01321;}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType(),IntLiteral(0o1321)))])]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """Class Rectangle {Val $length: Int = 01321; Val $width: String = "12";}"""
        expect = str(Program([ClassDecl(Id("Rectangle"),[AttributeDecl(Static(),ConstDecl(Id("$length"),IntType(),IntLiteral(0o1321))),AttributeDecl(Static(),ConstDecl(Id("$width"),StringType(),StringLiteral("12")))])]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """Class Program { notmain(a,b:Int) {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("notmain"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2)),ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = """Class Program { notmain(a,b:Int; c:String) {Val a,b:Int = 2,3;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("notmain"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),StringType())],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2)),ConstDecl(Id('b'), IntType(), IntLiteral(3))]))])]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """Class Program { notmain(a,b:Int; c:String) {Val a,b:Int = 2,3;}notmain2(a:Int) {Val a:Int = 2;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("notmain"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),StringType())],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2)),ConstDecl(Id('b'), IntType(), IntLiteral(3))])), MethodDecl(Instance(),Id("notmain2"),[VarDecl(Id("a"),IntType())],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input, expect, 325))