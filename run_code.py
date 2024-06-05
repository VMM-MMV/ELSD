import sys
from Compiler import *
from DebugParser import *

# if len(sys.argv) < 2:
#     print("Error: Please provide a filename as a command-line argument.")
#     sys.exit(1)

filename = "Vasile_heart.medic" #sys.argv[1] #"Vasile.medic" 

try:
    with open(filename, 'r') as file:
        contents = file.read()

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

parser = Parser()
AST = parser.parse(contents)
compiler = Compiler()
code = compiler.handleBlock(AST, 0)
# print(code)
exec(code)