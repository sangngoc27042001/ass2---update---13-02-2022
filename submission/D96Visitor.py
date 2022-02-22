# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmConstructorDecl.
    def visitStmConstructorDecl(self, ctx:D96Parser.StmConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmdDestructorDecl.
    def visitStmdDestructorDecl(self, ctx:D96Parser.StmdDestructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameterList.
    def visitParameterList(self, ctx:D96Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#oneParam.
    def visitOneParam(self, ctx:D96Parser.OneParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:D96Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typeData.
    def visitTypeData(self, ctx:D96Parser.TypeDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typeDataPrimitive.
    def visitTypeDataPrimitive(self, ctx:D96Parser.TypeDataPrimitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayType.
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expIndex.
    def visitExpIndex(self, ctx:D96Parser.ExpIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#canBeIndex.
    def visitCanBeIndex(self, ctx:D96Parser.CanBeIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expObjCreation.
    def visitExpObjCreation(self, ctx:D96Parser.ExpObjCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalarVariable.
    def visitScalarVariable(self, ctx:D96Parser.ScalarVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expIndexFree.
    def visitExpIndexFree(self, ctx:D96Parser.ExpIndexFreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#canBeIndexFree.
    def visitCanBeIndexFree(self, ctx:D96Parser.CanBeIndexFreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expInstanceAttributeAccess.
    def visitExpInstanceAttributeAccess(self, ctx:D96Parser.ExpInstanceAttributeAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expTemp1.
    def visitExpTemp1(self, ctx:D96Parser.ExpTemp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expInstanceMethodInvocation.
    def visitExpInstanceMethodInvocation(self, ctx:D96Parser.ExpInstanceMethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expTemp2.
    def visitExpTemp2(self, ctx:D96Parser.ExpTemp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expStaticAttributeAccess.
    def visitExpStaticAttributeAccess(self, ctx:D96Parser.ExpStaticAttributeAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expStaticMethodInvocation.
    def visitExpStaticMethodInvocation(self, ctx:D96Parser.ExpStaticMethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listOfExpressions.
    def visitListOfExpressions(self, ctx:D96Parser.ListOfExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_0.
    def visitExp_0(self, ctx:D96Parser.Exp_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_1.
    def visitExp_1(self, ctx:D96Parser.Exp_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_2.
    def visitExp_2(self, ctx:D96Parser.Exp_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_3.
    def visitExp_3(self, ctx:D96Parser.Exp_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_4.
    def visitExp_4(self, ctx:D96Parser.Exp_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_5.
    def visitExp_5(self, ctx:D96Parser.Exp_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_6.
    def visitExp_6(self, ctx:D96Parser.Exp_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_7.
    def visitExp_7(self, ctx:D96Parser.Exp_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_8.
    def visitExp_8(self, ctx:D96Parser.Exp_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_9.
    def visitExp_9(self, ctx:D96Parser.Exp_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_10.
    def visitExp_10(self, ctx:D96Parser.Exp_10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_11.
    def visitExp_11(self, ctx:D96Parser.Exp_11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmVariableDecl.
    def visitStmVariableDecl(self, ctx:D96Parser.StmVariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_att.
    def visitList_att(self, ctx:D96Parser.List_attContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_att_term.
    def visitList_att_term(self, ctx:D96Parser.List_att_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmVariableDeclInFunction.
    def visitStmVariableDeclInFunction(self, ctx:D96Parser.StmVariableDeclInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_attInFunction.
    def visitList_attInFunction(self, ctx:D96Parser.List_attInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_att_termInFunction.
    def visitList_att_termInFunction(self, ctx:D96Parser.List_att_termInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmAssignment.
    def visitStmAssignment(self, ctx:D96Parser.StmAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmIf.
    def visitStmIf(self, ctx:D96Parser.StmIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmBreak.
    def visitStmBreak(self, ctx:D96Parser.StmBreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmContinue.
    def visitStmContinue(self, ctx:D96Parser.StmContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmReturn.
    def visitStmReturn(self, ctx:D96Parser.StmReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmMethodInvocation.
    def visitStmMethodInvocation(self, ctx:D96Parser.StmMethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_8V2.
    def visitExp_8V2(self, ctx:D96Parser.Exp_8V2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listOfStatement.
    def visitListOfStatement(self, ctx:D96Parser.ListOfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmBlock.
    def visitStmBlock(self, ctx:D96Parser.StmBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmBlockInFunction.
    def visitStmBlockInFunction(self, ctx:D96Parser.StmBlockInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statementInFunction.
    def visitStatementInFunction(self, ctx:D96Parser.StatementInFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmForEach.
    def visitStmForEach(self, ctx:D96Parser.StmForEachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmClassDecl.
    def visitStmClassDecl(self, ctx:D96Parser.StmClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classBody.
    def visitClassBody(self, ctx:D96Parser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmMethodDecl.
    def visitStmMethodDecl(self, ctx:D96Parser.StmMethodDeclContext):
        return self.visitChildren(ctx)



del D96Parser