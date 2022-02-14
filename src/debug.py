import sys, os
import subprocess
import unittest
import shutil
from antlr4 import *

for path in ['./test/', './main/d96/parser/', './main/d96/utils/', './main/d96/astgen/', './main/d96/checker/',
             './main/d96/codegen/']:
    sys.path.append(path)
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET_DIR = '../target'
GENERATE_DIR = 'main/d96/parser'


def main():
    os.system('python run.py gen')
    shutil.copy('../target/D96Parser.py','main/d96/astgen/D96Parser.py')
    shutil.copy('../target/D96Visitor.py', 'main/d96/astgen/D96Visitor.py')
    shutil.copy('main/d96/utils/AST.py','main/d96/astgen/AST.py')
    shutil.copy('main/d96/utils/AST.py', 'test/AST.py')
    shutil.copy('main/d96/utils/Visitor.py', 'main/d96/astgen/Visitor.py')

    if not os.path.isdir(TARGET_DIR + "/" + GENERATE_DIR):
        subprocess.run(
            ["java", "-jar", ANTLR_JAR, "-o", GENERATE_DIR, "-no-listener", "-visitor", "main/d96/parser/D96.g4"])
    if not (TARGET_DIR + "/" + GENERATE_DIR) in sys.path:
        sys.path.append(TARGET_DIR + "/" + GENERATE_DIR)
    if True:
        from ASTGenSuite import ASTGenSuite
        getAndTest(ASTGenSuite)


def getAndTest(cls):
    suite = unittest.makeSuite(cls)
    test(suite)


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())



if __name__ == "__main__":
    main()
