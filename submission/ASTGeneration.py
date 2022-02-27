from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        a=ctx.getText()
        decl=[]
        for declItem in ctx.stmClassDecl():
            decl.append(self.visit(declItem))
        return Program(decl)

    def visitStmClassDecl(self, ctx: D96Parser.StmClassDeclContext):
        classname = Id(ctx.ID()[0].getText())
        parentname=None
        if len(ctx.ID()) == 2:
            parentname = Id(ctx.ID()[1].getText())
        memlist= self.visit(ctx.classBody())

        return ClassDecl(classname,memlist,parentname)

    def visitClassBody(self, ctx:D96Parser.ClassBodyContext):
        ret=[]
        if ctx.getChildCount()!=2:
            for i in range(1, ctx.getChildCount() - 1):
                ret=ret+self.visit(ctx.getChild(i))
        return ret

    def visitStmVariableDecl(self, ctx:D96Parser.StmVariableDeclContext):
        a=ctx.getText()
        if ctx.VAR():
            kind, variable, varType, varInit=self.visit(ctx.list_att())
            a=zip(kind, variable, varInit)
            ret=[AttributeDecl(kind_,VarDecl(variable_,varType,varInit_)) for (kind_,variable_,varInit_) in a]
            return ret
        elif ctx.VAL():
            kind, variable, varType, varInit = self.visit(ctx.list_att())
            a = zip(kind, variable, varInit)
            ret = [AttributeDecl(kind_, ConstDecl(variable_, varType, varInit_)) for (kind_, variable_, varInit_) in a]
            return ret
        # return [AttributeDecl()]
        return self.visit(ctx.list_att())

    def visitList_att(self, ctx:D96Parser.List_attContext):
        a=ctx.getText()
        if ctx.list_att_term():
            variable=[Id(i.getText()) for i in ctx.getChildren() if i in (ctx.ID()+ctx.STATICID())]
            kind = [(Instance() if i in ctx.ID() else Static()) for i in ctx.getChildren() if i in (ctx.ID()+ctx.STATICID())]
            varInit=[self.visit(ctx.expression())]
            variable_,kind_,varInit_,varType = self.visit(ctx.list_att_term())
            variable, kind, varInit = variable + variable_, kind + kind_, varInit + varInit_
            varInit.reverse()
            return kind, variable, varType, varInit
        else:
            varType = self.visit(ctx.typeData())
            variable = [Id(i.getText()) for i in ctx.getChildren() if i in (ctx.ID()+ctx.STATICID())]
            kind = [(Instance() if i in ctx.ID() else Static()) for i in ctx.getChildren() if i in (ctx.ID()+ctx.STATICID())]
            varInit=[None for _ in (ctx.ID()+ctx.STATICID())]
            if isinstance(varType, ClassType):
                varInit = [NullLiteral() for _ in (ctx.ID() + ctx.STATICID())]
            return kind, variable, varType, varInit

    def visitList_att_term(self, ctx:D96Parser.List_att_termContext):
        if ctx.typeData():
            return [],[],[],self.visit(ctx.typeData())
        else:
            variable = [Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.STATICID().getText())]
            kind = [Instance() if ctx.ID() else Static()]
            varInit = [self.visit(ctx.expression())]
            variable_, kind_, varInit_, varType = self.visit(ctx.list_att_term())
            variable, kind, varInit = variable+variable_, kind+kind_, varInit+varInit_
            return variable, kind, varInit, varType

    def visitTypeData(self, ctx:D96Parser.TypeDataContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STR():
            return StringType()
        elif ctx.ID():
            return ClassType(classname=Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.arrayType())
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        size = None
        if ctx.P_INTLIT():
            if ctx.P_INTLIT().getText()[0]=='0':
                if ctx.P_INTLIT().getText()[1] in ['b','B']:
                    size = int(ctx.P_INTLIT().getText(), 2)
                elif ctx.P_INTLIT().getText()[1] in ['x','X']:
                    size = int(ctx.P_INTLIT().getText(), 16)
                else:
                    size = int(ctx.P_INTLIT().getText(), 8)
            else:
                size = int(ctx.P_INTLIT().getText(), 10)
        eleType=self.visit(ctx.typeDataPrimitive())
        return ArrayType(size,eleType)
    def visitTypeDataPrimitive(self, ctx:D96Parser.TypeDataPrimitiveContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STR():
            return StringType()
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())

    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visit(ctx.exp_0())
    def visitExp_0(self, ctx:D96Parser.Exp_0Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_1(0))
        else:
            op = ctx.STRCMP().getText()
            left = self.visit(ctx.exp_1()[0])
            right = self.visit(ctx.exp_1(1))
            return BinaryOp(op,left,right)
    def visitExp_1(self, ctx:D96Parser.Exp_1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_2(0))
        else:
            op = ctx.RELATIONAL().getText()
            left = self.visit(ctx.exp_2(0))
            right = self.visit(ctx.exp_2(1))
            return BinaryOp(op,left,right)
    def visitExp_2(self, ctx:D96Parser.Exp_2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_3())
        else:
            op = ctx.LOGICAL().getText()
            left = self.visit(ctx.exp_2())
            right = self.visit(ctx.exp_3())
            return BinaryOp(op,left,right)
    def visitExp_3(self, ctx:D96Parser.Exp_3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_4())
        else:
            op = ctx.ADD().getText() if ctx.ADD() else ctx.MINUS().getText()
            left = self.visit(ctx.exp_3())
            right = self.visit(ctx.exp_4())
            return BinaryOp(op,left,right)
    def visitExp_4(self, ctx:D96Parser.Exp_4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_5())
        else:
            op = ctx.MULnDIVnMOL().getText()
            left = self.visit(ctx.exp_4())
            right = self.visit(ctx.exp_5())
            return BinaryOp(op,left,right)
    def visitExp_5(self, ctx:D96Parser.Exp_5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_6())
        else:
            op = ctx.NOT().getText()
            body = self.visit(ctx.exp_5())
            return UnaryOp(op,body)
    def visitExp_6(self, ctx:D96Parser.Exp_6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_7())
        else:
            op = ctx.MINUS().getText()
            body = self.visit(ctx.exp_6())
            return UnaryOp(op,body)
    def visitExp_7(self, ctx:D96Parser.Exp_7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_8())
        else:
            idx=[self.visit(ctx.expression(i)) for i in range(len(ctx.expression()))]
            a=str(idx)
            arr = self.visit(ctx.exp_7())
            return ArrayCell(arr,idx)
    def visitExp_8(self, ctx:D96Parser.Exp_8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_9())
        else:
            if ctx.listOfExpressions():
                obj = self.visit(ctx.exp_8())
                method = Id(ctx.ID().getText())
                param = self.visit(ctx.listOfExpressions())
                return CallExpr(obj,method,param)
            else:
                obj = self.visit(ctx.exp_8())
                fieldname = Id(ctx.ID().getText())
                return FieldAccess(obj,fieldname)
            pass
    def visitExp_8V2(self, ctx:D96Parser.Exp_8V2Context):
        a=ctx.getText()
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_9())
        else:
            if ctx.listOfExpressions():
                obj = self.visit(ctx.exp_8V2())
                method = Id(ctx.ID().getText())
                param = self.visit(ctx.listOfExpressions())
                return CallExpr(obj,method,param)
            else:
                obj = self.visit(ctx.exp_8V2())
                fieldname = Id(ctx.ID().getText())
                return FieldAccess(obj,fieldname)
            pass
    def visitExp_9(self, ctx:D96Parser.Exp_9Context):
        a=ctx.getText()
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_10())
        else:
            if ctx.listOfExpressions():
                obj = Id(ctx.ID().getText())
                method = Id(ctx.STATICID().getText())
                param = self.visit(ctx.listOfExpressions())
                return CallExpr(obj,method,param)
            else:
                obj = Id(ctx.ID().getText())
                fieldname = Id(ctx.STATICID().getText())
                return FieldAccess(obj,fieldname)
            pass
    def visitExp_10(self, ctx:D96Parser.Exp_10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_11())
        else:
            classname = self.visit(ctx.exp_10())
            param = self.visit(ctx.listOfExpressions())
            return NewExpr(classname,param)
    def visitExp_11(self, ctx:D96Parser.Exp_11Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.SELF():
            return SelfLiteral()
        if ctx.NULL():
            return NullLiteral()
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.expression():
            return self.visit(ctx.expression())

    def visitListOfExpressions(self, ctx:D96Parser.ListOfExpressionsContext):
        return [self.visit(ctx.expression(i)) for i in range(len(ctx.expression()))]

    def visitStmMethodDecl(self, ctx:D96Parser.StmMethodDeclContext):
        kind=None
        name=None
        param=[]
        body=self.visit(ctx.stmBlockInFunction())
        if ctx.STATICID():
            kind = Static()
            name = Id(ctx.STATICID().getText())
        elif ctx.ID():
            kind = Instance()
            name = Id(ctx.ID().getText())
        if ctx.parameterList():
            param=self.visit(ctx.parameterList())
        if not ctx.STATICID() and ctx.ID().getText() == 'main':
            classBody = ctx.parentCtx
            classDecl = classBody.parentCtx
            class_name = classDecl.ID(0).getText()

            if class_name == 'Program':
                if len(param) == 0:
                    kind = Static()
                    name = Id(ctx.ID().getText())
                    return [MethodDecl(kind, name, param, body)]
        return [MethodDecl(kind, name,param,body)]

    def visitParameterList(self, ctx:D96Parser.ParameterListContext):
        if ctx.getChildCount()!=0:
            ret=[]
            for oneparam in ctx.oneParam():
                ret=ret+self.visit(oneparam)
            a=str(ret)
            return ret
        return []
        #return List[VarDecl]
    def visitOneParam(self, ctx:D96Parser.OneParamContext):
        varType=self.visit(ctx.typeData())
        ret=[VarDecl(Id(ctx.ID(i).getText()),varType) for i in range(len(ctx.ID()))]
        return ret
        # return List[VarDecl]
    def visitStmBlockInFunction(self, ctx:D96Parser.StmBlockInFunctionContext):
        inst=[]#Inst
        if ctx.getChildCount() != 2:
            for child in ctx.getChildren():
                if child not in ([ctx.LCB()] + [ctx.RCB()]):
                    if child in ctx.stmVariableDeclInFunction():
                        inst = inst + self.visit(child)
                    else:
                        inst = inst + [self.visit(child)]
            #còn stmt
        return Block(inst)

    def visitStmVariableDeclInFunction(self, ctx:D96Parser.StmVariableDeclInFunctionContext):
        a=ctx.getText()
        if ctx.VAR():
            kind, variable, varType, varInit = self.visit(ctx.list_attInFunction())
            a = zip(kind, variable, varInit)
            ret = [VarDecl(variable_,varType,varInit_) for (kind_, variable_, varInit_) in a]
            return ret
        elif ctx.VAL():
            kind, variable, varType, varInit = self.visit(ctx.list_attInFunction())
            a = zip(kind, variable, varInit)
            ret = [ConstDecl(variable_, varType, varInit_) for (kind_, variable_, varInit_) in a]
            return ret
    def visitList_attInFunction(self, ctx:D96Parser.List_attInFunctionContext):
        if ctx.list_att_termInFunction():
            variable = [Id(i.getText()) for i in ctx.ID()]
            kind = [(Instance() if i in ctx.ID() else Static()) for i in ctx.ID()]
            varInit = [self.visit(ctx.expression())]
            variable_, kind_, varInit_, varType = self.visit(ctx.list_att_termInFunction())
            variable, kind, varInit = variable + variable_, kind + kind_, varInit + varInit_
            varInit.reverse()
            return kind, variable, varType, varInit
        else:
            varType = self.visit(ctx.typeData())
            variable = [Id(i.getText()) for i in ctx.ID()]
            kind = [(Instance() if i in ctx.ID() else Static()) for i in ctx.ID()]
            varInit = [None for _ in ctx.ID()]
            if isinstance(varType, ClassType):
                varInit = [NullLiteral() for _ in ctx.ID()]
            return kind, variable, varType, varInit
    def visitList_att_termInFunction(self, ctx:D96Parser.List_att_termInFunctionContext):
        if ctx.typeData():
            return [], [], [], self.visit(ctx.typeData())
        else:
            variable = [Id(ctx.ID().getText())]
            kind = [Instance() if ctx.ID() else Static()]
            varInit = [self.visit(ctx.expression())]
            variable_, kind_, varInit_, varType = self.visit(ctx.list_att_term())
            variable, kind, varInit = variable + variable_, kind + kind_, varInit + varInit_
            return variable, kind, varInit, varType

    def visitStmAssignment(self, ctx:D96Parser.StmAssignmentContext):
        lhs= self.visit(ctx.lhs())
        exp = self.visit(ctx.expression())
        return Assign(lhs,exp)
    def visitLhs(self, ctx:D96Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.exp_7():
            return self.visit(ctx.exp_7())

    def visitStmBreak(self, ctx:D96Parser.StmBreakContext):
        return Break()

    def visitStmContinue(self, ctx:D96Parser.StmContinueContext):
        return Continue()

    def visitStmReturn(self, ctx:D96Parser.StmReturnContext):
        expr=None
        if ctx.expression():
            expr = self.visit(ctx.expression())
        return Return(expr)

    def visitStmConstructorDecl(self, ctx:D96Parser.StmConstructorDeclContext):
        param = self.visit(ctx.parameterList())
        body = self.visit(ctx.stmBlockInFunction())
        return [MethodDecl(Instance(),Id('''Constructor'''),param,body)]

    def visitStmdDestructorDecl(self, ctx:D96Parser.StmdDestructorDeclContext):
        param = []
        body = self.visit(ctx.stmBlockInFunction())
        return [MethodDecl(Instance(),Id('''Destructor'''),param,body)]

    def visitStmIf(self, ctx:D96Parser.StmIfContext):
        if (len(ctx.statementInFunction())<=2 and ctx.ELSE()) or len(ctx.statementInFunction())==1:
            expr=self.visit(ctx.expression(0))
            thenStmt=self.visit(ctx.statementInFunction(0))
            elseStmt=None
            if len(ctx.statementInFunction())==2:
                elseStmt = self.visit(ctx.statementInFunction(1))
            return If(expr,thenStmt,elseStmt)
        elif not ctx.ELSE():
            n_counter = list(range(len(ctx.statementInFunction())))
            n_counter.reverse()
            elseStmt_ = None
            for i in n_counter:
                expr_ = self.visit(ctx.expression(i))
                thenStmt_ = self.visit(ctx.statementInFunction(i))
                elseStmt_ = If(expr_, thenStmt_, elseStmt_)
            return elseStmt_
        else:
            expr = self.visit(ctx.expression(0))
            thenStmt = self.visit(ctx.statementInFunction(0))
            n_counter=list(range(len(ctx.statementInFunction())))
            n_counter.reverse()
            elseStmt = None

            expr_ = None
            thenStmt_ = None
            elseStmt_ = None
            for i in n_counter:
                if i == max(n_counter):
                    elseStmt_ = self.visit(ctx.statementInFunction(i))
                thenStmt_ = self.visit(ctx.statementInFunction(i-1))
                expr_ = self.visit(ctx.expression(i-1))
                elseStmt_= If(expr_,thenStmt_,elseStmt_)
                if i == 2:
                    break
            elseStmt = elseStmt_
            return If(expr, thenStmt, elseStmt)
    def visitStatementInFunction(self, ctx:D96Parser.StatementInFunctionContext):
        return self.visit(ctx.getChild(0))

    def visitStmMethodInvocation(self, ctx:D96Parser.StmMethodInvocationContext):
        a=ctx.getText()
        if ctx.exp_9():
            obj = self.visit(ctx.exp_9())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.listOfExpressions())
            return CallStmt(obj, method, param)
        elif ctx.exp_10():
            obj = self.visit(ctx.exp_10())
            method = Id(ctx.STATICID().getText())
            param = self.visit(ctx.listOfExpressions())
            return CallStmt(obj, method, param)
        elif ctx.exp_8V2():
            obj = self.visit(ctx.exp_8V2())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.listOfExpressions())
            return CallStmt(obj, method, param)

    def visitStmForEach(self, ctx:D96Parser.StmForEachContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1))
        loop = self.visit(ctx.stmBlockInFunction())
        expr3 = self.visit(ctx.expression(2)) if ctx.BY() else IntLiteral(1)
        return For(id, expr1, expr2, loop, expr3)
