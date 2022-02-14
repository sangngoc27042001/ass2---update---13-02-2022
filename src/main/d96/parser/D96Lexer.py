# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0270\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\5\2\u00a6\n\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00b1\n\4\3\5")
        buf.write("\3\5\3\5\5\5\u00b6\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3&\3&\5&\u015d\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0168\n\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,")
        buf.write("\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\7\66\u018a\n\66")
        buf.write("\f\66\16\66\u018d\13\66\3\67\3\67\38\38\68\u0193\n8\r")
        buf.write("8\168\u0194\39\39\39\39\59\u019b\n9\39\79\u019e\n9\f9")
        buf.write("\169\u01a1\139\3:\3:\5:\u01a5\n:\3:\7:\u01a8\n:\f:\16")
        buf.write(":\u01ab\13:\3;\3;\3;\3;\5;\u01b1\n;\3;\7;\u01b4\n;\f;")
        buf.write("\16;\u01b7\13;\3<\3<\3<\5<\u01bc\n<\3<\7<\u01bf\n<\f<")
        buf.write("\16<\u01c2\13<\3=\3=\3=\3=\5=\u01c8\n=\3=\3=\3>\3>\3>")
        buf.write("\3>\3>\5>\u01d1\n>\3>\7>\u01d4\n>\f>\16>\u01d7\13>\5>")
        buf.write("\u01d9\n>\3?\3?\3?\5?\u01de\n?\3?\7?\u01e1\n?\f?\16?\u01e4")
        buf.write("\13?\5?\u01e6\n?\3@\3@\3@\3@\3@\5@\u01ed\n@\3@\7@\u01f0")
        buf.write("\n@\f@\16@\u01f3\13@\5@\u01f5\n@\3A\3A\3A\3A\5A\u01fb")
        buf.write("\nA\3A\7A\u01fe\nA\fA\16A\u0201\13A\5A\u0203\nA\3B\3B")
        buf.write("\3B\3B\5B\u0209\nB\3B\3B\3C\3C\3D\3D\5D\u0211\nD\3D\6")
        buf.write("D\u0214\nD\rD\16D\u0215\3E\3E\7E\u021a\nE\fE\16E\u021d")
        buf.write("\13E\3F\3F\3F\3F\3F\3F\5F\u0225\nF\3F\3F\3F\5F\u022a\n")
        buf.write("F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3I\5I\u0238\nI\3J\3")
        buf.write("J\7J\u023c\nJ\fJ\16J\u023f\13J\3J\3J\3J\3K\7K\u0245\n")
        buf.write("K\fK\16K\u0248\13K\3L\3L\3L\3M\3M\3M\3M\3M\3M\3N\6N\u0254")
        buf.write("\nN\rN\16N\u0255\3N\3N\3O\3O\7O\u025c\nO\fO\16O\u025f")
        buf.write("\13O\3O\3O\3P\3P\3P\3Q\3Q\7Q\u0268\nQ\fQ\16Q\u026b\13")
        buf.write("Q\3Q\3Q\3Q\3Q\3\u0246\2R\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U\2W,Y-[.]/_\60a\61c\62")
        buf.write("e\63g\64i\65k\66m\2o\67q\2s\2u\2w\2y8{\2}\2\177\2\u0081")
        buf.write("\2\u00839\u0085\2\u0087\2\u0089\2\u008b:\u008d\2\u008f")
        buf.write(";\u0091\2\u0093<\u0095\2\u0097\2\u0099=\u009b>\u009d?")
        buf.write("\u009f@\u00a1A\3\2\32\4\2>>@@\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\4\2DDdd\3\2\63\63\3\2aa\3\2\62\63\3\2\63;\3\2\62;\4")
        buf.write("\2ZZzz\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\3\2\62\62\4")
        buf.write("\2GGgg\4\2--//\3\2))\3\2$$\t\2))^^ddhhppttvv\6\2\n\f\16")
        buf.write("\17$$^^\3\2\"\"\5\2\n\f\16\17\"\"\b\2^^ddhhppttvv\2\u0291")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2o\3\2\2\2\2y\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008f\3\2\2\2\2\u0093\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\3\u00a5\3\2\2\2\5\u00a7\3\2\2\2\7\u00b0")
        buf.write("\3\2\2\2\t\u00b5\3\2\2\2\13\u00b7\3\2\2\2\r\u00bd\3\2")
        buf.write("\2\2\17\u00c6\3\2\2\2\21\u00c9\3\2\2\2\23\u00d0\3\2\2")
        buf.write("\2\25\u00d5\3\2\2\2\27\u00dd\3\2\2\2\31\u00e2\3\2\2\2")
        buf.write("\33\u00e8\3\2\2\2\35\u00ee\3\2\2\2\37\u00f1\3\2\2\2!\u00f5")
        buf.write("\3\2\2\2#\u00fb\3\2\2\2%\u0103\3\2\2\2\'\u010a\3\2\2\2")
        buf.write(")\u010f\3\2\2\2+\u0116\3\2\2\2-\u011c\3\2\2\2/\u0120\3")
        buf.write("\2\2\2\61\u0124\3\2\2\2\63\u0130\3\2\2\2\65\u013b\3\2")
        buf.write("\2\2\67\u013f\3\2\2\29\u0142\3\2\2\2;\u0147\3\2\2\2=\u0149")
        buf.write("\3\2\2\2?\u014c\3\2\2\2A\u014e\3\2\2\2C\u0150\3\2\2\2")
        buf.write("E\u0152\3\2\2\2G\u0154\3\2\2\2I\u0156\3\2\2\2K\u015c\3")
        buf.write("\2\2\2M\u0167\3\2\2\2O\u0169\3\2\2\2Q\u016b\3\2\2\2S\u016e")
        buf.write("\3\2\2\2U\u0171\3\2\2\2W\u0173\3\2\2\2Y\u0175\3\2\2\2")
        buf.write("[\u0177\3\2\2\2]\u0179\3\2\2\2_\u017b\3\2\2\2a\u017d\3")
        buf.write("\2\2\2c\u017f\3\2\2\2e\u0181\3\2\2\2g\u0183\3\2\2\2i\u0185")
        buf.write("\3\2\2\2k\u0187\3\2\2\2m\u018e\3\2\2\2o\u0190\3\2\2\2")
        buf.write("q\u0196\3\2\2\2s\u01a2\3\2\2\2u\u01ac\3\2\2\2w\u01b8\3")
        buf.write("\2\2\2y\u01c7\3\2\2\2{\u01cb\3\2\2\2}\u01e5\3\2\2\2\177")
        buf.write("\u01e7\3\2\2\2\u0081\u01f6\3\2\2\2\u0083\u0208\3\2\2\2")
        buf.write("\u0085\u020c\3\2\2\2\u0087\u020e\3\2\2\2\u0089\u0217\3")
        buf.write("\2\2\2\u008b\u0229\3\2\2\2\u008d\u022d\3\2\2\2\u008f\u0230")
        buf.write("\3\2\2\2\u0091\u0237\3\2\2\2\u0093\u0239\3\2\2\2\u0095")
        buf.write("\u0246\3\2\2\2\u0097\u0249\3\2\2\2\u0099\u024c\3\2\2\2")
        buf.write("\u009b\u0253\3\2\2\2\u009d\u0259\3\2\2\2\u009f\u0262\3")
        buf.write("\2\2\2\u00a1\u0265\3\2\2\2\u00a3\u00a6\5\27\f\2\u00a4")
        buf.write("\u00a6\5\31\r\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3\2\2")
        buf.write("\2\u00a6\4\3\2\2\2\u00a7\u00a8\7x\2\2\u00a8\u00a9\7q\2")
        buf.write("\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7f\2\2\u00ab\6\3\2\2")
        buf.write("\2\u00ac\u00b1\5=\37\2\u00ad\u00ae\7?\2\2\u00ae\u00af")
        buf.write("\7?\2\2\u00af\u00b1\7\60\2\2\u00b0\u00ac\3\2\2\2\u00b0")
        buf.write("\u00ad\3\2\2\2\u00b1\b\3\2\2\2\u00b2\u00b6\5A!\2\u00b3")
        buf.write("\u00b6\5C\"\2\u00b4\u00b6\5E#\2\u00b5\u00b2\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\n\3\2\2\2\u00b7")
        buf.write("\u00b8\7D\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write("\u00bb\7c\2\2\u00bb\u00bc\7m\2\2\u00bc\f\3\2\2\2\u00bd")
        buf.write("\u00be\7E\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7p\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3")
        buf.write("\u00c4\7w\2\2\u00c4\u00c5\7g\2\2\u00c5\16\3\2\2\2\u00c6")
        buf.write("\u00c7\7K\2\2\u00c7\u00c8\7h\2\2\u00c8\20\3\2\2\2\u00c9")
        buf.write("\u00ca\7G\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\u00cd\7g\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7h\2\2\u00cf")
        buf.write("\22\3\2\2\2\u00d0\u00d1\7G\2\2\u00d1\u00d2\7n\2\2\u00d2")
        buf.write("\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\24\3\2\2\2\u00d5")
        buf.write("\u00d6\7H\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7t\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7e\2\2\u00db")
        buf.write("\u00dc\7j\2\2\u00dc\26\3\2\2\2\u00dd\u00de\7V\2\2\u00de")
        buf.write("\u00df\7t\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1\7g\2\2\u00e1")
        buf.write("\30\3\2\2\2\u00e2\u00e3\7H\2\2\u00e3\u00e4\7c\2\2\u00e4")
        buf.write("\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7\7g\2\2\u00e7")
        buf.write("\32\3\2\2\2\u00e8\u00e9\7C\2\2\u00e9\u00ea\7t\2\2\u00ea")
        buf.write("\u00eb\7t\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7{\2\2\u00ed")
        buf.write("\34\3\2\2\2\u00ee\u00ef\7K\2\2\u00ef\u00f0\7p\2\2\u00f0")
        buf.write("\36\3\2\2\2\u00f1\u00f2\7K\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4 \3\2\2\2\u00f5\u00f6\7H\2\2\u00f6")
        buf.write("\u00f7\7n\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7c\2\2\u00f9")
        buf.write("\u00fa\7v\2\2\u00fa\"\3\2\2\2\u00fb\u00fc\7D\2\2\u00fc")
        buf.write("\u00fd\7q\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7n\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100\u0101\7c\2\2\u0101\u0102\7p\2\2\u0102")
        buf.write("$\3\2\2\2\u0103\u0104\7U\2\2\u0104\u0105\7v\2\2\u0105")
        buf.write("\u0106\7t\2\2\u0106\u0107\7k\2\2\u0107\u0108\7p\2\2\u0108")
        buf.write("\u0109\7i\2\2\u0109&\3\2\2\2\u010a\u010b\7P\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7n\2\2\u010d\u010e\7n\2\2\u010e")
        buf.write("(\3\2\2\2\u010f\u0110\7T\2\2\u0110\u0111\7g\2\2\u0111")
        buf.write("\u0112\7v\2\2\u0112\u0113\7w\2\2\u0113\u0114\7t\2\2\u0114")
        buf.write("\u0115\7p\2\2\u0115*\3\2\2\2\u0116\u0117\7E\2\2\u0117")
        buf.write("\u0118\7n\2\2\u0118\u0119\7c\2\2\u0119\u011a\7u\2\2\u011a")
        buf.write("\u011b\7u\2\2\u011b,\3\2\2\2\u011c\u011d\7X\2\2\u011d")
        buf.write("\u011e\7c\2\2\u011e\u011f\7n\2\2\u011f.\3\2\2\2\u0120")
        buf.write("\u0121\7X\2\2\u0121\u0122\7c\2\2\u0122\u0123\7t\2\2\u0123")
        buf.write("\60\3\2\2\2\u0124\u0125\7E\2\2\u0125\u0126\7q\2\2\u0126")
        buf.write("\u0127\7p\2\2\u0127\u0128\7u\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\u012a\7t\2\2\u012a\u012b\7w\2\2\u012b\u012c\7e\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\7q\2\2\u012e\u012f\7t\2\2\u012f")
        buf.write("\62\3\2\2\2\u0130\u0131\7F\2\2\u0131\u0132\7g\2\2\u0132")
        buf.write("\u0133\7u\2\2\u0133\u0134\7v\2\2\u0134\u0135\7t\2\2\u0135")
        buf.write("\u0136\7w\2\2\u0136\u0137\7e\2\2\u0137\u0138\7v\2\2\u0138")
        buf.write("\u0139\7q\2\2\u0139\u013a\7t\2\2\u013a\64\3\2\2\2\u013b")
        buf.write("\u013c\7P\2\2\u013c\u013d\7g\2\2\u013d\u013e\7y\2\2\u013e")
        buf.write("\66\3\2\2\2\u013f\u0140\7D\2\2\u0140\u0141\7{\2\2\u0141")
        buf.write("8\3\2\2\2\u0142\u0143\7U\2\2\u0143\u0144\7g\2\2\u0144")
        buf.write("\u0145\7n\2\2\u0145\u0146\7h\2\2\u0146:\3\2\2\2\u0147")
        buf.write("\u0148\7-\2\2\u0148<\3\2\2\2\u0149\u014a\7-\2\2\u014a")
        buf.write("\u014b\7\60\2\2\u014b>\3\2\2\2\u014c\u014d\7/\2\2\u014d")
        buf.write("@\3\2\2\2\u014e\u014f\7,\2\2\u014fB\3\2\2\2\u0150\u0151")
        buf.write("\7\61\2\2\u0151D\3\2\2\2\u0152\u0153\7\'\2\2\u0153F\3")
        buf.write("\2\2\2\u0154\u0155\7#\2\2\u0155H\3\2\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157J\3\2\2\2\u0158\u0159\7(\2\2\u0159\u015d\7")
        buf.write("(\2\2\u015a\u015b\7~\2\2\u015b\u015d\7~\2\2\u015c\u0158")
        buf.write("\3\2\2\2\u015c\u015a\3\2\2\2\u015dL\3\2\2\2\u015e\u0168")
        buf.write("\t\2\2\2\u015f\u0160\7>\2\2\u0160\u0168\7?\2\2\u0161\u0162")
        buf.write("\7@\2\2\u0162\u0168\7?\2\2\u0163\u0164\7?\2\2\u0164\u0168")
        buf.write("\7?\2\2\u0165\u0166\7#\2\2\u0166\u0168\7?\2\2\u0167\u015e")
        buf.write("\3\2\2\2\u0167\u015f\3\2\2\2\u0167\u0161\3\2\2\2\u0167")
        buf.write("\u0163\3\2\2\2\u0167\u0165\3\2\2\2\u0168N\3\2\2\2\u0169")
        buf.write("\u016a\5\65\33\2\u016aP\3\2\2\2\u016b\u016c\7<\2\2\u016c")
        buf.write("\u016d\7<\2\2\u016dR\3\2\2\2\u016e\u016f\7\60\2\2\u016f")
        buf.write("\u0170\7\60\2\2\u0170T\3\2\2\2\u0171\u0172\7$\2\2\u0172")
        buf.write("V\3\2\2\2\u0173\u0174\7=\2\2\u0174X\3\2\2\2\u0175\u0176")
        buf.write("\7.\2\2\u0176Z\3\2\2\2\u0177\u0178\7<\2\2\u0178\\\3\2")
        buf.write("\2\2\u0179\u017a\7\60\2\2\u017a^\3\2\2\2\u017b\u017c\7")
        buf.write("*\2\2\u017c`\3\2\2\2\u017d\u017e\7+\2\2\u017eb\3\2\2\2")
        buf.write("\u017f\u0180\7]\2\2\u0180d\3\2\2\2\u0181\u0182\7_\2\2")
        buf.write("\u0182f\3\2\2\2\u0183\u0184\7}\2\2\u0184h\3\2\2\2\u0185")
        buf.write("\u0186\7\177\2\2\u0186j\3\2\2\2\u0187\u018b\t\3\2\2\u0188")
        buf.write("\u018a\t\4\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cl\3\2\2")
        buf.write("\2\u018d\u018b\3\2\2\2\u018e\u018f\7&\2\2\u018fn\3\2\2")
        buf.write("\2\u0190\u0192\5m\67\2\u0191\u0193\t\4\2\2\u0192\u0191")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195p\3\2\2\2\u0196\u0197\7\62\2\2\u0197")
        buf.write("\u0198\t\5\2\2\u0198\u019f\t\6\2\2\u0199\u019b\t\7\2\2")
        buf.write("\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\3")
        buf.write("\2\2\2\u019c\u019e\t\b\2\2\u019d\u019a\3\2\2\2\u019e\u01a1")
        buf.write("\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("r\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a9\t\t\2\2\u01a3")
        buf.write("\u01a5\t\7\2\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a6\3\2\2\2\u01a6\u01a8\t\n\2\2\u01a7\u01a4\3")
        buf.write("\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aat\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad")
        buf.write("\7\62\2\2\u01ad\u01ae\t\13\2\2\u01ae\u01b5\t\f\2\2\u01af")
        buf.write("\u01b1\t\7\2\2\u01b0\u01af\3\2\2\2\u01b0\u01b1\3\2\2\2")
        buf.write("\u01b1\u01b2\3\2\2\2\u01b2\u01b4\t\r\2\2\u01b3\u01b0\3")
        buf.write("\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6v\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9")
        buf.write("\7\62\2\2\u01b9\u01c0\t\16\2\2\u01ba\u01bc\t\7\2\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01bf\t\17\2\2\u01be\u01bb\3\2\2\2\u01bf\u01c2")
        buf.write("\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("x\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c8\5q9\2\u01c4")
        buf.write("\u01c8\5s:\2\u01c5\u01c8\5u;\2\u01c6\u01c8\5w<\2\u01c7")
        buf.write("\u01c3\3\2\2\2\u01c7\u01c4\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\b")
        buf.write("=\2\2\u01caz\3\2\2\2\u01cb\u01cc\7\62\2\2\u01cc\u01d8")
        buf.write("\t\5\2\2\u01cd\u01d9\7\62\2\2\u01ce\u01d5\t\6\2\2\u01cf")
        buf.write("\u01d1\t\7\2\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d4\t\b\2\2\u01d3\u01d0\3")
        buf.write("\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8")
        buf.write("\u01cd\3\2\2\2\u01d8\u01ce\3\2\2\2\u01d9|\3\2\2\2\u01da")
        buf.write("\u01e6\t\20\2\2\u01db\u01e2\t\t\2\2\u01dc\u01de\t\7\2")
        buf.write("\2\u01dd\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df")
        buf.write("\3\2\2\2\u01df\u01e1\t\n\2\2\u01e0\u01dd\3\2\2\2\u01e1")
        buf.write("\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2")
        buf.write("\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01da\3")
        buf.write("\2\2\2\u01e5\u01db\3\2\2\2\u01e6~\3\2\2\2\u01e7\u01e8")
        buf.write("\7\62\2\2\u01e8\u01f4\t\13\2\2\u01e9\u01f5\7\62\2\2\u01ea")
        buf.write("\u01f1\t\f\2\2\u01eb\u01ed\t\7\2\2\u01ec\u01eb\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\t")
        buf.write("\r\2\2\u01ef\u01ec\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3")
        buf.write("\u01f1\3\2\2\2\u01f4\u01e9\3\2\2\2\u01f4\u01ea\3\2\2\2")
        buf.write("\u01f5\u0080\3\2\2\2\u01f6\u0202\7\62\2\2\u01f7\u0203")
        buf.write("\7\62\2\2\u01f8\u01ff\t\16\2\2\u01f9\u01fb\t\7\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u01fe\t\17\2\2\u01fd\u01fa\3\2\2\2\u01fe\u0201")
        buf.write("\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200")
        buf.write("\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u01f7\3\2\2\2")
        buf.write("\u0202\u01f8\3\2\2\2\u0203\u0082\3\2\2\2\u0204\u0209\5")
        buf.write("{>\2\u0205\u0209\5}?\2\u0206\u0209\5\177@\2\u0207\u0209")
        buf.write("\5\u0081A\2\u0208\u0204\3\2\2\2\u0208\u0205\3\2\2\2\u0208")
        buf.write("\u0206\3\2\2\2\u0208\u0207\3\2\2\2\u0209\u020a\3\2\2\2")
        buf.write("\u020a\u020b\bB\3\2\u020b\u0084\3\2\2\2\u020c\u020d\t")
        buf.write("\n\2\2\u020d\u0086\3\2\2\2\u020e\u0210\t\21\2\2\u020f")
        buf.write("\u0211\t\22\2\2\u0210\u020f\3\2\2\2\u0210\u0211\3\2\2")
        buf.write("\2\u0211\u0213\3\2\2\2\u0212\u0214\5\u0085C\2\u0213\u0212")
        buf.write("\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0088\3\2\2\2\u0217\u021b\7\60\2")
        buf.write("\2\u0218\u021a\5\u0085C\2\u0219\u0218\3\2\2\2\u021a\u021d")
        buf.write("\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u008a\3\2\2\2\u021d\u021b\3\2\2\2\u021e\u0224\5}?\2\u021f")
        buf.write("\u0225\5\u0089E\2\u0220\u0225\5\u0087D\2\u0221\u0222\5")
        buf.write("\u0089E\2\u0222\u0223\5\u0087D\2\u0223\u0225\3\2\2\2\u0224")
        buf.write("\u021f\3\2\2\2\u0224\u0220\3\2\2\2\u0224\u0221\3\2\2\2")
        buf.write("\u0225\u022a\3\2\2\2\u0226\u0227\5\u0089E\2\u0227\u0228")
        buf.write("\5\u0087D\2\u0228\u022a\3\2\2\2\u0229\u021e\3\2\2\2\u0229")
        buf.write("\u0226\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\bF\4\2")
        buf.write("\u022c\u008c\3\2\2\2\u022d\u022e\t\23\2\2\u022e\u022f")
        buf.write("\t\24\2\2\u022f\u008e\3\2\2\2\u0230\u0231\7^\2\2\u0231")
        buf.write("\u0232\t\25\2\2\u0232\u0090\3\2\2\2\u0233\u0238\n\26\2")
        buf.write("\2\u0234\u0238\5\u008fH\2\u0235\u0238\5\u008dG\2\u0236")
        buf.write("\u0238\t\27\2\2\u0237\u0233\3\2\2\2\u0237\u0234\3\2\2")
        buf.write("\2\u0237\u0235\3\2\2\2\u0237\u0236\3\2\2\2\u0238\u0092")
        buf.write("\3\2\2\2\u0239\u023d\5U+\2\u023a\u023c\5\u0091I\2\u023b")
        buf.write("\u023a\3\2\2\2\u023c\u023f\3\2\2\2\u023d\u023b\3\2\2\2")
        buf.write("\u023d\u023e\3\2\2\2\u023e\u0240\3\2\2\2\u023f\u023d\3")
        buf.write("\2\2\2\u0240\u0241\5U+\2\u0241\u0242\bJ\5\2\u0242\u0094")
        buf.write("\3\2\2\2\u0243\u0245\13\2\2\2\u0244\u0243\3\2\2\2\u0245")
        buf.write("\u0248\3\2\2\2\u0246\u0247\3\2\2\2\u0246\u0244\3\2\2\2")
        buf.write("\u0247\u0096\3\2\2\2\u0248\u0246\3\2\2\2\u0249\u024a\7")
        buf.write("%\2\2\u024a\u024b\7%\2\2\u024b\u0098\3\2\2\2\u024c\u024d")
        buf.write("\5\u0097L\2\u024d\u024e\5\u0095K\2\u024e\u024f\5\u0097")
        buf.write("L\2\u024f\u0250\3\2\2\2\u0250\u0251\bM\6\2\u0251\u009a")
        buf.write("\3\2\2\2\u0252\u0254\t\30\2\2\u0253\u0252\3\2\2\2\u0254")
        buf.write("\u0255\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2")
        buf.write("\u0256\u0257\3\2\2\2\u0257\u0258\bN\6\2\u0258\u009c\3")
        buf.write("\2\2\2\u0259\u025d\5U+\2\u025a\u025c\5\u0091I\2\u025b")
        buf.write("\u025a\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2")
        buf.write("\u025d\u025e\3\2\2\2\u025e\u0260\3\2\2\2\u025f\u025d\3")
        buf.write("\2\2\2\u0260\u0261\bO\7\2\u0261\u009e\3\2\2\2\u0262\u0263")
        buf.write("\13\2\2\2\u0263\u0264\bP\b\2\u0264\u00a0\3\2\2\2\u0265")
        buf.write("\u0269\5U+\2\u0266\u0268\5\u0091I\2\u0267\u0266\3\2\2")
        buf.write("\2\u0268\u026b\3\2\2\2\u0269\u0267\3\2\2\2\u0269\u026a")
        buf.write("\3\2\2\2\u026a\u026c\3\2\2\2\u026b\u0269\3\2\2\2\u026c")
        buf.write("\u026d\7^\2\2\u026d\u026e\n\31\2\2\u026e\u026f\bQ\t\2")
        buf.write("\u026f\u00a2\3\2\2\2+\2\u00a5\u00b0\u00b5\u015c\u0167")
        buf.write("\u018b\u0194\u019a\u019f\u01a4\u01a9\u01b0\u01b5\u01bb")
        buf.write("\u01c0\u01c7\u01d0\u01d5\u01d8\u01dd\u01e2\u01e5\u01ec")
        buf.write("\u01f1\u01f4\u01fa\u01ff\u0202\u0208\u0210\u0215\u021b")
        buf.write("\u0224\u0229\u0237\u023d\u0246\u0255\u025d\u0269\n\3=")
        buf.write("\2\3B\3\3F\4\3J\5\b\2\2\3O\6\3P\7\3Q\b")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLNUM = 1
    VOIDTYPE = 2
    STRCMP = 3
    MULnDIVnMOL = 4
    BREAK = 5
    CONTINUE = 6
    IF = 7
    ELSEIF = 8
    ELSE = 9
    FOREACH = 10
    TRUE = 11
    FALSE = 12
    ARRAY = 13
    IN = 14
    INT = 15
    FLOAT = 16
    BOOLEAN = 17
    STR = 18
    NULL = 19
    RETURN = 20
    CLASS = 21
    VAL = 22
    VAR = 23
    CONSTRUCTOR = 24
    DESTRUCTOR = 25
    NEW = 26
    BY = 27
    SELF = 28
    ADD = 29
    CONCAT = 30
    MINUS = 31
    MULTIPLY = 32
    DEVIDE = 33
    MODULO = 34
    NOT = 35
    ASSIGN = 36
    LOGICAL = 37
    RELATIONAL = 38
    NEWOP = 39
    DOUBLE_COLON = 40
    DOUBLE_DOT = 41
    SEMI = 42
    COMMA = 43
    COLON = 44
    DOT = 45
    LB = 46
    RB = 47
    LSB = 48
    RSB = 49
    LCB = 50
    RCB = 51
    ID = 52
    STATICID = 53
    P_INTLIT = 54
    INTLIT = 55
    FLOATLIT = 56
    ESC_SEQ = 57
    STRINGLIT = 58
    COMMENT = 59
    WS = 60
    UNCLOSE_STRING = 61
    ERROR_CHAR = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Null'", "'Return'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'Self'", "'+'", "'+.'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'='", "'::'", "'..'", "';'", "','", "':'", "'.'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLNUM", "VOIDTYPE", "STRCMP", "MULnDIVnMOL", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
            "IN", "INT", "FLOAT", "BOOLEAN", "STR", "NULL", "RETURN", "CLASS", 
            "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
            "ADD", "CONCAT", "MINUS", "MULTIPLY", "DEVIDE", "MODULO", "NOT", 
            "ASSIGN", "LOGICAL", "RELATIONAL", "NEWOP", "DOUBLE_COLON", 
            "DOUBLE_DOT", "SEMI", "COMMA", "COLON", "DOT", "LB", "RB", "LSB", 
            "RSB", "LCB", "RCB", "ID", "STATICID", "P_INTLIT", "INTLIT", 
            "FLOATLIT", "ESC_SEQ", "STRINGLIT", "COMMENT", "WS", "UNCLOSE_STRING", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOLNUM", "VOIDTYPE", "STRCMP", "MULnDIVnMOL", "BREAK", 
                  "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                  "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STR", 
                  "NULL", "RETURN", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "CONCAT", "MINUS", 
                  "MULTIPLY", "DEVIDE", "MODULO", "NOT", "ASSIGN", "LOGICAL", 
                  "RELATIONAL", "NEWOP", "DOUBLE_COLON", "DOUBLE_DOT", "DOUBLEQUOTE", 
                  "SEMI", "COMMA", "COLON", "DOT", "LB", "RB", "LSB", "RSB", 
                  "LCB", "RCB", "ID", "STATIC", "STATICID", "P_INT_BIN", 
                  "P_INT_DEC", "P_INT_HEX", "P_INT_OCT", "P_INTLIT", "INT_BIN", 
                  "INT_DEC", "INT_HEX", "INT_OCT", "INTLIT", "DIGIT", "FLOAT_EXP", 
                  "FLOAT_DEC", "FLOATLIT", "QUOTE_IN_STR", "ESC_SEQ", "CHAR_STRING", 
                  "STRINGLIT", "LEGAL_COMMENT_STRING", "COMMENT_SIGN", "COMMENT", 
                  "WS", "UNCLOSE_STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.P_INTLIT_action 
            actions[64] = self.INTLIT_action 
            actions[68] = self.FLOATLIT_action 
            actions[72] = self.STRINGLIT_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ERROR_CHAR_action 
            actions[79] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def P_INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

              content = str(self.text)
              self.text = content[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                   text = str(self.text)
                   raise UncloseString(text[1:])
               
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                   raise ErrorToken(self.text)
               
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                   raise IllegalEscape(self.text[1:])
               
     


