import unittest
from TestUtils import TestAST
from TestUtils import TestParser
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input, expect, 501))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
        Class Program {
            main_a () {
                Self.putIntLn(4);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(Self(),Id(putIntLn),[IntLit(4)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 502))

    def test_call_without_parameter(self):
        """More complex program"""
        input = """
        Class Program {
            main_a () {
                Self.getIntLn();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main_a),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 503))

    def test_class_has_parent(self):
        """Class has parent"""
        input = """
        Class Program {
            mainA () {
                Self.getIntLn();
            }
        }
        Class SubProgram : Program {
            something() {
                Program::$func();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))]),ClassDecl(Id(SubProgram),Id(Program),[MethodDecl(Id(something),Instance,[],Block([Call(Id(Program),Id($func),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 504))

    def test_class_has_attr(self):
        """Class has 1 attr"""
        input = """
        Class Program {
            Var a : Int;
            mainA () {
                Self.getIntLn();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(mainA),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 505))

    def test_class_has_attrs_1(self):
        """Class has many attrs"""
        input = """
        Class Program {
            Var a, b : String;
            mainA () {
                Self.getIntLn();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),StringType)),AttributeDecl(Instance,VarDecl(Id(b),StringType)),MethodDecl(Id(mainA),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 506))

    def test_class_has_attrs_2(self):
        """Class has many attrs"""
        input = """
        Class Program {
            Var a, $b : Boolean;
            mainA () {
                Self.getIntLn();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),BoolType)),AttributeDecl(Static,VarDecl(Id($b),BoolType)),MethodDecl(Id(mainA),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 507))

    def test_class_has_attrs_3(self):
        """Class has many attrs"""
        input = """
        Class Program {
            Var a : Float;
            Var $b : Array[String, 10];
            mainA () {
                Self.getIntLn();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Static,VarDecl(Id($b),ArrayType(10,StringType))),MethodDecl(Id(mainA),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 508))

    def test_class_has_attrs_4(self):
        """Class has many attrs"""
        input = """
        Class Program {
            Var a, $l, a1, c, cccc: Array[Array[Int, 10], 0xAF];
            Var c, $b : Sth;
            mainA () {
                Self.getIntLn();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(175,ArrayType(10,IntType)))),AttributeDecl(Static,VarDecl(Id($l),ArrayType(175,ArrayType(10,IntType)))),AttributeDecl(Instance,VarDecl(Id(a1),ArrayType(175,ArrayType(10,IntType)))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(175,ArrayType(10,IntType)))),AttributeDecl(Instance,VarDecl(Id(cccc),ArrayType(175,ArrayType(10,IntType)))),AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(Sth)))),AttributeDecl(Static,VarDecl(Id($b),ClassType(Id(Sth)))),MethodDecl(Id(mainA),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 509))

    def test_simple_program_1(self):
        input = """Class Program {
            Var a : Int;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"
        self.assertTrue(TestAST.test(input, expect, 511))

    def test_simple_program_2(self):
        input = """Class Program {
            Var a : Int;
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 512))

    def test_simple_program_3(self):
        input = """Class Program {
            Var $b, a : Int;
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 513))

    def test_const_decl_1(self):
        input = """Class Rectangle {
            Val $x: Int = 10;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input, expect, 514))

    def test_const_decl_2(self):
        input = """Class Rectangle {
            Val $x: Int = 10;
            Var a, b, c : Int = 10, 0xAF, 11;
            Val $a, c, somthing : String = "Hello", "World", "\\n";
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(175))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(11))),AttributeDecl(Static,ConstDecl(Id($a),StringType,StringLit(Hello))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,StringLit(World))),AttributeDecl(Instance,ConstDecl(Id(somthing),StringType,StringLit(\\n)))])])"
        self.assertTrue(TestAST.test(input, expect, 515))

    def test_float_lit_1(self):
        input = """Class Something : Object {
            Var $a, b, c : Float = 10.0, 11., 1e15;
            Val a, c, d : Float = .e5, 0.000, 0.2;
            Var c, d, e : Float = 1e-12, 1E+4, 11.1123e10;
            Val $a, $y, $x : Float = 50.1123E-5, .5e5, .4e+5;
            Var x, y : Float = .1123e-10, 1123E123;
        }"""
        expect = "Program([ClassDecl(Id(Something),Id(Object),[AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(10.0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(11.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1000000000000000.0))),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(d),FloatType,FloatLit(0.2))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1e-12))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(10000.0))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(111123000000.0))),AttributeDecl(Static,ConstDecl(Id($a),FloatType,FloatLit(0.000501123))),AttributeDecl(Static,ConstDecl(Id($y),FloatType,FloatLit(50000.0))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(40000.0))),AttributeDecl(Instance,VarDecl(Id(x),FloatType,FloatLit(1.123e-11))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(1.123e+126)))])])"
        self.assertTrue(TestAST.test(input, expect, 516))

    def test_boolean(self):
        input = """Class A : B {
            Val a, b : Boolean = True, False;
        }"""
        expect = "Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(b),BoolType,BooleanLit(False)))])])"
        self.assertTrue(TestAST.test(input, expect, 517))

    def test_simple_array_lit_1(self):
        """Simple array literal is the array whose element is Literal not Expression"""
        input = """Class A : B {
            Val a : Array[Int, 3] = Array(1, 100, 11);
            Var b : Array[String, 4] = Array("This is a string", "Another string", "A", "B\\n");
            Var c : Array[Boolean, 3] = Array(True, False, True);
            Var d : Array[Float, 5] = Array(.e5, 1123E123, .5e5, 0.2, 50.1123E-5);
            Val e : Array[Int, 1] = Array();
            Var f : Array[Array[Int, 2], 2] = Array(Array(1, 2), Array(3, 4));
        }
        """
        expect = "Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(3,IntType),[IntLit(1),IntLit(100),IntLit(11)])),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(4,StringType),[StringLit(This is a string),StringLit(Another string),StringLit(A),StringLit(B\\n)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(3,BoolType),[BooleanLit(True),BooleanLit(False),BooleanLit(True)])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(5,FloatType),[FloatLit(0.0),FloatLit(1.123e+126),FloatLit(50000.0),FloatLit(0.2),FloatLit(0.000501123)])),AttributeDecl(Instance,ConstDecl(Id(e),ArrayType(1,IntType),[])),AttributeDecl(Instance,VarDecl(Id(f),ArrayType(2,ArrayType(2,IntType)),[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)]]))])])"
        self.assertTrue(TestAST.test(input, expect, 518))

    def test_simple_expr_1(self):
        """Only arithmethic operator"""
        input = """Class Program {
            Var a : Int = 1 + 1;
            Var b : Int = 2 * 2;
            Var c : Int = (3 + 4) * 5 - 6 / 7 % 8;
            Var d : Int = -2 * 8 + 17;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(*,IntLit(2),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLit(3),IntLit(4)),IntLit(5)),BinaryOp(%,BinaryOp(/,IntLit(6),IntLit(7)),IntLit(8))))),AttributeDecl(Instance,VarDecl(Id(d),IntType,BinaryOp(+,BinaryOp(*,UnaryOp(-,IntLit(2)),IntLit(8)),IntLit(17))))])])"
        self.assertTrue(TestAST.test(input, expect, 519))

    def test_simple_expr_2(self):
        """Variable in used"""
        input = """Class Program {
            Val a : Int = 100 + 1;
            Var b : Int = a * 2;
            Var c : Float = 100 / b;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(100),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),IntType,BinaryOp(*,Id(a),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,BinaryOp(/,IntLit(100),Id(b))))])])"
        self.assertTrue(TestAST.test(input, expect, 520))

    def test_simple_expr_3(self):
        """Self and Null came in practise"""
        input = """Class Program : ABC {
            Val a : Float = 0.0;
            Var b : SomeMeta = Null;
            Val c : Delta = Self;
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(ABC),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(SomeMeta)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(Delta)),Self()))])])"
        self.assertTrue(TestAST.test(input, expect, 521))

    def test_simple_expr_4(self):
        input = """Class Program {
            Val a, b, c : Int = 1 + 1, 2 * 2, 3 / 3;
            Var a : Array[Int, 5] = Array(1 * 2 / 3, 3 + 3 / 3, 10 - -9, 100 * 3, 100 % 10);
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(*,IntLit(2),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(/,IntLit(3),IntLit(3)))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(+,IntLit(3),BinaryOp(/,IntLit(3),IntLit(3))),BinaryOp(-,IntLit(10),UnaryOp(-,IntLit(9))),BinaryOp(*,IntLit(100),IntLit(3)),BinaryOp(%,IntLit(100),IntLit(10))]))])])"
        self.assertTrue(TestAST.test(input, expect, 522))

    def test_simple_expr_5(self):
        """String operator"""
        input = """Class Program : Facebook {
            Val a, b : String = "Hello", "World";
            Var c : String = a +. b;
            Var d : String = ("Hello" +. " ") +. "World";
            Var e : Boolean = c ==. d;
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(Facebook),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,StringLit(Hello))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,StringLit(World))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(d),StringType,BinaryOp(+.,BinaryOp(+.,StringLit(Hello),StringLit( )),StringLit(World)))),AttributeDecl(Instance,VarDecl(Id(e),BoolType,BinaryOp(==.,Id(c),Id(d))))])])"
        self.assertTrue(TestAST.test(input, expect, 523))

    def test_simple_expr_6(self):
        """Relational operator"""
        input = """Class Program : ABCMeta {
            Val a, b : Int = 1, 1;
            Var c : Boolean = a > b;
            Var d : Boolean = a < b;
            Var e, f, g, h : Boolean = a == b, a != b, a >= b, a <= b;
            Var i, j, k, l : Boolean = 1 <= 2, 2 != 3, 3.0 == 4.0, 4.5 > 4.0;
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(ABCMeta),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),BoolType,BinaryOp(>,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BinaryOp(<,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(e),BoolType,BinaryOp(==,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(f),BoolType,BinaryOp(!=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(g),BoolType,BinaryOp(>=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(h),BoolType,BinaryOp(<=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(i),BoolType,BinaryOp(<=,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(j),BoolType,BinaryOp(!=,IntLit(2),IntLit(3)))),AttributeDecl(Instance,VarDecl(Id(k),BoolType,BinaryOp(==,FloatLit(3.0),FloatLit(4.0)))),AttributeDecl(Instance,VarDecl(Id(l),BoolType,BinaryOp(>,FloatLit(4.5),FloatLit(4.0))))])])"
        self.assertTrue(TestAST.test(input, expect, 524))

    def test_simple_expr_7(self):
        """Logical operator"""
        input = """Class Program : BAKC {
            Val a, b : Int = 3, 4;
            Var c : Boolean = (a > b) && (a == b);
            Var d : Boolean = (True == False) && (True == True) || True && False;
            Var e : Boolean = ("Hello" ==. "World") || (a == b);
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(BAKC),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(3))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(4))),AttributeDecl(Instance,VarDecl(Id(c),BoolType,BinaryOp(&&,BinaryOp(>,Id(a),Id(b)),BinaryOp(==,Id(a),Id(b))))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(==,BooleanLit(True),BooleanLit(False)),BinaryOp(==,BooleanLit(True),BooleanLit(True))),BooleanLit(True)),BooleanLit(False)))),AttributeDecl(Instance,VarDecl(Id(e),BoolType,BinaryOp(||,BinaryOp(==.,StringLit(Hello),StringLit(World)),BinaryOp(==,Id(a),Id(b)))))])])"
        self.assertTrue(TestAST.test(input, expect, 525))

    def test_simple_expr_8(self):
        """Not logical operator"""
        input = """Class Program : ABCMEhoh {
            Val c : Boolean = !a;
            Var $d : Boolean = !(a == b);
            Var $e : Boolean = !((a != b) && !(a ==. b));
            Var f : Boolean = !a || b;
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(ABCMEhoh),[AttributeDecl(Instance,ConstDecl(Id(c),BoolType,UnaryOp(!,Id(a)))),AttributeDecl(Static,VarDecl(Id($d),BoolType,UnaryOp(!,BinaryOp(==,Id(a),Id(b))))),AttributeDecl(Static,VarDecl(Id($e),BoolType,UnaryOp(!,BinaryOp(&&,BinaryOp(!=,Id(a),Id(b)),UnaryOp(!,BinaryOp(==.,Id(a),Id(b))))))),AttributeDecl(Instance,VarDecl(Id(f),BoolType,BinaryOp(||,UnaryOp(!,Id(a)),Id(b))))])])"
        self.assertTrue(TestAST.test(input, expect, 526))

    def test_expr_arr_1(self):
        """Simple array access on the right hand side"""
        input = """Class Program : Something {
            Var a : Array[Int, 5] = Array(1, 2, 3, 4, 5);
            Val c : Int = a[1];
            Val b : Int = a[1][2];
            Val $d : Int = a[arr[1]];
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(Something),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])),AttributeDecl(Instance,ConstDecl(Id(c),IntType,ArrayCell(Id(a),[IntLit(1)]))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,ArrayCell(Id(a),[IntLit(1),IntLit(2)]))),AttributeDecl(Static,ConstDecl(Id($d),IntType,ArrayCell(Id(a),[ArrayCell(Id(arr),[IntLit(1)])])))])])"
        self.assertTrue(TestAST.test(input, expect, 527))

    def test_expr_arr_2(self):
        """Matrix mutliplication"""
        input = """Class So : A {
            Val a : Array[Array[Int, 5], 5];
            ##c[i][j] = c[i][j] + a[i][k] * b[k][j]##
            Val d : Int = c[i][j] + a[i][k] * b[k][j];
        }"""
        expect = "Program([ClassDecl(Id(So),Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(5,ArrayType(5,IntType)),None)),AttributeDecl(Instance,ConstDecl(Id(d),IntType,BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)])))))])])"
        self.assertTrue(TestAST.test(input, expect, 528))

    def test_expr_instance_access_1(self):
        """Instance access on the right hand side"""
        input = """Class Program {
            Val a : Sth = a.a;
            Val b : Int = b.foo();
            Var c : String = b.foo(1 + 1, 2 * 2, 3 + 3);
            Var d : String = a.a + b.b + c.foo(100 % 5);
            Var e : Float = a.b.c.e + a.b.c.foo(1 + 1, 2 + 2) / a.c.d.bar();
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(Sth)),FieldAccess(Id(a),Id(a)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,CallExpr(Id(b),Id(foo),[]))),AttributeDecl(Instance,VarDecl(Id(c),StringType,CallExpr(Id(b),Id(foo),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(*,IntLit(2),IntLit(2)),BinaryOp(+,IntLit(3),IntLit(3))]))),AttributeDecl(Instance,VarDecl(Id(d),StringType,BinaryOp(+,BinaryOp(+,FieldAccess(Id(a),Id(a)),FieldAccess(Id(b),Id(b))),CallExpr(Id(c),Id(foo),[BinaryOp(%,IntLit(100),IntLit(5))])))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,BinaryOp(+,FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(e)),BinaryOp(/,CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(foo),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(2),IntLit(2))]),CallExpr(FieldAccess(FieldAccess(Id(a),Id(c)),Id(d)),Id(bar),[])))))])])"
        self.assertTrue(TestAST.test(input, expect, 529))

    def test_expr_instance_access_2(self):
        input = """Class Program {
            Val a : Sth = b.foo(1);
            Var a : String = b.c.foo(a[1]);
            Var d : Int = a[1][b.c.foo(1 + a[1], -2, b, c)];
            Var e : aClass = Null;
            Var d : Sth = Self.local(Self.something, Self.a(), Null);
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(Sth)),CallExpr(Id(b),Id(foo),[IntLit(1)]))),AttributeDecl(Instance,VarDecl(Id(a),StringType,CallExpr(FieldAccess(Id(b),Id(c)),Id(foo),[ArrayCell(Id(a),[IntLit(1)])]))),AttributeDecl(Instance,VarDecl(Id(d),IntType,ArrayCell(Id(a),[IntLit(1),CallExpr(FieldAccess(Id(b),Id(c)),Id(foo),[BinaryOp(+,IntLit(1),ArrayCell(Id(a),[IntLit(1)])),UnaryOp(-,IntLit(2)),Id(b),Id(c)])]))),AttributeDecl(Instance,VarDecl(Id(e),ClassType(Id(aClass)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(Sth)),CallExpr(Self(),Id(local),[FieldAccess(Self(),Id(something)),CallExpr(Self(),Id(a),[]),NullLiteral()])))])])"
        self.assertTrue(TestAST.test(input, expect, 530))

    def test_expr_instance_access_3(self):
        input = """Class Program {
            Val a : Int = a.foo[1];
            Var b : String = (a[1]).foo;
            Var c : Int = (a[1][2]).foo(1);
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(Id(a),Id(foo)),[IntLit(1)]))),AttributeDecl(Instance,VarDecl(Id(b),StringType,FieldAccess(ArrayCell(Id(a),[IntLit(1)]),Id(foo)))),AttributeDecl(Instance,VarDecl(Id(c),IntType,CallExpr(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(foo),[IntLit(1)])))])])"
        self.assertTrue(TestAST.test(input, expect, 531))

    def test_expr_static_access_1(self):
        """Static access on the right hand side"""
        input = """Class Program {
            Val a : Int = Car::$a;
            Val b : Int = MotorBike::$b();
            Val c : Float = Car::$foo(a, Car::$wheels, Car::$engine(a[1], 1 + 1, 2 * 3));
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,FieldAccess(Id(Car),Id($a)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,CallExpr(Id(MotorBike),Id($b),[]))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,CallExpr(Id(Car),Id($foo),[Id(a),FieldAccess(Id(Car),Id($wheels)),CallExpr(Id(Car),Id($engine),[ArrayCell(Id(a),[IntLit(1)]),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(*,IntLit(2),IntLit(3))])])))])])"
        self.assertTrue(TestAST.test(input, expect, 532))

    def test_expr_static_access_2(self):
        """Static access and instance combine"""
        input = """Class Program {
            Val a : Int = Self.func().b.c;
            Val b : Int = ClassABC::$a.a.c.b;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,FieldAccess(FieldAccess(CallExpr(Self(),Id(func),[]),Id(b)),Id(c)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(ClassABC),Id($a)),Id(a)),Id(c)),Id(b))))])])"
        self.assertTrue(TestAST.test(input, expect, 533))

    def test_expr_newobj_1(self):
        """New object"""
        input = """Class ABC : ABCD {
            Val a : Int = 1;
        }
        Class Program {
            Val a : ABC = New ABC(1 + 1);
            Val b : ABC = New ABC(1 * 2, 2 + 3, 2 / 3, 3 % 5);
            Var c : ABC = New ABC(New A(), Self.BC(), Null);
            Val $d : ABC = New ABC(New X(New Something(), New ManyThing()));
        }"""
        expect = "Program([ClassDecl(Id(ABC),Id(ABCD),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1)))]),ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(ABC)),NewExpr(Id(ABC),[BinaryOp(+,IntLit(1),IntLit(1))]))),AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(ABC)),NewExpr(Id(ABC),[BinaryOp(*,IntLit(1),IntLit(2)),BinaryOp(+,IntLit(2),IntLit(3)),BinaryOp(/,IntLit(2),IntLit(3)),BinaryOp(%,IntLit(3),IntLit(5))]))),AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(ABC)),NewExpr(Id(ABC),[NewExpr(Id(A),[]),CallExpr(Self(),Id(BC),[]),NullLiteral()]))),AttributeDecl(Static,ConstDecl(Id($d),ClassType(Id(ABC)),NewExpr(Id(ABC),[NewExpr(Id(X),[NewExpr(Id(Something),[]),NewExpr(Id(ManyThing),[])])])))])])"
        self.assertTrue(TestAST.test(input, expect, 535))

    def test_expr_newobj_2(self):
        """New object and function"""
        input = """Class Program : ABC {
            Val a : Int = New Obj(1).foo();
            Val r : Int = New Obj(1, 1, 2 + 3, d).a().b().c().foo(New X().foo().a.b);
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(ABC),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,CallExpr(NewExpr(Id(Obj),[IntLit(1)]),Id(foo),[]))),AttributeDecl(Instance,ConstDecl(Id(r),IntType,CallExpr(CallExpr(CallExpr(CallExpr(NewExpr(Id(Obj),[IntLit(1),IntLit(1),BinaryOp(+,IntLit(2),IntLit(3)),Id(d)]),Id(a),[]),Id(b),[]),Id(c),[]),Id(foo),[FieldAccess(FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(foo),[]),Id(a)),Id(b))])))])])"
        self.assertTrue(TestAST.test(input, expect, 536))

    def test_expr_newobj_3(self):
        """New object and index access"""
        input = """Class Program : ABCD {
            Val a : Int = New Obj(1).a[1];
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(ABCD),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(NewExpr(Id(Obj),[IntLit(1)]),Id(a)),[IntLit(1)])))])])"
        self.assertTrue(TestAST.test(input, expect, 537))

    def test_method_decl_1(self):
        """Params for the method declaration"""
        input = """Class Program {
            a() {}
            b(w : Int) {}
            c(w : Int; h : Float) {}
            d(w, h : Int; s : String) {}
            e(w, h : Int; s, t : String; h, g : Float) {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([])),MethodDecl(Id(b),Instance,[param(Id(w),IntType)],Block([])),MethodDecl(Id(c),Instance,[param(Id(w),IntType),param(Id(h),FloatType)],Block([])),MethodDecl(Id(d),Instance,[param(Id(w),IntType),param(Id(h),IntType),param(Id(s),StringType)],Block([])),MethodDecl(Id(e),Instance,[param(Id(w),IntType),param(Id(h),IntType),param(Id(s),StringType),param(Id(t),StringType),param(Id(h),FloatType),param(Id(g),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 538))

    def test_method_decl_2(self):
        """Params for method declaration. Advanced type"""
        input = """Class Program {
            a(b, c : AClass; d, e : Array[Int, 5]; f : Array[Array[Array[String, 0x10], 0b10], 024]) {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[param(Id(b),ClassType(Id(AClass))),param(Id(c),ClassType(Id(AClass))),param(Id(d),ArrayType(5,IntType)),param(Id(e),ArrayType(5,IntType)),param(Id(f),ArrayType(20,ArrayType(2,ArrayType(16,StringType))))],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 539))

    def test_constructor_method_decl_1(self):
        """Constructor and its overloading version"""
        input = """Class Program {
            Constructor() {}
            Constructor(w : String) {}
            Constructor(w : Float; h : Int) {}
            Constructor(w, i : Float; h, f : Int) {}
            Constructor(w, i : ClassA; h, f : Array[Array[Int, 10], 100]) {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(w),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(w),FloatType),param(Id(h),IntType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(w),FloatType),param(Id(i),FloatType),param(Id(h),IntType),param(Id(f),IntType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(w),ClassType(Id(ClassA))),param(Id(i),ClassType(Id(ClassA))),param(Id(h),ArrayType(100,ArrayType(10,IntType))),param(Id(f),ArrayType(100,ArrayType(10,IntType)))],Block([]))])])"""
        self.assertTrue(TestAST.test(input, expect, 540))

    def test_destructor_method_decl_1(self):
        """Destructor"""
        input = """Class Program {
            Destructor() {}
        }
        Class ABC : ABCD {
            Destructor() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(ABC),Id(ABCD),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 541))

    def test_method_invocation_statements_1(self):
        """Obj.something();"""
        input = """Class Program {
            a() {
                A.foo();
                MotorBike::$ab();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(A),Id(foo),[]),Call(Id(MotorBike),Id($ab),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 542))

    def test_method_invocation_statements_2(self):
        input = """Class Program {
            a() {
                A.a.a.foo();
                (a.a[1][2][3]).foo();
                MotorBike::$ab.foo();
                (MotorBike::$a.a[1][2]).foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(FieldAccess(FieldAccess(Id(A),Id(a)),Id(a)),Id(foo),[]),Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[]),Call(FieldAccess(Id(MotorBike),Id($ab)),Id(foo),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(MotorBike),Id($a)),Id(a)),[IntLit(1),IntLit(2)]),Id(foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 543))

    def test_method_invocation_statements_4(self):
        input = """Class Program {
            a() {
                a.a.foo().a().a.foo();
                New X().func();
                New Y().a.func();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(FieldAccess(CallExpr(CallExpr(FieldAccess(Id(a),Id(a)),Id(foo),[]),Id(a),[]),Id(a)),Id(foo),[]),Call(NewExpr(Id(X),[]),Id(func),[]),Call(FieldAccess(NewExpr(Id(Y),[]),Id(a)),Id(func),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 545))

    def test_method_invocation_statements_5(self):
        input = """Class Program {
            a() {
                (a.a[1][2][3]).foo();
                (a.a[1][2]).a().foo().a.foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[]),Call(FieldAccess(CallExpr(CallExpr(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2)]),Id(a),[]),Id(foo),[]),Id(a)),Id(foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 546))

    def test_method_invocation_statements_6(self):
        input = """Class Program {
            a() {
                Self.func();
                Self.a.func(1, a, 1 + 1, 2 * 3);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Self(),Id(func),[]),Call(FieldAccess(Self(),Id(a)),Id(func),[IntLit(1),Id(a),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(*,IntLit(2),IntLit(3))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 547))

    def test_break_stm_1(self):
        input = """Class Program {
            a(w : Int; h : Float) {
                Obj.doSth();
                Break;
                Obj.foo.a();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[param(Id(w),IntType),param(Id(h),FloatType)],Block([Call(Id(Obj),Id(doSth),[]),Break,Call(FieldAccess(Id(Obj),Id(foo)),Id(a),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 548))

    def test_continue_stm_1(self):
        input = """Class Program {
            b(w, h : Int; b, c : Float) {
                Self.google();
                Continue;
                Self.callFunc(1, a, b, a != b);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(b),Instance,[param(Id(w),IntType),param(Id(h),IntType),param(Id(b),FloatType),param(Id(c),FloatType)],Block([Call(Self(),Id(google),[]),Continue,Call(Self(),Id(callFunc),[IntLit(1),Id(a),Id(b),BinaryOp(!=,Id(a),Id(b))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 549))

    def test_return_stm_1(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 550))

    def test_return_stm_2(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return New X().a;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(FieldAccess(NewExpr(Id(X),[]),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 551))

    def test_return_stm_3(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 552))

    def test_return_stm_4(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return (1 + 1) * a + 100 / 2;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(BinaryOp(+,BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(1)),Id(a)),BinaryOp(/,IntLit(100),IntLit(2))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 553))

    def test_return_stm_5(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return a.foo(1 + 1, 2, a, New X(w, 1, 2).a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(CallExpr(Id(a),Id(foo),[BinaryOp(+,IntLit(1),IntLit(1)),IntLit(2),Id(a),FieldAccess(NewExpr(Id(X),[Id(w),IntLit(1),IntLit(2)]),Id(a))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 554))

    def test_return_stm_6(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return Motor::$engihe;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(FieldAccess(Id(Motor),Id($engihe)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 555))

    def test_return_stm_7(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return Motor::$engihe[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(FieldAccess(Id(Motor),Id($engihe)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 556))

    def test_return_stm_8(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return a[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 557))

    def test_return_stm_9(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return a.a()[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(CallExpr(Id(a),Id(a),[]),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 558))

    def test_return_stm_10(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return New X(1, 12, 10 * 20);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(NewExpr(Id(X),[IntLit(1),IntLit(12),BinaryOp(*,IntLit(10),IntLit(20))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 559))

    def test_return_stm_11(self):
        input = """Class Program {
            a() {
                Obj.doMany();
                Return (a == b) || (a > b);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(>,Id(a),Id(b))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 560))

    def test_destructor_body_2(self):
        input = """Class Program {
            Destructor() {
                Obj.doMany();
                Return Motor::$engihe[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(FieldAccess(Id(Motor),Id($engihe)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 562))

    def test_constructor_body_2(self):
        input = """Class Program {
            Constructor() {
                Obj.doMany();
                Return Motor::$engihe[1][2][3];
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(FieldAccess(Id(Motor),Id($engihe)),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 564))

    def test_block_stm_1(self):
        input = """Class Program {
            aaa() {
                Self.print(a);
                {
                    Self.doSth();
                    Continue;
                }
                Return Self.Something();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(aaa),Instance,[],Block([Call(Self(),Id(print),[Id(a)]),Block([Call(Self(),Id(doSth),[]),Continue]),Return(CallExpr(Self(),Id(Something),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 566))

    def test_val_decl_stm_1(self):
        input = """Class Program {
            a() {
                Val a : Int;
                Val b : String;
                Val c, d : Array[Float, 2];
                Self.print(a);
                Self.print(b +. Self.convertToString(a));
                Self.print(c * d);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),StringType,None),ConstDecl(Id(c),ArrayType(2,FloatType),None),ConstDecl(Id(d),ArrayType(2,FloatType),None),Call(Self(),Id(print),[Id(a)]),Call(Self(),Id(print),[BinaryOp(+.,Id(b),CallExpr(Self(),Id(convertToString),[Id(a)]))]),Call(Self(),Id(print),[BinaryOp(*,Id(c),Id(d))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 567))

    def test_val_decl_stm_2(self):
        input = """Class Program {
            a() {
                Val a : Int = 10;
                Val b : String = "Hello World";
                Val c, d : Array[Float, 2] = Array(.e5, 1.0), Array(1e-1, 4.4);
                Self.print(a);
                Self.print(b +. Self.convertToString(a));
                Self.print(c * d);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(10)),ConstDecl(Id(b),StringType,StringLit(Hello World)),ConstDecl(Id(c),ArrayType(2,FloatType),[FloatLit(0.0),FloatLit(1.0)]),ConstDecl(Id(d),ArrayType(2,FloatType),[FloatLit(0.1),FloatLit(4.4)]),Call(Self(),Id(print),[Id(a)]),Call(Self(),Id(print),[BinaryOp(+.,Id(b),CallExpr(Self(),Id(convertToString),[Id(a)]))]),Call(Self(),Id(print),[BinaryOp(*,Id(c),Id(d))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 568))

    def test_val_decl_stm_3(self):
        input = """Class Program {
            a() {
                Val a : AClass = New X(1, 2, 3);
                Var b : Int = a + b + c;
                Var c : Float = 1.0;
                Var d : String = c +. " World";
                Self.print(a);
                Self.print(b +. Self.convertToString(a));
                Self.print(c * d);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(AClass)),NewExpr(Id(X),[IntLit(1),IntLit(2),IntLit(3)])),VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))),VarDecl(Id(c),FloatType,FloatLit(1.0)),VarDecl(Id(d),StringType,BinaryOp(+.,Id(c),StringLit( World))),Call(Self(),Id(print),[Id(a)]),Call(Self(),Id(print),[BinaryOp(+.,Id(b),CallExpr(Self(),Id(convertToString),[Id(a)]))]),Call(Self(),Id(print),[BinaryOp(*,Id(c),Id(d))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 569))

    def test_assign_stm_1(self):
        input = """Class Program {
            a() {
                Val a : Int;
                a = 1 + 1 + a - 3 * b / 7 + d;
                Self.print(a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),IntType,None),AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),Id(a)),BinaryOp(/,BinaryOp(*,IntLit(3),Id(b)),IntLit(7))),Id(d))),Call(Self(),Id(print),[Id(a)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 570))

    def test_assign_stm_2(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 571))

    def test_assign_stm_3(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                a.a = 10;
                a.b = -100.00 + a.foo();
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10)),AssignStmt(FieldAccess(Id(a),Id(b)),BinaryOp(+,UnaryOp(-,FloatLit(100.0)),CallExpr(Id(a),Id(foo),[]))),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 572))

    def test_assign_stm_4(self):
        input = """Class Program {
            a() {
                Val a : ClassAC = Null;
                a = New X(1 + 1, a - 3 * b, 10 / 7 + d);
                a.a = 10;
                a.b = -100.00 + a.foo();
                a.a.b[1] = Array(1, 2, 3);
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(3),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d))])),AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10)),AssignStmt(FieldAccess(Id(a),Id(b)),BinaryOp(+,UnaryOp(-,FloatLit(100.0)),CallExpr(Id(a),Id(foo),[]))),AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(a)),Id(b)),[IntLit(1)]),[IntLit(1),IntLit(2),IntLit(3)]),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 573))

    def test_assign_stm_5(self):
        input = """Class Program {
            $a() {
                MotorBike::$eng = Array(1, 2+a, a * b);
                a[1][(i - j)][3] = c[i][k] + b[1][(j+1)][(k - 2)][3];
                
                Self.print(a.a);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($a),Static,[],Block([AssignStmt(FieldAccess(Id(MotorBike),Id($eng)),[IntLit(1),BinaryOp(+,IntLit(2),Id(a)),BinaryOp(*,Id(a),Id(b))]),AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(-,Id(i),Id(j)),IntLit(3)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(k)]),ArrayCell(Id(b),[IntLit(1),BinaryOp(+,Id(j),IntLit(1)),BinaryOp(-,Id(k),IntLit(2)),IntLit(3)]))),Call(Self(),Id(print),[FieldAccess(Id(a),Id(a))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 574))

    def test_assign_stm_6(self):
        input = """Class Program {
            $a() {
                a.f().a[1][23] = a.foo() +. AClass::$foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($a),Static,[],Block([AssignStmt(ArrayCell(FieldAccess(CallExpr(Id(a),Id(f),[]),Id(a)),[IntLit(1),IntLit(23)]),BinaryOp(+.,CallExpr(Id(a),Id(foo),[]),CallExpr(Id(AClass),Id($foo),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 575))

    def test_foreach_stm_1(self):
        input = """Class Program {
            a() {
                Foreach (a In 1 .. 100 By 2) {
                    Self.print(a + 1);
                    b = a * 2;
                    Self.print(b.a.c);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([Call(Self(),Id(print),[BinaryOp(+,Id(a),IntLit(1))]),AssignStmt(Id(b),BinaryOp(*,Id(a),IntLit(2))),Call(Self(),Id(print),[FieldAccess(FieldAccess(Id(b),Id(a)),Id(c))])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 577))

    def test_foreach_stm_2(self):
        input = """Class Program {
            a() {
                Foreach (a In b + c .. b - c * 100) {
                    Self.print(a);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),BinaryOp(+,Id(b),Id(c)),BinaryOp(-,Id(b),BinaryOp(*,Id(c),IntLit(100))),IntLit(1),Block([Call(Self(),Id(print),[Id(a)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 578))

    def test_foreach_stm_3(self):
        input = """Class Program {
            a() {
                Foreach (a In New X(1, 2, 3) .. Self.foo().a.bar() By MotherBoard::$capacitor.foo()) {
                    Self.print(a);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(a),NewExpr(Id(X),[IntLit(1),IntLit(2),IntLit(3)]),CallExpr(FieldAccess(CallExpr(Self(),Id(foo),[]),Id(a)),Id(bar),[]),CallExpr(FieldAccess(Id(MotherBoard),Id($capacitor)),Id(foo),[]),Block([Call(Self(),Id(print),[Id(a)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 579))

    def test_if_stm_1(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Else {
                    Self.print("Oh no");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),Block([Call(Self(),Id(print),[StringLit(Oh no)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 580))

    def test_if_stm_2(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Elseif (a > b) {
                    Self.print("Greater");
                } Else {
                    Self.print("Oh no");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Greater)])]),Block([Call(Self(),Id(print),[StringLit(Oh no)])])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 581))

    def test_if_stm_3(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Elseif (a > b) {
                    Self.print("Greater");
                } Elseif (a < b) {
                    Self.print("Less");
                } Else {
                    Self.print("Oh no");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Greater)])]),If(BinaryOp(<,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Less)])]),Block([Call(Self(),Id(print),[StringLit(Oh no)])]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 582))

    def test_if_stm_4(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                } Elseif (a > b) {
                    Self.print("Greater");
                } Elseif (a < b) {
                    Self.print("Less");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Greater)])]),If(BinaryOp(<,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Less)])]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 583))

    def test_if_stm_5(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Self.print("Hurray");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 584))

    def test_if_stm_6(self):
        input = """Class Program {
            a() {
                If (a == b) {
                    Foreach (i In j .. b By a/2) {
                        b = b + 1;
                        c = b * a;
                        d = c / 2;
                        Self.print(d.foo().a.bar());
                    }
                } Elseif ((a < b) || (b < d) && (i == (j + 1))) {
                    If (a == b) {
                        Self.print("Index out of bound");
                    } Else {
                        a[1][2][(b+1)] = c[(b+2)][(b*2)];
                    }
                } Else {
                    Out.println("An error has occured");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([For(Id(i),Id(j),Id(b),BinaryOp(/,Id(a),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1))),AssignStmt(Id(c),BinaryOp(*,Id(b),Id(a))),AssignStmt(Id(d),BinaryOp(/,Id(c),IntLit(2))),Call(Self(),Id(print),[CallExpr(FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(a)),Id(bar),[])])])])]),If(BinaryOp(&&,BinaryOp(||,BinaryOp(<,Id(a),Id(b)),BinaryOp(<,Id(b),Id(d))),BinaryOp(==,Id(i),BinaryOp(+,Id(j),IntLit(1)))),Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Index out of bound)])]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),BinaryOp(+,Id(b),IntLit(1))]),ArrayCell(Id(c),[BinaryOp(+,Id(b),IntLit(2)),BinaryOp(*,Id(b),IntLit(2))]))]))]),Block([Call(Id(Out),Id(println),[StringLit(An error has occured)])])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 585))

    def test_if_stm_7(self):
        input = """Class Program {
            a() {
                Foreach (i In 0 .. 1000 By a) {
                    If (i == 100) {
                        Break;
                    } Else {
                        i = i + 1;
                    }
                }
                Self.print(a.a.foo());
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(i),IntLit(0),IntLit(1000),Id(a),Block([If(BinaryOp(==,Id(i),IntLit(100)),Block([Break]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])]),Call(Self(),Id(print),[CallExpr(FieldAccess(Id(a),Id(a)),Id(foo),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 586))

    def test_if_stm_8(self):
        input = """Class Program {
            a() {
                Foreach (i In 0 .. 1000 By a) {
                    If (i == 100) {
                        Continue;
                    } Else {
                        i = i + 1;
                    }
                }
                Self.print(a.a.foo());
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(i),IntLit(0),IntLit(1000),Id(a),Block([If(BinaryOp(==,Id(i),IntLit(100)),Block([Continue]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])]),Call(Self(),Id(print),[CallExpr(FieldAccess(Id(a),Id(a)),Id(foo),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 587))

    def test_if_stm_9(self):
        input = """Class Program {
            a() {
                Foreach (i In 0 .. 1000 By a) {
                    If (i == 100) {
                        Return New X();
                    } Else {
                        i = i + 1;
                    }
                }
                Self.print(a.a.foo());
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([For(Id(i),IntLit(0),IntLit(1000),Id(a),Block([If(BinaryOp(==,Id(i),IntLit(100)),Block([Return(NewExpr(Id(X),[]))]),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))])]),Call(Self(),Id(print),[CallExpr(FieldAccess(Id(a),Id(a)),Id(foo),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 588))

    def test_main_func_1(self):
        """main inside Program class -> static, not Program -> instance"""
        input = """Class Program {
            main() {}
        }
        Class ABC {
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(ABC),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 589))

    def test_main_func_2(self):
        """main() inside Program class -> static, main(params) -> instance"""
        input = """Class Program {
            main() {}
            main(w, h: Int) {}
        }
        Class ABC {
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(w),IntType),param(Id(h),IntType)],Block([]))]),ClassDecl(Id(ABC),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 590))

    def test_simple_program_4(self):
        input = """Class Program {
            main() {
                Val a : Int;
                Foreach (i In 1 .. 100 By 1)
                {
                    Clib.printf("enter the number:");
                    Clib.scanf("%d", a);
                    If ( a == 0 ) {
                        Break;
                    }
                }
                Return 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Clib),Id(printf),[StringLit(enter the number:)]),Call(Id(Clib),Id(scanf),[StringLit(%d),Id(a)]),If(BinaryOp(==,Id(a),IntLit(0)),Block([Break]))])]),Return(IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 591))

    def test_matrix_mul_2(self):
        """Matrix mutliplication"""
        input = """Class So : A {
            Val a : Array[Array[Int, 5], 5];
            main() {
                c[i][j] = c[i][j] + a[i][k] * b[k][j];
            }
        }"""
        expect = "Program([ClassDecl(Id(So),Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(5,ArrayType(5,IntType)),None)),MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 592))

    def test_simple_program_5(self):
        input = """Class Program {
                    main() {
                        (a[1]).func();
                        a[1] = 1;
                        Out.println(a.a[1]);
                        ((((a[1][2]).a[1]).func()[0]).a[1]).func();
                        Return;
                    }
                }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(a),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(a)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 593))

    def test_complex_program_4(self):
        input = """
        Class SomethingNormal {
            aFunc123(str: Array[String, 10]) {
                Val parameters: Map = SomeClass::$parseParameters(args);

                Val builder : ChainedOptionsBuilder = New OptionsBuilder()
                .include(BigMatrixMultiplicationBenchmarking.class.getSimpleName())
                .mode(Mode.AverageTime)
                .forks(2)
                .warmupIterations(10)
                .measurementIterations(10)
                .timeUnit(TimeUnit.SECONDS);

                Return New Runner(builder.build()).run();
            }
    homemadeMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Return HomemadeMatrix
          .multiplyMatrices(matrixProvider.getFirstMatrix(), matrixProvider.getSecondMatrix());
    }

    nd4jMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Val firstMatrix : INDArray = Nd4j.create(matrixProvider.getFirstMatrix());
        Val secondMatrix : INDArray = Nd4j.create(matrixProvider.getSecondMatrix());

        Return firstMatrix.mmul(secondMatrix);
    }

    coltMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Val doubleFactory2D : DoubleFactory2D = DoubleFactory2D.dense;

        Val firstMatrix : DoubleMatrix2D= doubleFactory2D.make(matrixProvider.getFirstMatrix());
        Val secondMatrix : DoubleMatrix2D = doubleFactory2D.make(matrixProvider.getSecondMatrix());

        Var algebra : Algebra = New Algebra();
        Return algebra.mult(firstMatrix, secondMatrix);
    }

    ejmlMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Var firstMatrix : SimpleMatrix = New SimpleMatrix(matrixProvider.getFirstMatrix());
        Var secondMatrix : SimpleMatrix = New SimpleMatrix(matrixProvider.getSecondMatrix());

        Return firstMatrix.mult(secondMatrix);
    }

    apacheCommonsMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Var firstMatrix : RealMatrix = New Array2DRowRealMatrix(matrixProvider.getFirstMatrix());
        Val secondMatrix : RealMatrix = New Array2DRowRealMatrix(matrixProvider.getSecondMatrix());

        Return firstMatrix.multiply(secondMatrix);
    }

    la4jMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Val firstMatrix : Matrix = New Basic2DMatrix(matrixProvider.getFirstMatrix());
        Val secondMatrix : Matrix = New Basic2DMatrix(matrixProvider.getSecondMatrix());

        Return firstMatrix.multiply(secondMatrix);
    }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Var a : Int = a.b.c.d();
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(SomethingNormal),[MethodDecl(Id(aFunc123),Instance,[param(Id(str),ArrayType(10,StringType))],Block([ConstDecl(Id(parameters),ClassType(Id(Map)),CallExpr(Id(SomeClass),Id($parseParameters),[Id(args)])),ConstDecl(Id(builder),ClassType(Id(ChainedOptionsBuilder)),CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(NewExpr(Id(OptionsBuilder),[]),Id(include),[CallExpr(FieldAccess(Id(BigMatrixMultiplicationBenchmarking),Id(class)),Id(getSimpleName),[])]),Id(mode),[FieldAccess(Id(Mode),Id(AverageTime))]),Id(forks),[IntLit(2)]),Id(warmupIterations),[IntLit(10)]),Id(measurementIterations),[IntLit(10)]),Id(timeUnit),[FieldAccess(Id(TimeUnit),Id(SECONDS))])),Return(CallExpr(NewExpr(Id(Runner),[CallExpr(Id(builder),Id(build),[])]),Id(run),[]))])),MethodDecl(Id(homemadeMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([Return(CallExpr(Id(HomemadeMatrix),Id(multiplyMatrices),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[]),CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])]))])),MethodDecl(Id(nd4jMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(firstMatrix),ClassType(Id(INDArray)),CallExpr(Id(Nd4j),Id(create),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(INDArray)),CallExpr(Id(Nd4j),Id(create),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(mmul),[Id(secondMatrix)]))])),MethodDecl(Id(coltMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(doubleFactory2D),ClassType(Id(DoubleFactory2D)),FieldAccess(Id(DoubleFactory2D),Id(dense))),ConstDecl(Id(firstMatrix),ClassType(Id(DoubleMatrix2D)),CallExpr(Id(doubleFactory2D),Id(make),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(DoubleMatrix2D)),CallExpr(Id(doubleFactory2D),Id(make),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),VarDecl(Id(algebra),ClassType(Id(Algebra)),NewExpr(Id(Algebra),[])),Return(CallExpr(Id(algebra),Id(mult),[Id(firstMatrix),Id(secondMatrix)]))])),MethodDecl(Id(ejmlMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([VarDecl(Id(firstMatrix),ClassType(Id(SimpleMatrix)),NewExpr(Id(SimpleMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),VarDecl(Id(secondMatrix),ClassType(Id(SimpleMatrix)),NewExpr(Id(SimpleMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(mult),[Id(secondMatrix)]))])),MethodDecl(Id(apacheCommonsMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([VarDecl(Id(firstMatrix),ClassType(Id(RealMatrix)),NewExpr(Id(Array2DRowRealMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(RealMatrix)),NewExpr(Id(Array2DRowRealMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(multiply),[Id(secondMatrix)]))])),MethodDecl(Id(la4jMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(firstMatrix),ClassType(Id(Matrix)),NewExpr(Id(Basic2DMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(Matrix)),NewExpr(Id(Basic2DMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(multiply),[Id(secondMatrix)]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(My2ndCons),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),VarDecl(Id(a),IntType,CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[])),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 597))

    def test_complex_program_3(self):
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
                Return;
            }
            clean() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 1)
                {
                    el = Self.key[k];

                    Self.free(el);
                    Self.key = Null;
                }
                Self.free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    Self.free(el);
                    Self.value = Null;
                }
                Self.free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            mainA() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Map),[AttributeDecl(Instance,ConstDecl(Id(key),ArrayType(10,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(value),ArrayType(10,StringType),None)),MethodDecl(Id(Constructor),Instance,[param(Id(key),ArrayType(10,StringType)),param(Id(value),ArrayType(10,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(key)),Id(key)),AssignStmt(FieldAccess(Self(),Id(value)),Id(value)),Return()])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(clean),[FieldAccess(Self(),Id(key))]),Call(Self(),Id(clean),[FieldAccess(Self(),Id(value))]),Return()])),MethodDecl(Id(clean),Instance,[],Block([Call(Id(Out),Id(println),[StringLit(Cleaning)]),For(Id(k),IntLit(0),CallExpr(FieldAccess(Self(),Id(key)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(Self(),Id(key)),[Id(k)])),Call(Self(),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(key)),NullLiteral())])]),Call(Self(),Id(free),[Id(key)]),AssignStmt(FieldAccess(Self(),Id(key)),NullLiteral()),For(Id(v),IntLit(0),CallExpr(FieldAccess(Self(),Id(value)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(FieldAccess(Self(),Id(value)),Id(a)),[Id(v)])),Call(Self(),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral())])]),Call(Self(),Id(free),[Id(value)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral()),ConstDecl(Id(a),BoolType,BooleanLit(True)),ConstDecl(Id(b),IntType,IntLit(1)),Return(BinaryOp(&&,BinaryOp(||,BooleanLit(True),BooleanLit(False)),BinaryOp(==,Id(a),Id(b))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(My2ndCons),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 598))

    def test_complex_program_1(self):
        input = """
	Class Node {
		Var data : Int;
		Val next : Node;

		Constructor(d : Int)
		{
			data = d;
			next = Null;
		}

        ## Function to reverse the linked list ##
        reverse(node : Node)
        {
            Var prev : Node = Null;
            Val current : Node = node;
            Val next : Node = Null;
            Foreach (i In 1 .. forever By 1) {
                If (current == Null) {
                    Break;
                } Else {
                    next = current.next;
                    current.next = prev;
                    prev = current;
                    current = next;
                }
            }
            node = prev;
            Return node;
        }

        printList(node : Node)
        {
            Foreach (a In 1 .. infinity By 1) {
                If (node != Null) {
                    System.out.print(node.data +. " ");
                    node = node.next;
                } Else {
                    Break;
                }
            }
        }
    }

    Class Program {
        mainA()
        {
            Val list : LinkedList = New LinkedList();
            list.head = New Node(85);
            list.head.next = New Node(15);
            list.head.next.next = New Node(4);
            list.head.next.next.next = New Node(20);

            System.out.println("Given Linked list");
            list.printList(head);
            head = list.reverse(head);
            System.out.println("");
            System.out.println("Reversed linked list ");
            list.printList(head);
        }
    }
        """
        expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,ConstDecl(Id(next),ClassType(Id(Node)),None)),MethodDecl(Id(Constructor),Instance,[param(Id(d),IntType)],Block([AssignStmt(Id(data),Id(d)),AssignStmt(Id(next),NullLiteral())])),MethodDecl(Id(reverse),Instance,[param(Id(node),ClassType(Id(Node)))],Block([VarDecl(Id(prev),ClassType(Id(Node)),NullLiteral()),ConstDecl(Id(current),ClassType(Id(Node)),Id(node)),ConstDecl(Id(next),ClassType(Id(Node)),NullLiteral()),For(Id(i),IntLit(1),Id(forever),IntLit(1),Block([If(BinaryOp(==,Id(current),NullLiteral()),Block([Break]),Block([AssignStmt(Id(next),FieldAccess(Id(current),Id(next))),AssignStmt(FieldAccess(Id(current),Id(next)),Id(prev)),AssignStmt(Id(prev),Id(current)),AssignStmt(Id(current),Id(next))]))])]),AssignStmt(Id(node),Id(prev)),Return(Id(node))])),MethodDecl(Id(printList),Instance,[param(Id(node),ClassType(Id(Node)))],Block([For(Id(a),IntLit(1),Id(infinity),IntLit(1),Block([If(BinaryOp(!=,Id(node),NullLiteral()),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+.,FieldAccess(Id(node),Id(data)),StringLit( ))]),AssignStmt(Id(node),FieldAccess(Id(node),Id(next)))]),Block([Break]))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([ConstDecl(Id(list),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(list),Id(head)),NewExpr(Id(Node),[IntLit(85)])),AssignStmt(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),NewExpr(Id(Node),[IntLit(15)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),NewExpr(Id(Node),[IntLit(4)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),Id(next)),NewExpr(Id(Node),[IntLit(20)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Given Linked list)]),Call(Id(list),Id(printList),[Id(head)]),AssignStmt(Id(head),CallExpr(Id(list),Id(reverse),[Id(head)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit()]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Reversed linked list )]),Call(Id(list),Id(printList),[Id(head)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 600))