############################################
################ CODE Ở ĐÂY ################
############################################
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        a=ctx.getText()
        if ctx.P_INTLIT():
            if ctx.getText()[0]=='0':
                if ctx.getText()[1] in ['b','B']:
                    return IntLiteral(int(ctx.P_INTLIT().getText(), 2))
                elif ctx.getText()[1] in ['x','X']:
                    return IntLiteral(int(ctx.P_INTLIT().getText(), 16))
                else:
                    return IntLiteral(int(ctx.P_INTLIT().getText(), 8))
            return IntLiteral(int(ctx.P_INTLIT().getText(), 10))
        elif ctx.INTLIT():
            if ctx.getText()[0] == '0' and len(ctx.getText())>1:
                if ctx.getText()[1] in ['b', 'B']:
                    return IntLiteral(int(ctx.INTLIT().getText(), 2))
                elif ctx.getText()[1] in ['x', 'X']:
                    return IntLiteral(int(ctx.INTLIT().getText(), 16))
                else:
                    return IntLiteral(int(ctx.INTLIT().getText(), 8))
            return IntLiteral(int(ctx.INTLIT().getText(), 10))
        elif ctx.FLOATLIT():
            a=ctx.getText()
            if ctx.getText()[:2] == '.e':
                return FloatLiteral(float(0))
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLNUM():
            return BooleanLiteral(bool(ctx.BOOLNUM().getText() == 'True'))
        elif ctx.NULL():
            return None
        else:
            return self.visit(ctx.arrayLiteral())

    def visitArrayLiteral(self, ctx:D96Parser.ArrayLiteralContext):
        a=ctx.getText()
        value=[self.visit(i) for i in ctx.expression()]
        return ArrayLiteral(value)