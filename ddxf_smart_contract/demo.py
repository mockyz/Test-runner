

def CompileContract():
    sc = """OntCversion = '2.0.0'
from ontology.interop.System.Runtime import Log
def Main(operation, args):
    if operation == 'LogTest':
        return LogTest()
    return False
def LogTest():
    Log('Hello, world!')
    return True
"""

    try:
        avm = compilerler.Compile_Contract(sc)
        return avm
    except Exception as error:
        print("[CompileContract Error]: " + str(error))
        return ""

def CompileFile():
    try:
        avm = compiler.Compile_File("basic-contract.py")
        return avm
    except Exception as error:
        print("[CompileFile Error]: " + str(error))
        return ""

assert CompileContract() == CompileFile(), 'Compile test failed'

