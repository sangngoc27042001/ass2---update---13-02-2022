import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_300(self):
    #     input = '''
    #     Class Program {
    #     main(){}
    #     }
    #     '''
    #     expect = 'Program([ClassDecl(Id(A),[])])'
    #     self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = '''
        Class A {}
        '''
        expect = 'Program([ClassDecl(Id(A),[])])'
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = '''
        Class A:B {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[])])'
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = '''
        Class A:B {}
        Class C {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[]),ClassDecl(Id(C),[])])'
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = '''
        Class A:B {}
        Class C:D {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[]),ClassDecl(Id(C),Id(D),[])])'
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = '''
        Class A:B {}
        Class C:D {}
        Class E {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[]),ClassDecl(Id(C),Id(D),[]),ClassDecl(Id(E),[])])'
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = '''
        Class A{
            Var N : Int;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(N),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = '''
        Class A{
            Var x,y,$z : Int;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),AttributeDecl(Static,VarDecl(Id($z),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = '''
        Class A{
            Val $x,$z,y : String;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),StringType,None)),AttributeDecl(Static,ConstDecl(Id($z),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(y),StringType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = '''
        Class A{
            Val $x :Int = 1;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(1)))])])'
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = '''
         Class A{
            Val $x, $y : Int = 1, 2+2;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($y),IntType,BinaryOp(+,IntLit(2),IntLit(2))))])])'
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = '''
         Class A{
            Val $x, $y : Int = 1, 2+2;
            Var p,$q : Boolean = True, False;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(p),BoolType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($q),BoolType,BooleanLit(False)))])])'
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = '''
        Class A{
           Var $x, $y : Int = 0, 0;
           Val a, $b : Int = 0x0, 0B0;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(0)))])])'
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = '''
        Class A{
            func(){}
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = '''
        Class C{
            func(a : Int){}
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[param(Id(a),IntType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = '''
        Class C{
            func(a : Int){
                Var x,y: Int = 1+1, 2+2;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[param(Id(a),IntType)],Block([VarDecl(Id(x),IntType,BinaryOp(+,IntLit(1),IntLit(1))),VarDecl(Id(y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = '''
        Class C{
            func(){
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[],Block([Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = '''
        Class C{
            func(){
                Return True;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[],Block([Return(BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = '''
        Class C{
            Constructor(a : Int){
                {}
                Return D;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([Block([]),Return(Id(D))]))])])'
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = '''
        Class C{
            Destructor(){ 
                ## Nothing ##
                Return GG;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(Destructor),Instance,[],Block([Return(Id(GG))]))])])'
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = '''
        Class C{
            func(a : Int){
                a = True;
                Return 2+3*4/5; 
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),BooleanLit(True)),Return(BinaryOp(+,IntLit(2),BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = '''
        Class Program{
            main(){
                Var x,y: Int = 1+1, 2+2;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,BinaryOp(+,IntLit(1),IntLit(1))),VarDecl(Id(y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = '''
        Class Program{
            main(a : Int){
                a = "String";
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),StringLit(String))]))])])'
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = '''
        Class Programming{
            Val $x: Int = 10_3;
            main(){
                Val y: Int = 11.23123;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(103))),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(y),IntType,FloatLit(11.23123))]))])])'
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = '''
        Class Programming{
            main(){
                If(1){
                Love = 0;
                }
                Elseif(2){
                Love = 1;}
                Else{
                Friendzone = True;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[MethodDecl(Id(main),Instance,[],Block([If(IntLit(1),Block([AssignStmt(Id(Love),IntLit(0))]),If(IntLit(2),Block([AssignStmt(Id(Love),IntLit(1))]),Block([AssignStmt(Id(Friendzone),BooleanLit(True))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = '''
        Class Programming{
            main(){
                If( (a < 2) && (b > 3)){
                    d = "OK";
                }
                Else{
                    e = "FAIL";
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(&&,BinaryOp(<,Id(a),IntLit(2)),BinaryOp(>,Id(b),IntLit(3))),Block([AssignStmt(Id(d),StringLit(OK))]),Block([AssignStmt(Id(e),StringLit(FAIL))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = '''
        Class Program{
            main(){
                If( number % 2 == 0){
                    System.printInt(Integer::$HEX);
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,BinaryOp(%,Id(number),IntLit(2)),IntLit(0)),Block([Call(Id(System),Id(printInt),[FieldAccess(Id(Integer),Id($HEX))])]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = '''
        Class Program{
            main(a : Int){
                Foreach (i In 1 .. 100 By 2) {
                Out.printInt(i);
                }
                Foreach (x In 5 .. 2) {
                Out.printInt(arr[x]);
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])]),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = '''
        Class Program{
            main(){
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])'
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = '''
        Class Program{
            main(a : Int){
                a = "String";
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),StringLit(String))]))])])'
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = '''
        Class Program{
            main(a : Int){
            If (1 + 2 == 0) {
                OutScreen.println(3 * 2);
            }
            Elseif (1 + 2 == "3") {
                Sys32.terminate(41241211 - "4124124124");
            }
            Else {
                Break;
                Return;
            }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(==,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(0)),Block([Call(Id(OutScreen),Id(println),[BinaryOp(*,IntLit(3),IntLit(2))])]),If(BinaryOp(==,BinaryOp(+,IntLit(1),IntLit(2)),StringLit(3)),Block([Call(Id(Sys32),Id(terminate),[BinaryOp(-,IntLit(41241211),StringLit(4124124124))])]),Block([Break,Return()])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = '''
        Class C{
                function(){
                    a = b%c + Self.foo();
                    a = b*c*d + Self.foo();
                    Self.foo();
                    Return True;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(function),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Self(),Id(foo),[]))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,BinaryOp(*,Id(b),Id(c)),Id(d)),CallExpr(Self(),Id(foo),[]))),Call(Self(),Id(foo),[]),Return(BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = '''
        Class B{
                main(){
                }
                foo(){
                    a = b%c + Self.foo();
                    Self.foo2(param1, param2);
                    a1 = Self.foo3(param1, param2);
                    b = 1 >= 3;
                    val1 = True == False;
                    b = ! val1;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(B),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Self(),Id(foo),[]))),Call(Self(),Id(foo2),[Id(param1),Id(param2)]),AssignStmt(Id(a1),CallExpr(Self(),Id(foo3),[Id(param1),Id(param2)])),AssignStmt(Id(b),BinaryOp(>=,IntLit(1),IntLit(3))),AssignStmt(Id(val1),BinaryOp(==,BooleanLit(True),BooleanLit(False))),AssignStmt(Id(b),UnaryOp(!,Id(val1)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = '''
        Class Vehicle{
                run(){
                    Self.running = True;
                }
                stop(){
                    Self.running = False;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(Vehicle),[MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = '''
        Class Vinfast{
            Var running: Boolean = True;
            Val speed: Int;
            Constructor(){
                Self.speed = 10000000;
            }
            Constructor(speed: Int){
                Self.speed = speed;
            }
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Vinfast),[AttributeDecl(Instance,VarDecl(Id(running),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(speed),IntType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(speed)),IntLit(10000000))])),MethodDecl(Id(Constructor),Instance,[param(Id(speed),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(speed)),Id(speed))])),MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = '''
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            open(){
                ## Open hood ##
                If (Hood==False){
                    Hood = True;
                    Return True;
                }
                Else{
                    Return False;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Car),Id(Vehicle),[AttributeDecl(Instance,ConstDecl(Id(sunScreen),BoolType,BooleanLit(False))),MethodDecl(Id(open),Instance,[],Block([If(BinaryOp(==,Id(Hood),BooleanLit(False)),Block([AssignStmt(Id(Hood),BooleanLit(True)),Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = '''
        Class Eval{
            getSpeedfromKm(a, b, c: Int; e, f: String){
                Outscreen.get("The speed = " +.  "1000km/h");
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Eval),[MethodDecl(Id(getSpeedfromKm),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),StringType),param(Id(f),StringType)],Block([Call(Id(Outscreen),Id(get),[BinaryOp(+.,StringLit(The speed = ),StringLit(1000km/h))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = '''
        Class Shape {
            foo(){
                a = ("a"+."b")+."b";
            } 
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+.,BinaryOp(+.,StringLit(a),StringLit(b)),StringLit(b)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = '''
        Class Shape {
            foo(){
                c = ("a"==."a")==True;
            } 
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(c),BinaryOp(==,BinaryOp(==.,StringLit(a),StringLit(a)),BooleanLit(True)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = '''
        Class Loop {
            function(){
                i=-1;
             } 
        }
        '''
        expect = 'Program([ClassDecl(Id(Loop),[MethodDecl(Id(function),Instance,[],Block([AssignStmt(Id(i),UnaryOp(-,IntLit(1)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = '''
        Class Sharp{
            foo(){
                _ID = New X().Y().Z();
                Var C : Array[Int, 0B1010];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Sharp),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(_ID),CallExpr(CallExpr(NewExpr(Id(X),[]),Id(Y),[]),Id(Z),[])),VarDecl(Id(C),ArrayType(10,IntType))]))])])'
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = '''
        Class Mine:Arr{
            func(){
                Var a: Array[Int, 01];
                Var a: Array[Int, 0x1];
                Var a: Array[Int, 0X1];
                Var a: Array[Int, 0b1];
                Var a: Array[Int, 0B1];
                Var a: Array[Int, 1];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Mine),Id(Arr),[MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType))]))])])'
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = '''
        Class Mine:Arr{
            func(){
                Var a: Array[Int, 1] = 1_23.456e+7990;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Mine),Id(Arr),[MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType),FloatLit(inf))]))])])'
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = '''
        Class Program{
            main(){
                Return Arr[1][2][3][3+1][4];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(ArrayCell(Id(Arr),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,IntLit(3),IntLit(1)),IntLit(4)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
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
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = '''
        Class Shape{
            func_tion(){
                Return A::$B * C::$DD--F::$H;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([Return(BinaryOp(-,BinaryOp(*,FieldAccess(Id(A),Id($B)),FieldAccess(Id(C),Id($DD))),UnaryOp(-,FieldAccess(Id(F),Id($H)))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = '''
        Class Shape{
            func_tion(){
                Foreach (Step In 1+1 .. 100+100 By D.func_tion()){}
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([For(Id(Step),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(D),Id(func_tion),[]),Block([])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = '''
        Class Shape{
            func_tion(){
               A[b[c[d[e[f::$g]]]]][h::$i][j.k()][F::$DDD()]=0;
            }
        }   
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([AssignStmt(ArrayCell(Id(A),[ArrayCell(Id(b),[ArrayCell(Id(c),[ArrayCell(Id(d),[ArrayCell(Id(e),[FieldAccess(Id(f),Id($g))])])])]),FieldAccess(Id(h),Id($i)),CallExpr(Id(j),Id(k),[]),CallExpr(Id(F),Id($DDD),[])]),IntLit(0))]))])])'
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
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
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
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
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_349(self):
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
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
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
        self.assertTrue(TestAST.test(input, expect, 350))







