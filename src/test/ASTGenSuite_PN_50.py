import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        input = '''Class X{Var $RY_6,$17:Array [Array [String ,9_8_8_1],0B1100100];}Class _43:_{}Class _{}Class p{}'''
        expect = '''Program([ClassDecl(Id(X),[AttributeDecl(Static,VarDecl(Id($RY_6),ArrayType(100,ArrayType(9881,StringType)))),AttributeDecl(Static,VarDecl(Id($17),ArrayType(100,ArrayType(9881,StringType))))]),ClassDecl(Id(_43),Id(_),[]),ClassDecl(Id(_),[]),ClassDecl(Id(p),[])])'''
        self.assertTrue(TestAST.test(input, expect, 0))

    def test_1(self):
        input = '''Class __W{Var $b,_W,a5_:Array [Array [Array [Boolean ,0xB],0xF],0x49];}Class U8SK_{}'''
        expect = '''Program([ClassDecl(Id(__W),[AttributeDecl(Static,VarDecl(Id($b),ArrayType(73,ArrayType(15,ArrayType(11,BoolType))))),AttributeDecl(Instance,VarDecl(Id(_W),ArrayType(73,ArrayType(15,ArrayType(11,BoolType))))),AttributeDecl(Instance,VarDecl(Id(a5_),ArrayType(73,ArrayType(15,ArrayType(11,BoolType)))))]),ClassDecl(Id(U8SK_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 1))

    def test_2(self):
        input = '''Class _:zG_3w_{Cp(_,i_QW:Array [Int ,05];__,U,d0,D89l:Float ;_:_6){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),Id(zG_3w_),[MethodDecl(Id(Cp),Instance,[param(Id(_),ArrayType(5,IntType)),param(Id(i_QW),ArrayType(5,IntType)),param(Id(__),FloatType),param(Id(U),FloatType),param(Id(d0),FloatType),param(Id(D89l),FloatType),param(Id(_),ClassType(Id(_6)))],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 2))

    def test_3(self):
        input = '''Class j{}Class V_{Constructor (U:Int ){}Var _5543:Array [Array [String ,0xB],13];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(j),[]),ClassDecl(Id(V_),[MethodDecl(Id(Constructor),Instance,[param(Id(U),IntType)],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_5543),ArrayType(13,ArrayType(11,StringType)))),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 3))

    def test_4(self):
        input = '''Class e:_N{Var W,$C,r,$43:Array [Float ,0B111000];}Class __{}'''
        expect = '''Program([ClassDecl(Id(e),Id(_N),[AttributeDecl(Instance,VarDecl(Id(W),ArrayType(56,FloatType))),AttributeDecl(Static,VarDecl(Id($C),ArrayType(56,FloatType))),AttributeDecl(Instance,VarDecl(Id(r),ArrayType(56,FloatType))),AttributeDecl(Static,VarDecl(Id($43),ArrayType(56,FloatType)))]),ClassDecl(Id(__),[])])'''
        self.assertTrue(TestAST.test(input, expect, 4))

    def test_5(self):
        input = '''Class r:__vp_m{Constructor (__3,_D:J){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(r),Id(__vp_m),[MethodDecl(Id(Constructor),Instance,[param(Id(__3),ClassType(Id(J))),param(Id(_D),ClassType(Id(J)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 5))

    def test_6(self):
        input = '''Class I{Var _k_4,$x:String ;Destructor (){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(I),[AttributeDecl(Instance,VarDecl(Id(_k_4),StringType)),AttributeDecl(Static,VarDecl(Id($x),StringType)),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 6))

    def test_7(self):
        input = '''Class eo{}Class G_{Var k6:Array [String ,0XF];}Class _D:_{}'''
        expect = '''Program([ClassDecl(Id(eo),[]),ClassDecl(Id(G_),[AttributeDecl(Instance,VarDecl(Id(k6),ArrayType(15,StringType)))]),ClassDecl(Id(_D),Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 7))

    def test_8(self):
        input = '''Class _rK{$9(){}Constructor (){Continue ;}Destructor (){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_rK),[MethodDecl(Id($9),Static,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[Continue])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 8))

    def test_9(self):
        input = '''Class _:_{}Class p{Constructor (){} }Class _1{}Class R:Z_{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(p),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))]),ClassDecl(Id(_1),[]),ClassDecl(Id(R),Id(Z_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 9))

    def test_10(self):
        input = '''Class _78:B{u7(___J,b7:Array [Float ,0b1];Q:yx;w3,f,_:_0;_6z:x7){} }'''
        expect = '''Program([ClassDecl(Id(_78),Id(B),[MethodDecl(Id(u7),Instance,[param(Id(___J),ArrayType(1,FloatType)),param(Id(b7),ArrayType(1,FloatType)),param(Id(Q),ClassType(Id(yx))),param(Id(w3),ClassType(Id(_0))),param(Id(f),ClassType(Id(_0))),param(Id(_),ClassType(Id(_0))),param(Id(_6z),ClassType(Id(x7)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 10))

    def test_11(self):
        input = '''Class W:u{Constructor (_J__P,g,N6S_2j:Array [String ,8];T_6,_8,D,_,_1s_a_a_:Int ;w,B:Array [Float ,0X5];_,_p:Array [Float ,8]){} }'''
        expect = '''Program([ClassDecl(Id(W),Id(u),[MethodDecl(Id(Constructor),Instance,[param(Id(_J__P),ArrayType(8,StringType)),param(Id(g),ArrayType(8,StringType)),param(Id(N6S_2j),ArrayType(8,StringType)),param(Id(T_6),IntType),param(Id(_8),IntType),param(Id(D),IntType),param(Id(_),IntType),param(Id(_1s_a_a_),IntType),param(Id(w),ArrayType(5,FloatType)),param(Id(B),ArrayType(5,FloatType)),param(Id(_),ArrayType(8,FloatType)),param(Id(_p),ArrayType(8,FloatType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 11))

    def test_12(self):
        input = '''Class __{$d_(){}Var _,$_fMgeB,$_Z_:l5;}Class _q_0_2hB0{}'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id($d_),Static,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(l5)))),AttributeDecl(Static,VarDecl(Id($_fMgeB),ClassType(Id(l5)))),AttributeDecl(Static,VarDecl(Id($_Z_),ClassType(Id(l5))))]),ClassDecl(Id(_q_0_2hB0),[])])'''
        self.assertTrue(TestAST.test(input, expect, 12))

    def test_13(self):
        input = '''Class d{}Class _q_:G{}Class _:_{l7_(_,_,I:String ){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(d),[]),ClassDecl(Id(_q_),Id(G),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(l7_),Instance,[param(Id(_),StringType),param(Id(_),StringType),param(Id(I),StringType)],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(input, expect, 13))

    def test_14(self):
        input = '''Class __{}Class ___:k5{Constructor (j:__;F:String ;__:Boolean ){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(__),[]),ClassDecl(Id(___),Id(k5),[MethodDecl(Id(Constructor),Instance,[param(Id(j),ClassType(Id(__))),param(Id(F),StringType),param(Id(__),BoolType)],Block([],[Continue]))])])'''
        self.assertTrue(TestAST.test(input, expect, 14))

    def test_15(self):
        input = '''Class Q_:A0{O_T(){}$_0(){}Var P:Array [Array [Boolean ,0b1],0b10101];}'''
        expect = '''Program([ClassDecl(Id(Q_),Id(A0),[MethodDecl(Id(O_T),Instance,[],Block([],[])),MethodDecl(Id($_0),Static,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(P),ArrayType(21,ArrayType(1,BoolType))))])])'''
        self.assertTrue(TestAST.test(input, expect, 15))

    def test_16(self):
        input = '''Class _{Var F_,$_4,$_G,$g,L_h4W,$_,$__4:Array [Array [Float ,01_7],0B1010100];}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(F_),ArrayType(84,ArrayType(15,FloatType)))),AttributeDecl(Static,VarDecl(Id($_4),ArrayType(84,ArrayType(15,FloatType)))),AttributeDecl(Static,VarDecl(Id($_G),ArrayType(84,ArrayType(15,FloatType)))),AttributeDecl(Static,VarDecl(Id($g),ArrayType(84,ArrayType(15,FloatType)))),AttributeDecl(Instance,VarDecl(Id(L_h4W),ArrayType(84,ArrayType(15,FloatType)))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(84,ArrayType(15,FloatType)))),AttributeDecl(Static,VarDecl(Id($__4),ArrayType(84,ArrayType(15,FloatType))))])])'''
        self.assertTrue(TestAST.test(input, expect, 16))

    def test_17(self):
        input = '''Class _{}Class J9_8{_(d,v,A4,e1LX,_:String ;_,CVI2:Float ){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(J9_8),[MethodDecl(Id(_),Instance,[param(Id(d),StringType),param(Id(v),StringType),param(Id(A4),StringType),param(Id(e1LX),StringType),param(Id(_),StringType),param(Id(_),FloatType),param(Id(CVI2),FloatType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 17))

    def test_18(self):
        input = '''Class _{Destructor (){} }Class _h_:y{Var p_7:Float ;$7ip_(Pz,_,a:_){} }'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_h_),Id(y),[AttributeDecl(Instance,VarDecl(Id(p_7),FloatType)),MethodDecl(Id($7ip_),Static,[param(Id(Pz),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(a),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 18))

    def test_19(self):
        input = '''Class L:f{}Class h:__14{$7(_,r1:Array [Float ,0x39];_,O,_,_3iY_1:Int ){} }'''
        expect = '''Program([ClassDecl(Id(L),Id(f),[]),ClassDecl(Id(h),Id(__14),[MethodDecl(Id($7),Static,[param(Id(_),ArrayType(57,FloatType)),param(Id(r1),ArrayType(57,FloatType)),param(Id(_),IntType),param(Id(O),IntType),param(Id(_),IntType),param(Id(_3iY_1),IntType)],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 19))

    def test_20(self):
        input = '''Class _:Ox{Constructor (Z:Array [Array [Float ,05],0120];_:_){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(Ox),[MethodDecl(Id(Constructor),Instance,[param(Id(Z),ArrayType(80,ArrayType(5,FloatType))),param(Id(_),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 20))

    def test_21(self):
        input = '''Class U0:T8{_(g,_8:Array [Array [Array [Array [Array [Array [Int ,17],17],17],0B1],01],0B1_0]){} }'''
        expect = '''Program([ClassDecl(Id(U0),Id(T8),[MethodDecl(Id(_),Instance,[param(Id(g),ArrayType(2,ArrayType(1,ArrayType(1,ArrayType(17,ArrayType(17,ArrayType(17,IntType))))))),param(Id(_8),ArrayType(2,ArrayType(1,ArrayType(1,ArrayType(17,ArrayType(17,ArrayType(17,IntType)))))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 21))

    def test_22(self):
        input = '''Class _9:_{}Class _4:pr{$U(){Break ;}Var u_,$qn,$l:Int ;}'''
        expect = '''Program([ClassDecl(Id(_9),Id(_),[]),ClassDecl(Id(_4),Id(pr),[MethodDecl(Id($U),Static,[],Block([],[Break])),AttributeDecl(Instance,VarDecl(Id(u_),IntType)),AttributeDecl(Static,VarDecl(Id($qn),IntType)),AttributeDecl(Static,VarDecl(Id($l),IntType))])])'''
        self.assertTrue(TestAST.test(input, expect, 22))

    def test_23(self):
        input = '''Class _E7w{Var $0,z_:Array [Boolean ,9];}Class _5{}Class __d{}Class _:O{}Class C{}'''
        expect = '''Program([ClassDecl(Id(_E7w),[AttributeDecl(Static,VarDecl(Id($0),ArrayType(9,BoolType))),AttributeDecl(Instance,VarDecl(Id(z_),ArrayType(9,BoolType)))]),ClassDecl(Id(_5),[]),ClassDecl(Id(__d),[]),ClassDecl(Id(_),Id(O),[]),ClassDecl(Id(C),[])])'''
        self.assertTrue(TestAST.test(input, expect, 23))

    def test_24(self):
        input = '''Class __a__L_1v4_:W{}Class Z:__h{}Class j_:_{Destructor (){} }Class Y:fB9_{}Class R_9l{Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(__a__L_1v4_),Id(W),[]),ClassDecl(Id(Z),Id(__h),[]),ClassDecl(Id(j_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(Y),Id(fB9_),[]),ClassDecl(Id(R_9l),[MethodDecl(Id(Constructor),Instance,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 24))

    def test_25(self):
        input = '''Class N63b4:_{Constructor (_,m0:Array [Array [Int ,79],03];f:E){ {Continue ;} }}'''
        expect = '''Program([ClassDecl(Id(N63b4),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ArrayType(3,ArrayType(79,IntType))),param(Id(m0),ArrayType(3,ArrayType(79,IntType))),param(Id(f),ClassType(Id(E)))],Block([],[Block([],[Continue])]))])])'''
        self.assertTrue(TestAST.test(input, expect, 25))

    def test_26(self):
        input = '''Class _231{$e_d(_19:Int ){Var Z923:Array [Array [Array [Array [Array [String ,0B1010101],047_6],06_63],706_7],0xD];} }'''
        expect = '''Program([ClassDecl(Id(_231),[MethodDecl(Id($e_d),Static,[param(Id(_19),IntType)],Block([VarDecl(Id(Z923),ArrayType(13,ArrayType(7067,ArrayType(435,ArrayType(318,ArrayType(85,StringType))))))],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 26))

    def test_27(self):
        input = '''Class kN:_{Constructor (M_yc,W:Boolean ;C,t_Mc_,_5w__,E_,G2,_j,_J,U5t5_0:o){}Var $e:Float ;Constructor (_K,____4:Array [String ,0X21]){} }'''
        expect = '''Program([ClassDecl(Id(kN),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(M_yc),BoolType),param(Id(W),BoolType),param(Id(C),ClassType(Id(o))),param(Id(t_Mc_),ClassType(Id(o))),param(Id(_5w__),ClassType(Id(o))),param(Id(E_),ClassType(Id(o))),param(Id(G2),ClassType(Id(o))),param(Id(_j),ClassType(Id(o))),param(Id(_J),ClassType(Id(o))),param(Id(U5t5_0),ClassType(Id(o)))],Block([],[])),AttributeDecl(Static,VarDecl(Id($e),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(_K),ArrayType(33,StringType)),param(Id(____4),ArrayType(33,StringType))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 27))

    def test_28(self):
        input = '''Class _t{V(_:_;K3g6Z,_,_:Int ){ {} }$_(d:K){}Destructor (){} }Class X_:_eV_98V_{}'''
        expect = '''Program([ClassDecl(Id(_t),[MethodDecl(Id(V),Instance,[param(Id(_),ClassType(Id(_))),param(Id(K3g6Z),IntType),param(Id(_),IntType),param(Id(_),IntType)],Block([],[Block([],[])])),MethodDecl(Id($_),Static,[param(Id(d),ClassType(Id(K)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(X_),Id(_eV_98V_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 28))

    def test_29(self):
        input = '''Class S__{Destructor (){} }Class h:_{}Class H1_:_{}Class H5_{}'''
        expect = '''Program([ClassDecl(Id(S__),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(h),Id(_),[]),ClassDecl(Id(H1_),Id(_),[]),ClassDecl(Id(H5_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 29))

    def test_30(self):
        input = '''Class _{Var _,_1_0,n_:Array [Array [Float ,0B101010],65];}Class _69{}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(65,ArrayType(42,FloatType)))),AttributeDecl(Instance,VarDecl(Id(_1_0),ArrayType(65,ArrayType(42,FloatType)))),AttributeDecl(Instance,VarDecl(Id(n_),ArrayType(65,ArrayType(42,FloatType))))]),ClassDecl(Id(_69),[])])'''
        self.assertTrue(TestAST.test(input, expect, 30))

    def test_31(self):
        input = '''Class __Lj8:_{_(_sM_N5,G:Array [Array [Array [Array [Array [Array [Array [Array [Float ,0x59],0B1],0X43],9],98],0140],0x59],0140];_:Array [String ,98];h:_9_J_b_5;__:Float ;_0,V_Nf,_:Int ;_:_){} }'''
        expect = '''Program([ClassDecl(Id(__Lj8),Id(_),[MethodDecl(Id(_),Instance,[param(Id(_sM_N5),ArrayType(96,ArrayType(89,ArrayType(96,ArrayType(98,ArrayType(9,ArrayType(67,ArrayType(1,ArrayType(89,FloatType))))))))),param(Id(G),ArrayType(96,ArrayType(89,ArrayType(96,ArrayType(98,ArrayType(9,ArrayType(67,ArrayType(1,ArrayType(89,FloatType))))))))),param(Id(_),ArrayType(98,StringType)),param(Id(h),ClassType(Id(_9_J_b_5))),param(Id(__),FloatType),param(Id(_0),IntType),param(Id(V_Nf),IntType),param(Id(_),IntType),param(Id(_),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 31))

    def test_32(self):
        input = '''Class _{Destructor (){}Constructor (){Return ;Return ;} }Class _:_{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[],Block([],[Return(None),Return(None)]))]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 32))

    def test_33(self):
        input = '''Class _{__(_,__:String ;_:_;_,_8:b){} }Class __i{}Class t5{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(__),Instance,[param(Id(_),StringType),param(Id(__),StringType),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(b))),param(Id(_8),ClassType(Id(b)))],Block([],[]))]),ClassDecl(Id(__i),[]),ClassDecl(Id(t5),[])])'''
        self.assertTrue(TestAST.test(input, expect, 33))

    def test_34(self):
        input = '''Class h:_{}Class _:__{}Class s:_N_{}Class R__3:_0{$3(){} }'''
        expect = '''Program([ClassDecl(Id(h),Id(_),[]),ClassDecl(Id(_),Id(__),[]),ClassDecl(Id(s),Id(_N_),[]),ClassDecl(Id(R__3),Id(_0),[MethodDecl(Id($3),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 34))

    def test_35(self):
        input = '''Class W{Var N,$e_:Array [Boolean ,0B1];}Class P{}Class _{}'''
        expect = '''Program([ClassDecl(Id(W),[AttributeDecl(Instance,VarDecl(Id(N),ArrayType(1,BoolType))),AttributeDecl(Static,VarDecl(Id($e_),ArrayType(1,BoolType)))]),ClassDecl(Id(P),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 35))

    def test_36(self):
        input = '''Class n{}Class ___:_R{Var $uq:Array [Int ,0x4E];Constructor (){}__(ej:__;_S,_223:Array [Array [Array [Int ,0B1011111],0X55],9]){} }'''
        expect = '''Program([ClassDecl(Id(n),[]),ClassDecl(Id(___),Id(_R),[AttributeDecl(Static,VarDecl(Id($uq),ArrayType(78,IntType))),MethodDecl(Id(Constructor),Instance,[],Block([],[])),MethodDecl(Id(__),Instance,[param(Id(ej),ClassType(Id(__))),param(Id(_S),ArrayType(9,ArrayType(85,ArrayType(95,IntType)))),param(Id(_223),ArrayType(9,ArrayType(85,ArrayType(95,IntType))))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 36))

    def test_37(self):
        input = '''Class r_9{pM(_:String ){}Destructor (){} }Class __3_M:x{}'''
        expect = '''Program([ClassDecl(Id(r_9),[MethodDecl(Id(pM),Instance,[param(Id(_),StringType)],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(__3_M),Id(x),[])])'''
        self.assertTrue(TestAST.test(input, expect, 37))

    def test_38(self):
        input = '''Class _{Destructor (){}Constructor (_6_3_,X,H80:Array [Array [Int ,0b1000],4];_5:x;_,nD1D_,__rT,b:Array [Float ,036];_:Array [Boolean ,0x5F];e:Array [Array [Array [Int ,0X31],0X1F205C_F4_66C0],0116]){} }Class O{}Class __{Constructor (_8:Int ;f9E:String ){} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Constructor),Instance,[param(Id(_6_3_),ArrayType(4,ArrayType(8,IntType))),param(Id(X),ArrayType(4,ArrayType(8,IntType))),param(Id(H80),ArrayType(4,ArrayType(8,IntType))),param(Id(_5),ClassType(Id(x))),param(Id(_),ArrayType(30,FloatType)),param(Id(nD1D_),ArrayType(30,FloatType)),param(Id(__rT),ArrayType(30,FloatType)),param(Id(b),ArrayType(30,FloatType)),param(Id(_),ArrayType(95,BoolType)),param(Id(e),ArrayType(78,ArrayType(34223858935488,ArrayType(49,IntType))))],Block([],[]))]),ClassDecl(Id(O),[]),ClassDecl(Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(_8),IntType),param(Id(f9E),StringType)],Block([],[]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 38))

    def test_39(self):
        input = '''Class _{}Class X{Constructor (h,Tf_,o65sj_:a;___:Array [Float ,51];__O:_){Var d:Array [String ,5];} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(X),[MethodDecl(Id(Constructor),Instance,[param(Id(h),ClassType(Id(a))),param(Id(Tf_),ClassType(Id(a))),param(Id(o65sj_),ClassType(Id(a))),param(Id(___),ArrayType(51,FloatType)),param(Id(__O),ClassType(Id(_)))],Block([VarDecl(Id(d),ArrayType(5,StringType))],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 39))

    def test_40(self):
        input = '''Class k4{Constructor (_,_,h2:Float ;m,F:__){Break ;{} }}'''
        expect = '''Program([ClassDecl(Id(k4),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(_),FloatType),param(Id(h2),FloatType),param(Id(m),ClassType(Id(__))),param(Id(F),ClassType(Id(__)))],Block([],[Break,Block([],[])]))])])'''
        self.assertTrue(TestAST.test(input, expect, 40))

    def test_41(self):
        input = '''Class k_:G{}Class __p_{Destructor (){}Destructor (){}Var $2,b5z_,Mi:Float ;}'''
        expect = '''Program([ClassDecl(Id(k_),Id(G),[]),ClassDecl(Id(__p_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Static,VarDecl(Id($2),FloatType)),AttributeDecl(Instance,VarDecl(Id(b5z_),FloatType)),AttributeDecl(Instance,VarDecl(Id(Mi),FloatType))])])'''
        self.assertTrue(TestAST.test(input, expect, 41))

    def test_42(self):
        input = '''Class y:m{d(_Bv,_,_:Boolean ){ {} }}Class _{Destructor (){} }Class _:_zF{}'''
        expect = '''Program([ClassDecl(Id(y),Id(m),[MethodDecl(Id(d),Instance,[param(Id(_Bv),BoolType),param(Id(_),BoolType),param(Id(_),BoolType)],Block([],[Block([],[])]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),Id(_zF),[])])'''
        self.assertTrue(TestAST.test(input, expect, 42))

    def test_43(self):
        input = '''Class x_52:_{}Class F_:_{}Class _H:q{}Class _:_{Var $O,$2:_;}'''
        expect = '''Program([ClassDecl(Id(x_52),Id(_),[]),ClassDecl(Id(F_),Id(_),[]),ClassDecl(Id(_H),Id(q),[]),ClassDecl(Id(_),Id(_),[AttributeDecl(Static,VarDecl(Id($O),ClassType(Id(_)))),AttributeDecl(Static,VarDecl(Id($2),ClassType(Id(_))))])])'''
        self.assertTrue(TestAST.test(input, expect, 43))

    def test_44(self):
        input = '''Class _{}Class f{Var e:Array [Int ,0xC_A];}Class __48{$5(){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(f),[AttributeDecl(Instance,VarDecl(Id(e),ArrayType(202,IntType)))]),ClassDecl(Id(__48),[MethodDecl(Id($5),Static,[],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 44))

    def test_45(self):
        input = '''Class zH:_{}Class _{Destructor (){} }Class _{}Class w:_4{Var $0SRXE:_;}Class d:__{}'''
        expect = '''Program([ClassDecl(Id(zH),Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[]))]),ClassDecl(Id(_),[]),ClassDecl(Id(w),Id(_4),[AttributeDecl(Static,VarDecl(Id($0SRXE),ClassType(Id(_))))]),ClassDecl(Id(d),Id(__),[])])'''
        self.assertTrue(TestAST.test(input, expect, 45))

    def test_46(self):
        input = '''Class S{Var $5R5:Float ;}Class _{}Class _:A{_X(i:Array [Boolean ,0105];_a_p7:B_;S4__:Array [Int ,04]){Continue ;}_(_p,Q:_){} }'''
        expect = '''Program([ClassDecl(Id(S),[AttributeDecl(Static,VarDecl(Id($5R5),FloatType))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),Id(A),[MethodDecl(Id(_X),Instance,[param(Id(i),ArrayType(69,BoolType)),param(Id(_a_p7),ClassType(Id(B_))),param(Id(S4__),ArrayType(4,IntType))],Block([],[Continue])),MethodDecl(Id(_),Instance,[param(Id(_p),ClassType(Id(_))),param(Id(Q),ClassType(Id(_)))],Block([],[]))])])'''
        self.assertTrue(TestAST.test(input, expect, 46))

    def test_47(self):
        input = '''Class _{Destructor (){}Var _:Array [Array [Array [Int ,0X50],75],0102];}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([],[])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(66,ArrayType(75,ArrayType(80,IntType)))))])])'''
        self.assertTrue(TestAST.test(input, expect, 47))

    def test_48(self):
        input = '''Class j:u{Var u:Array [Array [Array [Array [String ,0x3],0x3],044],0b11];sEe(){}Destructor (){Continue ;} }Class __:_{}'''
        expect = '''Program([ClassDecl(Id(j),Id(u),[AttributeDecl(Instance,VarDecl(Id(u),ArrayType(3,ArrayType(36,ArrayType(3,ArrayType(3,StringType)))))),MethodDecl(Id(sEe),Instance,[],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[Continue]))]),ClassDecl(Id(__),Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 48))

    def test_49(self):
        input = '''Class R:_{}Class _H{Var $0,r,$5vM,$rs:V;}Class xtV:_0_{Constructor (_2A,__,t7i_:z_;_B1P:Array [Array [Array [String ,0x5D],0B1],06_1]){} }Class Y:p_{}Class R_{}'''
        expect = '''Program([ClassDecl(Id(R),Id(_),[]),ClassDecl(Id(_H),[AttributeDecl(Static,VarDecl(Id($0),ClassType(Id(V)))),AttributeDecl(Instance,VarDecl(Id(r),ClassType(Id(V)))),AttributeDecl(Static,VarDecl(Id($5vM),ClassType(Id(V)))),AttributeDecl(Static,VarDecl(Id($rs),ClassType(Id(V))))]),ClassDecl(Id(xtV),Id(_0_),[MethodDecl(Id(Constructor),Instance,[param(Id(_2A),ClassType(Id(z_))),param(Id(__),ClassType(Id(z_))),param(Id(t7i_),ClassType(Id(z_))),param(Id(_B1P),ArrayType(49,ArrayType(1,ArrayType(93,StringType))))],Block([],[]))]),ClassDecl(Id(Y),Id(p_),[]),ClassDecl(Id(R_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 49))

    