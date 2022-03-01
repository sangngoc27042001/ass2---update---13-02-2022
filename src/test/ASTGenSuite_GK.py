import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """
        Class Program {}
        """
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,300))

    def test_301(self):
        input = "Class Motor:Vehicle {}"
        expect = "Program([ClassDecl(Id(Motor),Id(Vehicle),[])])"
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = "Class Motor {} Class Plane {} Class Train {}"
        expect = "Program([ClassDecl(Id(Motor),[]),ClassDecl(Id(Plane),[]),ClassDecl(Id(Train),[])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test_303(self):
        input = """
        Class Motor {
            Var maxSpeed:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Instance,VarDecl(Id(maxSpeed),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,303))

    def test_304(self):
        """Simple program: int main() {} """
        input = """
        Class Motor {
            Var maxSpeed:Int;
            Var haveAbs:Boolean;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Instance,VarDecl(Id(maxSpeed),IntType)),AttributeDecl(Instance,VarDecl(Id(haveAbs),BoolType))])])'
        self.assertTrue(TestAST.test(input,expect,304))

    def test_305(self):
        input = """
        Class Stock {
            Var motorStock:Array[Int,5];
        }
        """
        expect = 'Program([ClassDecl(Id(Stock),[AttributeDecl(Instance,VarDecl(Id(motorStock),ArrayType(5,IntType)))])])'
        self.assertTrue(TestAST.test(input,expect,305))

    def test_306(self):
        input = """
        Class Motor {
            Var numOfWheels:Int=2;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Instance,VarDecl(Id(numOfWheels),IntType,IntLit(2)))])])'
        self.assertTrue(TestAST.test(input,expect,306))

    def test_307(self):
        input = """
        Class Car {
            Var numOfWheels:Int=2+2;
        }
        """
        expect = 'Program([ClassDecl(Id(Car),[AttributeDecl(Instance,VarDecl(Id(numOfWheels),IntType,BinaryOp(+,IntLit(2),IntLit(2))))])])'
        self.assertTrue(TestAST.test(input,expect,307))

    def test_308(self):
        input = """
        Class A {
            Var a:Int=1+1*2;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(1),IntLit(2)))))])])'
        self.assertTrue(TestAST.test(input,expect,308))

    def test_309(self):
        input = """
        Class Motor {
            Var Name:Int=\"yamaha\"+.2+3;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Instance,VarDecl(Id(Name),IntType,BinaryOp(+.,StringLit(yamaha),BinaryOp(+,IntLit(2),IntLit(3)))))])])'
        self.assertTrue(TestAST.test(input,expect,309))
    def test_310(self):
        input = """
        Class Car {
            Var maxSpeed:Int=!!motorSpeed---3*---4;
        }
        """
        expect = 'Program([ClassDecl(Id(Car),[AttributeDecl(Instance,VarDecl(Id(maxSpeed),IntType,BinaryOp(-,UnaryOp(!,UnaryOp(!,Id(motorSpeed))),BinaryOp(*,UnaryOp(-,UnaryOp(-,IntLit(3))),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(4))))))))])])'
        self.assertTrue(TestAST.test(input,expect,310))

    def test_311(self):
        input = """
        Class Motor {
            Val over150cc:Boolean=False;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Instance,ConstDecl(Id(over150cc),BoolType,BooleanLit(False)))])])'
        self.assertTrue(TestAST.test(input,expect,311))

    def test_312(self):
        input = """
        Class Car {
            Val brand:String=specs[1][1];
        }
        """
        expect = 'Program([ClassDecl(Id(Car),[AttributeDecl(Instance,ConstDecl(Id(brand),StringType,ArrayCell(Id(specs),[IntLit(1),IntLit(1)])))])])'
        self.assertTrue(TestAST.test(input,expect,312))

    def test_313(self):
        """Simple program: int main() {} """
        input = """
        Class Motor {
            Var newWheel:Int = New Wheel();
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Instance,VarDecl(Id(newWheel),IntType,NewExpr(Id(Wheel),[])))])])'
        self.assertTrue(TestAST.test(input,expect,313))
    def test_314(self):
        """Simple program: int main() {} """
        input = """
        Class Car {
            Val Name:Int = Null;
        }
        """
        expect = 'Program([ClassDecl(Id(Car),[AttributeDecl(Instance,ConstDecl(Id(Name),IntType,NullLiteral()))])])'
        self.assertTrue(TestAST.test(input,expect,314))

    def test_315(self):
        """Simple program: int main() {} """
        input = """
        Class Train {
            Val section_1:Int = New Section("Section" + "1",Null);
        }
        """
        expect = 'Program([ClassDecl(Id(Train),[AttributeDecl(Instance,ConstDecl(Id(section_1),IntType,NewExpr(Id(Section),[BinaryOp(+,StringLit(Section),StringLit(1)),NullLiteral()])))])])'
        self.assertTrue(TestAST.test(input,expect,315))

    def test_316(self):
        """Simple program: int main() {} """
        input = """
        Class Motor {
            Var $maxSpeed:Float=100;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Static,VarDecl(Id($maxSpeed),FloatType,IntLit(100)))])])'
        self.assertTrue(TestAST.test(input,expect,316))

    def test_317(self):
        input = """
        Class Motor {
            run(){}
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = """
        Class Motor {
            run(min_speed,max_speed:Int;avg_speed:Float){}
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[param(Id(min_speed),IntType),param(Id(max_speed),IntType),param(Id(avg_speed),FloatType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """
        Class Motor {
            run(speed:Int;fast:Boolean;des:String){}
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[param(Id(speed),IntType),param(Id(fast),BoolType),param(Id(des),StringType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_320(self):
        input = """
        Class Motor {
            run(){
                Var speed:Int;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[],Block([VarDecl(Id(speed),IntType)]))])])'
        self.assertTrue(TestAST.test(input, expect, 320))
    def test_321(self):
        input = """
        Class Motor {
            fillGas(){
                Var Amount:Float = 10;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(fillGas),Instance,[],Block([VarDecl(Id(Amount),FloatType,IntLit(10))]))])])'
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = """
        Class Motor {
            run(){
                Var maxSpeed:Int = 100;
                Var avgSpeed:Float = 30;
                Val customized:Boolean = False;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[],Block([VarDecl(Id(maxSpeed),IntType,IntLit(100)),VarDecl(Id(avgSpeed),FloatType,IntLit(30)),ConstDecl(Id(customized),BoolType,BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 322))
    def test_323(self):
        input = """
        Class Motor {
            Var $count:Int = 1;
            stop(){
                Var status:Int = 0;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[AttributeDecl(Static,VarDecl(Id($count),IntType,IntLit(1))),MethodDecl(Id(stop),Instance,[],Block([VarDecl(Id(status),IntType,IntLit(0))]))])])'
        self.assertTrue(TestAST.test(input, expect, 323))
    def test_324(self):
        input = """
        Class Motor {
            carry(a,b,c,d,e:Int){
                Var people:Int = 3+3/2;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(carry),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(e),IntType)],Block([VarDecl(Id(people),IntType,BinaryOp(+,IntLit(3),BinaryOp(/,IntLit(3),IntLit(2))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """
        Class Car {
            $updateCount(){
                Var count:Int = count;
                count=1;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Car),[MethodDecl(Id($updateCount),Static,[],Block([VarDecl(Id(count),IntType,Id(count)),AssignStmt(Id(count),IntLit(1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 325))
    def test_326(self):
        input = """
        Class Motor {
            $updateStock(){
                stock[1][3]= stock[1][3] + 1;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id($updateStock),Static,[],Block([AssignStmt(ArrayCell(Id(stock),[IntLit(1),IntLit(3)]),BinaryOp(+,ArrayCell(Id(stock),[IntLit(1),IntLit(3)]),IntLit(1)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = """
        Class Motor {
            speak(){
                voice[1][b[3]]="hey";
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(speak),Instance,[],Block([AssignStmt(ArrayCell(Id(voice),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]),StringLit(hey))]))])])'
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = """
        Class Motor {
            changeName(){
                Self.name1.name2="yamaha";
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(changeName),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Self(),Id(name1)),Id(name2)),StringLit(yamaha))]))])])'
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_329(self):
        input = """
        Class Motor {
            changeName(){
                Self.name1.name2[1]=Self.name3.getName(1,"first");
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(changeName),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(FieldAccess(Self(),Id(name1)),Id(name2)),[IntLit(1)]),CallExpr(FieldAccess(Self(),Id(name3)),Id(getName),[IntLit(1),StringLit(first)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = """
        Class Motor {
            foo(){
                Var speed:Speed = Self.s.getSpeed(10,20+30) + 20;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(speed),ClassType(Id(Speed)),BinaryOp(+,CallExpr(FieldAccess(Self(),Id(s)),Id(getSpeed),[IntLit(10),BinaryOp(+,IntLit(20),IntLit(30))]),IntLit(20)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = """
        Class Car {
            foo(){
                Var carStock:Array[Array[Int,5],5];
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Car),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(carStock),ArrayType(5,ArrayType(5,IntType)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 331))
    def test_332(self):
        input = """
        Class Car {
            foo(){
                Break;
                Continue;
                Return Car==.!Motor;
                {}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Car),[MethodDecl(Id(foo),Instance,[],Block([Break,Continue,Return(BinaryOp(==.,Id(Car),UnaryOp(!,Id(Motor)))),Block([])]))])])'
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = """
        Class Car:Vehicle{
            createCar(){
                Car = New Car("huyndai").model.init();
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Car),Id(Vehicle),[MethodDecl(Id(createCar),Instance,[],Block([AssignStmt(Id(Car),CallExpr(FieldAccess(NewExpr(Id(Car),[StringLit(huyndai)]),Id(model)),Id(init),[]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = """
        Class Motor:Vehicle{
            createMotor(){
                motor = New Motor("honda").b.init();
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(createMotor),Instance,[],Block([AssignStmt(Id(motor),CallExpr(FieldAccess(NewExpr(Id(Motor),[StringLit(honda)]),Id(b)),Id(init),[]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 334))
    def test_335(self):
        input = """
        Class Motor:Vehicle{
            foo(){
                speed = (10+20)*3;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(speed),BinaryOp(*,BinaryOp(+,IntLit(10),IntLit(20)),IntLit(3)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_336(self):
        input = """
        Class Car:Vehicle{
            recur(){
                Return Self.recur();
            }
            Constructor (speed,brand:Name){}
            Destructor (){}
        }
        """
        expect = 'Program([ClassDecl(Id(Car),Id(Vehicle),[MethodDecl(Id(recur),Instance,[],Block([Return(CallExpr(Self(),Id(recur),[]))])),MethodDecl(Id(Constructor),Instance,[param(Id(speed),ClassType(Id(Name))),param(Id(brand),ClassType(Id(Name)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = """
        Class Motor:Vehicle{
            Var speed,$good:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Instance,VarDecl(Id(speed),IntType)),AttributeDecl(Static,VarDecl(Id($good),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 337))
    def test_338(self):
        input = """
        Class Motor:Vehicle{
            Var minSpeed,$maxSpeed:Int = 0,100;
            Val $count,boo:Boolean = True, Null;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Instance,VarDecl(Id(minSpeed),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($maxSpeed),IntType,IntLit(100))),AttributeDecl(Static,ConstDecl(Id($count),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(boo),BoolType,NullLiteral()))])])'
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_339(self):
        input = """
        Class Motor:Vehicle{
            Var speed1, speed2, speed3:Int;
            Foo(){
                Var speed1, speed2, speed3:Int;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Instance,VarDecl(Id(speed1),IntType)),AttributeDecl(Instance,VarDecl(Id(speed2),IntType)),AttributeDecl(Instance,VarDecl(Id(speed3),IntType)),MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(speed1),IntType),VarDecl(Id(speed2),IntType),VarDecl(Id(speed3),IntType)]))])])'
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_340(self):
        input = """
        Class Car:Vehicle{
            Foo(){
                Val speed1, speed1, speed1:Int = 10,20,30;
                Var d:Boolean = True;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Car),Id(Vehicle),[MethodDecl(Id(Foo),Instance,[],Block([ConstDecl(Id(speed1),IntType,IntLit(10)),ConstDecl(Id(speed1),IntType,IntLit(20)),ConstDecl(Id(speed1),IntType,IntLit(30)),VarDecl(Id(d),BoolType,BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = """
        Class Motor:Vehicle{
            Var $stock:Array[Int,3] = Array(1,1,1);
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($stock),ArrayType(3,IntType),[IntLit(1),IntLit(1),IntLit(1)]))])])'
        self.assertTrue(TestAST.test(input, expect, 341))
    def test_342(self):
        input = """
        Class Motor:Vehicle{
            Var $car:Array[Array[Int,1],3] = Array(Array(1),Array(1),Array(1));
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($car),ArrayType(3,ArrayType(1,IntType)),[[IntLit(1)],[IntLit(1)],[IntLit(1)]]))])])'
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_343(self):
        input = """
        Class Motor:Vehicle{
            Var $3:Int;
            $foo(i:Array [Boolean ,0105]){
                d=0105;
                e.z(Self,Null,Array(1)).d=0x12DEF;
                g[k][w[x]]=0B1010111011101;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($3),IntType)),MethodDecl(Id($foo),Static,[param(Id(i),ArrayType(69,BoolType))],Block([AssignStmt(Id(d),IntLit(69)),AssignStmt(FieldAccess(CallExpr(Id(e),Id(z),[Self(),NullLiteral(),[IntLit(1)]]),Id(d)),IntLit(77295)),AssignStmt(ArrayCell(Id(g),[Id(k),ArrayCell(Id(w),[Id(x)])]),IntLit(5597))]))])])'
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_344(self):
        input = """
        Class Motor:Vehicle{
            Var $0,s,$s1,sb,$2s,cs:Int = 50,40,30,20,10,0;
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($0),IntType,IntLit(50))),AttributeDecl(Instance,VarDecl(Id(s),IntType,IntLit(40))),AttributeDecl(Static,VarDecl(Id($s1),IntType,IntLit(30))),AttributeDecl(Instance,VarDecl(Id(sb),IntType,IntLit(20))),AttributeDecl(Static,VarDecl(Id($2s),IntType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(cs),IntType,IntLit(0)))])])'
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_345(self):
        input = """
        Class Motor:Vehicle{
            Run(){
                If(3){}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(Run),Instance,[],Block([If(IntLit(3),Block([]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = """
        Class Motor:Vehicle{
            Run(){
                If(10){}
                If(20){}Else{}
                If(30){}Elseif(40){}Else{stop=1;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(Run),Instance,[],Block([If(IntLit(10),Block([])),If(IntLit(20),Block([]),Block([])),If(IntLit(30),Block([]),If(IntLit(40),Block([]),Block([AssignStmt(Id(stop),IntLit(1))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 346))
    def test_347(self):
        input = """
        Class Motor:Vehicle{
            Run(){
                If(3){}Elseif(4){}Elseif(5){}Else{a=1;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(Run),Instance,[],Block([If(IntLit(3),Block([]),If(IntLit(4),Block([]),If(IntLit(5),Block([]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 347))
    def test_348(self):
        input = """
        Class Motor:Vehicle{
            Foo(){
                motor.foo(1+20,30*4-50.50);
                If(10)
                    {}
                Elseif(20)
                    {}
                Elseif(30)
                    {}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(motor),Id(foo),[BinaryOp(+,IntLit(1),IntLit(20)),BinaryOp(-,BinaryOp(*,IntLit(30),IntLit(4)),FloatLit(50.5))]),If(IntLit(10),Block([]),If(IntLit(20),Block([]),If(IntLit(30),Block([]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = """
        Class Motor:Vehicle
        {
            Foo()
            {
                If(30)
                    {Val hex: Int = 0X1234;}
                Elseif(40)
                    {{}}
                Elseif(50)
                    {Return Self;}
                Else
                    {dec = 10;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(30),Block([ConstDecl(Id(hex),IntType,IntLit(4660))]),If(IntLit(40),Block([Block([])]),If(IntLit(50),Block([Return(Self())]),Block([AssignStmt(Id(dec),IntLit(10))]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        line = '''
        Class Motor {
            $countMotor() {
                If (count == (1+1) ){
                    Var x,y:Boolean = False, True;
                }
                Foreach (i In 1 .. 55 By 3) {
                     Var x:Boolean = True;
                }
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(Motor),[MethodDecl(Id($countMotor),Static,[],Block([If(BinaryOp(==,Id(count),BinaryOp(+,IntLit(1),IntLit(1))),Block([VarDecl(Id(x),BoolType,BooleanLit(False)),VarDecl(Id(y),BoolType,BooleanLit(True))])),For(Id(i),IntLit(1),IntLit(55),IntLit(3),Block([VarDecl(Id(x),BoolType,BooleanLit(True))])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 350))

    def test_351(self):
        line = """
            Class Motor{
                run(){
                    Foreach (p In 1+1 .. 200+200 By b.foo(10+2*30,3+"str_"+.1+20)){}
                }
            }
        """
        expect = '''Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[],Block([For(Id(p),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(200),IntLit(200)),CallExpr(Id(b),Id(foo),[BinaryOp(+,IntLit(10),BinaryOp(*,IntLit(2),IntLit(30))),BinaryOp(+.,BinaryOp(+,IntLit(3),StringLit(str_)),BinaryOp(+,IntLit(1),IntLit(20)))]),Block([])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 351))

    def test_352(self):
        line = """
            Class Motor{
                run(){
                    Foreach (x1 In c::$d() .. x.y.z.t By b::$xyz){
                        Foreach (x2 In d::$e() .. p.t.u.r By a::$xyz){}
                    }
                }
            }
        """
        expect = '''Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[],Block([For(Id(x1),CallExpr(Id(c),Id($d),[]),FieldAccess(FieldAccess(FieldAccess(Id(x),Id(y)),Id(z)),Id(t)),FieldAccess(Id(b),Id($xyz)),Block([For(Id(x2),CallExpr(Id(d),Id($e),[]),FieldAccess(FieldAccess(FieldAccess(Id(p),Id(t)),Id(u)),Id(r)),FieldAccess(Id(a),Id($xyz)),Block([])])])])]))])])'''
        self.assertTrue(TestAST.test(line, expect, 352))

    def test_353(self):
        line = """
            Class Motor{
            stop(){
                    If ( break == -1--1){
                        Foreach(xyz In 1 .. 99 By 2){
                            If ( t == -1--1){
                                Foreach(a In 100 .. 1 By -2){
                                }
                            }
                        }
                    }
                }
            }
        """

        expect = '''Program([ClassDecl(Id(Motor),[MethodDecl(Id(stop),Instance,[],Block([If(BinaryOp(==,Id(break),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(xyz),IntLit(1),IntLit(99),IntLit(2),Block([If(BinaryOp(==,Id(t),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(a),IntLit(100),IntLit(1),UnaryOp(-,IntLit(2)),Block([])])]))])])]))]))])])'''
        self.assertTrue(TestAST.test(line, expect, 353))

    def test_354(self):
        line = """
        Class Program{
            main(){}
            main(status,x,y:Int){}
        }
        Class NotAProgram{
            main(){}
        }
        """

        expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(status),IntType),param(Id(x),IntType),param(Id(y),IntType)],Block([]))]),ClassDecl(Id(NotAProgram),[MethodDecl(Id(main),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 354))

    def test_355(self):
        input = """Class Program {
            Val x : Int = Vehicle::$y.x.z.t[1][2][3][(0 + 012 + 0xA2 + 0XA2 + 0b101 + 0B101)];
            Var y : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(Vehicle),Id($y)),Id(x)),Id(z)),Id(t)),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(10)),IntLit(162)),IntLit(162)),IntLit(5)),IntLit(5))]))),AttributeDecl(Instance,VarDecl(Id(y),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0))))])])"
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = """
        Class Motor {
            run() {
                Val x, y : Float = .e5 , 12e-10;
            }
        }"""
        expect = "Program([ClassDecl(Id(Motor),[MethodDecl(Id(run),Instance,[],Block([ConstDecl(Id(x),FloatType,FloatLit(0.0)),ConstDecl(Id(y),FloatType,FloatLit(1.2e-09))]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        """Static access, instance and index combine"""
        input = """
        Class Car {
            stop() {
                Val avgSpeed, maxSpeed : Float = 2.e5 , 0.5e-1;
            }
        }"""
        expect = "Program([ClassDecl(Id(Car),[MethodDecl(Id(stop),Instance,[],Block([ConstDecl(Id(avgSpeed),FloatType,FloatLit(200000.0)),ConstDecl(Id(maxSpeed),FloatType,FloatLit(0.05))]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = """Class Program {
            main() {
                (x[1]).func();
                x[1] = 1;
                Out.println(y.y[1]);
                ((((t[1][2]).w[1]).func()[0]).z[1]).func();
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(x),[IntLit(1)]),Id(func),[]),AssignStmt(ArrayCell(Id(x),[IntLit(1)]),IntLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(y),Id(y)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(t),[IntLit(1),IntLit(2)]),Id(w)),[IntLit(1)]),Id(func),[]),[IntLit(0)]),Id(z)),[IntLit(1)]),Id(func),[]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = """
        Class Program {
            main() {
                y[1][exp1::$x().s[exp2::$t().s2[exp3::$foo().d]]] = 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(y),[IntLit(1),ArrayCell(FieldAccess(CallExpr(Id(exp1),Id($x),[]),Id(s)),[ArrayCell(FieldAccess(CallExpr(Id(exp2),Id($t),[]),Id(s2)),[FieldAccess(CallExpr(Id(exp3),Id($foo),[]),Id(d))])])]),IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = """
        Class Car {
            run() {
                Car.x.y.start();
                (x.y[1][2][3]).operate1();
                Automobile::$cc.operate2();
                (Automobile::$g.w[3][1]).operate3();
            }
        }"""
        expect = "Program([ClassDecl(Id(Car),[MethodDecl(Id(run),Instance,[],Block([Call(FieldAccess(FieldAccess(Id(Car),Id(x)),Id(y)),Id(start),[]),Call(ArrayCell(FieldAccess(Id(x),Id(y)),[IntLit(1),IntLit(2),IntLit(3)]),Id(operate1),[]),Call(FieldAccess(Id(Automobile),Id($cc)),Id(operate2),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(Automobile),Id($g)),Id(w)),[IntLit(3),IntLit(1)]),Id(operate3),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = """Class Car{
            Var _5f2s1, $_234: l_yut;
            run(){
                Var i1,i2:I;
            }
        }"""
        expect = "Program([ClassDecl(Id(Car),[AttributeDecl(Instance,VarDecl(Id(_5f2s1),ClassType(Id(l_yut)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_234),ClassType(Id(l_yut)),NullLiteral())),MethodDecl(Id(run),Instance,[],Block([VarDecl(Id(i1),ClassType(Id(I)),NullLiteral()),VarDecl(Id(i2),ClassType(Id(I)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(d),IntType)),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(str1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = """
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Vehicle),[AttributeDecl(Instance,VarDecl(Id(running),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(speed),IntType)),AttributeDecl(Instance,VarDecl(Id(model_name),StringType)),AttributeDecl(Static,VarDecl(Id($numOfVehicle),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(speed)),IntLit(30))])),MethodDecl(Id(Constructor),Instance,[param(Id(speed),IntType),param(Id(model_name),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(speed)),Id(speed)),AssignStmt(FieldAccess(Self(),Id(model_name)),Id(model_name))]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = """
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Vehicle),[AttributeDecl(Instance,VarDecl(Id(running),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(speed),IntType)),AttributeDecl(Instance,VarDecl(Id(model_name),StringType)),AttributeDecl(Static,VarDecl(Id($numOfVehicle),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(speed)),IntLit(30))])),MethodDecl(Id(Constructor),Instance,[param(Id(speed),IntType),param(Id(model_name),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(speed)),Id(speed)),AssignStmt(FieldAccess(Self(),Id(model_name)),Id(model_name))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = """
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Car),Id(Vehicle),[AttributeDecl(Instance,ConstDecl(Id(sunScreen),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(doors),ArrayType(4,BoolType),None)),AttributeDecl(Instance,ConstDecl(Id(backDoor),ClassType(Id(Door)),NewExpr(Id(Door),[]))),MethodDecl(Id(openCabin),Instance,[],Block([If(BinaryOp(==,Id(openedCabin),BooleanLit(False)),Block([AssignStmt(Id(openedCabin),BooleanLit(True)),Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = """
        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Val maxSpeed: Int = 40;
            Constructor(){

            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($motorList),ArrayType(100,IntType))),AttributeDecl(Instance,ConstDecl(Id(maxSpeed),IntType,IntLit(40))),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(maxSpeed),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(maxSpeed)),Id(maxSpeed))]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = """
        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Val maxSpeed: Int = 40;
            Constructor(){

            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($motorList),ArrayType(100,IntType))),AttributeDecl(Instance,ConstDecl(Id(maxSpeed),IntType,IntLit(40))),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(maxSpeed),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(maxSpeed)),Id(maxSpeed))]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = """
        Class Motor:Vehicle{
            Var $motorList:Array[Int, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor(){
                a = b;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Motor),Id(Vehicle),[AttributeDecl(Static,VarDecl(Id($motorList),ArrayType(100,IntType))),AttributeDecl(Static,VarDecl(Id($numOfMotor),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(maxSpeed),IntType,IntLit(40))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(ArrayCell(Id(motorList),[FieldAccess(Id(Motor),Id($numOfMotor))]),Self()),AssignStmt(FieldAccess(Id(Motor),Id($numOfMotor)),BinaryOp(+,FieldAccess(Id(Motor),Id($numOfMotor)),IntLit(1)))])),MethodDecl(Id(Constructor),Instance,[param(Id(maxSpeed),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(maxSpeed)),Id(maxSpeed))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),Id(b))]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + Self.foo();
                Self.foo2(param1, param2);
                a1 = Self.foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(d),IntType)),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var1),StringType,StringLit(str1))])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Self(),Id(foo),[]))),Call(Self(),Id(foo2),[Id(param1),Id(param2)]),AssignStmt(Id(a1),CallExpr(Self(),Id(foo3),[Id(param1),Id(param2)])),VarDecl(Id(b),BoolType,BinaryOp(>=,IntLit(1),IntLit(3))),ConstDecl(Id(val1),BoolType,BinaryOp(==,BooleanLit(True),BooleanLit(False))),AssignStmt(Id(b),UnaryOp(!,Id(val1))),Return(BooleanLit(True))]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = """
        Class Diary{
            Val $arr: Array[Array[String, 2], 5];
            Constructor(){}
            addDiary(diary: Array[String, 2]){
                Diary::$arr[0] = diary;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Diary),[AttributeDecl(Static,ConstDecl(Id($arr),ArrayType(5,ArrayType(2,StringType)),None)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(addDiary),Instance,[param(Id(diary),ArrayType(2,StringType))],Block([AssignStmt(ArrayCell(FieldAccess(Id(Diary),Id($arr)),[IntLit(0)]),Id(diary))]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Diary::$numOfDiary] = diary;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Diary),[AttributeDecl(Static,VarDecl(Id($arr),ArrayType(5,ArrayType(2,StringType)))),AttributeDecl(Static,VarDecl(Id($numOfDiary),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Diary),Id($numOfDiary)),BinaryOp(+,FieldAccess(Id(Diary),Id($numOfDiary)),IntLit(1)))])),MethodDecl(Id(getNumOfDiary),Instance,[],Block([Return(FieldAccess(Id(Motor),Id($numOfDiary)))])),MethodDecl(Id(addDiary),Instance,[param(Id(diary),ArrayType(2,StringType))],Block([AssignStmt(ArrayCell(FieldAccess(Id(Diary),Id($arr)),[FieldAccess(Id(Diary),Id($numOfDiary))]),Id(diary))]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                    Else{
                        Motor::$arr[i] = Null;
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Diary),[AttributeDecl(Static,VarDecl(Id($arr),ArrayType(5,ArrayType(2,StringType)))),AttributeDecl(Static,VarDecl(Id($numOfDiary),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Diary),Id($numOfDiary)),BinaryOp(+,FieldAccess(Id(Diary),Id($numOfDiary)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([For(Id(i),FieldAccess(Id(Motor),Id($numOfDiary)),IntLit(1),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(==,ArrayCell(FieldAccess(Id(Motor),Id($arr)),[Id(i)]),NullLiteral()),Block([Continue]),Block([AssignStmt(ArrayCell(FieldAccess(Id(Motor),Id($arr)),[Id(i)]),NullLiteral())]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                    Else{
                        Motor::$arr[i] = Null;
                    }
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Diary),[AttributeDecl(Static,VarDecl(Id($arr),ArrayType(5,ArrayType(2,StringType)))),AttributeDecl(Static,VarDecl(Id($numOfDiary),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Diary),Id($numOfDiary)),BinaryOp(+,FieldAccess(Id(Diary),Id($numOfDiary)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([For(Id(i),FieldAccess(Id(Motor),Id($numOfDiary)),IntLit(1),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(==,ArrayCell(FieldAccess(Id(Motor),Id($arr)),[Id(i)]),NullLiteral()),Block([Continue]),Block([AssignStmt(ArrayCell(FieldAccess(Id(Motor),Id($arr)),[Id(i)]),NullLiteral())]))])])])),MethodDecl(Id(getNumOfDiary),Instance,[],Block([Return(FieldAccess(Id(Motor),Id($numOfDiary)))])),MethodDecl(Id(addDiary),Instance,[param(Id(diary),ArrayType(2,StringType))],Block([AssignStmt(ArrayCell(FieldAccess(Id(Diary),Id($arr)),[CallExpr(Self(),Id(getNumOfDiary),[])]),Id(diary))])),MethodDecl(Id(deleteDiary),Instance,[param(Id(id),IntType)],Block([AssignStmt(ArrayCell(FieldAccess(Id(Diary),Id($arr)),[Id(id)]),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
        }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType)))))])])"
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
            }
            foo(){
                (a + b).foo();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([Call(BinaryOp(+,Id(a),Id(b)),Id(foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                        } 
                    }
                }
            }
            foo(){
                a = b.foo();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(Constructor),Instance,[],Block([For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([])])])])])])])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(Id(b),Id(foo),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = """
        Class Image{
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Destructor(){
                Foreach (row In 1 .. 256 By 1){
                    Foreach (col In 256 .. 1 By -1){
                        Foreach (channel In 1 .. 3 By 1){
                            matrix[row][col][channel] = 0;
                        } 
                    }
                }
            }
            foo(){
                a = b.foo();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(Destructor),Instance,[],Block([For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(Id(matrix),[Id(row),Id(col),Id(channel)]),IntLit(0))])])])])])])])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(Id(b),Id(foo),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """
        Class Shape{
                foo(){
                    a = New X().Y();
                    Var a: Array[Int, 265];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),CallExpr(NewExpr(Id(X),[]),Id(Y),[])),VarDecl(Id(a),ArrayType(265,IntType))]))])])"
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = """
        Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                Constructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 255;
                            } 
                        }
                    }
                }
                Destructor(){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = 0;
                            } 
                        }
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(Constructor),Instance,[],Block([For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]),IntLit(255))])])])])])])])),MethodDecl(Id(Destructor),Instance,[],Block([For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]),IntLit(0))])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = """
        Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                add(img: Image){
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.matrix[row][col][channel] = Self.matrix[row][col][channel] + img.matrix[row][col][channel];
                            } 
                        }
                    }
                }
                concat(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                }
            }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(add),Instance,[param(Id(img),ClassType(Id(Image)))],Block([For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]),BinaryOp(+,ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]),ArrayCell(FieldAccess(Id(img),Id(matrix)),[Id(row),Id(col),Id(channel)])))])])])])])])])),MethodDecl(Id(concat),Instance,[param(Id(img),ClassType(Id(Image)))],Block([VarDecl(Id(concatMatrix),ArrayType(512,ArrayType(512,ArrayType(3,IntType))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = """
        Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                concat(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(concat),Instance,[param(Id(img),ClassType(Id(Image)))],Block([VarDecl(Id(concatMatrix),ArrayType(512,ArrayType(512,ArrayType(3,IntType)))),For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(concatMatrix)),[Id(row),Id(col),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]))])])])])])])]))])])"

        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = """
        Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                vstack(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                                Self.concatMatrix[row+256][col][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(vstack),Instance,[param(Id(img),ClassType(Id(Image)))],Block([VarDecl(Id(concatMatrix),ArrayType(512,ArrayType(512,ArrayType(3,IntType)))),For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(concatMatrix)),[Id(row),Id(col),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)])),AssignStmt(ArrayCell(FieldAccess(Self(),Id(concatMatrix)),[BinaryOp(+,Id(row),IntLit(256)),Id(col),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]))])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = """
        Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                hstack(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                                Self.concatMatrix[row][col+256][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(hstack),Instance,[param(Id(img),ClassType(Id(Image)))],Block([VarDecl(Id(concatMatrix),ArrayType(512,ArrayType(512,ArrayType(3,IntType)))),For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(concatMatrix)),[Id(row),Id(col),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)])),AssignStmt(ArrayCell(FieldAccess(Self(),Id(concatMatrix)),[Id(row),BinaryOp(+,Id(col),IntLit(256)),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]))])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = """
        Class ElectricalDevice{
                Var weight: Float;
                Var useBattery: Boolean;
            }
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(ElectricalDevice),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType)),AttributeDecl(Instance,VarDecl(Id(useBattery),BoolType))]),ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
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
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(ElectricalDevice),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType)),AttributeDecl(Instance,VarDecl(Id(useBattery),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat))]))]),ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))]))])])"
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
            Class Laptop:Electrical{
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(ElectricalDevice),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType)),AttributeDecl(Instance,VarDecl(Id(useBattery),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat))]))]),ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
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
        Class Laptop:Electrical{

                $Refresh(){
                    Foreach(i In ElectricalDevice::$numOfDevices .. 0 By -1){

                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id($Refresh),Static,[],Block([For(Id(i),FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(0),UnaryOp(-,IntLit(1)),Block([])])])),MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = """
        Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                $Refresh(){
                    Foreach(i In (ElectricalDevice::$numOfDevices*100)/100 + 1 .. 100-100+35%34 By -1){
                        (laptops[i]).refresh();
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
        }
        """
        expect = "Program([ClassDecl(Id(Laptop),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($numOfLaptops),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id($Refresh),Static,[],Block([For(Id(i),BinaryOp(+,BinaryOp(/,BinaryOp(*,FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(100)),IntLit(100)),IntLit(1)),BinaryOp(+,BinaryOp(-,IntLit(100),IntLit(100)),BinaryOp(%,IntLit(35),IntLit(34))),UnaryOp(-,IntLit(1)),Block([Call(ArrayCell(Id(laptops),[Id(i)]),Id(refresh),[])])])])),MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = """
        Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                Constructor(weight: Float; useBat:Boolean){
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                    ElectricalDevice::$devices[ElectricalDevice::$numOfDevices] = Self;
                    Laptop::$laptops[ElectricalDevice::$numOfDevices] = Self;
                    ElectricalDevice::$numOfDevices = ElectricalDevice::$numOfDevices+1;
                }
        }
        """
        expect = "Program([ClassDecl(Id(Laptop),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($numOfLaptops),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat)),AssignStmt(ArrayCell(FieldAccess(Id(ElectricalDevice),Id($devices)),[FieldAccess(Id(ElectricalDevice),Id($numOfDevices))]),Self()),AssignStmt(ArrayCell(FieldAccess(Id(Laptop),Id($laptops)),[FieldAccess(Id(ElectricalDevice),Id($numOfDevices))]),Self()),AssignStmt(FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),BinaryOp(+,FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = """
        Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
        }
        """
        expect = "Program([ClassDecl(Id(Laptop),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($numOfLaptops),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = """
        Class Laptop:Electrical{
                Var $numOfLaptops: Int;
                Var $laptops: Array[Boolean, 100];

                $checkVirus(){
                    Foreach(i In Laptop::$numOfLaptops/100*100 + 1 .. 100-100+35%34 By -1){
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
        expect = "Program([ClassDecl(Id(Laptop),Id(Electrical),[AttributeDecl(Static,VarDecl(Id($numOfLaptops),IntType)),AttributeDecl(Static,VarDecl(Id($laptops),ArrayType(100,BoolType))),MethodDecl(Id($checkVirus),Static,[],Block([For(Id(i),BinaryOp(+,BinaryOp(*,BinaryOp(/,FieldAccess(Id(Laptop),Id($numOfLaptops)),IntLit(100)),IntLit(100)),IntLit(1)),BinaryOp(+,BinaryOp(-,IntLit(100),IntLit(100)),BinaryOp(%,IntLit(35),IntLit(34))),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(==,FieldAccess(ArrayCell(Id(laptops),[Id(i)]),Id(checked)),BooleanLit(True)),Block([Continue]),Block([AssignStmt(FieldAccess(ArrayCell(Id(laptops),[Id(i)]),Id(checked)),BooleanLit(True))]))])])]))])])"
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
        Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList[Classroom::$numOfStudents] = newStu;
                } 
            }
            Class Student{}
        """
        expect = "Program([ClassDecl(Id(Classroom),[AttributeDecl(Static,VarDecl(Id($numOfStudents),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($studentList),ArrayType(40,StringType))),MethodDecl(Id(addStudent),Instance,[param(Id(newStu),ClassType(Id(Student)))],Block([AssignStmt(ArrayCell(FieldAccess(Id(Classroom),Id($studentList)),[FieldAccess(Id(Classroom),Id($numOfStudents))]),Id(newStu))]))]),ClassDecl(Id(Student),[])])"
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = """
        Class Classroom{
                Var $numOfStudents : Int = 0;
                Var $studentList: Array[String, 40];
                addStudent(newStu: Student){
                     Classroom::$studentList.append(newStu);
                } 
            }
        """
        expect = "Program([ClassDecl(Id(Classroom),[AttributeDecl(Static,VarDecl(Id($numOfStudents),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($studentList),ArrayType(40,StringType))),MethodDecl(Id(addStudent),Instance,[param(Id(newStu),ClassType(Id(Student)))],Block([Call(FieldAccess(Id(Classroom),Id($studentList)),Id(append),[Id(newStu)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = """
        Class Student{
                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){}
            }
        """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Classroom),Id($numOfStudents)),BinaryOp(+,FieldAccess(Id(Classroom),Id($numOfStudents)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = """
        Class Student{
                Constructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents - 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Classroom),Id($numOfStudents)),BinaryOp(+,FieldAccess(Id(Classroom),Id($numOfStudents)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Classroom),Id($numOfStudents)),BinaryOp(-,FieldAccess(Id(Classroom),Id($numOfStudents)),IntLit(1)))]))])])"
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
                    Classroom::$numOfStudents = Classroom::$numOfStudents + 1;
                }
                Destructor(){
                    Classroom::$numOfStudents = Classroom::$numOfStudents - 1;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Student),[MethodDecl(Id(learn),Instance,[],Block([Call(Self(),Id(print),[StringLit(Learning)])])),MethodDecl(Id(goToSchool),Instance,[],Block([Call(Self(),Id(byeMom),[]),Call(Self(),Id(byeDad),[StringLit(by dad)])])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Classroom),Id($numOfStudents)),BinaryOp(+,FieldAccess(Id(Classroom),Id($numOfStudents)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Classroom),Id($numOfStudents)),BinaryOp(-,FieldAccess(Id(Classroom),Id($numOfStudents)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 399))

