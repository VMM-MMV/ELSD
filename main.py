from Parser import *
import json
parser: Parser = Parser()
code: str = r"""
Person.load()

Person.visualize()
"""
result: dict = parser.parse(code)

print(json.dumps(result, indent=2)) 

from Compiler import *

compiler = Compiler()
code = compiler.handleBlock(result, 0)