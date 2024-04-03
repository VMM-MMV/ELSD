from Parser import *
import json
parser: Parser = Parser()
code: str = '''
Create Template {
    name: "Obesity",
    params: {
        pregnancies: "int",
        glucose: "float",
        bloodPressure: "float",
        skinThickness: "float",
        insulin: "float",
        bmi: "float",
        age: "float",
    },
    target: {diagnosis: "float",},
} 
'''
# print(code[146:])
result: dict = parser.parse(code)

print(json.dumps(result, indent=2)) 