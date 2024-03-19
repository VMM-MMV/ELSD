from Parser import *
import json
parser: Parser = Parser()
code: str = '''
pregnancies = 5;
diagnosis = 'Bad';'''

result: dict = parser.parse(code)

print(json.dumps(result, indent=2)) 