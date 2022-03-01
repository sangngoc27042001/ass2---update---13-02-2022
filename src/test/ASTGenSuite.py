import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        """Simple program: int main() {} """
        input = "Class Program {}"
        expect = 'Program([ClassDecl(Id(Program),[])])'
        self.assertTrue(TestAST.test(input,expect,300))
    def test_301(self):
        """Simple program: int main() {} """
        input = "Class A:B {}"
        expect = 'Program([ClassDecl(Id(A),Id(B),[])])'
        self.assertTrue(TestAST.test(input,expect,301))
    def test_302(self):
        """Simple program: int main() {} """
        input = "Class A {} Class B {} Class C {}"
        expect = 'Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(C),[])])'
        self.assertTrue(TestAST.test(input,expect,302))
    def test_303(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,303))
    def test_304(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int;
            Var b:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,304))
    def test_305(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Array[Int,5];
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType)))])])'
        self.assertTrue(TestAST.test(input,expect,305))
    def test_306(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int=1;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1)))])])'
        self.assertTrue(TestAST.test(input,expect,306))
    def test_307(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int=1+1;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1))))])])'
        self.assertTrue(TestAST.test(input,expect,307))
    def test_308(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int=1+1*2;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(1),IntLit(2)))))])])'
        self.assertTrue(TestAST.test(input,expect,308))
    def test_309(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int=\"abc\"+.1+2;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))))])])'
        self.assertTrue(TestAST.test(input,expect,309))
    def test_310(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int=!!a---2*---3;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(-,UnaryOp(!,UnaryOp(!,Id(a))),BinaryOp(*,UnaryOp(-,UnaryOp(-,IntLit(2))),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(3))))))))])])'
        self.assertTrue(TestAST.test(input,expect,310))
    def test_311(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Val a:Boolean=True;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BooleanLit(True)))])])'
        self.assertTrue(TestAST.test(input,expect,311))
    def test_312(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Val a:String=b[1][1];
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(Id(b),[IntLit(1),IntLit(1)])))])])'
        self.assertTrue(TestAST.test(input,expect,312))
    def test_313(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var a:Int = New a();
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,NewExpr(Id(a),[])))])])'
        self.assertTrue(TestAST.test(input,expect,313))
    def test_314(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Val b:Int = Null;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NullLiteral()))])])'
        self.assertTrue(TestAST.test(input,expect,314))
    def test_315(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Val b:Int = New a(1+2,Null);
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NewExpr(Id(a),[BinaryOp(+,IntLit(1),IntLit(2)),NullLiteral()])))])])'
        self.assertTrue(TestAST.test(input,expect,315))
    def test_316(self):
        """Simple program: int main() {} """
        input = """
        Class A {
            Var $b:Float=6.9;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(6.9)))])])'
        self.assertTrue(TestAST.test(input,expect,316))
    def test_317(self):
        input = """
        Class A {
            foo(){}
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_318(self):
        input = """
        Class A {
            foo(a,b:Int;c:Float){}
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_319(self):
        input = """
        Class A {
            foo(a:Int;b:Boolean;c:String){}
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),BoolType),param(Id(c),StringType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_320(self):
        input = """
        Class A {
            foo(){
                Var a:Int;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType)]))])])'
        self.assertTrue(TestAST.test(input, expect, 320))
    def test_321(self):
        input = """
        Class A {
            foo(){
                Var a:Int = 1;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 321))
    def test_322(self):
        input = """
        Class A {
            foo(){
                Var a:Int = 1;
                Var b:Float = 1.0;
                Val c:Boolean = True;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),FloatType,FloatLit(1.0)),ConstDecl(Id(c),BoolType,BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 322))
    def test_323(self):
        input = """
        Class A {
            Var $b:Int = 1;
            foo(){
                Var a:Int = 1;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(1))),MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 323))
    def test_324(self):
        input = """
        Class A {
            foo(a,b,c,d,e:Int){
                Var f:Int = 1+2*3;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(e),IntType)],Block([VarDecl(Id(f),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 324))
    def test_325(self):
        input = """
        Class A {
            $foo(){
                Var a:Int = 2/3;
                a=1;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([VarDecl(Id(a),IntType,BinaryOp(/,IntLit(2),IntLit(3))),AssignStmt(Id(a),IntLit(1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 325))
    def test_326(self):
        input = """
        Class A {
            $foo(){
                a[1][3+4]=1;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(+,IntLit(3),IntLit(4))]),IntLit(1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 326))
    def test_327(self):
        input = """
        Class A {
            foo(){
                a[1][b[3]]="abc";
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]),StringLit(abc))]))])])'
        self.assertTrue(TestAST.test(input, expect, 327))
    def test_328(self):
        input = """
        Class A {
            foo(){
                a.b.c="abc";
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),StringLit(abc))]))])])'
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_329(self):
        input = """
        Class A {
            foo(){
                a.b.c[1]=d.e.f(1,2+3);
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),[IntLit(1)]),CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 329))
    def test_330(self):
        input = """
        Class A {
            foo(){
                Var a:A = d.e.f(1,2+3) + 2;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ClassType(Id(A)),BinaryOp(+,CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]),IntLit(2)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 330))
    def test_331(self):
        input = """
        Class A {
            foo(){
                Var a:Array[Array[Int,5],5];
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 331))
    def test_332(self):
        input = """
        Class A {
            foo(){
                Break;
                Continue;
                Return a==.!b;
                {}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([Break,Continue,Return(BinaryOp(==.,Id(a),UnaryOp(!,Id(b)))),Block([])]))])])'
        self.assertTrue(TestAST.test(input, expect, 332))
    def test_333(self):
        input = """
        Class A:B{
            foo(){
                a = New a(1+2*3/4).b.c();
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_334(self):
        input = """
        Class A:B{
            foo(){
                a = New a(1+2*3/4).b.c();
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 334))
    def test_335(self):
        input = """
        Class A:B{
            foo(){
                a = (1+2)*3;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_336(self):
        input = """
        Class A:B{
            foo(){
                Return Self.foo();
            }
            Constructor (a,b:J){}
            Destructor (){}
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([Return(CallExpr(Self(),Id(foo),[]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(J))),param(Id(b),ClassType(Id(J)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 336))
    def test_337(self):
        input = """
        Class A:B{
            Var a,$b:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 337))
    def test_338(self):
        input = """
        Class A:B{
            Var a,$b:Int = 1,2;
            Val $c,d:Boolean = True, Null;
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id($c),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,NullLiteral()))])])'
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_339(self):
        input = """
        Class A:B{
            Var a, b, c:Int;
            Foo(){
                Var a, b, c:Int;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)]))])])'
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_340(self):
        input = """
        Class A:B{
            Foo(){
                Val a, b, c:Int = 1,2,3;
                Var d:Boolean = True;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),ConstDecl(Id(c),IntType,IntLit(3)),VarDecl(Id(d),BoolType,BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 340))
    def test_341(self):
        input = """
        Class A:B{
            Var $a:Array[Int,3] = Array(1,1,1);
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,IntType),[IntLit(1),IntLit(1),IntLit(1)]))])])'
        self.assertTrue(TestAST.test(input, expect, 341))
    def test_342(self):
        input = """
        Class A:B{
            Var $a:Array[Array[Int,1],3] = Array(Array(1),Array(1),Array(1));
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,ArrayType(1,IntType)),[[IntLit(1)],[IntLit(1)],[IntLit(1)]]))])])'
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_343(self):
        input = """
        Class A:B{
            Var $0:Int;
            $foo(i:Array [Boolean ,0105]){
                a=0105;
                b.c(Self,Null,Array(1)).d=0x12DEF;
                d[e][f[g]]=0B1010111011101;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType)),MethodDecl(Id($foo),Static,[param(Id(i),ArrayType(69,BoolType))],Block([AssignStmt(Id(a),IntLit(69)),AssignStmt(FieldAccess(CallExpr(Id(b),Id(c),[Self(),NullLiteral(),[IntLit(1)]]),Id(d)),IntLit(77295)),AssignStmt(ArrayCell(Id(d),[Id(e),ArrayCell(Id(f),[Id(g)])]),IntLit(5597))]))])])'
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_344(self):
        input = """
        Class A:B{
            Var $0,a,$1,b,$2,c:Int = 5,4,3,2,1,0;
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(4))),AttributeDecl(Static,VarDecl(Id($1),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($2),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(0)))])])'
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_345(self):
        input = """
        Class A:B{
            Foo(){
                If(1){}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 345))
    def test_346(self):
        input = """
        Class A:B{
            Foo(){
                If(1){}
                If(2){}Else{}
                If(3){}Elseif(4){}Else{a=1;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(4),Block([]),Block([AssignStmt(Id(a),IntLit(1))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 346))
    def test_347(self):
        input = """
        Class A:B{
            Foo(){
                If(3){}Elseif(4){}Elseif(5){}Else{a=1;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([]),If(IntLit(4),Block([]),If(IntLit(5),Block([]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 347))
    def test_348(self):
        input = """
        Class A:B{
            Foo(){
                a.b(1+2,3*4-5.5);
                If(1)
                    {}
                Elseif(2)
                    {}
                Elseif(3)
                    {}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(a),Id(b),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,BinaryOp(*,IntLit(3),IntLit(4)),FloatLit(5.5))]),If(IntLit(1),Block([]),If(IntLit(2),Block([]),If(IntLit(3),Block([]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 348))
    def test_349(self):
        input = """
        Class A: B
        {
            Foo()
            {
                If(3)
                    {Val a: Int = 0X1234;}
                Elseif(4)
                    {{}}
                Elseif(5)
                    {Return Self;}
                Else
                    {a = 1;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([ConstDecl(Id(a),IntType,IntLit(4660))]),If(IntLit(4),Block([Block([])]),If(IntLit(5),Block([Return(Self())]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_350(self):
        line = '''Class D:__p{}Class c{}Class _73_{}Class I_:C{Destructor (){ {l::$0V4___();} }}'''
        expect = '''Program([ClassDecl(Id(D),Id(__p),[]),ClassDecl(Id(c),[]),ClassDecl(Id(_73_),[]),ClassDecl(Id(I_),Id(C),[MethodDecl(Id(Destructor),Instance,[],Block([Block([Call(Id(l),Id($0V4___),[])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 350))
    def test_351(self):
        line = '''Class Y7t_C2_oW:g__{Constructor (_,s,AN4_F,__,g,_s:v;_:VZV2_;k_,_k,_4,P:Float ){_::$aJ.HF_.UZ._();} }Class _:__{}'''
        expect = '''Program([ClassDecl(Id(Y7t_C2_oW),Id(g__),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(v))),param(Id(s),ClassType(Id(v))),param(Id(AN4_F),ClassType(Id(v))),param(Id(__),ClassType(Id(v))),param(Id(g),ClassType(Id(v))),param(Id(_s),ClassType(Id(v))),param(Id(_),ClassType(Id(VZV2_))),param(Id(k_),FloatType),param(Id(_k),FloatType),param(Id(_4),FloatType),param(Id(P),FloatType)],Block([Call(FieldAccess(FieldAccess(FieldAccess(Id(_),Id($aJ)),Id(HF_)),Id(UZ)),Id(_),[])]))]),ClassDecl(Id(_),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 351))
    def test_352(self):
        line = '''Class G{$Z3(p,_:Array [Array [Array [Int ,0B1001100],061],0b1_0];M:Float ;K,v5_:Int ;p,_,t:_){_::$_()._0._EkG();}$0(j9,E_,_:j){}$_(_xy:Array [Boolean ,061]){} }Class _:_AE{}'''
        expect = '''Program([ClassDecl(Id(G),[MethodDecl(Id($Z3),Static,[param(Id(p),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(_),ArrayType(2,ArrayType(49,ArrayType(76,IntType)))),param(Id(M),FloatType),param(Id(K),IntType),param(Id(v5_),IntType),param(Id(p),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(t),ClassType(Id(_)))],Block([Call(FieldAccess(CallExpr(Id(_),Id($_),[]),Id(_0)),Id(_EkG),[])])),MethodDecl(Id($0),Static,[param(Id(j9),ClassType(Id(j))),param(Id(E_),ClassType(Id(j))),param(Id(_),ClassType(Id(j)))],Block([])),MethodDecl(Id($_),Static,[param(Id(_xy),ArrayType(49,BoolType))],Block([]))]),ClassDecl(Id(_),Id(_AE),[])])'''
        self.assertTrue(TestAST.test(line, expect, 352))
    def test_353_683_PN(self):
        line = """Class D{Var _9f1,_:l_;}Class m_:r_{Val $_:Int =---"\\t";Var _17_:Int ;}"""
        expect = '''Program([ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_9f1),ClassType(Id(l_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(l_)),NullLiteral()))]),ClassDecl(Id(m_),Id(r_),[AttributeDecl(Static,ConstDecl(Id($_),IntType,UnaryOp(-,UnaryOp(-,UnaryOp(-,StringLit(\\t)))))),AttributeDecl(Instance,VarDecl(Id(_17_),IntType))])])'''
        self.assertTrue(TestAST.test(line, expect, 353))
    def test_354_905_PN(self):
        line = '''Class _{}Class l__:_k_6t{}Class W{Val T4:String =!!J_::$__;}'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(l__),Id(_k_6t),[]),ClassDecl(Id(W),[AttributeDecl(Instance,ConstDecl(Id(T4),StringType,UnaryOp(!,UnaryOp(!,FieldAccess(Id(J_),Id($__))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 354))
    def test_355_745_PN(self):
        line = '''Class _:x4_{Val _GO:k=!__.F()<=yYF9::$7._()._A_N._.L7K+!tW0::$iw_9();}'''
        expect = '''Program([ClassDecl(Id(_),Id(x4_),[AttributeDecl(Instance,ConstDecl(Id(_GO),ClassType(Id(k)),BinaryOp(<=,UnaryOp(!,CallExpr(Id(__),Id(F),[])),BinaryOp(+,FieldAccess(FieldAccess(FieldAccess(CallExpr(FieldAccess(Id(yYF9),Id($7)),Id(_),[]),Id(_A_N)),Id(_)),Id(L7K)),UnaryOp(!,CallExpr(Id(tW0),Id($iw_9),[]))))))])])'''
        self.assertTrue(TestAST.test(line, expect, 355))
    def test_356_646_PN(self):
        line = '''Class _V_7{Var _86:Int =!-New k___()._.j_Z._._s3();Destructor (){} }Class _{Var $_5_,z_:Array [Array [String ,2],80];}'''
        expect = '''Program([ClassDecl(Id(_V_7),[AttributeDecl(Instance,VarDecl(Id(_86),IntType,UnaryOp(!,UnaryOp(-,CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(k___),[]),Id(_)),Id(j_Z)),Id(_)),Id(_s3),[]))))),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_5_),ArrayType(80,ArrayType(2,StringType)))),AttributeDecl(Instance,VarDecl(Id(z_),ArrayType(80,ArrayType(2,StringType))))])])'''
        self.assertTrue(TestAST.test(line, expect, 356))
    def test_357_597_PN(self):
        line = '''Class _j{Constructor (_,_4m_q_R6r:_){}Var $o:String ;Val $3O:H=_::$_;}'''
        expect = '''Program([ClassDecl(Id(_j),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_4m_q_R6r),ClassType(Id(_)))],Block([])),AttributeDecl(Static,VarDecl(Id($o),StringType)),AttributeDecl(Static,ConstDecl(Id($3O),ClassType(Id(H)),FieldAccess(Id(_),Id($_))))])])'''
        self.assertTrue(TestAST.test(line, expect, 357))
    def test_358_313_PN(self):
        line = '''Class _:qc0R{}Class E{Var _:E=-New _().kD9.p.F.d().k.h6e71_;}'''
        expect = '''Program([ClassDecl(Id(_),Id(qc0R),[]),ClassDecl(Id(E),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(E)),UnaryOp(-,FieldAccess(FieldAccess(CallExpr(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(_),[]),Id(kD9)),Id(p)),Id(F)),Id(d),[]),Id(k)),Id(h6e71_)))))])])'''
        self.assertTrue(TestAST.test(line, expect, 358))
    def test_359_233_PN(self):
        line = '''Class R:_{}Class _8_:_B{}Class _:_4{Var $b:Array [String ,0B1]=!-Self ;}'''
        expect = '''Program([ClassDecl(Id(R),Id(_),[]),ClassDecl(Id(_8_),Id(_B),[]),ClassDecl(Id(_),Id(_4),[AttributeDecl(Static,VarDecl(Id($b),ArrayType(1,StringType),UnaryOp(!,UnaryOp(-,Self()))))])])'''
        self.assertTrue(TestAST.test(line, expect, 359))
    def test_360(self):
        line = '''Class R:_{foo(){New a(1).a();}}'''
        expect = '''Program([ClassDecl(Id(R),Id(_),[MethodDecl(Id(foo),Instance,[],Block([Call(NewExpr(Id(a),[IntLit(1)]),Id(a),[])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 360))
    def test_361(self):
        line = '''
                Class Shape2 {
            $getNumOfShape() {
                If (a == (1+1) ){
                    Var b,c:Boolean = True, False;
                }
                Foreach (i In 1 .. 100 By 2) {
                     Var a:Boolean = True;
                }
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(Shape2),[MethodDecl(Id($getNumOfShape),Static,[],Block([If(BinaryOp(==,Id(a),BinaryOp(+,IntLit(1),IntLit(1))),Block([VarDecl(Id(b),BoolType,BooleanLit(True)),VarDecl(Id(c),BoolType,BooleanLit(False))])),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 361))
    def test_362(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1+1 .. 100+100 By a.foo(1+2*3,"abc"+.1+2)){}
                    }
                }
            """
        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(a),Id(foo),[BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))]),Block([])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 362))
    def test_363(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
                        }
                    }
                }
                """
        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([For(Id(x),CallExpr(Id(a),Id($b),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(c)),Id(c)),Id(c)),FieldAccess(Id(a),Id($foo)),Block([])])])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 363))
    def test_364(self):
        line = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            Foreach(x In 1 .. 100 By 2){
                                If ( a == -1--1){
                                    Foreach(x In 1 .. 100 By 2){

                                    }
                                }
                            }
                        }
                    }
                }
                """

        expect = '''Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([])])]))])])]))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 364))
    def test_365(self):
        line = """
        Class Program{
            main(){}
            main(a,b,c:Int){}
        }
        Class DelPhaiProgram{
            main(){}
        }
        """

        expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([]))]),ClassDecl(Id(DelPhaiProgram),[MethodDecl(Id(main),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 365))
    def test_366(self):
        """Static access, instance and index combine"""
        input = """Class Program {
            Val b : Int = ClassABC::$a.a.c.b[1][2][3][(0 + 012 + 0xA2 + 0XA2 +0b101+0B101)];
            Var c : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(ClassABC),Id($a)),Id(a)),Id(c)),Id(b)),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(10)),IntLit(162)),IntLit(162)),IntLit(5)),IntLit(5))]))),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0))))])])"
        self.assertTrue(TestAST.test(input, expect, 366))
    def test_367(self):
        """Static access, instance and index combine"""
        input = """Class Program {
            a() {
                Val c, d : Float = .e5 , 1e-1;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(c),FloatType,FloatLit(0.0)),ConstDecl(Id(d),FloatType,FloatLit(0.1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))
    def test_368(self):
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
        self.assertTrue(TestAST.test(input, expect, 368))
    def test_369(self):
        input = """Class Program {
            main() {
                a[1][exp::$b().c[exp::$b().c[exp::$b().c]]] = 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(FieldAccess(CallExpr(Id(exp),Id($b),[]),Id(c)),[ArrayCell(FieldAccess(CallExpr(Id(exp),Id($b),[]),Id(c)),[FieldAccess(CallExpr(Id(exp),Id($b),[]),Id(c))])])]),IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))
    def test_370(self):
        input = """Class Program {
            a() {
                A.a.a.foo();
                (a.a[1][2][3]).foo();
                MotorBike::$ab.foo();
                (MotorBike::$a.a[1][2]).foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([Call(FieldAccess(FieldAccess(Id(A),Id(a)),Id(a)),Id(foo),[]),Call(ArrayCell(FieldAccess(Id(a),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(foo),[]),Call(FieldAccess(Id(MotorBike),Id($ab)),Id(foo),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(MotorBike),Id($a)),Id(a)),[IntLit(1),IntLit(2)]),Id(foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """Class D{
            Var _9f1, $_: l_;
            foo(){
                Var a,b:I;
            }
        }"""
        expect = "Program([ClassDecl(Id(D),[AttributeDecl(Instance,VarDecl(Id(_9f1),ClassType(Id(l_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(l_)),NullLiteral())),MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ClassType(Id(I)),NullLiteral()),VarDecl(Id(b),ClassType(Id(I)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))
    def test_372(self):
        input = """
	Class NodeClass {
		Var data : Int;
		Val next : NodeClass;

		Constructor(d : Int)
		{
			data = d;
			next = Null;
		}

        ## Function to reverse the linked list ##
        reverse(nodePoint : NodeClass)
        {
            Var prev : NodeClass = Null;
            Val current : NodeClass = nodePoint;
            Val next : NodeClass = Null;
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
            nodePoint = prev;
            Return nodePoint;
        }

        printList(nodePoint : NodeClass)
        {
            Foreach (a In 1 .. infinity By 1) {
                If (nodePoint != Null) {
                    System.out.print(nodePoint.data +. " ");
                    nodePoint = nodePoint.next;
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
            list.head = New NodeClass(85);
            list.head.next = New NodeClass(15);
            list.head.next.next = New NodeClass(4);
            list.head.next.next.next = New NodeClass(20);

            System.out.println("Given Linked list");
            list.printList(head);
            head = list.reverse(head);
            System.out.println("");
            System.out.println("Reversed linked list ");
            list.printList(head);
        }
    }
        """
        expect = """Program([ClassDecl(Id(NodeClass),[AttributeDecl(Instance,VarDecl(Id(data),IntType)),AttributeDecl(Instance,ConstDecl(Id(next),ClassType(Id(NodeClass)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(d),IntType)],Block([AssignStmt(Id(data),Id(d)),AssignStmt(Id(next),NullLiteral())])),MethodDecl(Id(reverse),Instance,[param(Id(nodePoint),ClassType(Id(NodeClass)))],Block([VarDecl(Id(prev),ClassType(Id(NodeClass)),NullLiteral()),ConstDecl(Id(current),ClassType(Id(NodeClass)),Id(nodePoint)),ConstDecl(Id(next),ClassType(Id(NodeClass)),NullLiteral()),For(Id(i),IntLit(1),Id(forever),IntLit(1),Block([If(BinaryOp(==,Id(current),NullLiteral()),Block([Break]),Block([AssignStmt(Id(next),FieldAccess(Id(current),Id(next))),AssignStmt(FieldAccess(Id(current),Id(next)),Id(prev)),AssignStmt(Id(prev),Id(current)),AssignStmt(Id(current),Id(next))]))])]),AssignStmt(Id(nodePoint),Id(prev)),Return(Id(nodePoint))])),MethodDecl(Id(printList),Instance,[param(Id(nodePoint),ClassType(Id(NodeClass)))],Block([For(Id(a),IntLit(1),Id(infinity),IntLit(1),Block([If(BinaryOp(!=,Id(nodePoint),NullLiteral()),Block([Call(FieldAccess(Id(System),Id(out)),Id(print),[BinaryOp(+.,FieldAccess(Id(nodePoint),Id(data)),StringLit( ))]),AssignStmt(Id(nodePoint),FieldAccess(Id(nodePoint),Id(next)))]),Block([Break]))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([ConstDecl(Id(list),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(list),Id(head)),NewExpr(Id(NodeClass),[IntLit(85)])),AssignStmt(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),NewExpr(Id(NodeClass),[IntLit(15)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),NewExpr(Id(NodeClass),[IntLit(4)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),Id(next)),NewExpr(Id(NodeClass),[IntLit(20)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Given Linked list)]),Call(Id(list),Id(printList),[Id(head)]),AssignStmt(Id(head),CallExpr(Id(list),Id(reverse),[Id(head)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit()]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Reversed linked list )]),Call(Id(list),Id(printList),[Id(head)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    def test_373(self):
        input = """
        Class Cak {
            abcdeFu123(str: Array[String, 10]) {
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
        Val firstMatrix : TheMatrix = New Basic2DMatrix(matrixProvider.getFirstMatrix());
        Val secondMatrix : TheMatrix = New Basic2DMatrix(matrixProvider.getSecondMatrix());

        Return firstMatrix.multiply(secondMatrix);
    }
        }
        Class Program {
            main() {
                Val const1, const2: Int = 1 + 5, 2;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Var a : Int = a.b.c.d();
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Cak),[MethodDecl(Id(abcdeFu123),Instance,[param(Id(str),ArrayType(10,StringType))],Block([ConstDecl(Id(parameters),ClassType(Id(Map)),CallExpr(Id(SomeClass),Id($parseParameters),[Id(args)])),ConstDecl(Id(builder),ClassType(Id(ChainedOptionsBuilder)),CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(NewExpr(Id(OptionsBuilder),[]),Id(include),[CallExpr(FieldAccess(Id(BigMatrixMultiplicationBenchmarking),Id(class)),Id(getSimpleName),[])]),Id(mode),[FieldAccess(Id(Mode),Id(AverageTime))]),Id(forks),[IntLit(2)]),Id(warmupIterations),[IntLit(10)]),Id(measurementIterations),[IntLit(10)]),Id(timeUnit),[FieldAccess(Id(TimeUnit),Id(SECONDS))])),Return(CallExpr(NewExpr(Id(Runner),[CallExpr(Id(builder),Id(build),[])]),Id(run),[]))])),MethodDecl(Id(homemadeMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([Return(CallExpr(Id(HomemadeMatrix),Id(multiplyMatrices),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[]),CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])]))])),MethodDecl(Id(nd4jMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(firstMatrix),ClassType(Id(INDArray)),CallExpr(Id(Nd4j),Id(create),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(INDArray)),CallExpr(Id(Nd4j),Id(create),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(mmul),[Id(secondMatrix)]))])),MethodDecl(Id(coltMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(doubleFactory2D),ClassType(Id(DoubleFactory2D)),FieldAccess(Id(DoubleFactory2D),Id(dense))),ConstDecl(Id(firstMatrix),ClassType(Id(DoubleMatrix2D)),CallExpr(Id(doubleFactory2D),Id(make),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(DoubleMatrix2D)),CallExpr(Id(doubleFactory2D),Id(make),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),VarDecl(Id(algebra),ClassType(Id(Algebra)),NewExpr(Id(Algebra),[])),Return(CallExpr(Id(algebra),Id(mult),[Id(firstMatrix),Id(secondMatrix)]))])),MethodDecl(Id(ejmlMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([VarDecl(Id(firstMatrix),ClassType(Id(SimpleMatrix)),NewExpr(Id(SimpleMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),VarDecl(Id(secondMatrix),ClassType(Id(SimpleMatrix)),NewExpr(Id(SimpleMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(mult),[Id(secondMatrix)]))])),MethodDecl(Id(apacheCommonsMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([VarDecl(Id(firstMatrix),ClassType(Id(RealMatrix)),NewExpr(Id(Array2DRowRealMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(RealMatrix)),NewExpr(Id(Array2DRowRealMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(multiply),[Id(secondMatrix)]))])),MethodDecl(Id(la4jMatrixMultiplication),Instance,[param(Id(matrixProvider),ClassType(Id(BigMatrixProvider)))],Block([ConstDecl(Id(firstMatrix),ClassType(Id(TheMatrix)),NewExpr(Id(Basic2DMatrix),[CallExpr(Id(matrixProvider),Id(getFirstMatrix),[])])),ConstDecl(Id(secondMatrix),ClassType(Id(TheMatrix)),NewExpr(Id(Basic2DMatrix),[CallExpr(Id(matrixProvider),Id(getSecondMatrix),[])])),Return(CallExpr(Id(firstMatrix),Id(multiply),[Id(secondMatrix)]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(const1),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(const2),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),VarDecl(Id(a),IntType,CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[])),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))
    def test_374(self):
        input = """
        Class Map {
            Val bean: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(bean: Array[String, 10]; value: Array[String, 10]) {
                Self.bean = bean;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.bean);
                Self.clean(Self.value);
                Return;
            }
            clean() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.bean.length() By 1)
                {
                    el = Self.bean[k];

                    Self.free(el);
                    Self.bean = Null;
                }
                Self.free(bean);
                Self.bean = Null;
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
                Val const1, const2: Int = 1 + 5, 2;
                Var x, y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Map),[AttributeDecl(Instance,ConstDecl(Id(bean),ArrayType(10,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(value),ArrayType(10,StringType),None)),MethodDecl(Id(Constructor),Instance,[param(Id(bean),ArrayType(10,StringType)),param(Id(value),ArrayType(10,StringType))],Block([AssignStmt(FieldAccess(Self(),Id(bean)),Id(bean)),AssignStmt(FieldAccess(Self(),Id(value)),Id(value)),Return()])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(clean),[FieldAccess(Self(),Id(bean))]),Call(Self(),Id(clean),[FieldAccess(Self(),Id(value))]),Return()])),MethodDecl(Id(clean),Instance,[],Block([Call(Id(Out),Id(println),[StringLit(Cleaning)]),For(Id(k),IntLit(0),CallExpr(FieldAccess(Self(),Id(bean)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(Self(),Id(bean)),[Id(k)])),Call(Self(),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(bean)),NullLiteral())])]),Call(Self(),Id(free),[Id(bean)]),AssignStmt(FieldAccess(Self(),Id(bean)),NullLiteral()),For(Id(v),IntLit(0),CallExpr(FieldAccess(Self(),Id(value)),Id(length),[]),IntLit(1),Block([AssignStmt(Id(el),ArrayCell(FieldAccess(FieldAccess(Self(),Id(value)),Id(a)),[Id(v)])),Call(Self(),Id(free),[Id(el)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral())])]),Call(Self(),Id(free),[Id(value)]),AssignStmt(FieldAccess(Self(),Id(value)),NullLiteral()),ConstDecl(Id(a),BoolType,BooleanLit(True)),ConstDecl(Id(b),IntType,IntLit(1)),Return(BinaryOp(&&,BinaryOp(||,BooleanLit(True),BooleanLit(False)),BinaryOp(==,Id(a),Id(b))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([ConstDecl(Id(const1),IntType,BinaryOp(+,IntLit(1),IntLit(5))),ConstDecl(Id(const2),IntType,IntLit(2)),VarDecl(Id(x),IntType,IntLit(0)),VarDecl(Id(y),IntType,IntLit(0)),ConstDecl(Id(sth),ClassType(Id(Sth)),NewExpr(Id(Sth),[])),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))
    def test_375(self):
        input = '''
        Class Mine:Arr{
            func(){
                Var a: Array[Float, 01];
                Var a: Array[Float, 0x1];
                Var a: Array[Float, 0X1];
                Var a: Array[Float, 0b1];
                Var a: Array[Float, 0B1];
                Var a: Array[Float, 1];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Mine),Id(Arr),[MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(a),ArrayType(1,FloatType)),VarDecl(Id(a),ArrayType(1,FloatType)),VarDecl(Id(a),ArrayType(1,FloatType)),VarDecl(Id(a),ArrayType(1,FloatType)),VarDecl(Id(a),ArrayType(1,FloatType)),VarDecl(Id(a),ArrayType(1,FloatType))]))])])'
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = '''
        Class Mine:Arr{
            func(){
                Var a: Array[Int, 1] = 1_23.456e+7990;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Mine),Id(Arr),[MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType),FloatLit(inf))]))])])'
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = '''
        Class Program{
            main(){
                Return Arr[1][2][3][3+1][4];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(ArrayCell(Id(Arr),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,IntLit(3),IntLit(1)),IntLit(4)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = '''
        Class Program {
            main() {
                (abc[123]).funct();
                a[123] = "1";
                Out.println(f.a[1]);
                ((((efh[32][1]).a[21]).funct()[0]).a[21]).funct();
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(abc),[IntLit(123)]),Id(funct),[]),AssignStmt(ArrayCell(Id(a),[IntLit(123)]),StringLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(f),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(efh),[IntLit(32),IntLit(1)]),Id(a)),[IntLit(21)]),Id(funct),[]),[IntLit(0)]),Id(a)),[IntLit(21)]),Id(funct),[]),Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = '''
        Class Shape{
            func_tion(){
                Return A::$B * C::$DD--F::$H;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([Return(BinaryOp(-,BinaryOp(*,FieldAccess(Id(A),Id($B)),FieldAccess(Id(C),Id($DD))),UnaryOp(-,FieldAccess(Id(F),Id($H)))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = '''
        Class Shape{
            func_tion(){
                Foreach (Step In 1+1 .. 100+100 By D.func_tion()){}
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([For(Id(Step),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(D),Id(func_tion),[]),Block([])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = '''
        Class Shape{
            func_tion(){
               A[b[c[d[e[f::$g]]]]][h::$i][j.k()][F::$DDD()]=0;
            }
        }   
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([AssignStmt(ArrayCell(Id(A),[ArrayCell(Id(b),[ArrayCell(Id(c),[ArrayCell(Id(d),[ArrayCell(Id(e),[FieldAccess(Id(f),Id($g))])])])]),FieldAccess(Id(h),Id($i)),CallExpr(Id(j),Id(k),[]),CallExpr(Id(F),Id($DDD),[])]),IntLit(0))]))])])'
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = '''
        Class Shape{
            func_tion(){
                If (a == -1--1){
                    If(b == "c"+."c"){}
                    Elseif(SHAPE == b ==. c){}
                }
            }
        }   
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([If(BinaryOp(+.,BinaryOp(==,Id(b),StringLit(c)),StringLit(c)),Block([]),If(BinaryOp(==.,BinaryOp(==,Id(SHAPE),Id(b)),Id(c)),Block([])))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = '''
        Class Shape{
            $a(){
                Break;
                Continue;
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id($a),Static,[],Block([Break,Continue,Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = '''
        Class Shape{
            $a(){
                Break;
                Continue;
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id($a),Static,[],Block([Break,Continue,Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = '''
        Class League_of_Legend{
           Destructor(){
            Status = 0x123;
            Return;
            Run::$Client.start();
            } 
        }

        Class Master:Rank{}
        '''
        expect = 'Program([ClassDecl(Id(League_of_Legend),[MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(Status),IntLit(291)),Return(),Call(FieldAccess(Id(Run),Id($Client)),Id(start),[])]))]),ClassDecl(Id(Master),Id(Rank),[])])'
        self.assertTrue(TestAST.test(input, expect, 385))
    def test_386(self):
        input = """
        Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
            }
            Class DellLap:Electrical{
                start(){
                    DellLap::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(ElectricalDevice),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType)),AttributeDecl(Instance,VarDecl(Id(useBattery),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat))]))]),ClassDecl(Id(DellLap),Id(Electrical),[MethodDecl(Id(start),Instance,[],Block([Call(Id(DellLap),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = """
        Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
                Var $numOfDevices: Int;
                Var $devices: Array[Float, 100];
                Constructor(){}
                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }
                Destructor(){}

            }
        """
        expect = "Program([ClassDecl(Id(ElectricalDevice),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType)),AttributeDecl(Instance,VarDecl(Id(useBattery),BoolType)),AttributeDecl(Static,VarDecl(Id($numOfDevices),IntType)),AttributeDecl(Static,VarDecl(Id($devices),ArrayType(100,FloatType))),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat)),AssignStmt(ArrayCell(FieldAccess(Id(ElectricalDevice),Id($devices)),[FieldAccess(Id(ElectricalDevice),Id($numOfDevices))]),Self()),AssignStmt(FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),BinaryOp(+,FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = """
        Class DellLap:Electrical{

                $Refresh(){
                    Foreach(i In ElectricalDevice::$numOfDevices .. 0 By -1){

                    }
                }
                start(){
                    DellLap::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(DellLap),Id(Electrical),[MethodDecl(Id($Refresh),Static,[],Block([For(Id(i),FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(0),UnaryOp(-,IntLit(1)),Block([])])])),MethodDecl(Id(start),Instance,[],Block([Call(Id(DellLap),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """
        Class DellLap:Electrical{
                Var $NoDellLap: Int;
                Var $laptops: Array[Boolean, 100];

                $Refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        (laptops[i]).refresh();
                    }
                }
                start(){
                    DellLap::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
        }
        """
        expect = "Program([ClassDecl(Id(DellLap),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($NoDellLap),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id($Refresh),Static,[],Block([For(Id(i),BinaryOp(+,BinaryOp(/,BinaryOp(*,FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(100)),IntLit(100)),IntLit(1)),BinaryOp(+,BinaryOp(-,IntLit(100),IntLit(100)),BinaryOp(%,IntLit(35),IntLit(34))),UnaryOp(-,IntLit(1)),Block([Call(ArrayCell(Id(laptops),[Id(i)]),Id(refresh),[])])])])),MethodDecl(Id(start),Instance,[],Block([Call(Id(DellLap),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """
        Class DellLap:Electrical{
                Var $NoDellLap: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    DellLap::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }
        }
        """
        expect = "Program([ClassDecl(Id(DellLap),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($NoDellLap),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat)),AssignStmt(ArrayCell(FieldAccess(Id(ElectricalDevice),Id($devices)),[FieldAccess(Id(ElectricalDevice),Id($numOfDevices))]),Self()),AssignStmt(ArrayCell(FieldAccess(Id(DellLap),Id($laptops)),[FieldAccess(Id(ElectricalDevice),Id($numOfDevices))]),Self()),AssignStmt(FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),BinaryOp(+,FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """
        Class DellLap:Electrical{
                Var $NoDellLap: Int;
                Var $laptops: Array[Boolean, 100];

                start(){
                    DellLap::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
        }
        """
        expect = "Program([ClassDecl(Id(DellLap),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($NoDellLap),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id(start),Instance,[],Block([Call(Id(DellLap),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """
        Class DellLap:Electrical{
                Var $NoDellLap: Int;
                Var $laptops: Array[Boolean, 100];

                $checkVirus(){
                    Foreach(i In DellLap::$NoDellLap/100*100 + 1 .. 100-100+35%34 By -1){
                        If ((laptops[i]).checked == True){
                            Continue;
                        }
                        Else{
                            (laptops[i]).checked = True;
                        }
                    }
                }
        }
        """
        expect = "Program([ClassDecl(Id(DellLap),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($NoDellLap),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id($checkVirus),Static,[],Block([For(Id(i),BinaryOp(+,BinaryOp(*,BinaryOp(/,FieldAccess(Id(DellLap),Id($NoDellLap)),IntLit(100)),IntLit(100)),IntLit(1)),BinaryOp(+,BinaryOp(-,IntLit(100),IntLit(100)),BinaryOp(%,IntLit(35),IntLit(34))),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(==,FieldAccess(ArrayCell(Id(laptops),[Id(i)]),Id(checked)),BooleanLit(True)),Block([Continue]),Block([AssignStmt(FieldAccess(ArrayCell(Id(laptops),[Id(i)]),Id(checked)),BooleanLit(True))]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = """
        Class iPhone:ElectricalDevice{
                Val $os: String = "iOS";
                Var number: String; 
                Var $numOfPhones: Int;
                Var $phone: Array[Boolean, 100];

                Constructor(){

                }
                Destructor(){

                }
            }
        """
        expect = "Program([ClassDecl(Id(iPhone),Id(ElectricalDevice),[AttributeDecl(Static,ConstDecl(Id($os),StringType,StringLit(iOS))),AttributeDecl(Instance,VarDecl(Id(number),StringType)),AttributeDecl(Static,VarDecl(Id($numOfPhones),IntType)),AttributeDecl(Static,VarDecl(Id($phone),ArrayType(100,BoolType))),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = """
        Class iPhone:ElectricalDevice{
                Val $os: String = "iOS";
                Var number: String; 
                Var $numOfPhones: Int;
                Var $phone: Array[Boolean, 100];

                insertSIM(sim: SIM){
                    Self.number = SIM.number;
                }

                detachSIM(){
                    Self.number = Null;
                }
            }
        """
        expect = "Program([ClassDecl(Id(iPhone),Id(ElectricalDevice),[AttributeDecl(Static,ConstDecl(Id($os),StringType,StringLit(iOS))),AttributeDecl(Instance,VarDecl(Id(number),StringType)),AttributeDecl(Static,VarDecl(Id($numOfPhones),IntType)),AttributeDecl(Static,VarDecl(Id($phone),ArrayType(100,BoolType))),MethodDecl(Id(insertSIM),Instance,[param(Id(sim),ClassType(Id(SIM)))],Block([AssignStmt(FieldAccess(Self(),Id(number)),FieldAccess(Id(SIM),Id(number)))])),MethodDecl(Id(detachSIM),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(number)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """
        Class RommSSaaa{
                Var $NoStu : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     RommSSaaa::$studentList[RommSSaaa::$NoStu] = newStu;
                } 
            }
            Class Student{}
        """
        expect = "Program([ClassDecl(Id(RommSSaaa),[AttributeDecl(Static,VarDecl(Id($NoStu),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($studentList),ArrayType(40,StringType))),MethodDecl(Id(addStudent),Instance,[param(Id(newStu),ClassType(Id(Student)))],Block([AssignStmt(ArrayCell(FieldAccess(Id(RommSSaaa),Id($studentList)),[FieldAccess(Id(RommSSaaa),Id($NoStu))]),Id(newStu))]))]),ClassDecl(Id(Student),[])])"
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """
        Class RommSSaaa{
                Var $NoStu : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     RommSSaaa::$studentList.append(newStu);
                } 
            }
        """
        expect = "Program([ClassDecl(Id(RommSSaaa),[AttributeDecl(Static,VarDecl(Id($NoStu),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($studentList),ArrayType(40,StringType))),MethodDecl(Id(addStudent),Instance,[param(Id(newStu),ClassType(Id(Student)))],Block([Call(FieldAccess(Id(RommSSaaa),Id($studentList)),Id(append),[Id(newStu)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """
        Class Student{
                Constructor(){
                    RommSSaaa::$NoStu = RommSSaaa::$NoStu + 1;
                }
                Destructor(){}
            }
        """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(RommSSaaa),Id($NoStu)),BinaryOp(+,FieldAccess(Id(RommSSaaa),Id($NoStu)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """
        Class Student{
                Constructor(){
                    RommSSaaa::$NoStu = RommSSaaa::$NoStu + 1;
                }
                Destructor(){
                    RommSSaaa::$NoStu = RommSSaaa::$NoStu - 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(RommSSaaa),Id($NoStu)),BinaryOp(+,FieldAccess(Id(RommSSaaa),Id($NoStu)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(RommSSaaa),Id($NoStu)),BinaryOp(-,FieldAccess(Id(RommSSaaa),Id($NoStu)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = """
        Class Student{
                learn(){
                    Self.print("Learning");   
                }

                goToSchool(){
                    Self.byeMom();
                    Self.byeDad("by dad");    
                }

                Constructor(){
                    RommSSaaa::$NoStu = RommSSaaa::$NoStu + 1;
                }
                Destructor(){
                    RommSSaaa::$NoStu = RommSSaaa::$NoStu - 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(learn),Instance,[],Block([Call(Self(),Id(print),[StringLit(Learning)])])),MethodDecl(Id(goToSchool),Instance,[],Block([Call(Self(),Id(byeMom),[]),Call(Self(),Id(byeDad),[StringLit(by dad)])])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(RommSSaaa),Id($NoStu)),BinaryOp(+,FieldAccess(Id(RommSSaaa),Id($NoStu)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(RommSSaaa),Id($NoStu)),BinaryOp(-,FieldAccess(Id(RommSSaaa),Id($NoStu)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 399))