import sys
from Compiler import *
from Parser import *

if len(sys.argv) < 2:
    print("Error: Please provide a filename as a command-line argument.")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        contents = file.read()
    parser = Parser()
    compiler = Compiler()
    AST = parser.parse(contents)
    compiler = Compiler()
    code = compiler.handleBlock(AST, 0)
    exec(code)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")